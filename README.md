# 🃏 Riddle Joker Card Game

**A small card game about Riddle Joker made by Sunshine6153 with Python.**

## ✨ 项目简介 (Introduction)

本项目是基于知名 Galgame **《Riddle Joker》** 主题的桌面小卡牌游戏同人实现。

游戏通过简洁的图形界面和卡牌元素，旨在提供一个轻量级的互动体验。本项目完全使用 **Python** 语言开发，主要技术栈依赖于标准库和常用的图形库：

* **`tkinter`**: 用于构建游戏的用户图形界面 (GUI) 和处理交互逻辑。
* **`Pillow (PIL)`**: 用于高效加载、处理和显示游戏中的卡牌图片资源和背景素材。

---

## 🖥️ 运行环境与安装 (Getting Started)

要成功运行本项目，请确保您已安装 Python 3 环境，并按以下步骤操作：

### 1. 克隆仓库 (Clone Repository)

打开您的终端，将本项目克隆到本地：

```bash
git clone [https://github.com/Sunshine6153/RiddleJokerGame.git](https://github.com/Sunshine6153/RiddleJokerGame.git)
cd RiddleJockerGame
```

### 2. 安装依赖 (Install Dependencies)
如果您是macOS用户，记得创造虚拟环境
```bash
pip install Pillow
```
### 3. 启动游戏 (Launch Game)
```bash
python login.py
```
### ⚠️ 跨平台兼容性警告 (Compatibility Warning)

本项目在 **macOS** 环境下开发完成。如果您尝试在 **Windows** 环境下运行，可能会遇到**文件路径错误**问题，因为 macOS/Linux 使用斜杠 `/` 作为路径分隔符，而 Windows 使用反斜杠 `\`。

**建议的解决方案：** 
在 Python 代码中处理文件路径时，请始终使用 [`os.path.join()`](https://docs.python.org/zh-cn/3/library/os.path.html) 函数，
或者使用 Python 3.4+ 提供的 [`pathlib`](https://docs.python.org/zh-cn/3/library/pathlib.html) 模块，以确保代码能自动适应不同操作系统的路径分隔符。
或者您发挥自己的主观能动性改一下，自适应谢谢喵！
