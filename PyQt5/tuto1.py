from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

class RoundWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setMinimumSize(800,400)
		self.setStyleSheet("""
			background-color: gray;
			color: white;
		""")

		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		self.setLayout(self.layout)

		self.titleBar = TitleBar(self)
		self.layout.addWidget(self.titleBar)

		self.label = QLabel("YOO")
		self.layout.addWidget(self.label)

		self.label = QLabel("YOO")
		self.layout.addWidget(self.label)

		self.label = QLabel("YOO")
		self.layout.addWidget(self.label)
		self.layout.addStretch(-1)

class TitleBar(QWidget):
	def __init__(self,parent):
		self.parent = parent
		super(TitleBar,self).__init__()

		self.layout = QHBoxLayout()
		self.setLayout(self.layout)
		# self.layout.setContentsMargins(0,0,0,0)

		self.menu_button = QPushButton("E")
		self.menu_button.setFixedSize(35, 35)
		self.menu_button.clicked.connect(self.onMenuClick)

		self.title = QLabel("Title bar")
		self.title.setFixedHeight(45)
		self.title.setAlignment(Qt.AlignCenter)
		self.title.setStyleSheet("QLabel {background-color: red;}")

		self.close_button = QPushButton("X")
		self.close_button.setFixedSize(35, 35)
		self.close_button.clicked.connect(self.onClose)

		self.layout.addWidget(self.menu_button)
		self.layout.addWidget(self.title)
		self.layout.addSpacing(10)
		self.layout.addWidget(self.close_button)

		self.start = (QPoint(0, 0),QPoint(0, 0))
		self.pressing = False

	def onClose(self):
		self.parent.close()

	def onMenuClick(self):
		pass

	def resizeEvent(self, QResizeEvent):
		super(TitleBar, self).resizeEvent(QResizeEvent)
		self.title.setFixedWidth(self.parent.width())

	def mousePressEvent(self, event):
		self.start = (self.mapToGlobal(event.pos()),event.pos())
		self.pressing = True
		print(self.start)

	def mouseMoveEvent(self, event):
		if self.pressing:
			self.end = self.mapToGlobal(event.pos())
			self.delta = self.end-self.start[0]
			self.pos = self.start[0] + self.delta - self.start[1]
			self.parent.setGeometry(self.pos.x(),
								self.pos.y(),
								self.parent.width(),
								self.parent.height())
			self.start = (self.end, self.start[1])

	def mouseReleaseEvent(self, QMouseEvent):
		self.pressing = False

app = QApplication([])

# palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.red)
# app.setPalette(palette)

window = RoundWindow()
window.show()
app.exec()