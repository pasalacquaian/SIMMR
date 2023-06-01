from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QLabel,
                             QGridLayout, QStackedWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

from init_scanner_ui import InitScannerUI
from scanner_init_ui import SetScannerUI
from coil_control_ui import CoilOverviewUI
from coil_design_ui import CoilDesignUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SimMR") # Set main window title

        self.window = QWidget()
        self.setCentralWidget(self.window)
        self.layout = QGridLayout()
        self.window.setLayout(self.layout)

        self.tl_w = Control_Panel_Widget(self.window)
        self.layout.addWidget(self.tl_w, 0, 0)
        self.tr_w = QLabel('Placeholder', self.window)
        self.layout.addWidget(self.tr_w, 0, 1)
        self.bl_w = QLabel('Placeholder', self.window)
        self.layout.addWidget(self.bl_w, 1, 0)
        self.br_w = QLabel('Placeholder', self.window)
        self.layout.addWidget(self.br_w, 1, 1)

        self.showMaximized() # Open GUI to maximized screen size

class Control_Panel_Widget(QWidget):

    BBOX_MIN_VALUE = 0.001 # Double (minimum double)
    BBOX_MAX_VALUE = 10.000 # Double (maximum double)
    BBOX_MIN_MAX_DEC = 3 # Integer (number of decimal places)

    bbox_validator = QDoubleValidator(BBOX_MIN_VALUE, BBOX_MAX_VALUE, BBOX_MIN_MAX_DEC)

    MIN_RESOLUTION = 0.01 # Double (minimum double)
    MAX_RESOLUTION = 1.00 # Double (maximum double)
    MIN_MAX_RES_DEC = 2 # Integer (number of decimal places)

    vol_res_validator = QDoubleValidator(MIN_RESOLUTION, MAX_RESOLUTION, MIN_MAX_RES_DEC)

    def __init__(self, parent : QWidget):
        super().__init__(parent)

        self.stack = QStackedWidget(self)

        self.init_scanner = InitScannerUI() # Prompt to initialize a scanner
        self.set_scanner = SetScannerUI() # To define scanner parameters
        self.coil_control = CoilOverviewUI() # 'Overview' of coils in a given scanner
        self.coil_design = CoilDesignUI() # Designing / modifying a coil (adding/editing segments etc.)

        self.stack.addWidget(self.init_scanner)
        self.stack.addWidget(self.set_scanner)
        self.stack.addWidget(self.coil_control)
        self.stack.addWidget(self.coil_design)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.stack)

        self.stack.setCurrentIndex(0)
