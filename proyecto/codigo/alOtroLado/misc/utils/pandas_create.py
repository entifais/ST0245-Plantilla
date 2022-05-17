import pandas as pd
import numpy as np

DATACSVFILE="data/calles_de_medellin_con_acoso.csv"

def ponderate(length,harassmentRisk,pomval=0.025):
    return length*pomval+harassmentRisk

def cretecsv():
    data=pd.read_csv(DATACSVFILE,sep=";")
    print(data)
    newdata="name;origin;destination;length;oneway;harassmentRisk;geometry;weights;edges;node\n"

    mean=np.mean(data["harassmentRisk"])
    names=[]
    harassmentRisk=[]
    weights2=[]
    edges2=[]
    nodes=[]
    for i in range(len(data)):
        length=data["length"][i]
        node=str(data["origin"][i][1:-1])
        noded=str(data["destination"][i][1:-1])
        edges="[["+str(node)+"],["+str(data["destination"][i][1:-1])+"]]"
        weights=(data["harassmentRisk"][i]*length)/length

        if np.isnan(data["harassmentRisk"][i]) and  (data["name"][i]=="nan" or type(data["name"][i])==type(0.0)):
            weights=ponderate(length,mean)
            names.append(str(i))
            harassmentRisk.append(mean)
            weights2.append(weights)
            newdata+=str(i)+";"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(mean)+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)#+"\n"
        elif data["name"][i]=="nan" or type(data["name"][i])==type(0.0) :
            names.append(str(i))
            newdata+=str(i)+";"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(data["harassmentRisk"][i])+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)#+"\n"
        elif np.isnan(data["harassmentRisk"][i]):
            harassmentRisk.append(mean)
            weights=ponderate(length,mean)
            weights2.append(weights)
            newdata+=str(data["name"][i])+";"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(mean)+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)#+"\n"
        else:
            newdata+=str(data["name"][i])+";"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(data["harassmentRisk"][i])+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)#+"\n"
        edges2.append(edges)
        nodes.append(str(nodes))
    newtmpdf=pd.DataFrame(
    {'name': names,
     'harassmentRisk': harassmentRisk,
     'weights': weights2,
     'edges': edges2,
     'node': nodes
    })
    data["name"]=newtmpdf["name"]
    data["harassmentRisk"]=newtmpdf["harassmentRisk"]
    data.insert(len(data), "weights", weights2)
    data.insert(len(data), "edges", edges2)
    data.insert(len(data), "nodes", nodes)

    name="data_pandas"

    data.to_csv(data_pandas)
    data.to_json(data_pandas)

cretecsv()