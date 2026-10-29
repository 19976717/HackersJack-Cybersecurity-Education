from scripts.pipeline import summarize,construct_pairs

def test_paired_gain():
    rows=[{'pre':1,'post':3},{'pre':2,'post':5},{'pre':3,'post':7}]
    out=summarize(rows)
    assert out['n']==3
    assert out['gain']==3
    assert out['df']==2

def test_combined_requires_both_components():
    def row(kind,occasion,score,valid=True):
        return {'grade':5,'class':'A','code':'X1','kind':kind,'occasion':occasion,'score':score,'valid':valid}
    data=[row('MCQ','pre',10),row('MCQ','post',15),row('TF','pre',5),row('TF','post',8)]
    pairs=construct_pairs(data)
    assert len([r for r in pairs if r['kind']=='Combined'])==1
    assert [r for r in pairs if r['kind']=='Combined'][0]['post']==23
    data[-1]['valid']=False
    assert not [r for r in construct_pairs(data) if r['kind']=='Combined']
