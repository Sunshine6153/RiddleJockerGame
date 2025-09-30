import tkinter as tk
class Card:
    def __init__(self, parent_frame, card_id, face_image, back_image, row, col):
        self.id=card_id
        self.face_image=face_image
        self.back_image=back_image
        self.is_flipped = False
        self.is_matched = False

        # 创建 Tkinter Label 来显示卡牌图片
        self.tk_label=tk.Label(
            parent_frame,
            image=self.back_image,
            relief="raised",
            bd=2
        )
        self.tk_label.image = self.back_image
        self.tk_label.grid(
            row=row,
            column=col, 
            padx=5, 
            pady=5, 
            sticky="nsew"
        )
    
    def flip_to_face(self):
        if not self.is_matched and not self.is_flipped:
            self.tk_label.config(image=self.face_image)#告诉程序需要翻页
            self.tk_label.image=self.face_image#保持显示而不是被销毁
            self.is_flipped= True
    
    def flip_to_back(self):
        if not self.is_matched and self.is_flipped:
            self.tk_label.config(image=self.back_image)#告诉程序需要翻页
            self.tk_label.image=self.back_image#保持显示而不是被销毁
            self.is_flipped= False
    
    def set_matched(self):
        self.is_matched=True
        self.tk_label.config(relief="flat", bd=0, bg="#E0E0E0")
        self.tk_label.unbind("<Button-1>")