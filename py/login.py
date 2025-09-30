import tkinter as tk
from tkinter import ttk, messagebox 

BG_COLOR = "#ff3535"

root = tk.Tk()
root.title("欢迎来到Riddle_Joker卡牌游戏")
root.geometry("1280x720")
root.resizable(False, False) 
root.configure(bg=BG_COLOR)
title_label = tk.Label(root, text="欢迎来到Riddle_Joker翻卡牌游戏", font=("微软雅黑", 24, "bold"), bg=BG_COLOR)
title_label.pack(pady=20)

def start_game(root):
    messagebox.showinfo("游戏加载中", "卡牌正在洗牌，请稍候...")
    root.withdraw()
    from main import Riddle_Jocker
    Riddle_Jocker(root)

def Login():
# 主 Frame 居中设置
    main_frame = ttk.Frame(root, padding=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=0) 
    main_frame.grid_columnconfigure(2, weight=1)

    rules_frame = ttk.LabelFrame(
        main_frame, 
        text=" 翻卡牌游戏规则：", 
        padding=15, 
    )
# 将 LabelFrame 放在 main_frame 的中心列 (column=1)
    rules_frame.grid(column=1, row=0, pady=30, padx=20, sticky="ew")

# 2. 创建 Text 控件，父容器设置为 rules_frame
    rules_text = tk.Text(rules_frame, height=8, width=70, wrap='word', font=("微软雅黑", 16))

    rules_content = (
        "欢迎来到 Riddle Joker 翻卡牌的世界！请熟记以下规则，开启你的挑战：\n"
        "1. 游戏总览：场上一共有 10 对 (20 张) 卡牌。\n"
        "   卡牌构成：分为五种角色的红、白卡牌，相同角色相同底色才为一对。\n"
        "2. 匹配成功：如果连续翻开的两张卡牌图案相同，它们将永久保持翻开状态并消除。\n"
        "3. 匹配失败：如果两张卡牌图案不同，它们将在短暂延迟后自动翻回背面。\n"
        "4. 胜利条件：当场上所有卡牌都被匹配消除时，你将获得胜利！\n"
        "5. 计分：游戏将记录你的翻牌次数，越少越好！\n"
    )#这是个string,要插入到容器里面
    rules_text.insert(tk.END, rules_content)
# 4. 配置 Text 控件：禁用编辑并打包填充
    rules_text.config(state='disabled', background='#f0f0f0', foreground='#333333') 
    rules_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    Button_frame = ttk.Frame(main_frame, padding="20 20 20 20")
    Button_frame.grid(column=1, row=1, pady=20)

    from style import style  # 导入样式配置

    start_button = ttk.Button(Button_frame, text="开始游戏", command=lambda: start_game(root))
    start_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()#保持监听

if __name__ == '__main__':
    Login()