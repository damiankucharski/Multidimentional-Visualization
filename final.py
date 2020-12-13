import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton, QLineEdit,QInputDialog
import pyqtgraph as pg
import numpy as np
from nii import Image3D
import glob
from functools import partial


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.input_path = self.getText()
        paths = glob.glob("{}/*".format(self.input_path))
        self.images = [Image3D(path).nii_data for path in paths]
        self.alphas =[0 for _ in paths]
        cumulativearray = np.zeros_like(self.images[0])
        for idx, array in enumerate(self.images):
            cumulativearray += (array * self.alphas[idx])
        self.sliders = [] 
        for i in range(len(self.images)):
            sl = QSlider(Qt.Vertical)
            sl.setMinimum(0)
            sl.setMaximum(255)
            sl.setValue(0)
            sl.setTickPosition(QSlider.TicksBelow)
            sl.setTickInterval(1)
            sl.sliderReleased.connect(partial(self.valuechange, i))
            self.sliders.append(sl)
        data = np.transpose(cumulativearray, axes = [2,1,0])
        data2 = np.transpose(cumulativearray, axes = [0,2,1])
        data3 = np.transpose(cumulativearray, axes = [1,0,2])
        self.imv = pg.ImageView()
        self.imv2 = pg.ImageView()
        self.imv3 = pg.ImageView()
        self.imv4 = pg.ImageView()
        self.imv.setImage(data)
        self.imv2.setImage(data2)
        self.imv3.setImage(data3)
        self.imv4.setImage(np.stack([self.images[0],self.images[1],self.images[2]],axis=3))
        self.layout = QGridLayout()
        self.layout.addWidget(self.imv,0,0)
        self.layout.addWidget(self.imv2,1,0)
        self.layout.addWidget(self.imv3,0,1)
        self.layout.addWidget(self.imv4,1,1)
        for i,slider in enumerate(self.sliders):
            self.layout.addWidget(slider,1,2+i)
        self.setLayout(self.layout)
        self.setGeometry(400, 400, 750, 750)
        self.move(60, 15)
        self.setWindowTitle('Absolute')
        self.show()
        
    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Select path to folder:", QLineEdit.Normal, "")
        if okPressed and text != '':
            if len(glob.glob("{}/*".format(text))) > 0:
                return text
    def valuechange(self,i):
        self.alphas[i] = self.sliders[i].value()/255
        self.alphas = [x/sum(self.alphas) for x in self.alphas]
        cumulativearray = np.zeros_like(self.images[0])
        for idx, array in enumerate(self.images):
            cumulativearray += (array * self.alphas[idx])
        #self.imv4.setImage(cumulativearray)
        self.imv.setImage(np.transpose(cumulativearray, axes = [2,1,0]))
        self.imv2.setImage(np.transpose(cumulativearray, axes = [0,2,1]))
        self.imv3.setImage(np.transpose(cumulativearray, axes = [1,0,2]))
            


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()