# Dołączenie modułów QApplication, QLabel z pakietu PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton, QLineEdit
import pyqtgraph as pg
import numpy as np
from nii import Image3D

X1 = Image3D(r"BraTS20_Training_003/BraTS20_Training_003_t1.nii.gz")
X2 = Image3D(r"BraTS20_Training_005/BraTS20_Training_005_t1.nii.gz")
data = np.transpose(X1.nii_data, axes = [2,1,0])
data2 = np.transpose(X1.nii_data, axes = [0,2,1])
data3 = np.transpose(X1.nii_data, axes = [1,0,2])
data4 = np.transpose(X2.nii_data, axes = [2,1,0])
# Inicjalizacja okna aplikacji
app = QApplication([])
# data = np.random.randn(255,255,255)
imv = pg.ImageView()
imv2 = pg.ImageView()
imv3 = pg.ImageView()
imv4 = pg.ImageView()
print(np.stack([data,data4],axis=3).shape)
imv.setImage(data)
imv2.setImage(data2)
imv3.setImage(data3)
imv4.setImage(np.stack([X1.nii_data,X2.nii_data,np.zeros_like(X1.nii_data)],axis=3))

# Tworzenie widżetu przechowującego elementy interfejsu (np. pola tekstowe)
window = QWidget()

# Ustawienie tytułu okna
window.setWindowTitle('PyQt5 Lab')

# Ustawienie wielkości okna
window.setGeometry(400, 400, 750, 750)

# Ustawienie pozycji początkowej okna
window.move(60, 15)
layout = QGridLayout()

# Dodanie pierwszego elementu do layoutu - do lewego górnego rogu
layout.addWidget(imv,0,0)
layout.addWidget(imv2,1,0)
layout.addWidget(imv3,0,1)
layout.addWidget(imv4,1,1)


# Podłączenie stworzonego layoutu do widżetu
window.setLayout(layout)

# Wyświetlenie widżetu
window.show()
app.exec_()




