#Necesitas descargar la libreria motionless que es la que uso para la imagen png
#Esta libreria usa la API de google maps para crear mapas estaticos

import requests
from motionless import DecoratedMap, LatLonMarker



#Defino las latitudes y longitudes de origen y destino...
latorigen = -31.438459
longorigen = -64.202148
latdestino = -31.441901
londestino = -64.199753

#Creo el mapa del tipo y zoom que elija. La key la modifique desde la clase DecoratedMap
#Lo mejor seria que bajes vos la libreria y modifiques la key aca abajo, cuando crees la clase.
#La key la pones como atributo cuando la creas key=claveTuya
road_styles = [ { 'feature': 'road.highway','element': 'geomoetry','rules': {'visibility': 'off','color': '#c280e9'} }
              , { 'feature': 'transit.line','rules': {'visibility': 'simplified','color': '#bababa'}}
              , { 'feature': 'road', "element": "labels.text", "rules": { "visibility": "off" } }
              , { 'feature': 'poi', "element" : "labels.text","rules": { "visibility": "off" } }
              , { 'feature': 'landscape', "element" : "labels.text","rules": { "visibility": "off" } } 
              , { 'feature': 'transit', "element" : "labels.text","rules": { "visibility": "off" } }
              , { 'feature': 'administrative', "element" : "labels.text","rules": { "visibility": "off" } } ]

dmap = DecoratedMap(style=road_styles,maptype='roadmap', zoom=15)

#Agrego los marcadores
dmap.add_marker(LatLonMarker(latorigen, longorigen, label='O',color='blue'))
dmap.add_marker(LatLonMarker(latdestino, londestino, label='D'))

#Genero la URL desde donde se descarga la imagen...
url = dmap.generate_url()

#Creo la imagen...
f=open('estatico.png','wb')
f.write(requests.get(url).content)
f.close()


