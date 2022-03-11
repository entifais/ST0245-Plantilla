import networkx as nx
import pandas as pd

data = pd.read_json("graph_medellin_all_data.json").head(10)
Grafo = nx.Graph()

source=""
tarjet=""
#print(data["node"])
#print(data["node"][0])
for i in range(len(data)):
    #edges=data["path"][i][0]+data["path"][i][1]
    node=data["node"][i]
    #print(type(node))
    weight=(data["harassmentRisk"][i]+data["length"][i])/100
    #print(weight)
    Grafo.add_edge(str(data["path"][i][0]),str(data["path"][i][1]),weight=weight)
    Grafo.add_node(str(node))
    #print(i,"passs\n\n")
    if i==4:
        source=node
    if i==len(data)-1:
        tarjet=node
print(nx.to_edgelist(Grafo))
    #,source,tarjet)
#pa=nx.bellman_ford_path_length(Grafo,source,tarjet)
#print(pa)