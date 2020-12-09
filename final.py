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
        self.imv4 = pg.ImageView()
        imv.setImage(data)
        imv2.setImage(data2)
        imv3.setImage(data3)
        self.layout = QGridLayout()
        self.layout.addWidget(imv,0,0)
        self.layout.addWidget(imv2,1,0)
        self.layout.addWidget(imv3,0,1)
        self.layout.addWidget(self.imv4,1,1)
        self.layout.addWidget(self.sl,1,2)
        self.sl.valueChanged.connect(self.valuechange)
        self.imv4.setImage(np.stack([self.X1_nii,self.X2_nii,np.zeros_like(self.X1_nii)],axis=3))
        self.setLayout(self.layout)
        self.setGeometry(400, 400, 750, 750)
        self.move(60, 15)
        self.setWindowTitle('Absolute')
        self.show()
    
    def valuechange(self):
        slide_by = self.sl.value()
        zeros = np.zeros((self.X1_nii.shape[0],self.X1_nii.shape[1],abs(slide_by*10)))
        if(slide_by < 0):
            X1_nii_ = np.append(self.X1_nii, zeros,axis=2)
            X2_nii_ = np.append(zeros,self.X2_nii ,axis=2)
        elif(slide_by > 0):
            X1_nii_ = np.append(zeros,self.X1_nii,axis=2)
            X2_nii_ = np.append(self.X2_nii,zeros ,axis=2)
        else: 
            X1_nii_ = self.X1_nii
            X2_nii_ = self.X2_nii
        self.imv4.setImage(np.stack([X1_nii_,X2_nii_,np.zeros_like(X1_nii_)],axis=3))
        self.setLayout(self.layout)
        


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()