import networkx as nx
import pandas as pd
import pydeck as pdk


data = pd.read_json("graph_medellin_all_data.json")#.head(10000)
Grafo = nx.Graph()

source=""
tarjet=""

for i in range(len(data)):
    node=data["node"][i]
    weight=(data["length"][i])#+data["harassmentRisk"][i])
    Grafo.add_edge(str(data["path"][i][0]),str(data["path"][i][1]),weight=weight)
    Grafo.add_node(str(node))
    if i==4:
        source=node
    if i==len(data)-1:
        tarjet=node
print(data["path"].head(2))
#print(nx.to_edgelist(Grafo))

djNodes=nx.dijkstra_path(Grafo, "[-75.5728593, 6.2115169]", "[-75.5705202, 6.2106275]", weight='weight')
djPath=[]

tmp=list(Grafo.edges(djNodes,data=True))
for i in range(len(tmp)):
    djPath.append([tmp[i][0],tmp[i][1]])


#print(tmp[i][0]+tmp[i][1])
#print(djNodes,djPath,len(djNodes),len(djPath))
#print(djPath,len(djNodes),len(djPath))
#,source,tarjet)
#pa=nx.bellman_ford_path_length(Grafo,source,tarjet)

path=[]
for i in djNodes:
    path.append(eval(i))
print(djNodes)
#pathdj=pd.DataFrame({"path":path})
#print(data.head(5))
print(data)
"""
[
  {
    "name": "Richmond - Millbrae",
    "path": path
    }
]
"""
pathdj=pd.DataFrame([{"name":"path","path":path}])
print(pathdj)
view = pdk.ViewState(latitude=6.256405968932449, longitude= -75.59835591123756, pitch=20, zoom=9)
layer3 = pdk.Layer(
    type="PathLayer",
    data=pathdj,
    pickable=False,
    get_color=(0,15,205),
    width_scale=5,
    width_min_pixels=5,
    get_path="path",
    get_width=5,
)
layer2 = pdk.Layer(
    "ScatterplotLayer",
    data=pathdj,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=6,
    radius_min_pixels=1,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position="node",
    get_radius=1,
    get_fill_color=[137, 36, 250],
    get_line_color=[0, 0, 0],
)

layer1 = pdk.Layer(
    type="PathLayer",
    data=data,
    pickable=True,
    get_color=(0,155,0),
    width_scale=2,
    width_min_pixels=1,
    get_path="path",
    get_width=1,
)
r = pdk.Deck(layers=[layer3,layer2,layer1], initial_view_state=view)
r.to_html('tmp.html')