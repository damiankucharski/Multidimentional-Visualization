import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton, QLineEdit
import pyqtgraph as pg
import numpy as np
from nii import Image3D


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.sl = QSlider(Qt.Vertical)
        self.sl.setMinimum(-5)
        self.sl.setMaximum(5)
        self.sl.setValue(0)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(5)
        X1 = Image3D(r"BraTS20_Training_003/BraTS20_Training_003_t1.nii.gz")
        X2 = Image3D(r"BraTS20_Training_005/BraTS20_Training_005_t1.nii.gz")
        self.X1_nii = X1.nii_data
        self.X2_nii = X2.nii_data
        data = np.transpose(X1.nii_data, axes = [2,1,0])
        data2 = np.transpose(X1.nii_data, axes = [0,2,1])
        data3 = np.transpose(X1.nii_data, axes = [1,0,2])
        data4 = np.transpose(X2.nii_data, axes = [2,1,0])
        imv = pg.ImageView()
        imv2 = pg.ImageView()
        imv3 = pg.ImageView()
        imv4 = pg.ImageView()
        imv.setImage(data)
        imv2.setImage(data2)
        imv3.setImage(data3)
        layout = QGridLayout()
        layout.addWidget(imv,0,0)
        layout.addWidget(imv2,1,0)
        layout.addWidget(imv3,0,1)
        layout.addWidget(imv4,1,1)
        layout.addWidget(self.sl,1,2)
        self.sl.valueChanged.connect(self.valuechange)
        imv4.setImage(np.stack([self.X1_nii,self.X2_nii,np.zeros_like(self.X1_nii)],axis=3))
        self.setLayout(layout)
        self.setGeometry(400, 400, 750, 750)
        self.move(60, 15)
        self.setWindowTitle('Absolute')
        self.show()
    
    def valuechange(self):
        slide_by = self.sl.value()
        if(slide_by < 0):
            pass
        elif(slide_by > 0):
            pass
        else: pass
        


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()