import pandas as pd
#https://towardsdatascience.com/from-dataframe-to-network-graph-bbb35c8ab675
dataclear="["
SOURCEURL="https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv"
FILE="calles_de_medellin_con_acoso.csv"
data=pd.read_csv(FILE, on_bad_lines='skip',sep=";")#.head(1000)
#data.replace(np.nan, 0)
print(data)
origin=data["origin"][0]
origin=(origin[1:-1].split(","))
print(origin[0])
destination=data["destination"][0]
destination=(destination[1:-1].split(","))
print(destination[0])

print(dataclear)
#while True:
#list(data["origin"][0])[1::1]
#print(eval(input()))
for i in range(len(data)): 
  origin=data["origin"][i]
  origin=(origin[1:-1].split(","))
  #print(origin[0])
  destination=data["destination"][i]
  destination=(destination[1:-1].split(","))
  #print(destination[0])
  try:
    dataclear+='{"name":"'+data["name"][i]+'","color": "(255, 255, 255)","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+"]]},"
  except:
    dataclear+='{"name":"'+str(i)+'","color": "(255, 255, 255)","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+"]]},"
    print(i,data["name"][i],origin,destination)
print(dataclear)
"""
 "name": "Richmond - Millbrae",
    "cQolor": "#ed1c24",
    "path": [
      [
        -122.3535851,
        37.9360513
      ],
      [
        -122.3179784,
        37.9249513
      ],
      [
        -122.300284,
        37.902646
      ],
      [
        -122.2843653,
        37.8735039
      ],
      [
        -122.269058,
        37.8694562
      ],
      [
        -122.2709185,
        37.85301
      ],
      [
        -122.2689342,
        37.8283973
      ],
      [
        -122.2707195,
"""
def writetxt(name,content):
  """
  writetxt(name,content) , write in txt file something  
  """
  content =str(content)
  with open(name, 'w') as file:
    file.write(content)
    file.close()
writetxt("out.json",dataclear[:-1]+"]")