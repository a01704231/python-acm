'''
==== DESCRIPCIÓN ====
# Nombre: KOKAS 
# Matrícula: A1704518
Generar un mapa en html 
====================
'''


'''
==== LIBRERÍAS ====
Importamos la librería folium 
https://python-visualization.github.io/folium/ 
Es plugin de javascript adaptado al ecosistema de python 
===================
'''
# pip install folium
import folium 

'''
==== COMANDOS ====
En la documentación podrás encontrar diferentes comandos interesantes.
Para este caso utilizaremos "Map" para generar un mapa.
Escribimos una variable "map" que estará guardando el mapa, primeramente tenemos que escribir "folium";
ya que tenemos que referenciar de donde se están sacando los comando. 
Luego escribimos la fucnión "Map" y los paramentros de la función ("latitud y longitud").
==================
'''
# folium.Map(location=[latitud, longitud])
map=folium.Map(location=[20.8416003,-100.3802813])

'''
==== GUARDAR ====
Indicamos a la variable "map" que se guarde en formato html 
=================
'''
# Salvamos el mapa en formato html
map.save("map.html")
















import KOKAS as p__q
p__q.Kokas().H0()
