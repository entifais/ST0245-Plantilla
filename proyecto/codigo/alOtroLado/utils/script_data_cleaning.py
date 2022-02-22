import pandas as pd

dataclear=""
SOURCEURL="https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv"

try:
    FILE="calles_de_medellin_con_acoso.csv"
    data=pd.read_csv(FILE, on_bad_lines='skip')
except:
    data=pd.read_csv(SOURCEURL, on_bad_lines='skip',sep=";")
print(data)

#dataclear+="name'"+data[i]["name"][0]+",'color': '#ffffff','path': "list(data["origin"][0][])#+data[i]["name"][0]
print(data["origin"][0])
#eval(list(data["origin"][0])[1:-1])
while True:
#list(data["origin"][0])[1::1]
  print(eval(input()))
"""
for i in range(len(data)): 
  dataclear+="name'"+data["name"][i]+",'color': '#ffffff','path': "#+data[i]["name"][0]
  print(dataclear)
 "name": "Richmond - Millbrae",
    "color": "#ed1c24",
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