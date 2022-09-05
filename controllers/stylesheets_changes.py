from inspect import _void
from PyQt5.QtWidgets import QTabWidget, QFrame
from PyQt5.QtCore import *

def update_tab_tools(widget:QTabWidget, frame:QFrame, image_load:bool) -> _void:
    qtbw_border_top_0 = "border-top: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(5, 97, 5, 255), stop:1 rgba(254, 254, 254, 255));\n"
    qtbw_border_top_1 = "border-top: 1px solid #C2C7CB;\n"
    qtbw_not_selected_border_bottom = "border-bottom: 2px solid rgb(74, 161, 74);\n"
    qtbw_first_tab_border_bottom = "border-bottom: 1px solid rgb(78, 78, 78);\n"
    qtbw_first_tab_loaded_border_bottom = "border-bottom: 1px solid #ff4500;\n"

    first_tab_selected_style = set_qtbw_styleSheet(qtbw_border_top_0, qtbw_not_selected_border_bottom, qtbw_first_tab_border_bottom)
    else_tab_selected_style = set_qtbw_styleSheet(qtbw_border_top_1, "", qtbw_first_tab_border_bottom)
    first_tab_selected_and_tool_style = set_qtbw_styleSheet(qtbw_border_top_0, qtbw_not_selected_border_bottom, qtbw_first_tab_loaded_border_bottom)

    if image_load == False:
        if widget.currentIndex() == 0:
            widget.setStyleSheet(first_tab_selected_style)
            frame.setStyleSheet("QFrame{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(64, 156, 64, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
		    )
        else:
            widget.setStyleSheet(else_tab_selected_style)
            frame.setStyleSheet("QFrame{\n"
            "    background-color: rgb(78, 78, 78);\n"
            "}\n"
		    )
    
    if image_load == True:
        if widget.currentIndex() == 0:
            widget.setStyleSheet(first_tab_selected_style)
            frame.setStyleSheet("QFrame{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(64, 156, 64, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
	        	)
        elif widget.currentIndex() == 4:
            widget.setStyleSheet(first_tab_selected_and_tool_style)
            frame.setStyleSheet("QFrame{\n"
            "    background-color: #ff4500;\n"
            "}\n"
	    	)
        else:
            widget.setStyleSheet(else_tab_selected_style)
            frame.setStyleSheet("QFrame{\n"
            "    background-color: rgb(78, 78, 78);\n"
            "}\n"
	    	)
   
