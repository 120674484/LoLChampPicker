import tkinter as tk
import random
import requests
response=requests.get('https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js')
data = response.json()
heroes = [item['name'] for item in data['hero']]
def show_random_hero():
    label.config(text=random.choice(heroes))
root = tk.Tk()
root.title("英雄联盟冠军杯赛")
root.state('zoomed')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
label = tk.Label(root, text="", font=("Arial", 48))
label.pack(pady=100)
button = tk.Button(root, text="随机选择英雄", font=("Arial", 36), command=show_random_hero)
button.pack(pady=50)
root.mainloop()