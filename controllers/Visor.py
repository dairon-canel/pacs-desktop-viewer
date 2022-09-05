from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *

from controllers.stylesheets_changes import *

from views.UI_Visor import *

class Visor(QDialog):
	"""docstring for Visor"""
	def __init__(self):
		super().__init__()
		self.ui = UI_Visor()
		self.ui.setupUi(self)

		self.image_loaded = False

		self.init_visor()
		
		self.ui.stackedWidget.setCurrentIndex(0)
		self.ui.pushButton.setChecked(True)

		self.ui.tabWidget.currentChanged.connect(self.tab_widget_tab_changed)

		self.ui.pushButton.clicked.connect(self.stacked_w_set_abrir)
		self.ui.pushButton_2.clicked.connect(self.stacked_w_set_impres)

		self.ui.pushButton_8.clicked.connect(self.load_image_label)

	def load_image_label(self):
		if self.image_loaded == False:
			self.ui.label_49.setText("Image: Loaded")
			self.ui.pushButton_8.setText("Clear")
			self.image_loaded = True
			self.load_dicom_image()
		elif self.image_loaded == True:
			self.ui.label_49.setText("Image: Not Loaded")
			self.ui.pushButton_8.setText("Load")
			self.image_loaded = False
			self.init_visor()

	def init_visor(self):
		self.ui.frame_87.setEnabled(False)
		self.ui.frame_89.setEnabled(False)
		self.ui.frame_56.setEnabled(False)
		self.ui.frame_63.setEnabled(False)
		self.ui.frame_64.setEnabled(False)
		self.ui.frame_65.setEnabled(False)
		self.ui.frame_66.setEnabled(False)
		self.ui.frame_73.setEnabled(False)
		self.ui.frame_58.setEnabled(False)
		self.ui.frame_62.setEnabled(False)
		self.ui.frame_82.setEnabled(False)
		self.ui.frame_86.setEnabled(False)
		self.ui.frame_106.setEnabled(False)
		self.ui.tabWidget.setTabEnabled(4,False)
		self.ui.tabWidget.tabBar().moveTab(4,5)
		self.ui.label_50.hide()
		self.ui.frame_100.setStyleSheet("QFrame{\n"
"    background-color: transparent;\n"
"}\n"
		)
		self.ui.frame_99.setStyleSheet("QFrame{\n"
"    background-color: transparent;\n"
"}\n"
		)

	def load_dicom_image(self):
		self.ui.frame_87.setEnabled(True)
		self.ui.frame_89.setEnabled(True)
		self.ui.frame_56.setEnabled(True)
		self.ui.frame_63.setEnabled(True)
		self.ui.frame_64.setEnabled(True)
		self.ui.frame_65.setEnabled(True)
		self.ui.frame_66.setEnabled(True)
		self.ui.frame_73.setEnabled(True)
		self.ui.frame_58.setEnabled(True)
		self.ui.frame_62.setEnabled(True)
		self.ui.frame_82.setEnabled(True)
		self.ui.frame_86.setEnabled(True)
		self.ui.frame_106.setEnabled(True)
		self.ui.tabWidget.setTabEnabled(5,True)
		self.ui.tabWidget.tabBar().moveTab(5,4)
		update_tab_tools(self.ui.tabWidget, self.ui.frame_122, self.image_loaded)
		self.ui.label_50.show()
		self.ui.frame_100.setStyleSheet("QFrame{\n"
"    background-color: red;\n"
"}\n"
		)
		self.ui.frame_99.setStyleSheet("QFrame{\n"
"    background-color: blue;\n"
"}\n"
		)
	
	def tab_widget_tab_changed(self):
		update_tab_tools(self.ui.tabWidget, self.ui.frame_122, self.image_loaded)
			
	def stacked_w_set_abrir(self):
		self.ui.stackedWidget.setCurrentIndex(0)
		self.ui.pushButton.setChecked(True)
		self.ui.pushButton_2.setChecked(False)

	def stacked_w_set_impres(self):
		self.ui.stackedWidget.setCurrentIndex(1)
		self.ui.pushButton.setChecked(False)
		self.ui.pushButton_2.setChecked(True)
