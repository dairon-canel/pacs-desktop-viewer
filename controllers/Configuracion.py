from PyQt5.QtCore import *
from PyQt5.Qt import QAbstractItemView
from PyQt5.Qt import QHeaderView
from PyQt5.QtWidgets import QMessageBox

from views.UI_Configuracion import *
from controllers.Adicionar_nodo import *
from controllers.Modificar_nodo import *


class Configuracion(QDialog):
	"""docstring for Configuracion"""
	def __init__(self, nodos, nodo_manager):
		super().__init__()
		self.ui = Ui_Dialog_Configuracion()
		self.ui.setupUi(self)
		self.ui.tableWidget_4.verticalHeader().hide()
		self.ui.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget_4.setColumnWidth(0,51)
		self.ui.tableWidget_4.setColumnWidth(1,133)
		self.ui.tableWidget_4.setColumnWidth(2,79)
		self.ui.tableWidget_4.setColumnWidth(3,92)
		self.ui.tableWidget_4.setColumnWidth(4,74)

		self.ui.tableWidget.verticalHeader().hide()
		self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.ui.tableWidget.setColumnWidth(0,200)
		self.ui.tableWidget.setColumnWidth(1,50)
		self.ui.tableWidget.setColumnWidth(2,57)

		
		self.ui.tableWidget_5.verticalHeader().hide()
		self.ui.tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget_5.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget_5.horizontalHeader().setStretchLastSection(True)
		self.ui.tableWidget_5.setColumnWidth(0,150)
		self.ui.tableWidget_5.setColumnWidth(1,140)
		self.ui.tableWidget_5.setColumnWidth(2,140)

		
		self.ui.tableWidget_6.verticalHeader().hide()
		self.ui.tableWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ui.tableWidget_6.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.ui.tableWidget_6.horizontalHeader().setStretchLastSection(True)
		self.ui.tableWidget_6.setColumnWidth(0,150)
		self.ui.tableWidget_6.setColumnWidth(1,70)
		self.ui.tableWidget_6.setColumnWidth(2,100)
		self.ui.tableWidget_6.setColumnWidth(3,57)
		self.ui.tableWidget_6.setColumnWidth(4,50)
		
		self.lista_nodos = nodos
		self.nodo_manager = nodo_manager

		self.ui_adicionar_nodo:Adicionar_nodo
		self.ui_modificar_nodo:Modificar_nodo
		self.mostrar_nodos()

		self.ui.pushButton.setCheckable(True)
		self.ui.pushButton_2.setCheckable(True)
		self.ui.pushButton_3.setCheckable(True)
		self.ui.pushButton_4.setCheckable(True)
		self.ui.pushButton_5.setCheckable(True)
		self.ui.pushButton_6.setCheckable(True)

		self.ui.stackedWidget.setCurrentIndex(0)
		self.ui.pushButton.setChecked(True)

		self.ui.pushButton.clicked.connect(self.stacked_w_set_general)
		self.ui.pushButton_2.clicked.connect(self.stacked_w_set_visor)
		self.ui.pushButton_3.clicked.connect(self.stacked_w_set_bandeja_de_casos)
		self.ui.pushButton_4.clicked.connect(self.stacked_w_set_reportador)
		self.ui.pushButton_5.clicked.connect(self.stacked_w_set_impresion)
		self.ui.pushButton_6.clicked.connect(self.stacked_w_set_licencia)

		self.ui.tableWidget_4.itemSelectionChanged.connect(self.tableWidgetSelection)

		self.current_row = -1
		self.ui.pushButton_21.clicked.connect(self.adicionar_nodo)
		self.ui.pushButton_20.clicked.connect(self.modificar_nodo)
		self.ui.pushButton_19.clicked.connect(self.eliminar_nodo)


	def tableWidgetSelection(self):
		row = self.ui.tableWidget_4.currentRow()
		if  self.current_row == row:
			self.current_row = -1
			self.ui.pushButton_20.setEnabled(False)
			self.ui.pushButton_19.setEnabled(False)
		else:
			self.current_row = self.ui.tableWidget_4.currentRow()	
			self.ui.pushButton_20.setEnabled(True)
			self.ui.pushButton_19.setEnabled(True)

	def stacked_w_set_general(self):
		self.ui.stackedWidget.setCurrentIndex(0)
		self.ui.pushButton.setChecked(True)
		self.ui.pushButton_2.setChecked(False)
		self.ui.pushButton_3.setChecked(False)
		self.ui.pushButton_4.setChecked(False)
		self.ui.pushButton_5.setChecked(False)
		self.ui.pushButton_6.setChecked(False)

	def stacked_w_set_visor(self):
		self.ui.stackedWidget.setCurrentIndex(1)
		self.ui.pushButton.setChecked(False)
		self.ui.pushButton_2.setChecked(True)
		self.ui.pushButton_3.setChecked(False)
		self.ui.pushButton_4.setChecked(False)
		self.ui.pushButton_5.setChecked(False)
		self.ui.pushButton_6.setChecked(False)

	def stacked_w_set_bandeja_de_casos(self):
		self.ui.stackedWidget.setCurrentIndex(2)
		self.ui.pushButton.setChecked(False)
		self.ui.pushButton_2.setChecked(False)
		self.ui.pushButton_3.setChecked(True)
		self.ui.pushButton_4.setChecked(False)
		self.ui.pushButton_5.setChecked(False)
		self.ui.pushButton_6.setChecked(False)

	def stacked_w_set_reportador(self):
		self.ui.stackedWidget.setCurrentIndex(3)
		self.ui.pushButton.setChecked(False)
		self.ui.pushButton_2.setChecked(False)
		self.ui.pushButton_3.setChecked(False)
		self.ui.pushButton_4.setChecked(True)
		self.ui.pushButton_5.setChecked(False)
		self.ui.pushButton_6.setChecked(False)

	def stacked_w_set_impresion(self):
		self.ui.stackedWidget.setCurrentIndex(4)
		self.ui.pushButton.setChecked(False)
		self.ui.pushButton_2.setChecked(False)
		self.ui.pushButton_3.setChecked(False)
		self.ui.pushButton_4.setChecked(False)
		self.ui.pushButton_5.setChecked(True)
		self.ui.pushButton_6.setChecked(False)

	def stacked_w_set_licencia(self):
		self.ui.stackedWidget.setCurrentIndex(5)
		self.ui.pushButton.setChecked(False)
		self.ui.pushButton_2.setChecked(False)
		self.ui.pushButton_3.setChecked(False)
		self.ui.pushButton_4.setChecked(False)
		self.ui.pushButton_5.setChecked(False)
		self.ui.pushButton_6.setChecked(True)

	def mostrar_nodos(self):
		self.nodo_manager.mostrar_nodos(self.ui.tableWidget_4)

	def adicionar_nodo(self):
		self.ui_adicionar_nodo = Adicionar_nodo(self.nodo_manager, self.lista_nodos, self.ui.tableWidget_4, self.ui)
		self.ui_adicionar_nodo.show()

	def modificar_nodo(self):
		self.ui_modificar_nodo = Modificar_nodo(self.nodo_manager, self.lista_nodos, self.ui.tableWidget_4, self.ui)
		self.ui_modificar_nodo.show()

	def eliminar_nodo(self):
		reply = QMessageBox.question(self, "Eliminar nodo", "Esta seguro de querer eliminar el nodo?",
				QMessageBox.Yes | QMessageBox.No)
		
		if reply == QMessageBox.Yes:
			self.nodo_manager.delete(self.lista_nodos.pop(self.current_row))
			self.ui.tableWidget_4.removeRow(self.current_row)
			self.ui.pushButton_20.setEnabled(False)
			self.ui.pushButton_19.setEnabled(False)
		else:
			pass


	
