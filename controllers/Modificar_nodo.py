from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *

from views.UI_Modificar_nodo import *
from controllers.nodo import Nodo

class Modificar_nodo(QDialog):
	"""docstring for Modificar_nodo"""
	def __init__(self, nodo_manager, lista_nodos, table_widget, call_widget):
		super().__init__()
		self.ui = UI_Modificar_nodo()
		self.ui.setupUi(self)
		point = call_widget.pushButton_20.rect().bottomRight()
		global_point = call_widget.pushButton_20.mapToGlobal(point)
		self.move(global_point - QPoint(self.width(), 0))

		self.updated = False

		self.nodo_manager = nodo_manager
		self.lista_nodos = lista_nodos
		self.table_widget = table_widget

		self.ui.lineEdit.setText(lista_nodos[table_widget.currentRow()].get_nombre_serv())
		self.ui.lineEdit_2.setText(lista_nodos[table_widget.currentRow()].get_titulo_ea())
		self.ui.lineEdit_3.setText(lista_nodos[table_widget.currentRow()].get_ip())
		self.ui.lineEdit_4.setText(lista_nodos[table_widget.currentRow()].get_puerto())
		self.ui.comboBox.setCurrentText(lista_nodos[table_widget.currentRow()].get_tipo())

		self.ui.pushButton.clicked.connect(self.modificar_a_lista)
		

	def modificar_a_lista(self):
		self.hide()
		nombre_serv = self.lista_nodos[self.table_widget.currentRow()].get_nombre_serv()
		titulo_ea = self.lista_nodos[self.table_widget.currentRow()].get_titulo_ea()
		ip = self.lista_nodos[self.table_widget.currentRow()].get_ip()
		puerto = self.lista_nodos[self.table_widget.currentRow()].get_puerto()
		tipo = self.lista_nodos[self.table_widget.currentRow()].get_tipo()

		new_data = [tipo, nombre_serv, titulo_ea, ip, puerto]
			
		if nombre_serv != self.ui.lineEdit.text():
			self.updated = True
			new_data[1] = self.ui.lineEdit.text()	

		if titulo_ea != self.ui.lineEdit_2.text():
			self.updated = True
			new_data[2] = self.ui.lineEdit_2.text()
		
		if ip != self.ui.lineEdit_3.text():
			self.updated = True
			new_data[3] = self.ui.lineEdit_3.text()
		
		if puerto != self.ui.lineEdit_4.text():
			self.updated = True
			new_data[4] = self.ui.lineEdit_4.text()
		
		if tipo != self.ui.comboBox.currentText():
			self.updated = True
			new_data[0] = self.ui.comboBox.currentText()

		if self.updated == True:

			old_obj = self.lista_nodos[self.table_widget.currentRow()]
			obj = Nodo(new_data[0], new_data[1], new_data[2], new_data[3], new_data[4])
			indice_fila = self.table_widget.currentRow()

			self.nodo_manager.update(old_obj, obj)
			self.lista_nodos[self.table_widget.currentRow()] = obj

			for indice_col in range(5):

				item = QtWidgets.QTableWidgetItem()
				item.setTextAlignment(Qt.AlignCenter)

				item.setData(Qt.EditRole, new_data[indice_col])
				self.table_widget.setItem(indice_fila, indice_col, item)
				indice_col += 1

