import sqlite3
from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton
from PyQt5.Qt import QAbstractItemView
from PyQt5.Qt import QHeaderView

class NodeDoesNotExist(Exception):
	pass

class Nodo_Manager(object):
	
	def __init__(self, database = None):
		if not database:
			database = "models/node_database.db"
		self.conn = sqlite3.connect(database)
		self.cursor = self.conn.cursor()

	def insert(self, obj):
		query = 'INSERT INTO node VALUES ("{}", "{}", "{}", "{}", "{}" )'.format(obj.tipo, obj.nombre_serv, obj.titulo_ea, obj.ip, obj.puerto)
		self.cursor.execute(query)
		self.conn.commit()
		
	def get(self, nombre_serv):
		query = 'SELECT * FROM node WHERE nombre_serv = "{}"'.format(nombre_serv)
		self.cursor.execute(query)
		data = self.cursor.fetchone()
		if not data:
			raise NodeDoesNotExist("No existe el nodo de nombre {}".format(nombre_serv))
		return Nodo(tipo = data[0], nombre_serv = data[1], titulo_ea = data[2], ip = data[3], puerto = data[4])

	def filter(self, **kwargs):
		tipo = kwargs.get("tipo")
		nombre_serv = kwargs.get("nombre_serv")
		titulo_ea = kwargs.get("titulo_ea")
		ip = kwargs.get("ip")
		puerto = kwargs.get("puerto")

		condition = " WHERE"
		add_and = False
		add_condition = False

		if tipo:
			condition += ' tipo = "{}"'.format(tipo)
			add_condition = True
			add_and = False
		if nombre_serv:
			if add_and:
				condition += ' AND'
			condition += ' nombre_serv = "{}"'.format(nombre_serv)
			add_condition = True
			add_and = False
		if titulo_ea:
			if add_and:
				condition += ' AND'
			condition += ' titulo_ea = "{}"'.format(titulo_ea)
			add_condition = True
			add_and = False
		if ip:
			if add_and:
				condition += ' AND'
			condition += ' ip = "{}"'.format(ip)
			add_condition = True
			add_and = False
		if puerto:
			if add_and:
				condition += ' AND'
			condition += 'puerto = "{}" '.format(puerto)
			add_condition = True
			add_and = False
		
		query = 'SELECT * FROM node'
		if add_condition:
			query += condition
		print(query)
		self.cursor.execute(query)
		result = self.cursor.fetchall()

		nodes = []
		for data in result:
			node = Nodo(tipo = data[0], nombre_serv = data[1], titulo_ea = data[2], ip = data[3], puerto = data[4])
			nodes.append(node)

		return nodes
	
	def update(self, old_obj, obj):
		updated = False
		add_coma = False

		query = 'UPDATE node SET '

		if old_obj.tipo != obj.tipo:
			if add_coma:
				query += ', '
			query += 'tipo = "{}" '.format(obj.tipo)
			updated = True
			add_coma = True
		if old_obj.nombre_serv != obj.nombre_serv:
			if add_coma:
				query += ', '
			query += 'nombre_serv = "{}" '.format(obj.nombre_serv)
			updated = True
			add_coma = True
		if old_obj.titulo_ea != obj.titulo_ea:
			if add_coma:
				query += ', '
			query += 'titulo_ea = "{}" '.format(obj.titulo_ea)
			updated = True
			add_coma = True
		if old_obj.ip != obj.ip:
			if add_coma:
				query += ', '
			query += 'ip = "{}" '.format(obj.ip)
			updated = True
			add_coma = True		
		if old_obj.puerto != obj.puerto:
			if add_coma:
				query += ', '
			query += 'puerto = "{}" '.format(obj.puerto)
			updated = True
			add_coma = True

		if updated:
			query += 'WHERE tipo = "{}" '.format(old_obj.tipo)
			query += 'AND nombre_serv = "{}" '.format(old_obj.nombre_serv)
			query += 'AND titulo_ea = "{}" '.format(old_obj.titulo_ea)
			query += 'AND ip = "{}" '.format(old_obj.ip)
			query += 'AND puerto = "{}" '.format(old_obj.puerto)
			self.cursor.execute(query)
			self.conn.commit()

	def delete(self, obj):
		query = 'DELETE FROM node WHERE tipo = "{}" '.format(obj.tipo)
		query += 'AND nombre_serv = "{}" '.format(obj.nombre_serv)
		query += 'AND titulo_ea = "{}" '.format(obj.titulo_ea)
		query += 'AND ip = "{}" '.format(obj.ip)
		query += 'AND puerto = "{}" '.format(obj.puerto)
		self.cursor.execute(query)
		self.conn.commit()

	def mostrar_nodos(self, table_widget):
		self.lista_nodos = self.filter()
		lista = []
		if self.lista_nodos:
			for node in self.lista_nodos:
				indice_fila = table_widget.rowCount()
				table_widget.insertRow(indice_fila)
				lista = [node.get_tipo(), node.get_nombre_serv(), node.get_titulo_ea(), node.get_ip(), node.get_puerto()]

				for indice_col in range(5):

					item = QTableWidgetItem()
					item.setTextAlignment(Qt.AlignCenter)

					item.setData(Qt.EditRole, lista[indice_col])
					table_widget.setItem(indice_fila, indice_col, item)
					indice_col += 1

	def mostrar_nodos_bandeja_casos(self, table_widget):
		self.lista_nodos = self.filter(tipo = "Servidor")
		lista = []
		if self.lista_nodos:
			for node in self.lista_nodos:
				indice_fila = table_widget.rowCount()
				table_widget.insertRow(indice_fila)
				lista = [node.get_nombre_serv(), node.get_titulo_ea(), node.get_ip(), node.get_puerto()]

				for indice_col in range(4):

					item = QTableWidgetItem()
					item.setTextAlignment(Qt.AlignCenter)

					item.setData(Qt.EditRole, lista[indice_col])
					table_widget.setItem(indice_fila, indice_col, item)
					indice_col += 1

				btn = QPushButton(table_widget)
				btn.setText('')
				btn.setStyleSheet("QPushButton{\n"
"	margin: 4 25 4 25;\n"
"	background-color: transparent;\n"
"	image: url(:/bandeja_de_casos/assets/bandeja_de_casos/ServerOff.png);"
"	}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.455273, y1:1, x2:0.460273, y2:0, stop:0 rgba(253, 247, 225, 255), stop:0.301136 rgba(252, 228, 137, 255), stop:0.829545 rgba(253, 235, 168, 255), stop:1 rgba(253, 238, 177, 255));\n"
"	border-top: 2px solid qlineargradient(spread:pad, x1:0.465909, y1:0, x2:0.465909, y2:1, stop:0 rgba(241, 202, 88, 255), stop:1 rgba(253, 249, 232, 255));\n"
"	border-right: 2px solid qlineargradient(spread:pad, x1:0.994318, y1:0.568, x2:0, y2:0.568, stop:0 rgba(241, 204, 84, 255), stop:1 rgba(253, 246, 221, 255));\n"
"	border-bottom: 2px solid qlineargradient(spread:pad, x1:0.471, y1:1, x2:0.494, y2:0, stop:0 rgba(244, 213, 73, 255), stop:1 rgba(253, 253, 235, 255));\n"
"	border-left: 2px solid qlineargradient(spread:pad, x1:0, y1:0.642, x2:1, y2:0.659, stop:0 rgba(242, 205, 83, 255), stop:1 rgba(253, 246, 223, 255));\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.477, y2:0.426, stop:0 rgba(254, 226, 135, 255), stop:1 rgba(250, 214, 121, 255));\n"
"	border-top: 2px solid qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.517, y2:1, stop:0 rgba(194, 118, 43, 255), stop:1 rgba(246, 200, 103, 255));\n"
"	border-right: 2px solid qlineargradient(spread:pad, x1:1, y1:0.557, x2:0, y2:0.563, stop:0 rgba(194, 128, 50, 255), stop:1 rgba(248, 208, 113, 255));\n"
"	border-bottom: 2px solid qlineargradient(spread:pad, x1:0.449, y1:1, x2:0.449, y2:0, stop:0 rgba(194, 158, 71, 255), stop:1 rgba(250, 215, 122, 255));\n"
"	border-left: 2px solid qlineargradient(spread:pad, x1:0, y1:0.545455, x2:1, y2:0.54, stop:0 rgba(194, 132, 53, 255), stop:1 rgba(248, 209, 114, 255));\n"
"}\n"
"}")
				table_widget.setCellWidget(indice_fila, 4, btn)
				btn.clicked.connect(partial(self.button_pressed, indice_fila))


	def button_pressed(self, indice_fila:int):
		print("Button %d pressed" %(indice_fila))

class Nodo(object):

	def __init__(self, tipo, nombre_serv, titulo_ea, ip, puerto):
		self.tipo = tipo
		self.nombre_serv = nombre_serv
		self.titulo_ea = titulo_ea
		self.ip = ip
		self.puerto = puerto

	def get_tipo(self):
		return self.tipo
	def get_nombre_serv(self):
		return self.nombre_serv
	def get_titulo_ea(self):
		return self.titulo_ea
	def get_ip(self):
		return self.ip
	def get_puerto(self):
		return self.puerto

	def set_tipo(self, tipo):
		self.tipo = tipo
	def set_nombre_serv(self, nombre_serv):
		self.nombre_serv = nombre_serv
	def set_titulo_ea(self, titulo_ea):
		self.titulo_ea = titulo_ea
	def set_ip(self, ip):
		self.ip = ip
	def set_puerto(self, puerto):
		self.puerto = puerto

	def connect(self):
		pass


	