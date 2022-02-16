import pydeck as pdk
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#FILE="calles_de_medellin_con_acoso.csv"
SOURCEURL="https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv"
#data=pd.read_csv(SOURCEURL, on_bad_lines='skip')
#data=pd.read_csv(FILE, on_bad_lines='skip')
#print(data.to_string())

view = pdk.ViewState(latitude=6.256405968932449, longitude= -75.59835591123756, pitch=50, zoom=9)
# 2014 locations of car accidents in the UK

# Define a layer to display on a map
layer = pdk.Layer(
    type="PathLayer",
    data=SOURCEURL,
    pickable=True,
    get_color="color",
    width_scale=20,
    width_min_pixels=2,
    get_path="path",
    get_width=5,
)
#https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart-lines.json
#https://deck.gl/docs/api-reference/layers/path-layer
#https://pydeck.gl/gallery/path_layer.html
r = pdk.Deck(layers=[layer], initial_view_state=view)
r.to_html('demo.html')