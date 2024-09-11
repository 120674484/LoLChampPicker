import tkinter as tk
import random
heroes = ['奥瑞利安·索尔', '卡蜜尔', '烬', '德莱文', '索拉卡', '奥莉安娜', '薇恩', '霞', '卡莎', '阿卡丽', '布隆', '努努和威朗普', '迦娜', '亚索', '厄运小姐', '奥拉夫', '阿利斯塔', '拉克丝', '内瑟斯', '蔚', '安妮', '艾希', '赛娜', '提莫', '易', '布里茨', '金克丝', '德玛西亚之力', '阿狸', '崔斯特', '沃里克', '薇古丝', '永恩', '蕾欧娜', '莎弥拉', '菲奥娜']
def show_random_hero():
    label.config(text=random.choice(heroes))
root = tk.Tk()
root.title("英雄联盟手游")
root.state('zoomed')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
label = tk.Label(root, text="", font=("Arial", 48))
label.pack(pady=100)
button = tk.Button(root, text="随机选择英雄", font=("Arial", 36), command=show_random_hero)
button.pack(pady=50)
root.mainloop()