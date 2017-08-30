import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
	app=QApplication(sys.argv)
	win=QWidget()

	b1=QPushButton("Button1")
	b2=QPushButton("Button2")

	vbox=QVBoxLayout()
	vbox.addWidget(b1)
	vbox.addStretch()
	vbox.addWidget(b2)
	win.setLayout(vbox)

	win.setWindowTitle("PyQt")
	win.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	window()
