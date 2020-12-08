# Dołączenie modułów QApplication, QLabel z pakietu PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton, QLineEdit
import pyqtgraph as pg
import numpy as np
from nii import Image3D

X = Image3D(r"C:\Users\cdami\PycharmProjects\Multidimentional-Visualization\avg152T1_LR_nifti.nii.gz")
data = np.transpose(X.nii_data, axes = [2,1,0])
data2 = np.transpose(X.nii_data, axes = [0,2,1])
data3 = np.transpose(X.nii_data, axes = [1,0,2])

# Inicjalizacja okna aplikacji
app = QApplication([])
# data = np.random.randn(255,255,255)
imv = pg.ImageView()
imv2 = pg.ImageView()
imv3 = pg.ImageView()
imv.setImage(data)
imv2.setImage(data2)
imv3.setImage(data3)

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
layout.addWidget(imv3,2,0)



# Podłączenie stworzonego layoutu do widżetu
window.setLayout(layout)

# Wyświetlenie widżetu
window.show()
app.exec_()




