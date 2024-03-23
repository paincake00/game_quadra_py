from PyQt5.QtWidgets import QTableWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from config import Config
from logic import Logic

class Game(QTableWidget):
    def __init__(self, matrix, cur_x, cur_y, rows, moves, turns, level, message):
        super().__init__(len(matrix), len(matrix[0]))
        self.matrix = matrix
        self.length = len(matrix)
        self.current_row = cur_x
        self.current_column = cur_y
        self.rows = rows
        self.moves = moves
        self.turns = turns
        self.level = level
        self.message = message

        self.cur_moves = 0
        self.cur_turns = 0
        self.cur_level = 1

        self.show_field(cur_x, cur_y)

        self.setFocusPolicy(Qt.StrongFocus)

    def show_field(self, cur_x, cur_y):
        for i in range(self.length):
            for j in range(self.length):
                color_label = QLabel()
                color = Config.COLORS[self.matrix[i][j]]
                if (cur_x-1 <= i <= cur_x+1 and cur_y-1 <= j <= cur_y+1):
                    color = self._darkenColor(color, 50)
                color_label.setStyleSheet(f"background-color: {color.name()}")

                self.setCellWidget(i, j, color_label)
    
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_L:
            if self.cur_level + 1 < 5:
                self.cur_level += 1
            else:
                self.cur_level = 1
            self.start_game()
        elif key == Qt.Key_X:
            self.matrix = Logic.turnR(self.current_row, self.current_column, self.matrix)
            self.cur_turns += 1
        elif key == Qt.Key_Z:
            self.matrix = Logic.turnL(self.current_row, self.current_column, self.matrix)
            self.cur_turns += 1
        elif key == Qt.Key_F:
            self.matrix = Logic.matrix_shuffle(self.matrix)
            self.start_game()
        elif key == Qt.Key_Left:
            self.current_column = max(1, self.current_column - 1)
            self.cur_moves += 1
        elif key == Qt.Key_Right:
            self.current_column = min(self.length - 2, self.current_column + 1)
            self.cur_moves += 1
        elif key == Qt.Key_Up:
            self.current_row = max(1, self.current_row - 1)
            self.cur_moves += 1
        elif key == Qt.Key_Down:
            self.current_row = min(self.length - 2, self.current_row + 1)
            self.cur_moves += 1    
        if Logic.rows_count(self.matrix) == self.length:
            self.message.setText('Победа!')
        self.show_field(self.current_row, self.current_column)
        self.level.setText(f"level: {self.cur_level}")
        self.rows.setText(f"rows: {Logic.rows_count(self.matrix)}/{self.length}")
        self.moves.setText(f"moves: {self.cur_moves}")
        self.turns.setText(f"turns: {self.cur_turns}")
        self.update()

    def start_game(self):
        self.matrix = Logic.generate_level(self.cur_level, self.length)
        self.matrix = Logic.matrix_shuffle(self.matrix)
        self.cur_moves = 0
        self.cur_turns = 0
        self.message.setText('Удачи..')

    def _darkenColor(self, color, amount):
        h, s, l, a = color.getHsl()
        l = max(0, l - amount)
        return QColor.fromHsl(h, s, l, a)