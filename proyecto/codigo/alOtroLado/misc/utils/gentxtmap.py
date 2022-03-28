import pandas as pd
import pydeck as pdk
import json

data = pd.read_json("nodes_data.json")

view = pdk.ViewState(latitude=6.2564059689324, longitude= -75.5983559112375, pitch=20, zoom=15)

layer3 =pdk.Layer(
    "TextLayer",
    data=data,
    get_position="node",
    get_size=16,
    get_color=[255, 255, 255],
    get_text="node",
    get_angle=0
)
layer5 = pdk.Layer(
    "TextLayer",
    data=data,
    pickable=True,
    get_position="node",
    get_text="node",
    get_size=16,
    get_color=[0, 0, 0],
    get_angle=0,

)

layer2 = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=3,
    radius_min_pixels=4,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position="node",
    get_radius=1,
    get_fill_color=[137, 36, 250],
    get_line_color=[0, 0, 0],
)
r = pdk.Deck(layers=[], initial_view_state=view)
r.to_html('tmp.html')
