#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
alOtrolado - 2022 - por jero98772
alOtrolado - 2022 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
import pandas as pd
import pydeck as pdk
from core.tools import *
app = Flask(__name__)

class webpage():

class configData:
    def __init__(self,file,sep=";"):
        self.file = file
        self.data = pd.read_csv(file,sep=";")

    def downloadCsv():
        self.data.to_csv(index=False)

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
    def __init__(self):
       super().__init__()

    def genMapLayers(layers):
        self.view = pdk.ViewState(latitude=6.256405968932449, longitude= -75.59835591123756, pitch=50, zoom=10)
        #layers.append(mapBase)
        self.mapCompleate = pdk.Deck(layers=layers, initial_view_state=self.view)

    def saveMap(self,fileName):
        self.mapCompleate.to_html('mapa_inutil_y_vende_humo.html')

if __name__=='__main__':
        mapBase = pdk.Layer(
            type="PathLayer",
            data=data,
            pickable=True,
            get_color=(0,155,0),
            width_scale=1,
            width_min_pixels=1,
            get_path="path",
            get_width=1,
        )
	app.run(debug=True,host="0.0.0.0",port=9600)