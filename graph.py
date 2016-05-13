from math import*
from sets import*
from copy import*
class node(object):
    def __init__(self,data):
        self.cond=0
        self.cord=data
        self.aset=Set([])
        self.nbh=Set([])
def metric(p1,p2):
    res=0
    for i in range(len(p1.cord)):
        res+=(p1.cord[i]-p2.cord[i])**2
    return sqrt(res)
def gen_clique(cands,nocands,intersect,clq,res):
    while len(cands)!=0 and not intersect.issubset(nocands):
        for v in cands:
            break
        clq.add(v)
        new_cands=cands.intersection(v.nbh)
        new_nocands=nocands.intersection(v.nbh)
        new_intersect=intersect.intersection(v.nbh)
        if len(new_cands)==0 and len(new_nocands)==0:
            res=copy(clq)
            return res
        else:
            res=gen_clique(new_cands,new_nocands,new_intersect,clq,res)
            if len(res)!=0:
                #print res
                return res
            clq.discard(v)
            cands.discard(v)
            nocands.add(v)
    return clq
class graph(object):
    def __init__(self,elements):
        self.nds=elements
    def crasets(self,subd):
        for i in range(len(self.nds)):
            for j in self.nds[:i]+self.nds[i+1:]:
                if subd<=metric(self.nds[i],j):
                    self.nds[i].aset.add(j)
                else:
                    self.nds[i].nbh.add(j)
    def g_cl(self):
        cliques=Set([])
        for i in self.nds:
            cliques.add(gen_clique(i.nbh,i.aset,i.nbh,Set([i]),Set([])))
        print cliques