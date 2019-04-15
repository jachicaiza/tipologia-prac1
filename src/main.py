import gScholar
import uciScraper


"""1. Obtener datos desde Google Scholar (gScholar.py):
Para iniciar la búsqueda, se puede fijar el nombre de un investigador en concreto
o el nombre de una institución, por ejemplo: Universitat Oberta de Catalunya.
La función devuelve los datos de los investigadores que encajen en el patrón de búsqueda.
"""
print("Obteniendo datos desde Google Scholar")
nameR = 'Jordi Conesa' 
author = gScholar.get_author(nameR)


#Grabar los resultados en formatos csv y json:
nameF = 'researcherGS'
gScholar.save_toCSV(nameF+'.csv', author) # Grabar resultados en  CSV
gScholar.save_toJSON(nameF+'.json', author) # Grabar resultados en archivo JSON


"""2. Obtener datos desde UCI LM Repository (uciScraper.py):
Invocar al método scraper para de forma automática extraer los metadatos de cada dataset disponible en el sitio.
"""
print("Obteniendo datos desde UCI LM Repository")
datasetList = uciScraper.scraper()


#Grabar los resultados en formatos csv y json:
nameF = 'uci'
uciScraper.save_toCSV(nameF+'.csv', datasetList)
uciScraper.save_toJSON(nameF+'.json', datasetList)





 