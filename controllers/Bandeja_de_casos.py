from PyQt5.QtWidgets import QDialog

from PyQt5.Qt import QAbstractItemView
from PyQt5.Qt import QHeaderView

from views.UI_Bandeja_de_casos import *

class Bandeja_de_casos(QDialog):
	"""docstring for Bandeja_de_casos"""
	def __init__(self, nodos, nodo_manager):
		super().__init__()
		self.ui = Ui_Dialog_Bandeja_de_casos()
		self.ui.setupUi(self)

		self.ui.tableWidget_3.verticalHeader().hide()
		self.ui.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget_3.horizontalHeader().setStretchLastSection(True)
		self.ui.tableWidget_3.setColumnWidth(0,1)
		self.ui.tableWidget_3.setColumnWidth(1,250)
		self.ui.tableWidget_3.setColumnWidth(2,1)
		self.ui.tableWidget_3.setColumnWidth(3,200)
		self.ui.tableWidget_3.setColumnWidth(4,200)
		self.ui.tableWidget_3.setColumnWidth(5,80)
		self.ui.tableWidget_3.setColumnWidth(6,150)
		self.ui.tableWidget_3.setColumnWidth(7,150)
		
		self.ui.tableWidget_4.verticalHeader().hide()
		self.ui.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget_4.horizontalHeader().setStretchLastSection(True)
		self.ui.tableWidget_4.setColumnWidth(0,150)
		self.ui.tableWidget_4.setColumnWidth(1,1)
		self.ui.tableWidget_4.setColumnWidth(2,100)
		self.ui.tableWidget_4.setColumnWidth(3,100)
		self.ui.tableWidget_4.setColumnWidth(4,50)
		
		self.ui.tableWidget_2.verticalHeader().hide()
		self.ui.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget_2.horizontalHeader().setStretchLastSection(True)
		self.ui.tableWidget_2.setColumnWidth(0,1)
		self.ui.tableWidget_2.setColumnWidth(1,250)
		self.ui.tableWidget_2.setColumnWidth(2,1)
		self.ui.tableWidget_2.setColumnWidth(3,200)
		self.ui.tableWidget_2.setColumnWidth(4,200)
		self.ui.tableWidget_2.setColumnWidth(5,200)
		self.ui.tableWidget_2.setColumnWidth(6,200)
		self.ui.tableWidget_2.setColumnWidth(7,50)
			
		self.ui.tableWidget.verticalHeader().hide()
		self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.ui.tableWidget.setColumnWidth(0,110)
		self.ui.tableWidget.setColumnWidth(1,60)
		self.ui.tableWidget.setColumnWidth(2,100)
		self.ui.tableWidget.setColumnWidth(3,50)
		self.ui.tableWidget.setColumnWidth(4,50)

		self.lista_nodos = nodos
		self.nodo_manager = nodo_manager
		self.mostrar_nodos()


	def mostrar_nodos(self):
		self.nodo_manager.mostrar_nodos_bandeja_casos(self.ui.tableWidget)


	


     
     


		