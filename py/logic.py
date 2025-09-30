from tkinter import messagebox
from PIL import Image, ImageTk
import random
from card import Card 
import os

IMAGE_DIR = "./img"
CARD_BACK_IMG=os.path.join(IMAGE_DIR,"back.png")
CARD_WIDTH = 168
CARD_HEIGHT = 245
FACE_IMAGES = {}
BACK_IMAGE = None
REMAIN_CARDS = 20
FLIPPED_TIMES = 0
all_game_cards = [] 
flipped_cards = []
CARDS={
    "red_1": os.path.join(IMAGE_DIR, "red1.png"),
    "red_2": os.path.join(IMAGE_DIR, "red2.png"),
    "red_3": os.path.join(IMAGE_DIR, "red3.png"),
    "red_4": os.path.join(IMAGE_DIR, "red4.png"),
    "red_5": os.path.join(IMAGE_DIR, "red5.png"),
    "white_1": os.path.join(IMAGE_DIR, "white1.png"),
    "white_2": os.path.join(IMAGE_DIR, "white2.png"),
    "white_3": os.path.join(IMAGE_DIR, "white3.png"),
    "white_4": os.path.join(IMAGE_DIR, "white4.png"),
    "white_5": os.path.join(IMAGE_DIR, "white5.png"),
    }

#图片处理
def load_image(image_path):
    global CARD_WIDTH, CARD_HEIGHT
    try:
        original_image = Image.open(image_path)
        resized_image = original_image.resize((CARD_WIDTH, CARD_HEIGHT), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    except Exception as e:
        print(f"在{image_path}处理图片发生{e}错误")
        return None
        
def pre_load():
    global FACE_IMAGES, BACK_IMAGE
    BACK_IMAGE = load_image(CARD_BACK_IMG)
    if not BACK_IMAGE:
        return False
    for card_id, path in CARDS.items():
        FACE_IMAGES[card_id] = load_image(path)
        if not FACE_IMAGES[card_id]:
            return False
    if BACK_IMAGE and all(FACE_IMAGES.values()):
        return FACE_IMAGES, BACK_IMAGE
    return True
def random_cards():
    cards_id=list(CARDS.keys())*2
    random.shuffle(cards_id)#打乱ID实现洗牌效果
    return cards_id
def bind_all_cards(game_root,root):
    """重新绑定所有未配对卡牌的点击事件"""
    for card in all_game_cards:
        if not card.is_matched:
            card.tk_label.bind("<Button-1>", lambda event, c=card: handle_card_click(c,game_root,root))
def handle_card_click(card,game_root,root):
    """处理卡牌点击事件：翻面、追踪状态，并检查匹配"""
    global flipped_cards, REMAIN_CARDS, FLIPPED_TIMES 
    global remain_label, flipped_label
    
    # 忽略已翻开、已匹配或当前正在处理第三张牌的点击
    if card.is_flipped or card.is_matched or len(flipped_cards) == 2:
        return 
        
    # 翻开卡牌并添加到追踪列表
    card.flip_to_face() 
    flipped_cards.append(card)

    FLIPPED_TIMES += 1
    flipped_label.config(text=f"翻牌次数：{FLIPPED_TIMES}")

    # 如果翻开了两张牌，则启动匹配检查
    if len(flipped_cards) == 2:
        card1, card2 = flipped_cards
        
        # 禁用所有点击事件，防止用户在延迟期间点击
        for card in all_game_cards:
            card.tk_label.unbind("<Button-1>")
        
        if card1.id == card2.id:
            # 匹配成功：设置 matched 状态
            card1.set_matched()
            card2.set_matched()
            flipped_cards.clear()
            bind_all_cards(game_root,root)   
            # 匹配成功，立刻重新绑定点击事件
            REMAIN_CARDS = REMAIN_CARDS-2
            remain_label.config(text=f"未匹配的卡牌数：{REMAIN_CARDS}")
            #判断胜利条件
            if REMAIN_CARDS == 0:
                if FLIPPED_TIMES <= 50:
                    messagebox.showinfo("胜利", f"恭喜通关喵！总共翻牌 {FLIPPED_TIMES} 次")
                else:
                    messagebox.showinfo("雑魚!雑魚！", f"总共翻牌 {FLIPPED_TIMES} 次,真是雑魚！")
                game_root.destroy() 
                root.deiconify() 
                

        else:
            # 使用 after 延迟 1 秒
            card1.tk_label.after(1000, lambda: [
                card1.flip_to_back(), 
                card2.flip_to_back(), 
                flipped_cards.clear(),
                # 重新绑定点击事件，允许玩家继续游戏
                bind_all_cards(game_root,root) 
            ])
