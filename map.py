import folium
import webbrowser
from folium.plugins import MarkerCluster, HeatMap
import pandas as pd

data = pd.read_csv("C:/Users/beech/Documents/Graduate_School/CS6100/SafeMap/kzoo.csv")

m = folium.Map(
 location=[42.284756, -85.61049],
 zoom_start=14.5
)

lat = data['Latitude'].tolist()
lng = data['Longitude'].tolist()
locations = list(zip(lat,lng))
offense = data['Type'].tolist()

marker_cluster = MarkerCluster(
    name="Incidents by Marker",
    overlay=True,
    control=True
)

marker_cluster.add_to(m)

for i in range(len(lat)):
    location = lat[i], lng[i]
    crime_type = offense[i]
    #marker = folium.Marker(location=location)
    html = '''<b> Incident Type: </b> {}<br>
            Latitude: {}<br>
            Longitude:{}<br>'''.format(crime_type, location[0], location[1])
    iframe = folium.IFrame(html, width=200, height=200)
    popup = folium.Popup(iframe, max_width=200)
    marker = folium.Marker(location= location,popup=popup)
    marker_cluster.add_child(marker)

HeatMap(
    data=list(zip(lat, lng)),
    name="Incidents by Heatmap").add_to(m)
folium.LayerControl().add_to(m)

html_map = m._repr_html_()

webbrowser.open("m.html")
m.save("m.html")
