import networkx
import matplotlib.pyplot as plot
import collections
import copy
import networkx_addon

def simrank(G, r=0.9, max_iter=100):
    # init. vars
    sim_old = collections.defaultdict(list)
    sim = collections.defaultdict(list)
    for n in G.nodes():
        sim[n] = collections.defaultdict(int)
        sim[n][n] = 1
        sim_old[n] = collections.defaultdict(int)
        sim_old[n][n] = 0
    print("sim=======",sim)
    print("sim_old.keys===",sim_old.keys())



    # recursively calculate simrank
    for iter_ctr in range(max_iter):
        print("\nstart***************",iter_ctr)
        if _is_converge(sim, sim_old):
            break
        sim_old = copy.deepcopy(sim)
        for u in G.nodes():
            for v in G.nodes():
                if u == v:
                    continue
                s_uv = 0.0
                for n_u in G.neighbors(u):
                    for n_v in G.neighbors(v):
                        print("u===",u,"v===",v,"n_u=",n_u,"n_v=",n_v,"sim_old=",sim_old[n_u][n_v])
                        s_uv += sim_old[n_u][n_v]

                sim[u][v] = (r * s_uv / (len(G.neighbors(u)) * len(G.neighbors(v))))
                print("sim[u][v]=====",u,v,sim[u][v])
        print("sim=====", sim)
    return sim


def _is_converge(s1, s2, eps=1e-4):
    for i in s1.keys():
        for j in s1[i].keys():
            if abs(s1[i][j] - s2[i][j]) >= eps:
                return False
    return True


##-------------------------------自定义simrank调用
G=networkx.Graph()
G.add_edges_from([('a','b'),('b','c'),('a','c'),('c','d')])
sim=simrank(G)
print(sim)

##-------------------------------------
 #直接调用networkx_addon
'''
G = networkx.Graph()
G.add_edges_from([(0, 7), (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4), (4, 5), (4, 6)])
s=networkx_addon.similarity.simrank(G)
print(s)
'''


