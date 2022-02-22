#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
alOtrolado - 2022 - por jero98772
alOtrolado - 2022 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
import pandas as pd
import pydeck as pdk

app = Flask(__name__)

class webpage():

class configData:
    def __init__(self,file,sep=";"):
        self.file=file

    def downloadCsv():
        if ("https" in file  or  "http" in file) and "://" in file:
            self.data=pd.read_csv(self.file)
            self.df.to_csv(index=False)
    def clearData():
class configMap(configData):
	def __init__(self):
		super().__init__()
	def genMap():
	def saveMap():

if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0",port=9600)