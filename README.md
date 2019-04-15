# tipologia-prac1
Práctica enfocada en la recolección de datos relacionados a investigadores y conjuntos de datos.

# Autores
* Janneth Chicaiza Espinosa (https://github.com/jachicaiza)
* Jaime Velandia López (https://github.com/jvelandi)

# Descripción del proyecto
La Ciencia Abierta se ha constituido en un movimiento capaz de acelerar en gran medida la producción y difusión del conocimiento (Friesike, 2015). Gracias a este y otros paradigmas, los investigadores están publicando en la Web sus conjuntos de datos (datasets), así fomentan su reuso y contribuyen a mejorar la colaboración entre los miembros de la comunidad científica.

Esta iniciativa surge con el objetivo de ayudar a los investigadores a encontrar conjuntos de datos que puedan utilizar en sus estudios y experimentaciones. Para conseguir el objetivo propuesto, en este proyecto de la asignatura se han elegido dos métodos de recolección de datos desde la Web: 1) librería scholarly para recoger datos del perfil de investigadores en Google Scholar; y, 2) scrapy para leer los metadatos de los datasets de UCI Learning Machine Repository. 

En base a los intereses de un investigador (con un perfil en Google Scholar), el/ella podría ejecutar los scripts desarrollados para descargar los metadatos de los datasets disponibles en el repositorio seleccionado para la tarea de scrapy. Luego, se podría construir un agente que le recomiende los datasets que le ayude a generar nuevo conocimiento (McKiernan et. al. 2016).


# Descripción de datasets

* Researcher’s Profile: Describe los datos básicos de un investigador, o de un conjunto de investigadores asociados a una institución, de acuerdo a su perfil disponible en Google Scholar. En este caso se utilizó la librería scholarly (v. 0.2.4) para extraer información de los autores de este sitio.

* UCI Datasets: Describe las características de cada uno de los conjuntos de datos disponibles en el sitio de UCI Machine Learning Repository. Se utiliza la librería bs4 de python (Lawson, 2015) para recolectar los metadatos de cada dataset. 

Nota: En el directorio "doc", puede encontrar más información sobre el proyecto, el proceso aplicado y la estructura de cada dataset.

# Ficheros del código fuente

Los siguientes archivos fueron creados y probados en un entorno python 3.7:

* gScholar.py: permite buscar los investigadores de Google Scholar, por su nombre o afiliación. Requiere los siguientes paquetes python: scholarly, bs4,requests, json, os, csv. 
  
  Para que inicie el proceso de recolección, se debe ejecutar el método principal get_author() enviando como parámetro una cadena de texto, que bien puede ser el nombre de un investigador o el de una institución. Por ejemplo:
  
   author = gScholar.get_author('Jordi Conesa')
   
* uciScraper.py: obtiene la lista de todos los datasets disponibles en UCI LM Repository y luego accede a la página descriptiva de cada uno y extrae sus metadatos. Requiere las librerías: requests, urllib, re, bs4, urllib.parse, json, os, csv.
   Para iniciar la extracción de datos, se debe invocar al método principal scraper(), así:
   
   datasetList = uciScraper.scraper()
   
* main.py: invoca a los otros dos archivos, para comenzar la descarga de los datos y posteriomente guardarlos en un directorio específico.


  
# Recursos bibliográficos

* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
* Friesike, S.; Widenmayer, B.; Gassmann, O.; y Schildhauer, T. (2015). "Opening science: towards an agenda of open science in academia and industry,"" J. Technol. Transf., 40(4), pp. 581–601.
* McKiernan, E. C.; Bourne, P. E.; Brown, C. T.; Buck, S.; Kenall, A.; Lin, J.; McDougall, D.; Nosek, B. A.; Ram, K.; Soderberg, C. K.; Spies, J. R.; Thaney, K.; Updegrove, A.; Woo, K. H.; y Yarkoni, T. (2016). How open science helps researchers succeed," Elife, 5.