def set_qtbw_styleSheet(line_archive:str, border_bottom:str, first_tab_border_bottom:str) -> str:
    style_string = ("QTabWidget#tabWidget::pane {\n"
"    %s"
"    top: 0.1ex;\n"
"}\n"
"\n"
"QTabWidget#tabWidget::tab-bar{\n"
"    left: 5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: rgb(201, 201, 201);\n"
"    border: 1px solid rgb(94, 94, 94);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab::disabled {\n"
"    width: 0;\n"
"    height: 0;\n"
"    margin: 0;\n"
"    padding: 0;\n"
"    border: none;\n"
"}\n"
"\n"
"QTabBar::tab:first{\n"
"    color: white;\n"
"    margin-left: 0px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected{\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.528, y1:0, x2:0.523, y2:1, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    border-left: 2px solid qlineargradient(spread:pad, x1:0, y1:0.597, x2:1, y2:0.597, stop:0 rgba(72, 127, 72, 255), stop:0.460227 rgba(72, 128, 72, 255), stop:0.534091 rgba(97, 176, 97, 255), stop:1 rgba(95, 175, 95, 255));\n"
"    border-right: 2px solid qlineargradient(spread:pad, x1:1, y1:0.517, x2:0, y2:0.534, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    border-bottom:  2px solid qlineargradient(spread:pad, x1:0.557, y1:1, x2:0.557, y2:0, stop:0 rgba(4, 97, 4, 255), stop:1 rgba(63, 157, 63, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:0.517045, y1:0, x2:0.523, y2:1, stop:0 rgba(27, 141, 27, 255), stop:1 rgba(100, 178, 100, 255));\n"
"}\n"
"QTabBar::tab:first:selected:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.494318, y1:0, x2:0.511, y2:1, stop:0 rgba(40, 148, 40, 255), stop:1 rgba(124, 190, 124, 255));\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected{\n"
"    background-color: qlineargradient(spread:reflect, x1:0.511, y1:0.522636, x2:0.511, y2:1, stop:0.227273 rgba(3, 129, 3, 255), stop:0.829545 rgba(88, 171, 88, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.528, y1:0, x2:0.523, y2:1, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    border-left: 2px solid qlineargradient(spread:pad, x1:0, y1:0.597, x2:1, y2:0.597, stop:0 rgba(72, 127, 72, 255), stop:0.460227 rgba(72, 128, 72, 255), stop:0.534091 rgba(97, 176, 97, 255), stop:1 rgba(95, 175, 95, 255));\n"
"    border-right: 2px solid qlineargradient(spread:pad, x1:1, y1:0.517, x2:0, y2:0.534, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    %s"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected:hover{\n"
"    background-color: qlineargradient(spread:reflect, x1:0.518, y1:0.477318, x2:0.522727, y2:1, stop:0.261364 rgba(25, 141, 25, 255), stop:1 rgba(126, 191, 126, 255));\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.528, y1:0, x2:0.523, y2:1, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    border-left: 2px solid qlineargradient(spread:pad, x1:0, y1:0.597, x2:1, y2:0.597, stop:0 rgba(72, 127, 72, 255), stop:0.460227 rgba(72, 128, 72, 255), stop:0.534091 rgba(97, 176, 97, 255), stop:1 rgba(95, 175, 95, 255));\n"
"    border-right: 2px solid qlineargradient(spread:pad, x1:1, y1:0.517, x2:0, y2:0.534, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    %s"
"}\n"
"\n"
"QTabBar::tab:first:hover{\n"
"    background-color: qlineargradient(spread:reflect, x1:0.511, y1:0.522636, x2:0.511, y2:1, stop:0.227273 rgba(3, 129, 3, 255), stop:0.829545 rgba(88, 171, 88, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.528, y1:0, x2:0.523, y2:1, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"    border-left: 2px solid qlineargradient(spread:pad, x1:0, y1:0.597, x2:1, y2:0.597, stop:0 rgba(72, 127, 72, 255), stop:0.460227 rgba(72, 128, 72, 255), stop:0.534091 rgba(97, 176, 97, 255), stop:1 rgba(95, 175, 95, 255));\n"
"    border-right: 2px solid qlineargradient(spread:pad, x1:1, y1:0.517, x2:0, y2:0.534, stop:0 rgba(74, 125, 74, 255), stop:0.471591 rgba(86, 143, 86, 255), stop:0.522727 rgba(103, 169, 103, 255), stop:1 rgba(113, 184, 113, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: rgb(94, 94, 94);\n"
"    border-bottom-color:  rgb(201, 201, 201); /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover{\n"
"    border-left: 2px solid qlineargradient(spread:pad, x1:1, y1:0.539773, x2:0, y2:0.534, stop:0 rgba(201, 201, 201, 255), stop:0.495 rgba(201, 201, 201, 255), stop:0.505 rgba(94, 94, 94, 255), stop:1 rgba(94, 94, 94, 255));\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.5, y2:0, stop:0 rgba(201, 201, 201, 255), stop:0.495 rgba(201, 201, 201, 255), stop:0.505 rgba(94, 94, 94, 255), stop:1 rgba(94, 94, 94, 255));\n"
"    border-right: 2px solid qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.539773, stop:0 rgba(201, 201, 201, 255), stop:0.495 rgba(201, 201, 201, 255), stop:0.505 rgba(94, 94, 94, 255), stop:1 rgba(94, 94, 94, 255));\n"
"    %s"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0.54, y1:0.517045, x2:0.54, y2:1, stop:0.318182 rgba(36, 36, 36, 255), stop:1 rgba(71, 71, 71, 255));\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
#"QTabWidget#tabWidget::tab{\n"
#"    background-color: rgb(255, 0, 127);\n"
#"}\n"
#"\n"
"QFrame#frame_3, QFrame#frame_4{\n"
"    background-color: rgb(201, 201, 201);\n"
"}" %(line_archive, border_bottom, first_tab_border_bottom, first_tab_border_bottom))
    return style_string
