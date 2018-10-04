#Necesitas descargar la libreria motionless que es la que uso para la imagen png
#Esta libreria usa la API de google maps para crear mapas estáticos

import requests
from motionless import DecoratedMap, LatLonMarker



#Defino las latitudes y longitudes de origen y destino...
latorigen = -31.438459
longorigen = -64.202148
latdestino = -31.441901
londestino = -64.199753

#Creo el mapa del tipo y zoom que elija. La key la modifiqué desde la clase DecoratedMap
#Lo mejor seria que bajes vos la libreria y modifiques la key aca abajo, cuando crees la clase.
#La key la pones como atributo cuando la creas key=claveTuya
dmap = DecoratedMap(maptype='roadmap', zoom=1)

#Agrego los marcadores
dmap.add_marker(LatLonMarker(latorigen, longorigen, label='O'))
dmap.add_marker(LatLonMarker(latdestino, londestino, label='D'))

#Genero la URL desde donde se descarga la imagen...
url = dmap.generate_url()

#Creo la imagen...
f=open('estatico.png','wb')
f.write(requests.get(url).content)
f.close()


