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
        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(10)
        self.sl.setMaximum(30)
        self.sl.setValue(20)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(5)
        X1 = Image3D(r"BraTS20_Training_003/BraTS20_Training_003_t1.nii.gz")
        X2 = Image3D(r"BraTS20_Training_005/BraTS20_Training_005_t1.nii.gz")
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
        layout.addWidget(self.sl,2,1)
        self.sl.valueChanged.connect(self.valuechange)
        imv4.setImage(np.stack([X1.nii_data,X2.nii_data,np.zeros_like(X1.nii_data)],axis=3))
        self.setLayout(layout)
        self.setGeometry(400, 400, 750, 750)
        self.move(60, 15)
        self.setWindowTitle('Absolute')
        self.show()
    
    def valuechange(self):
        size = self.sl.value()
        print(size)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()