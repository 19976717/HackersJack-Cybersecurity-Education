"""Reproduce HackersJack pre/post analyses from authorised original Excel workbooks.
No raw student records are written to outputs. Run locally with approved access.
"""
import argparse, csv, hashlib, json, re, sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

from scipy import stats

OUTCOMES=('MCQ','TF','Combined')
EXPECTED={'Combined': {'n':216,'pre_mean':21.61,'post_mean':28.67,'gain':7.06,'t':40.17,'dz':2.73},'MCQ':{'n':225,'pre_mean':14.61,'post_mean':19.09,'gain':4.48,'t':31.49,'dz':2.10},'TF':{'n':231,'pre_mean':7.04,'post_mean':9.58,'gain':2.53,'t':28.50,'dz':1.88}}

def parse_sheet(sheet, kind, grade, class_id, file_name):
    """Find assessment section headers; never assume fixed row offsets.
    Only accept 20/10 binary items; blanks/absent invalidate that occasion.
    """
    rows=sheet.get_range('A1:V150').values
    sections=[]
    for i,row in enumerate(rows):
        cell=str(row[0] or '').strip().lower()
        if re.fullmatch(r'(pre|post)\s*assessment',cell):
            sections.append((i, 'pre' if cell.startswith('pre') else 'post'))
    if [s[1] for s in sections]!=['pre','post']:
        raise ValueError(f'{file_name} / {sheet.name}: expected one Pre and one Post section; found {sections}')
    result=[]; nitems=20 if kind=='MCQ' else 10
    for k,(start,occasion) in enumerate(sections):
        stop=sections[k+1][0] if k+1<len(sections) else len(rows)
        block=rows[start+1:stop]
        header=next((j for j,r in enumerate(block) if str(r[1] or '').strip().upper()=='Q1'),None)
        if header is None: raise ValueError(f'{file_name}/{sheet.name}/{occasion}: missing Q1 header')
        seen=set()
        for row in block[header+1:]:
            code=str(row[0] or '').strip()
            if not code or code.lower() in ('total','average','mean','sum'):continue
            if not re.search(r'\d',code): continue
            if code in seen: raise ValueError(f'Duplicate code within {file_name}/{sheet.name}/{occasion}: {code}')
            seen.add(code)
            vals=row[1:nitems+1]
            valid=all(isinstance(v,(int,float)) and not isinstance(v,bool) and v in (0,1) for v in vals)
            result.append({'grade':grade,'class':class_id,'code':code,'kind':kind,'occasion':occasion,'score':int(sum(vals)) if valid else None,'valid':valid,'items':vals if valid else None,'file':file_name})
    return result

def read_records(folder):
    files=sorted(folder.glob('*.xlsx'))
    if len(files)!=12: raise ValueError(f'Expected exactly 12 workbooks; found {len(files)}. Do not include duplicate filename versions.')
    records=[]; hashes=[]
    for path in files:
        grade_match=re.search(r'Grade\s*([56])',path.name,re.I)
        if not grade_match: raise ValueError(f'Cannot identify grade from {path.name}')
        grade=int(grade_match.group(1))
        class_id=path.name.split('Pre and Post')[0].strip(' -')
        hashes.append({'filename':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        wb=SpreadsheetFile.import_xlsx(Blob.load(str(path)))
        sheets=list(wb.worksheets.items)
        if len(sheets)!=2:raise ValueError(f'{path.name}: expected exactly 2 worksheets')
        for sheet in sheets:
            name=sheet.name.upper()
            kind='MCQ' if 'MCQ' in name else 'TF' if ('T-F' in name or 'T_F' in name) else None
            if kind is None:raise ValueError(f'Unknown assessment type: {sheet.name}')
            records.extend(parse_sheet(sheet,kind,grade,class_id,path.name))
    return records,hashes

def construct_pairs(records):
    bykey=defaultdict(dict)
    for r in records:
        key=(r['grade'],r['class'],r['code'],r['kind'])
        if r['occasion'] in bykey[key]:raise ValueError(f'Duplicate key: {key} {r["occasion"]}')
        bykey[key][r['occasion']]=r
    component={}
    for key,v in bykey.items():
        if all(x in v and v[x]['valid'] for x in ('pre','post')):
            component[key]={'grade':key[0],'class':key[1],'code':key[2],'kind':key[3], 'pre':v['pre']['score'],'post':v['post']['score']}
    combined=[]
    for (grade,cl,code,kind),r in component.items():
        if kind!='MCQ':continue
        tf=component.get((grade,cl,code,'TF'))
        if tf:
            combined.append({'grade':grade,'class':cl,'code':code,'kind':'Combined','pre':r['pre']+tf['pre'],'post':r['post']+tf['post']})
    return list(component.values())+combined

def summarize(pairs):
    if len(pairs)<2:return None
    pre=[r['pre'] for r in pairs];post=[r['post'] for r in pairs];diff=[b-a for a,b in zip(pre,post)]
    n=len(diff); sd=stdev(diff)
    t=mean(diff)/(sd/(n**0.5)) if sd else float('nan')
    ci=stats.t.interval(.95,n-1,loc=mean(diff),scale=sd/(n**.5)) if sd else (float('nan'),)*2
    return {'n':n,'pre_mean':mean(pre),'pre_sd':stdev(pre),'post_mean':mean(post),'post_sd':stdev(post),'gain':mean(diff),'gain_sd':sd,'t':t,'df':n-1,'p':float(2*stats.t.sf(abs(t),n-1)),'dz':mean(diff)/sd if sd else float('nan'),'ci_low':ci[0],'ci_high':ci[1]}

def run(input_dir,output_dir):
    output_dir.mkdir(parents=True,exist_ok=True)
    records,hashes=read_records(input_dir)
    pairs=construct_pairs(records)
    groups={}
    for kind in OUTCOMES:groups[kind]=summarize([r for r in pairs if r['kind']==kind])
    for grade in (5,6):groups[f'Grade {grade}']=summarize([r for r in pairs if r['kind']=='Combined' and r['grade']==grade])
    validation=[]
    for kind,expected in EXPECTED.items():
        observed=groups[kind]
        for metric,exp in expected.items():
            val=observed[metric]
            ok=(val==exp) if metric=='n' else abs(val-exp)<.00500001
            validation.append({'outcome':kind,'metric':metric,'reported':exp,'recomputed':val,'rounding_match':ok})
    # Only aggregates, counts, hashes are written; no student codes or individual scores.
    with (output_dir/'statistical_results.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['outcome']+list(next(iter(groups.values())).keys()));writer.writeheader()
        for k,v in groups.items():writer.writerow({'outcome':k,**v})
    with (output_dir/'verification.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['outcome','metric','reported','recomputed','rounding_match']);writer.writeheader();writer.writerows(validation)
    with (output_dir/'source_checksums.json').open('w') as f:json.dump(hashes,f,indent=2)
    counts=defaultdict(int)
    for r in records:counts[(r['kind'],r['occasion'],'valid' if r['valid'] else 'unavailable')]+=1
    with (output_dir/'data_quality_counts.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['component','occasion','status','records'])
        for (kind,occasion,status),n in sorted(counts.items()):w.writerow([kind,occasion,status,n])
    print(json.dumps({'summary':groups,'matches':all(x['rounding_match'] for x in validation),'verification':validation},indent=2))
    return all(x['rounding_match'] for x in validation)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path('data/private_original'));ap.add_argument('--output',type=Path,default=Path('outputs'));args=ap.parse_args()
    ok=run(args.input,args.output)
    sys.exit(0 if ok else 2)
