import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from card import Card 
from logic import (pre_load, random_cards, handle_card_click,  all_game_cards, REMAIN_CARDS,FLIPPED_TIMES) 

def Riddle_Jocker(root): 
    global all_game_cards,left_cards,game_root # 声明全局变量，以便在循环中添加卡牌
    game_root = tk.Toplevel(master=root)
    game_root.title("Riddle Joker 翻卡牌游戏 - 挑战中")
    game_root.geometry("1080x1080")

    images_result = pre_load()
    if not images_result:
        print("错误图片加载失败！") 
        game_root.destroy()
        return
    global FACE_IMAGES, BACK_IMAGE
    FACE_IMAGES, BACK_IMAGE = images_result 

    style = ttk.Style()
    style.configure("red_style.TFrame",background = "#ff3535")
    score_frame = ttk.Frame(game_root, padding ="15", relief ="raised",style="red_style.TFrame")
    score_frame.pack(side="top" ,fill="x", padx=10, pady=10)
    style = ttk.Style()
    style.configure("red_style.TLabel",background = "#ff3535",font=('微软雅黑', 16))
    flipped_label=ttk.Label(score_frame,text=f"翻牌次数：{FLIPPED_TIMES}",style="red_style.TLabel")
    flipped_label.pack(side="left",padx=50) 
    remain_label=ttk.Label(score_frame,text=f"未匹配的卡牌数：{REMAIN_CARDS}",style="red_style.TLabel")
    remain_label.pack(side="right",padx=50) 
    import logic
    logic.remain_label = remain_label
    logic.flipped_label= flipped_label

    card_frame = ttk.Frame(game_root, padding="20")
    card_frame.pack(expand=True, fill="both", padx=10, pady=10) 

    shuffled_ids = random_cards() 
    card_index = 0
    ROWS = 4
    COLS = 5
    
    # 配置 grid 权重
    for i in range(ROWS):
        card_frame.grid_rowconfigure(i, weight=1)
    for j in range(COLS):
        card_frame.grid_columnconfigure(j, weight=1)

    # 4. 循环创建 Card 实例
    for r in range(ROWS):
        for c in range(COLS):
            current_id = shuffled_ids[card_index]
            
            new_card = Card(
                parent_frame=card_frame, 
                card_id=current_id, 
                face_image=FACE_IMAGES[current_id],
                back_image=BACK_IMAGE, 
                row=r, 
                col=c
            )
            all_game_cards.append(new_card) # 必须存储，以便 handle_card_click 访问
            
            # 绑定初始点击事件
            new_card.tk_label.bind("<Button-1>", lambda event, card=new_card: handle_card_click(card,game_root,root))
            card_index += 1

    game_root.mainloop()
