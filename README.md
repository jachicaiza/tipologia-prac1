# tipologia-prac1
Práctica enfocada en la recolección de datos relacionados a investigadores y conjuntos de datos

# Descripción del proyecto

# Autores
* Janneth Chicaiza Espinosa (jachicaiza)
* Jaime Velandia López (jvelandi)

# Descripción de datasets

Dataset
Método de extracción de datos
Researcher’s Profile: Describe los datos básicos de un investigador, o de un conjunto de investigadores asociados a una institución, de acuerdo a su perfil disponible en Google Scholar.

Librería scholarly (v. 0.2.4) permite extraer información de autores y publicaciones de Google Scholar.
UCI Datasets: Describe las características de cada uno de los conjuntos de datos disponibles en el sitio de UCI Machine Learning Repository.

Técnica de scrapy utilizando la librería bs4 de python (Lawson, 2015)  (*) 

(*) No se encontraron impedimentos para realizar scraping puesto que es una práctica con fines académicos


# Ficheros del código fuente.

Por cada script python: indicar su descripción y requerimientos de su ejecución.

Para scholarly: 
  Requires arrow, 
  Beautiful Soup, 
  bibtexparser, 
  requests
  
Para Scraping
  requests
  urllib
  itertools
  re
  BeautifulSoup
  parser
  import urllib.parse

Adicionalmente para generar archivos CSV y JSON
  json
  os
  
# Recursos bibliográficos

Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.

Friesike, S.; Widenmayer, B.; Gassmann, O.; y Schildhauer, T. (2015). "Opening science: towards an agenda of open science in academia and industry,"" J. Technol. Transf., 40(4), pp. 581–601.

McKiernan, E. C.; Bourne, P. E.; Brown, C. T.; Buck, S.; Kenall, A.; Lin, J.; McDougall, D.; Nosek, B. A.; Ram, K.; Soderberg, C. K.; Spies, J. R.; Thaney, K.; Updegrove, A.; Woo, K. H.; y Yarkoni, T. (2016). How open science helps researchers succeed," Elife, 5.


