import tkinter as tk
from deal_imgdir import *
if __name__ == '__main__':
    window = tk.Tk()
    window.title('整理本子的窗口')
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x
    # 第4步，在图形界面上设定标签
    提示框里的字 = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
    提示框里的字.set('这是一个提示框\n用来显示一些东西')
    提示框 = tk.Label(window, textvariable=提示框里的字, bg='blue', fg='white', font=('Arial', 8), width=50, height=5)
    提示框.pack()
    文本框 = tk.Text(window, height=3)
    文本框.pack()
    # 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
    def 按钮点击事件():
        作用路径=作用路径框.get()
        目标路径=目标路径框.get()
        value = lb.get(lb.curselection())
        if(value==功能列表[0]):
            zip_todir(作用路径,目标路径)
        if(value==功能列表[1]):
            zipallimgdir(作用路径,目标路径)
        if(value==功能列表[2]):
            sendallbenzi(作用路径,目标路径)
    按钮 = tk.Button(window, text='选择一个选项后点我', font=('Arial', 12), width=20, height=1, command=按钮点击事件)
    按钮.pack()
    作用路径框里的字 = tk.StringVar()
    作用路径框里的字.set('E:\本子\待整理')
    作用路径框 = tk.Entry(window,textvariable = 作用路径框里的字,width=100)
    作用路径框.pack()
    目标路径框里的字 = tk.StringVar()
    目标路径框里的字.set('E:\本子\散装饼干')
    目标路径框 = tk.Entry(window,textvariable = 目标路径框里的字,width=100)
    目标路径框.pack()
    功能列表=['压缩至目标目录','压缩所有包含图片的子目录至目标目录','将文件下的所有压缩包归位']
    tup1=tuple(功能列表)
    选择框字体 = tk.StringVar()
    选择框字体.set((tup1))
    lb = tk.Listbox(window, listvariable=选择框字体,width=30)
    lb.pack()

    window.mainloop()
