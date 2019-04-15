# -*- encoding: utf-8 -*-

"""
	Obtiene metadatos de cada dataset disponible en UCI LM Repository
	Fecha de creación: abril de 2019
	Autores: Janneth Chicaiza / Jaime Velandia
	Universidad Oberta de Catalunya
"""
import requests
import urllib
import re
from bs4 import BeautifulSoup
import urllib.parse
import json
import os
import csv


_domain = "http://archive.ics.uci.edu/ml/"
_page = "datasets.php"
_item_list = []
_datasetsList = []
_dicDataset = dict.fromkeys(['link', 'datasetFolder', 'datasetDescription',
	'title', 'dsFeatures', 'numberObs', 'area', 'atributeType', 'numberAttr', 
	'dateDonated', 'missingValues', 'numberWebHits', 'image'])

_dataDir = '../data'

def scraper():
	"""Extraer metadatos de cada dataset de UCI LM Repository"""
	html = download(_domain+_page)
	soup = BeautifulSoup(html,"html.parser")
	_item_list = getDatasetURI(soup) # Obtener los links de la página
	ilist = set(_item_list) # eliminar duplicados, lista depurada
	#Acceder a cada página de cada dataset y extraer sus metadatos
	for p in ilist:
		url = _domain+p
		htmlDS = download(url)
		if htmlDS:
			soupDS = BeautifulSoup(htmlDS,"html.parser") 
			if 'does not appear to exist' in soupDS.text:
				print('Página no existe: ', url)
			else:
				_datasetsList.append(getDataset(soupDS, url))
		else:
			print('Error obteniendo página: ', url)
	return _datasetsList



def download(url, user_agent='Mozilla/5.0', num_retries=2):
	#Descarga una url. En caso de existir errores errores [500 600], intentar nuevamente.
	#Función adaptada desde (Lawson Richard, 2015)
	print('Descargando: ', url)
	headers = {'User-agent': user_agent}
	request = urllib.request.Request(url, headers=headers)
	try:
		html = urllib.request.urlopen(request).read()
	except urllib.error.URLError as e:
		print('Error descargando:', e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, user_agent, num_retries-1)
	return html

def getDatasetURI(soup):
	"""Obtener todos los links de los datasets disponibles en UCI datasets"""
	item_list = []
	items = soup.find_all(href=re.compile("datasets/"))
	for i in items:
		item_list.append(i.attrs['href'])
	return item_list


def getDataset(soup, url):
    """Generador que retorna objetos de tipo UCIDataset"""
    return UCIDataset(soup, url)


class UCIDataset(object):
	"""Accede a los elementos de cada página para obtener los metadatos"""
	def __init__(self, _data, url):
		if isinstance(_data, str):
			self.title = None
		else:
			"""Retorna un objeto de tipo UCIDataset"""
			details = _data.find_all(class_="normal")  # Obtener algunos elementos de información del dataset
			dataLinks = [a.attrs['href'] for a in details[1].find_all('a')]  # Links al archivo de datos y de la descripción
			self.link = url 
			self.datasetFolder = dataLinks[0].replace('../', _domain)
			self.datasetDescription = (dataLinks[1].replace('../', _domain) if dataLinks[1] != '#' else url + dataLinks[1])
			self.title = _data.title.string.replace('UCI Machine Learning Repository: ', '') # título del dataset
			features = _data.find('table', cellpadding="6")  # características de las variables
			featuresL =  features.find_all('td')
			# Obtener características del dataset
			self.dsFeatures = featuresL[1].text # Data Set Characteristics
			self.numberObs = featuresL[3].text # Number of Instances
			self.area = featuresL[5].text # Area
			self.atributeType = featuresL[7].text # Attribute Characteristics
			self.numberAttr= featuresL[9].text # Number of Attribute
			self.dateDonated= featuresL[11].text # Date Donated
			self.tasks = featuresL[13].text # Associated Tasks
			self.missingValues = featuresL[15].text # Missing Value?
			numberWebHits = featuresL[17] # Number of Web Hits
			if numberWebHits: # Number of Web Hits
				self.numberWebHits = numberWebHits.text
			else:
				self.numberWebHits = None
			self.abstract = details[2].text.split(': ')[1]   # Abstract del dataset
			self.source = details[21].text.replace('\r', '\n')  # Source del dataset
			self.information = details[22].text.replace('\r', '\n')  # Imformation del dataset
			self.attrInformation = details[23].text.replace('\r', '\n')  # Información de los atributos
			img = _data.find_all(src=re.compile("../assets/MLimages/"))	
			self.image = (img[0].attrs['src'].replace('../', _domain) if len(img) else None)

	def get_link(UCIDataset):
		"""Recuperar link de dataset"""
		try:
			if UCIDataset.link:
				return UCIDataset.link
		except:
			return None
 
	def get_datasetFolder(UCIDataset):
		"""Recuperar link del directorio de datos del dataset"""
		try:
			if UCIDataset.datasetFolder:
				return UCIDataset.datasetFolder
		except:
			return None

	def get_datasetDescription(UCIDataset):
		"""Recuperar link de la descripción del dataset"""
		try:
			if UCIDataset.datasetDescription:
				return UCIDataset.datasetDescription
		except:
			return None

	def get_title(UCIDataset):
		"""Recuperar título del dataset"""
		try:
			if UCIDataset.title:
				return UCIDataset.title
		except:
			return None

	def get_dsFeatures(UCIDataset):
		"""Recuperar características del dataset"""
		try:
			if UCIDataset.dsFeatures:
				return UCIDataset.dsFeatures
		except:
			return None

	def get_numberObs(UCIDataset):
		"""Recuperar número de observaciones del dataset"""
		try:
			if UCIDataset.numberObs:
				return UCIDataset.numberObs
		except:
			return None

	def get_area(UCIDataset):
		"""Recuperar número de observaciones del dataset"""
		try:
			if UCIDataset.area:
				return UCIDataset.area
		except:
			return None

	def get_atributeType(UCIDataset):
		"""Recuperar tipo de atributos"""
		try:
			if UCIDataset.atributeType:
				return UCIDataset.atributeType
		except:
			return None

	def get_numberAttr(UCIDataset):
		"""Recuperar número e atributos"""
		try:
			if UCIDataset.numberAttr:
				return UCIDataset.numberAttr
		except:
			return None

	def get_numberAttr(UCIDataset):
		"""Recuperar número e atributos"""
		try:
			if UCIDataset.numberAttr:
				return UCIDataset.numberAttr
		except:
			return None

	def get_dateDonated(UCIDataset):
		"""Recuperar fecha de donación"""
		try:
			if UCIDataset.dateDonated:
				return UCIDataset.dateDonated
		except:
			return None

	def get_missingValues(UCIDataset):
		"""Recuperar fecha de donación"""
		try:
			if UCIDataset.missingValues:
				return UCIDataset.missingValues
		except:
			return None

	def get_numberWebHits(UCIDataset):
		"""Recuperar número de hits del dataset"""
		try:
			if UCIDataset.numberWebHits:
				return UCIDataset.numberWebHits
		except:
			return None

	def get_abstract(UCIDataset):
		"""Recuperar abstract"""
		try:
			if UCIDataset.abstract:
				return UCIDataset.abstract
		except:
			return None


	def get_source(UCIDataset):
		"""Recuperar número de hits del dataset"""
		try:
			if UCIDataset.source:
				return UCIDataset.source
		except:
			return None

	def get_information(UCIDataset):
		"""Recuperar información del dataset"""
		try:
			if UCIDataset.information:
				return UCIDataset.information
		except:
			return None

	def get_attrInformation(UCIDataset):
		"""Recuperar información de atributos"""
		try:
			if UCIDataset.attrInformation:
				return UCIDataset.attrInformation
		except:
			return None

	def get_image(UCIDataset):
		"""Recuperar información de atributos"""
		try:
			if UCIDataset.image:
				return UCIDataset.image
		except:
			return None


