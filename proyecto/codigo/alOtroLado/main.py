#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
alOtrolado - 2022 - por jero98772
alOtrolado - 2022 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
import pandas as pd
import pydeck as pdk
from core.tools import writetxt

TEMPLATEDIR="templates/"
MAPNAME="map.html"
GENMAPFILE=TEMPLATEDIR+MAPNAME

DATASOURCE="https://raw.githubusercontent.com/entifais/ST0245-Plantilla/master/proyecto/codigo/alOtroLado/data/calles_de_medellin_con_acoso.csv"
DATACSVFILE="data/calles_de_medellin_con_acoso.csv"
DATAJSON="data/medellin_map.json"
app = Flask(__name__)

class webpage():
    @app.route("/")
    def index():
        return render_template("index.html")
    @app.route("/mapBase")
    def webMapBase():
        return render_template("mapBase.html")
    @app.route("/map")
    def webMap():
        return render_template(MAPNAME)

class configData:
    def __init__(self,file,sep=";"):
        self.file = file
        if file[-4:]==".csv":
            self.data = pd.read_csv(file,sep=";")
        if file[-5:]==".json":
            self.data = pd.read_json(file,sep)


    def downloadCsv(self):
        self.data.to_csv(index=False)
    def downloadJson(self):
        self.data.to_json(index=False)

    def getData(self):
        return self.data


    def clearDataJson(name="out.json"):
        dataclear = ""
        for i in range(len(data)): 
            origin = (data["origin"][i][1:-1].split(","))
            destination = (data["destination"][i][1:-1].split(","))
            try:
                dataclear+='{"name":"'+data["name"][i]+'","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+"]]},"
            except:
                dataclear+='{"name":"'+str(i)+'","path": ['+"["+origin[0]+","+origin[1]+"]"+",["+destination[0]+","+destination[1]+"]]},"
        writetxt(name,"["+dataclear[:-1]+"]")

class configMap(configData):
    def __init__(self,layers:list):
       self.layers=layers

    def genMapLayers(self):
        self.view = pdk.ViewState(latitude=6.256405968932449, longitude= -75.59835591123756, pitch=40, zoom=12)
        self.mapCompleate = pdk.Deck(layers=self.layers, initial_view_state=self.view)

    def saveMap(self,fileName):
        try:
            self.mapCompleate.to_html(fileName)
        except:
            writetxt(GENMAPFILE,"")
            self.mapCompleate.to_html(fileName)

if __name__=='__main__':
    """
    datamap=configData(DATAJSON)
    mapBase = pdk.Layer(
            type="PathLayer",
            data=datamap.getData(),
            pickable=True,
            get_color=(0,155,0),
            width_scale=1,
            width_min_pixels=1,
            get_path="path",
            get_width=1,
        )
    allmap=configMap([mapBase])
    allmap.genMapLayers()
    allmap.saveMap(GENMAPFILE) """   
    app.run(debug=True,host="0.0.0.0",port=9600)