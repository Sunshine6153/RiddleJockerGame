import tkinter as tk
from tkinter import ttk, messagebox 

BG_COLOR = "#ff3535"

root = tk.Tk()
root.title("欢迎来到Riddle_Joker卡牌游戏")
root.geometry("1080x800")
root.resizable(False, False) 
root.configure(bg=BG_COLOR)
title_label = tk.Label(root, text="欢迎来到Riddle_Joker翻卡牌游戏", font=("微软雅黑", 24, "bold"), bg=BG_COLOR)
title_label.pack(pady=20)

def Login():
    global player_name_var
    global diffculty
    player_name_var = tk.StringVar(value="在原晓")
    diffculty = tk.StringVar(value="中等 (10对/20张)")
    # 主 Frame 居中设置
    main_frame = ttk.Frame(root, padding=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=0) 
    main_frame.grid_columnconfigure(2, weight=1)
    main_frame.grid_rowconfigure(0, weight=1) 
    main_frame.grid_rowconfigure(1, weight=0)
    main_frame.grid_rowconfigure(2, weight=0)
    main_frame.grid_rowconfigure(3, weight=0)
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
        "1. 游戏总览：场上一共有偶数张牌,例如10对(20张)。\n"
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
    Button_frame.grid(column=1, row=3, pady=20)

    name_frame = ttk.Frame(main_frame, padding="10 0 10 10")
    name_frame.grid(column=1, row=1, pady=(0, 10), sticky="ew") 
    name_label = ttk.Label(name_frame, text="玩家姓名：", font=("微软雅黑", 14))
    name_label.pack(side=tk.LEFT, padx=(0, 10))
    name_entry = ttk.Entry(name_frame, textvariable=player_name_var, font=("微软雅黑", 14), width=20)
    name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    #选择难度
    diff_frame = ttk.Frame(main_frame, padding="10 0 10 10")
    diff_frame.grid(column=1, row=2, pady=(0, 10), sticky="ew") # 放在 row=2
    
    diff_label = ttk.Label(diff_frame, text="选择难度：", font=("微软雅黑", 14))
    diff_label.pack(side=tk.LEFT, padx=(0, 10))
    
    difficulty_options = [
        "入门 (5对/10张)", 
        "普通 (10对/20张)", 
    ]
    diff_combobox = ttk.Combobox(
        diff_frame, 
        textvariable=diffculty, 
        values=difficulty_options, 
        state="readonly",
        font=("微软雅黑", 14)
    )
    diff_combobox.pack(side=tk.LEFT, fill=tk.X, expand=True)

    from style import style  # 导入样式配置

    start_button = ttk.Button(Button_frame, text="开始游戏", command=lambda: start_game(root))
    start_button.pack(side=tk.LEFT, padx=10,pady=0)

    root.mainloop()#保持监听

def start_game(root):
    global player_name_var, diffculty
    player_name = player_name_var.get()
    difficulty_str = diffculty.get()
    import logic 
    logic.PLAYER_NAME = player_name
    logic.DIFFICULTY = difficulty_str
    messagebox.showinfo("游戏加载中", f"{player_name}大人，难度：{difficulty_str}，卡牌正在洗牌，请稍候...")
    root.withdraw()
    from main import Riddle_Jocker
    Riddle_Jocker(root)

if __name__ == '__main__':
    Login()