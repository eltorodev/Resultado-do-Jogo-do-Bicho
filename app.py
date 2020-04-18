from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QPushButton
from PyQt5.QtCore import QSize, Qt
import ojogo


# Daqui pra baixo começa o show de horrores rsrs.
class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self):
        # You must call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(540, 305))
        self.setWindowTitle("Deu no poste: Resultado do jogo do Bicho!")
        self.setGeometry(100, 100, 540, 305)
        central_widget = QWidget(self)
        # Install the central widget
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        label = QLabel(ojogo.caption)

        table = QTableWidget(self)
        table.setColumnCount(len(ojogo.th) - 1)
        table.setRowCount(7)

        # Set the table headers
        table.setHorizontalHeaderLabels([
            ojogo.th[1].getText(),
            ojogo.th[2].getText(),
            ojogo.th[3].getText(),
            ojogo.th[4].getText(),
            ojogo.th[5].getText()
        ])

        # Resultado PTM
        table.setItem(0, 0, QTableWidgetItem(
            ojogo.td[1].getText() if ojogo.td[1].get("title") != "0" else ""))
        table.setItem(1, 0, QTableWidgetItem(
            ojogo.td[7].getText() if ojogo.td[7].get("title") != "0" else ""))
        table.setItem(2, 0, QTableWidgetItem(
            ojogo.td[13].getText() if ojogo.td[13].get("title") != "0" else ""))
        table.setItem(3, 0, QTableWidgetItem(
            ojogo.td[19].getText() if ojogo.td[19].get("title") != "0" else ""))
        table.setItem(4, 0, QTableWidgetItem(
            ojogo.td[25].getText() if ojogo.td[25].get("title") != "0" else ""))
        table.setItem(5, 0, QTableWidgetItem(
            ojogo.td[31].getText() if ojogo.td[31].get("title") != "0" else ""))
        table.setItem(6, 0, QTableWidgetItem(
            ojogo.td[37].getText() if ojogo.td[37].get("title") != "0" else ""))

        # Resultado PT
        table.setItem(0, 1, QTableWidgetItem(
            ojogo.td[2].getText() if ojogo.td[2].get("title") != "0" else ""))
        table.setItem(1, 1, QTableWidgetItem(
            ojogo.td[8].getText() if ojogo.td[8].get("title") != "0" else ""))
        table.setItem(2, 1, QTableWidgetItem(
            ojogo.td[14].getText() if ojogo.td[14].get("title") != "0" else ""))
        table.setItem(3, 1, QTableWidgetItem(
            ojogo.td[20].getText() if ojogo.td[20].get("title") != "0" else ""))
        table.setItem(4, 1, QTableWidgetItem(
            ojogo.td[26].getText() if ojogo.td[26].get("title") != "0" else ""))
        table.setItem(5, 1, QTableWidgetItem(
            ojogo.td[32].getText() if ojogo.td[32].get("title") != "0" else ""))
        table.setItem(6, 1, QTableWidgetItem(
            ojogo.td[38].getText() if ojogo.td[38].get("title") != "0" else ""))

        # Resultado PTV
        table.setItem(0, 2, QTableWidgetItem(
            ojogo.td[3].getText() if ojogo.td[3].get("title") != "0" else ""))
        table.setItem(1, 2, QTableWidgetItem(
            ojogo.td[9].getText() if ojogo.td[9].get("title") != "0" else ""))
        table.setItem(2, 2, QTableWidgetItem(
            ojogo.td[15].getText() if ojogo.td[15].get("title") != "0" else ""))
        table.setItem(3, 2, QTableWidgetItem(
            ojogo.td[21].getText() if ojogo.td[21].get("title") != "0" else ""))
        table.setItem(4, 2, QTableWidgetItem(
            ojogo.td[27].getText() if ojogo.td[27].get("title") != "0" else ""))
        table.setItem(5, 2, QTableWidgetItem(
            ojogo.td[33].getText() if ojogo.td[33].get("title") != "0" else ""))
        table.setItem(6, 2, QTableWidgetItem(
            ojogo.td[39].getText() if ojogo.td[39].get("title") != "0" else ""))

        # Resultado PTN
        table.setItem(0, 3, QTableWidgetItem(
            ojogo.td[4].getText() if ojogo.td[4].get("title") != "0" else ""))
        table.setItem(1, 3, QTableWidgetItem(
            ojogo.td[10].getText() if ojogo.td[10].get("title") != "0" else ""))
        table.setItem(2, 3, QTableWidgetItem(
            ojogo.td[16].getText() if ojogo.td[16].get("title") != "0" else ""))
        table.setItem(3, 3, QTableWidgetItem(
            ojogo.td[22].getText() if ojogo.td[22].get("title") != "0" else ""))
        table.setItem(4, 3, QTableWidgetItem(
            ojogo.td[28].getText() if ojogo.td[28].get("title") != "0" else ""))
        table.setItem(5, 3, QTableWidgetItem(
            ojogo.td[34].getText() if ojogo.td[34].get("title") != "0" else ""))
        table.setItem(6, 3, QTableWidgetItem(
            ojogo.td[40].getText() if ojogo.td[40].get("title") != "0" else ""))

        # Resultado COR
        table.setItem(0, 4, QTableWidgetItem(
            ojogo.td[5].getText() if ojogo.td[5].get("title") != "0" else ""))
        table.setItem(1, 4, QTableWidgetItem(
            ojogo.td[11].getText() if ojogo.td[11].get("title") != "0" else ""))
        table.setItem(2, 4, QTableWidgetItem(
            ojogo.td[17].getText() if ojogo.td[17].get("title") != "0" else ""))
        table.setItem(3, 4, QTableWidgetItem(
            ojogo.td[23].getText() if ojogo.td[23].get("title") != "0" else ""))
        table.setItem(4, 4, QTableWidgetItem(
            ojogo.td[29].getText() if ojogo.td[29].get("title") != "0" else ""))
        table.setItem(5, 4, QTableWidgetItem(
            ojogo.td[35].getText() if ojogo.td[35].get("title") != "0" else ""))
        table.setItem(6, 4, QTableWidgetItem(
            ojogo.td[41].getText() if ojogo.td[41].get("title") != "0" else ""))

        table.resizeColumnsToContents()

        button = QPushButton("Atualizar")
        button.clicked.connect(self.update_ojogo)

        grid_layout.addWidget(label, 0, 0)
        grid_layout.addWidget(table, 10, 0)
        grid_layout.addWidget(button, 20, 0)

    def update_ojogo(self):
        central_widget = QWidget(self)
        # Install the central widget
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        label = QLabel(ojogo.caption)

        table = QTableWidget(self)
        table.setColumnCount(len(ojogo.th) - 1)
        table.setRowCount(7)

        # Set the table headers
        table.setHorizontalHeaderLabels([
            ojogo.th[1].getText(),
            ojogo.th[2].getText(),
            ojogo.th[3].getText(),
            ojogo.th[4].getText(),
            ojogo.th[5].getText()
        ])

        # Resultado PTM
        table.setItem(0, 0, QTableWidgetItem(
            ojogo.td[1].getText() if ojogo.td[1].get("title") != "0" else ""))
        table.setItem(1, 0, QTableWidgetItem(
            ojogo.td[7].getText() if ojogo.td[7].get("title") != "0" else ""))
        table.setItem(2, 0, QTableWidgetItem(
            ojogo.td[13].getText() if ojogo.td[13].get("title") != "0" else ""))
        table.setItem(3, 0, QTableWidgetItem(
            ojogo.td[19].getText() if ojogo.td[19].get("title") != "0" else ""))
        table.setItem(4, 0, QTableWidgetItem(
            ojogo.td[25].getText() if ojogo.td[25].get("title") != "0" else ""))
        table.setItem(5, 0, QTableWidgetItem(
            ojogo.td[31].getText() if ojogo.td[31].get("title") != "0" else ""))
        table.setItem(6, 0, QTableWidgetItem(
            ojogo.td[37].getText() if ojogo.td[37].get("title") != "0" else ""))

        # Resultado PT
        table.setItem(0, 1, QTableWidgetItem(
            ojogo.td[2].getText() if ojogo.td[2].get("title") != "0" else ""))
        table.setItem(1, 1, QTableWidgetItem(
            ojogo.td[8].getText() if ojogo.td[8].get("title") != "0" else ""))
        table.setItem(2, 1, QTableWidgetItem(
            ojogo.td[14].getText() if ojogo.td[14].get("title") != "0" else ""))
        table.setItem(3, 1, QTableWidgetItem(
            ojogo.td[20].getText() if ojogo.td[20].get("title") != "0" else ""))
        table.setItem(4, 1, QTableWidgetItem(
            ojogo.td[26].getText() if ojogo.td[26].get("title") != "0" else ""))
        table.setItem(5, 1, QTableWidgetItem(
            ojogo.td[32].getText() if ojogo.td[32].get("title") != "0" else ""))
        table.setItem(6, 1, QTableWidgetItem(
            ojogo.td[38].getText() if ojogo.td[38].get("title") != "0" else ""))

        # Resultado PTV
        table.setItem(0, 2, QTableWidgetItem(
            ojogo.td[3].getText() if ojogo.td[3].get("title") != "0" else ""))
        table.setItem(1, 2, QTableWidgetItem(
            ojogo.td[9].getText() if ojogo.td[9].get("title") != "0" else ""))
        table.setItem(2, 2, QTableWidgetItem(
            ojogo.td[15].getText() if ojogo.td[15].get("title") != "0" else ""))
        table.setItem(3, 2, QTableWidgetItem(
            ojogo.td[21].getText() if ojogo.td[21].get("title") != "0" else ""))
        table.setItem(4, 2, QTableWidgetItem(
            ojogo.td[27].getText() if ojogo.td[27].get("title") != "0" else ""))
        table.setItem(5, 2, QTableWidgetItem(
            ojogo.td[33].getText() if ojogo.td[33].get("title") != "0" else ""))
        table.setItem(6, 2, QTableWidgetItem(
            ojogo.td[39].getText() if ojogo.td[39].get("title") != "0" else ""))

        # Resultado PTN
        table.setItem(0, 3, QTableWidgetItem(
            ojogo.td[4].getText() if ojogo.td[4].get("title") != "0" else ""))
        table.setItem(1, 3, QTableWidgetItem(
            ojogo.td[10].getText() if ojogo.td[10].get("title") != "0" else ""))
        table.setItem(2, 3, QTableWidgetItem(
            ojogo.td[16].getText() if ojogo.td[16].get("title") != "0" else ""))
        table.setItem(3, 3, QTableWidgetItem(
            ojogo.td[22].getText() if ojogo.td[22].get("title") != "0" else ""))
        table.setItem(4, 3, QTableWidgetItem(
            ojogo.td[28].getText() if ojogo.td[28].get("title") != "0" else ""))
        table.setItem(5, 3, QTableWidgetItem(
            ojogo.td[34].getText() if ojogo.td[34].get("title") != "0" else ""))
        table.setItem(6, 3, QTableWidgetItem(
            ojogo.td[40].getText() if ojogo.td[40].get("title") != "0" else ""))

        # Resultado COR
        table.setItem(0, 4, QTableWidgetItem(
            ojogo.td[5].getText() if ojogo.td[5].get("title") != "0" else ""))
        table.setItem(1, 4, QTableWidgetItem(
            ojogo.td[11].getText() if ojogo.td[11].get("title") != "0" else ""))
        table.setItem(2, 4, QTableWidgetItem(
            ojogo.td[17].getText() if ojogo.td[17].get("title") != "0" else ""))
        table.setItem(3, 4, QTableWidgetItem(
            ojogo.td[23].getText() if ojogo.td[23].get("title") != "0" else ""))
        table.setItem(4, 4, QTableWidgetItem(
            ojogo.td[29].getText() if ojogo.td[29].get("title") != "0" else ""))
        table.setItem(5, 4, QTableWidgetItem(
            ojogo.td[35].getText() if ojogo.td[35].get("title") != "0" else ""))
        table.setItem(6, 4, QTableWidgetItem(
            ojogo.td[41].getText() if ojogo.td[41].get("title") != "0" else ""))

        button = QPushButton("Atualizar")
        button.clicked.connect(self.update_ojogo)

        grid_layout.addWidget(label, 0, 0)
        grid_layout.addWidget(table, 10, 0)
        grid_layout.addWidget(button, 20, 0)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
