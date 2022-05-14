import csv
import pandas as pd
import numpy as np
"""
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
"""
def cretecsv():
    DATACSVFILE="calles_de_medellin_con_acoso.csv"
    data=pd.read_csv(DATACSVFILE,sep=";")
    print(data)
    newdata="name;origin;destination;length;oneway;harassmentRisk;geometry;weights;edges;node\n"
    data["weights"]=""
    data["edges"]=""
    data["node"]=""
    mean=np.mean(data["harassmentRisk"])
    #print("mean",mean)
    with open('new.csv', 'w', newline='') as csvfile:
        file = csv.writer(csvfile, delimiter=';')#,quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            length=data["length"][i]
            #harassmentRisk=data["harassmentRisk"][i]
            node=str(data["origin"][i][1:-1])
            noded=str(data["destination"][i][1:-1])
            edges="[["+str(node)+"],["+str(data["destination"][i][1:-1])+"]]"
            weights=(data["harassmentRisk"][i]*length)/length
            #name=data["name"][i]

            #if i %1000==0:
               #print("works")
            if np.isnan(data["harassmentRisk"][i]) and  (data["name"][i]=="nan" or type(data["name"][i])==type(0.0)):
                weights=(mean*length)/length
                newdata=str(i)+" ;"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(mean)+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)+"\n"
            elif data["name"][i]=="nan" or type(data["name"][i])==type(0.0) :
                #print("name",i)
                #data["name"][i]=str(i)
                newdata=str(i)+" ;"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(data["harassmentRisk"][i])+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)+"\n"
            elif np.isnan(data["harassmentRisk"][i]):# or str(type(testvaluetype))=="<class 'numpy.float64'>":
                #print("harassmentRisk",i)
                #data["harassmentRisk"][i]=mean
                weights=(mean*length)/length
                newdata=str(data["name"][i])+";"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(mean)+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)+"\n"
            else:
                newdata=str(data["name"][i])+";"+str(data["origin"][i])+";"+str(data["destination"][i])+";"+str(data["length"][i])+";"+str(data["oneway"][i])+";"+str(data["harassmentRisk"][i])+";"+str(data["geometry"][i])+";"+str(weights)+";"+str(edges)+";"+str(node)+"\n"
            file.writerow(newdata)        
        #harassmentRisk=data["harassmentRisk"][i]
        #print(newdata)
        #data["node"][i]=node
        #data["edges"][i]=edges
        #data["weights"][i]=weights
    #print(data.to_csv())
    #print(data.to_json())
    #print(help(data.to_csv))
    name="data_csv"
    #writetxt(name+".csv",data.to_csv(sep=";",index=False))
    #writetxt(name+".json",data.to_json())

    #writetxt(name+".csv",newdata)
cretecsv()