def create_datadir():
	"""Crear directorio de datos"""
	try:
		os.stat(_dataDir)  # el directorio de datos existe
	except:
		os.mkdir(_dataDir)
		print("Creando directorio de datos (data)")

def save_toCSV(file, ilist):
	"""Grabar resultados en formato CSV"""
	try:
		create_datadir()  # crear directorio de datos
		filePath = os.path.relpath(os.path.join(_dataDir, file))
		with open(filePath, 'w', newline='') as csvfile:
			spamw = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC) 
			spamw.writerow(_dicDataset)
			for i in range(0, len(ilist)-1): 
				row = [ilist[i].get_link(), ilist[i].get_datasetFolder(), ilist[i].get_datasetDescription(), ilist[i].get_title(),
				ilist[i].get_dsFeatures(), ilist[i].get_numberObs(), ilist[i].get_area(), ilist[i].get_atributeType(), ilist[i].get_numberAttr(),
				ilist[i].get_dateDonated(), ilist[i].get_missingValues(), ilist[i].get_numberWebHits(), ilist[i].get_image()]
				spamw.writerow(row)
		csvfile.close()
		
		print("Proceso finalizado. Revise su archivo en " + _dataDir + '/' + file)	
	except:
		print("Ocurrió un problema mientras intentaba guardar el archivo")


def save_toJSON(file, ilist):
	"""Grabar resultados en formato JSON"""
	data = {} # iniciamos variable para el JSON
	data["dataset"]= []
	try:
		create_datadir()  # crear directorio de datos
		filePath = os.path.relpath(os.path.join(_dataDir, file))
		for i in range(0, len(ilist)-1): 
			mjson = ilist[i] 
			data["dataset"].append({
					"link":mjson.link, 
					"datasetFolder":mjson.datasetFolder, 
					"datasetDescription":mjson.datasetDescription,
					"title":mjson.title, 
					"dsFeatures":mjson.dsFeatures, 
					"numberObs":mjson.numberObs, 
					"area":mjson.area,
					"atributeType":mjson.atributeType, 
					"numberAttr":mjson.numberAttr, 
					"dateDonated":mjson.dateDonated, 
					"missingValues":mjson.missingValues, 
					"numberWebHits":mjson.numberWebHits, 
					"abstract":mjson.abstract, 
					"source":mjson.source,
					"information":mjson.information, 
					"attrInformation":mjson.attrInformation, 
					"image":mjson.image
			}) 
		with open(filePath, 'w') as jsonfile:
			json.dump(data, jsonfile)
			jsonfile.close()
		print("Proceso finalizado. Revise su archivo en " + _dataDir + '/' + file)	
	except:
		print("Ocurrió un problema mientras intentaba guardar el archivo")