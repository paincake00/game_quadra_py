from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QSize

from logic import Logic
from config import Config
from field import Field

class GridWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.win_width = 700
        self.win_height = 550
        self.cell_size = 100
        self.num_rows = 5
        self.num_columns = 5
        self.default_level = 1
        self.background = Config.BG_COLOR

        hor_lay = QHBoxLayout()
        ver_lay = QVBoxLayout()

        self.matrix = Logic.generate_level(self.default_level, self.num_rows)
        self.matrix = Logic.matrix_shuffle(self.matrix)

        self.message_label = QLabel()
        self.rules = QLabel()
        self.level_label = QLabel()
        self.rows = QLabel()
        self.moves = QLabel()
        self.turns = QLabel()

        self.table = Field(
            self.matrix, 
            self.num_rows // 2, 
            self.num_columns // 2, 
            self.rows, 
            self.moves, 
            self.turns, 
            self.level_label,
            self.message_label
        )
        self.table_config(self.table)
        hor_lay.addWidget(self.table)

        self.message_label.setText('Удачи..')
        self.rules.setText(u"\tRULES\nL - change level\nF - shuffle\nX/Z - turn\n\u2190 \u2191 \u2193 \u2192 - move")
        self.level_label.setText(f"level: {self.default_level}")
        self.rows.setText(f"rows: {Logic.rows_count(self.matrix)}/{self.num_rows}")
        self.moves.setText(f"moves: 0")
        self.turns.setText(f"turns: 0")
        ver_lay.addWidget(self.message_label)
        ver_lay.addWidget(self.rules)
        ver_lay.addWidget(self.level_label)
        ver_lay.addWidget(self.rows)
        ver_lay.addWidget(self.moves)
        ver_lay.addWidget(self.turns)

        hor_lay.addLayout(ver_lay)

        self.setWindowTitle("Квадротека")
        self.setStyleSheet(f"background-color: {self.background.name()}")
        self.setLayout(hor_lay)
        self.setFixedSize(QSize(self.win_width, self.win_height))

    def table_config(self, table):
        table.horizontalHeader().setDefaultSectionSize(self.cell_size)
        table.verticalHeader().setDefaultSectionSize(self.cell_size)
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)
        table.setFixedSize(QSize(self.cell_size * self.num_rows + 2, self.cell_size * self.num_columns + 2))