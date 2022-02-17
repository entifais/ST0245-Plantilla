try:    
    import pandas as pd
except:
    print("please install pandas\npip install pandas")

try:
    import pydeck as pdk
except:
    print("please install pydeck\npip install pydeck")
try:
    FILE="calles_de_medellin_con_acoso.csv"
    data=pd.read_csv(FILE, on_bad_lines='skip')
except:
    SOURCEURL="https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv"
    data=pd.read_csv(SOURCEURL, on_bad_lines='skip')
    print(data.to_string())

view = pdk.ViewState(latitude=6.256405968932449, longitude= -75.59835591123756, pitch=50, zoom=9)
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

r = pdk.Deck(layers=[layer], initial_view_state=view)
r.to_html('mapa_inutil.html')