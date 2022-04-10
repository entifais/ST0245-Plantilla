import pandas as pd
import numpy as np
DATACSVFILE="https://raw.githubusercontent.com/entifais/ST0245-Plantilla/master/proyecto/codigo/alOtroLado/data/calles_de_medellin_con_acoso.csv"
DATACSVFILE="data/calles_de_medellin_con_acoso.csv"
def writetxt(name,content,mode="w"):
  """
  writetxt(name,content) , write in txt file something  
  """
  content=str(content)
  with open(name, mode) as file:
    file.write(content)
    file.close()

def readtxt(name):
  """
  readtxt(name) , return txt content as array ,element by line 
  """
  content = []
  with open(name, 'r') as file:
    for i in file.readlines():
      content.append(str(i).replace("\n",""))
  return content
def readtxt2(name):
  """
  readtxt(name) , return txt content as array ,element by line 
  """
  content=""
  with open(name, 'r') as file:
    for i in file.readlines():
      content+=str(i)
      print(content)
  return content

class configData:
    def __init__(self,file,sep=";"):
        self._data=""
        if file[-4:]==".csv":
            self._data = pd.read_csv(file,sep=";")
        if file[-5:]==".json":
            self._data = pd.read_json(file)

    def downloadCsv(self):
        self._data.to_csv(index=False)

    def downloadJson(self):
        self._data.to_json(index=False)

    def getData(self):
        return self._data
        
    def clearDataJsonRoutes(data,name="out.json"):
        dataclear = ""
        for i in range(len(data)): 
            origin = (data["origin"][i][1:-1].split(","))
            destination = (data["destination"][i][1:-1].split(","))
            try:
                dataclear+='{"name":"'+data["name"][i]+'","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+"]]},"
            except:
                dataclear+='{"name":"'+str(i)+'","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+"]]},"
        writetxt(name,"["+dataclear[:-1]+"]")
    
    def clearAllDataJson(data,name="out.json"):
        dataclear = ""
        for i in range(len(data)): 
            origin = (data["origin"][i][1:-1].split(","))
            destination = (data["destination"][i][1:-1].split(","))
            try:
                dataclear+='{"name":"'+data["name"][i]+'","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+']],"node":['+origin[0]+","+origin[1]+'],"harassmentRisk":'+str(data["harassmentRisk"][i]).replace("nan","0")+',"length":'+str(data["length"][i])+'},'
            except:
                dataclear+='{"name":"'+str(i)+'","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+']],"node":['+origin[0]+","+origin[1]+'],"harassmentRisk":0,"length":'+str(data["length"][i])+'},'
        writetxt(name,"["+dataclear[:-1]+"]")

    def clearAllDataJson2(data,name="out.json"):
        dataclear = ""
        for i in range(len(data)): 
            origin = (data["origin"][i][1:-1].split(","))
            destination = (data["destination"][i][1:-1].split(","))
            dataclear+='{"name":"'+data["name"][i]+'","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+']],"node":['+origin[0]+","+origin[1]+'],"harassmentRisk":'+str(data["harassmentRisk"][i]).replace("nan","0")+',"length":'+str(data["length"][i])+'},'
        writetxt(name,"["+dataclear[:-1]+"]")


    def createNodes(self,data,name="out.json"):
        data=self.data
        dataclear = ""
        for i in range(len(data)): 
            origin = (data["origin"][i][1:-1].split(","))
            destination = (data["destination"][i][1:-1].split(","))
            try:
                dataclear+='{"name":"'+data["name"][i]+'","node":['+origin[0]+','+origin[1]+']},'
            except:
                dataclear+='{"name":"'+str(i)+'","node":['+origin[0]+','+origin[1]+']},'
        writetxt(name,"["+dataclear[:-1]+"]")

    def totalclearcsv(self,data,name="out.csv"):
        data=self.data
        dataclear = ""
        for i in range(len(data)): 
            origin = (data["origin"][i][1:-1].split(","))
            destination = (data["destination"][i][1:-1].split(","))
            try:
                dataclear+='{"name":"'+data["name"][i]+'","node":['+origin[0]+','+origin[1]+']},'
            except:
                dataclear+='{"name":"'+str(i)+'","node":['+origin[0]+','+origin[1]+']},'
        writetxt(name,"["+dataclear[:-1]+"]")

def main():
    #data=configData(DATACSVFILE)
    #riesgo de un trayecto * distancia del trayecto  ) / ( suma de distancia de los trayectos
    data=pd.read_csv(DATACSVFILE,sep=";").head(4000)
    data["weights"]=""
    data["edges"]=""
    data["node"]=""
    mean=np.mean(data["harassmentRisk"])
    print("mean",mean)
    for i in range(len(data)):
        length=data["length"][i]
        name=data["name"][i]
        if i %1000==0:
           print("works")
        if name=="nan" or type(name)==type(0.0) :
            print("name",i)
            data["name"][i]=str(i)
        if np.isnan(data["harassmentRisk"][i]):# or str(type(testvaluetype))=="<class 'numpy.float64'>":
            print("harassmentRisk",i)
            data["harassmentRisk"][i]=mean

        harassmentRisk=data["harassmentRisk"][i]
        
        node=[str(data["origin"][i][1:-1])]
        edges="["+str(node)+",["+str(data["destination"][i][1:-1])+"]]"
        weights=(harassmentRisk*length)/length
        data["node"][i]=node
        data["edges"][i]=edges
        data["weights"][i]=weights
    #print(data.to_csv())
    #print(data.to_json())
    #print(help(data.to_csv))
    name="tmp"
    writetxt(name+".csv",data.to_csv(sep=";",index=False))
    writetxt(name+".json",data.to_json())

    #data.to_json()
    #df_csv.to_csv(outputPath, 'again your settings here')
def test():
    data=pd.read_csv(DATACSVFILE,sep=";").head(100)
    #print(help(data))
    #print(help(data.to_csv))
    csvf=data.to_csv(index=False)
    print(csvf)
    writetxt("tmp.csv",csvf)
    data.to_json()
    #print(data)
def createcsv():

    dataclear = ""
def createjson():
    data=pd.read_csv(DATACSVFILE,sep=";").head(4000)
    data["weights"]=""
    data["edges"]=""
    data["node"]=""
    mean=np.mean(data["harassmentRisk"])
    for i in range(len(data)):
        length=data["length"][i]
        name=data["name"][i]
        harassmentRisk=data["harassmentRisk"][i]
        if name=="nan" or type(name)==type(0.0) :
            #print("name",i)
            #data["name"][i]=str(i)
            name=i
        if np.isnan(data["harassmentRisk"][i]):# or str(type(testvaluetype))=="<class 'numpy.float64'>":
            print("harassmentRisk",i)
            #data["harassmentRisk"][i]=mean
            harassmentRisk=mean
        node=[str(data["origin"][i][1:-1])]
        edges="["+str(node)+",["+str(data["destination"][i][1:-1])+"]]"
        weights=(harassmentRisk*length)/length
        data["node"][i]=node
        data["edges"][i]=edges
        data["weights"][i]=weights
        dataclear+='{"name":"'+name+'","node"'+str(node)+'","edges"'+str(edges)+'"weights":'+str(weights)

    
    dataclear = ""
#test()
main()