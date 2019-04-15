# tipologia-prac1
Práctica enfocada en la recolección de datos relacionados a investigadores y conjuntos de datos

# Descripción del proyecto
La Ciencia Abierta se ha constituido en un movimiento capaz de acelerar en gran medida la producción y difusión del conocimiento (Friesike, 2015). Gracias a este y otros paradigmas, los investigadores están publicando en la Web sus conjuntos de datos (datasets), así fomentan su reuso y contribuyen a mejorar la colaboración entre los miembros de la comunidad científica.
Esta iniciativa surge con el objetivo de ayudar a los investigadores a encontrar conjuntos de datos que puedan utilizar en sus estudios y experimentaciones. Para conseguir el objetivo propuesto, en este proyecto de la asignatura se han elegido dos métodos de recolección de datos desde la Web: 1) librería scholarly para recoger datos del perfil de investigadores en Google Scholar; y, 2) scrapy para leer los metadatos de los datasets de UCI Learning Machine Repository. 
En base a los intereses de un investigador (con un perfil en Google Scholar), el/ella podría ejecutar los scripts desarrollados para descargar los metadatos de los datasets disponibles en el repositorio seleccionado para la tarea de scrapy. Luego, se podría construir un agente que le recomiende los datasets que le ayude a generar nuevo conocimiento (McKiernan et. al. 2016).

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
  
Para Scraping:   
  requests
  urllib
  itertools
  re
  BeautifulSoup
  parser
  import urllib.parse

Adicionalmente para generar archivos CSV y JSON:   
  json
  os
  
# Recursos bibliográficos

Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.

Friesike, S.; Widenmayer, B.; Gassmann, O.; y Schildhauer, T. (2015). "Opening science: towards an agenda of open science in academia and industry,"" J. Technol. Transf., 40(4), pp. 581–601.

McKiernan, E. C.; Bourne, P. E.; Brown, C. T.; Buck, S.; Kenall, A.; Lin, J.; McDougall, D.; Nosek, B. A.; Ram, K.; Soderberg, C. K.; Spies, J. R.; Thaney, K.; Updegrove, A.; Woo, K. H.; y Yarkoni, T. (2016). How open science helps researchers succeed," Elife, 5.


