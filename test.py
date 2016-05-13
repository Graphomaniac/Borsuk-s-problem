from graph import *
def pdersets(gr):
    if len(gr.nds)!=len(gr.asets):
        gr.crasets(float(raw_input("Don't have subd, input please")))
    for i in range(len(gr.nds)):
        print 
        print gr.nds[i]
        print gr.asets[i]
        print gr.nbh[i]
file=open('set.dat','r+')
lines=file.readlines()
els=[]
for e in lines:
    els.append(node([float(x) for x in e.split()]))
gr = graph(els)
subd=float(raw_input())
gr.crasets(subd)
gr.g_cl()
#pdersets(gr)