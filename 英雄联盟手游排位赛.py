import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget
class HeroSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('英雄联盟手游排位赛')
        self.resize(800, 600)
        main_layout = QVBoxLayout()
        label_layout = QHBoxLayout()
        self.label = QLabel()
        self.label.setText("")
        self.label.setStyleSheet("font-size: 36px;")
        label_layout.addStretch(1)
        label_layout.addWidget(self.label)
        label_layout.addStretch(1)
        main_layout.addLayout(label_layout)
        button_layout = QHBoxLayout()
        button1 = QPushButton('单人')
        button1.clicked.connect(self.button1_click)
        button1.setFixedHeight(60)
        button_layout.addWidget(button1)
        button2 = QPushButton('打野')
        button2.clicked.connect(self.button2_click)
        button2.setFixedHeight(60)
        button_layout.addWidget(button2)
        button3 = QPushButton('中路')
        button3.clicked.connect(self.button3_click)
        button3.setFixedHeight(60)
        button_layout.addWidget(button3)
        button4 = QPushButton('射手')
        button4.clicked.connect(self.button4_click)
        button4.setFixedHeight(60)
        button_layout.addWidget(button4)
        button5 = QPushButton('辅助')
        button5.clicked.connect(self.button5_click)
        button5.setFixedHeight(60)
        button_layout.addWidget(button5)
        main_layout.addLayout(button_layout)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    def button1_click(self):
        heroes = ["提莫", "盖伦", "奥拉夫", "亚索", "阿卡丽", "泰达米尔", "德莱厄斯", "卡蜜尔", "墨菲特", "内瑟斯", "贾克斯", "沃里克", "永恩", "菲奥娜"]
        self.label.setText(random.choice(heroes))
    def button2_click(self):
        heroes = ["奥拉夫", "赵信", "泰达米尔", "蔚", "格雷福斯", "卡蜜尔", "易", "贾克斯", "努努和威朗普", "沃里克"]
        self.label.setText(random.choice(heroes))
    def button3_click(self):
        heroes = ["阿狸", "提莫", "吉格斯", "奥莉安娜", "布兰德", "拉克丝", "安妮", "亚索", "阿卡丽", "娑娜", "奥瑞利安·索尔", "薇古丝", "永恩"]
        self.label.setText(random.choice(heroes))
    def button4_click(self):
        heroes = ["艾希", "金克丝", "赛娜", "烬", "薇恩", "霞", "凯特琳", "德莱文", "厄运小姐", "卡莎", "莎弥拉"]
        self.label.setText(random.choice(heroes))
    def button5_click(self):
        heroes = ["赛娜", "布里茨", "提莫", "阿利斯塔", "奥莉安娜", "迦娜", "墨菲特", "蕾欧娜", "索拉卡"]
        self.label.setText(random.choice(heroes))
if __name__ == '__main__':
    app = QApplication([])
    window = HeroSelector()
    window.showMaximized()
    app.exec()