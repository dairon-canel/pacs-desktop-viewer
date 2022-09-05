from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *

from views.UI_Adicionar_nodo import *
from controllers.nodo import Nodo

class Adicionar_nodo(QDialog):
	"""docstring for Adicionar_nodo"""
	def __init__(self, nodo_manager, lista_nodos, table_widget, call_widget):
		super().__init__()
		self.ui = UI_Adicionar_nodo()
		self.ui.setupUi(self)
		point = call_widget.pushButton_21.rect().bottomRight()
		global_point = call_widget.pushButton_21.mapToGlobal(point)
		self.move(global_point - QPoint(self.width(), 0))

		self.nodo_manager = nodo_manager
		self.lista_nodos = lista_nodos
		self.table_widget = table_widget

		self.ui.pushButton.clicked.connect(self.adicionar_a_lista)
		

	def adicionar_a_lista(self):
		self.hide()
		tipo = self.ui.comboBox.currentText()
		nombre_nodo = self.ui.lineEdit.text()
		titulo_ea = self.ui.lineEdit_2.text()
		ip = self.ui.lineEdit_3.text()
		puerto = self.ui.lineEdit_4.text()
		fila = [tipo, nombre_nodo, titulo_ea, ip, puerto]

		nodox = Nodo(tipo, nombre_nodo, titulo_ea, ip, puerto)
		self.lista_nodos.append(nodox)
		self.nodo_manager.insert(nodox)

		indice_fila = self.table_widget.rowCount()
		self.table_widget.insertRow(indice_fila)

		for indice_col in range(5):

			item = QtWidgets.QTableWidgetItem()
			item.setTextAlignment(Qt.AlignCenter)

			item.setData(Qt.EditRole, fila[indice_col])
			self.table_widget.setItem(indice_fila, indice_col, item)
			indice_col += 1

