#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
alOtrolado - 2022 - por jero98772
alOtrolado - 2022 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
import pandas as pd
import pydeck as pdk
import networkx as nx

from core.tools import writetxt

TEMPLATEDIR="templates/"
MAPNAME="tmp.html"
GENMAPFILE=TEMPLATEDIR+MAPNAME

DATACSVFILE="https://raw.githubusercontent.com/entifais/ST0245-Plantilla/master/proyecto/codigo/alOtroLado/data/calles_de_medellin_con_acoso.csv"
DATACSVFILE="data/calles_de_medellin_con_acoso.csv"
DATAJSON="data/graph_medellin_all_data.json"

app = Flask(__name__)

class webpage():
    @app.route("/")
    def index():
        return render_template("index.html")
    @app.route("/tmp")
    def indextmp():
        return render_template("tmp.html")
    @app.route("/mapBase")
    def webMapBase():
        return render_template("mapBase.html")
    @app.route("/map")
    def webMap():
        return render_template(MAPNAME)
    @app.route("/")
    def config():
        return render_template("config.html")

class configData:
    def __init__(self,file,sep=";"):
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

class graphX():
    def __init__(self,data):
        Grafo = nx.Graph()
        for i in range(len(data)):
            node=data["node"][i]
            weight=(data["length"][i])
            Grafo.add_edge(str(data["path"][i][0]),str(data["path"][i][1]),weight=weight)
            Grafo.add_node(str(node))

    def dijkstra(self):
        djNodes=nx.dijkstra_path(Grafo, "[-75.6909483, 6.338773]", "[-75.5705202, 6.2106275]", weight='weight')
        pathdj=pd.DataFrame([{"name":"path","path":path}])

class configMap:
    def __init__(self,data):

        self.emptyMap = pdk.Layer(
            type="PathLayer",
            data="",
            pickable=True,
            get_color=(0,155,0),
            width_scale=1,
            width_min_pixels=1,
            get_path="path",
            get_width=1,
        )

        self.pathMap = pdk.Layer(
            type="PathLayer",
            data=data,
            pickable=True,
            get_color=(0,155,0),
            width_scale=1,
            width_min_pixels=1,
            get_path="path",
            get_width=2,
        )

        self.nodesMap = pdk.Layer(
            "ScatterplotLayer",
            data=data,
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
    def newPath(self,data,tag="path",color=(0,15,205)):
        newPath = pdk.Layer(
            type="PathLayer",
            data=data,
            pickable=False,
            get_color=color,
            width_scale=5,
            width_min_pixels=5,
            get_path=tag,
            get_width=5,
        )
        return newPath
    def genMapMultlayer(self,fileName,layers:list):
        view = pdk.ViewState(latitude=6.256405968932449, longitude= -75.59835591123756, pitch=40, zoom=12)
        mapCompleate = pdk.Deck(layers=layers, initial_view_state=view)
        try:
            mapCompleate.to_html(fileName)
        except:
            writetxt(GENMAPFILE,"")
            mapCompleate.to_html(fileName)
    
    def getEmptyMap(self):return self.emptyMap
    def getPathMap(self):return self.pathMap
    def getnodesMap(self):return self.nodesMap

if __name__=='__main__':
    data=configData(DATAJSON).getData()
    #data=configData(DATACSVFILE)
    #configData.clearAllDataJson(data.getData())

    maps=configMap(data)
    maps.genMapMultlayer(GENMAPFILE,[maps.getPathMap(),maps.getnodesMap()])
    #graphNetworX(data)
    app.run(debug=True,host="0.0.0.0",port=9600)