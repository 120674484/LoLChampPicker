import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget
class HeroSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('英雄联盟召唤师峡谷·排位赛')
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
        button1 = QPushButton('上路')
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
        button4 = QPushButton('下路')
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
        heroes = ["暗夜猎手", "不灭狂雷", "大发明家", "德玛西亚之力", "德玛西亚之翼", "法外狂徒", "海兽祭司", "海洋之灾","荒漠屠夫", "狂暴之心", "离群之刺", "炼金术士", "暮光之眼", "诺克萨斯统领", "诺克萨斯之手","熔岩巨兽", "沙漠死神", "山隐之焰", "亡灵战神", "无双剑姬", "无畏战车", "武器大师", "虚空恐惧","迅捷斥候", "正义天使", "祖安狂人", "龙血武姬", "纳祖芒荣耀", "未来守护者", "牧魂人", "狂战士"]
        self.label.setText(random.choice(heroes))
    def button2_click(self):
        heroes = ["傲之追猎者", "北地之怒", "不灭狂雷", "翠神", "恶魔小丑", "法外狂徒", "巨魔之王", "披甲龙龟","殇之木乃伊", "圣锤之毅", "兽灵行者", "上古领主", "死亡颂唱者", "痛苦之拥", "无极剑圣", "虚空遁地兽","雪原双子", "岩雀", "影流之主", "远古恐惧", "蜘蛛女皇", "祖安怒兽", "虚空女皇", "龙血武姬","皎月女神", "皮城执法官", "未来守护者", "狂厄蔷薇", "德玛西亚皇子", "战争之影", "虚空掠夺者", "盲僧"]
        self.label.setText(random.choice(heroes))
    def button3_click(self):
        heroes = ["冰霜女巫", "不祥之刃", "愁云使者", "大发明家", "符文法师", "光辉女郎", "海洋之灾","黑暗之女", "机械先驱", "九尾妖狐", "卡牌大师", "离群之刺", "诺克萨斯统领", "沙漠皇帝","邪恶小法师", "猩红收割者", "虚空行者", "岩雀", "影流之主", "远古巫灵", "正义巨像","冰晶凤凰", "皎月女神", "未来守护者", "百裂冥犬", "英勇投弹手", "异画师", "潮汐海灵",'诡术妖姬','刀锋之影']
        self.label.setText(random.choice(heroes))
    def button4_click(self):
        heroes = ["暗夜猎手", "暴走萝莉", "爆破鬼才", "残月之肃", "寒冰射手", "麦林炮手", "皮城女警","沙漠玫瑰", "探险家", "瘟疫之源", "战争女神", "赏金猎人", "惩戒之箭", "深渊巨口", "不羁之悦"]
        self.label.setText(random.choice(heroes))
    def button5_click(self):
        heroes = ["不屈之枪", "堕落天使", "风暴之怒", "复仇焰魂", "光辉女郎", "寒冰射手", "魂锁典狱长","荆棘之兴", "炼金男爵", "牛头酋长", "诺克萨斯统领", "镕铁少女", "时光守护者", "天启者","虚空之眼", "远古巫灵", "蒸汽机器人", "众星之子", "幻翎", "深海泰坦", "琴瑟仙女", "瓦洛兰之盾", "异画师"]
        self.label.setText(random.choice(heroes))
app = QApplication()
window = HeroSelector()
window.showMaximized()
app.exec()