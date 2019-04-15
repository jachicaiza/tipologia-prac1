# -*- encoding: utf-8 -*-

"""
	Obtiene metadatos de cada dataset disponible en UCI LM Repository
	Fecha de creación: abril de 2019
	Autores: Janneth Chicaiza / Jaime Velandia
	Universidad Oberta de Catalunya
"""

import scholarly
import json
import csv
import os


_entityList = [] # guarda un iterador de los resultados de búsqueda devueltos por la función scholarly.search_author
_data = []	# guarda resultados de búsqueda devueltos por la función scholarly.search_author
_dicAuthor = dict.fromkeys(['name', 'affiliation', 'citedby','email', 'interests', 'url_picture']) # diccionario con la estructura de datos a guardar de cada autor
_dataDir = '../data'

def get_author(strSearch):
	"""Invocar a la función de búsqueda de scholarly y guardar resultados en un iterador"""
	entity = strSearch
	elements = 0
	print("Buscando investigadores que se relacionen con la cadena de búsqueda ...")
	_data = searchEntity(entity)
	dataIter = iter(_data)
	while dataIter:
		try:
			row = next(dataIter)
			print("\t" + row.name)
			_entityList.append(row)
			elements += 1
		except StopIteration:
			break
	if  elements:
		print("Se ha(n) encontrado " + str(elements) + " resultados.")
	else:
		print("No se han encontrado resultados que se relacionen con la cadena de búsqueda.")
	return _entityList

def searchEntity(entity):
	"""Búsqueda de una institución o investigador en concreto"""
	return scholarly.search_author(entity)

def get_name(Author):
	"""Recuperar nombre de autor"""
	try:
		if Author.name:
			return Author.name
	except:
		return None

def get_affiliation(Author):
	"""Recuperar afiliación de autor"""
	try:
		if Author.affiliation:
			return Author.affiliation
	except:
		return None

def get_citedby(Author):
	"""Recuperar cantidad de citas de un autor"""
	try:
		if Author.citedby:
			return Author.citedby
	except:
		return None

def get_email(Author):
	"""Recuperar correo electrónico de autor"""
	try:
		if Author.email:
			return Author.email
	except:
		return None

def get_interests(Author):
	"""Recuperar intereses de autor"""
	try:
		if Author.interests:
			return Author.interests
	except:
		return None


def get_url_picture(Author):
	try:
		if Author.url_picture:
			return Author.url_picture
	except:
		return None			


def save_toCSV(file, ilist):
	"""Grabar resultados de búsqueda en formato CSV"""
	try:
		create_datadir()  # crear directorio de datos
		lenList = len(ilist)
		filePath = os.path.relpath(os.path.join(_dataDir, file))
		with open(filePath, 'w', newline='') as csvfile:  # abrir el archivo para escritura
			spamw = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC) # especificar características del csv
			spamw.writerow(_dicAuthor) # escribir línea de encabezado del csv (nombres de cada columna de dato)
			for i in range(0, lenList): # recorrer lista de resultados y filtrar ciertos atributos de los autores para grabar en el csv
				row = [get_name(ilist[i]), get_affiliation(ilist[i]), get_citedby(ilist[i]), get_email(ilist[i]), get_interests(ilist[i]), get_url_picture(ilist[i])]
				spamw.writerow(row)
		csvfile.close()
		print("Proceso finalizado. Revise su archivo en " + _dataDir + '/' +file)
	except:
		print("Ocurrió un problema mientras intentaba guardar el archivo")
	


def save_toJSON(file, ilist):
	"""Grabar resultados en formato JSON"""
	lenList = len(ilist)
	header = '{"entities": ['
	try:
		create_datadir()  # crear directorio de datos
		filePath = os.path.relpath(os.path.join(_dataDir, file))
		with open(filePath, 'w') as jsonfile: # abrir el archivo para escritura y escribir primera línea del archivo
				jsonfile.write(header)
		for i in range(0, lenList):
			# obtener datos devueltos por la librería
			dictJSON = {'name': get_name(ilist[i]), 'affiliation':get_affiliation(ilist[i]), 'citedby':get_citedby(ilist[i]), 'email': get_email(ilist[i]), 'interests':get_interests(ilist[i]), 'url_picture': get_url_picture(ilist[i])}
			with open(filePath, 'a') as jsonfile:
				j = json.dumps(dictJSON) # escribir datos de cada autor
				jsonfile.write(j)
				if (i < (lenList-1)):
					jsonfile.write(",\n")
				else:
					jsonfile.write("\n")
		with open(filePath, 'a') as jsonfile:  # finalizar escritura del json
			jsonfile.write(']}')
			jsonfile.close()
		print("Proceso finalizado. Revise su archivo en " + _dataDir + '/' +file)	
	except:
		print("Ocurrió un problema mientras intentaba guardar el archivo")
 

def create_datadir():
	"""Crear directorio de datos"""
	try:
		os.stat(_dataDir)  # el directorio de datos existe
	except:
		os.mkdir(_dataDir)
		print("Creando directorio de datos (data)")


		