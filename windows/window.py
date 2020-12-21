from analizators.lexer import Lexer
from analizators.parser import Parser
from PyQt5 import QtWidgets, QtGui


class BaseWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.show()

    def init_UI(self):
        self.setWindowIcon(QtGui.QIcon('image/easy_icon.png'))
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Easy Python')

        box_console = QtWidgets.QVBoxLayout()
        box_console.addWidget(QtWidgets.QLabel(text='Console'))
        self.tb_console = QtWidgets.QPlainTextEdit()
        box_console.addWidget(self.tb_console)

        box_analise = QtWidgets.QVBoxLayout()
        box_analise.addWidget(QtWidgets.QLabel(text='Analise'))
        self.tb_analize = QtWidgets.QPlainTextEdit()
        box_analise.addWidget(self.tb_analize)

        box_result = QtWidgets.QVBoxLayout()
        box_result.addWidget(QtWidgets.QLabel(text='Result'))
        self.tb_result = QtWidgets.QPlainTextEdit()
        box_result.addWidget(self.tb_result)

        box_box = QtWidgets.QHBoxLayout()
        box_box.addLayout(box_console)
        box_box.addLayout(box_analise)
        box_box.addLayout(box_result)

        box_button = QtWidgets.QVBoxLayout()
        box_button.addLayout(box_box)
        button = QtWidgets.QPushButton(text='Run')
        button.clicked.connect(self.action)
        button.resize(30, 30)
        box_button.addWidget(button)

        self.setLayout(box_button)

    def action(self):
        text_input = str(self.tb_console.toPlainText())

        lexer = Lexer().get_lexer()
        tokens = lexer.lex(text_input)

        analise = ''
        for i in tokens:
            analise += str(i) + '\n'
        self.tb_analize.setPlainText(analise)

        tokens = lexer.lex(text_input)
        pg = Parser()
        pg.parse()
        parser = pg.get_parser()
        result = str(parser.parse(tokens).eval())
        self.tb_result.setPlainText(result)

