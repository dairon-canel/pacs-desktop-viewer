import sys
import ctypes

from PyQt5.QtWidgets import QApplication

from controllers.Bandeja_de_casos import *
from controllers.Configuracion import *
from controllers.Visor import *

from controllers.nodo import Nodo_Manager


def main():

	app = QApplication(sys.argv)

	myappid = u'ryuzaks.aitools.tool.1'
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	
	nodo_manager = Nodo_Manager("models/node_database.db")
	nodos_conexion = nodo_manager.filter()
	bandeja_de_casos = Bandeja_de_casos(nodos_conexion, nodo_manager)
	configuracion = Configuracion(nodos_conexion, nodo_manager)
	visor = Visor()

	def show_Configuracion():
		configuracion.show()

	def show_Visor():
		visor.show()

	bandeja_de_casos.ui.toolButton_10.clicked.connect(show_Configuracion)
	bandeja_de_casos.ui.toolButton_2.clicked.connect(show_Visor)

	bandeja_de_casos.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()