
import tkinter
from tkinter import ttk
import os
#frame组件的大小由内部构件决定

class InfoWindows(tkinter.Frame):

	def __init__(self,master):

		frame = tkinter.Frame(master,width=80,height=50,bg = 'red')

		frame.grid(row=1, column=0)


		self.ev = tkinter.Variable()

		#创建一个Entry

		self.entry = tkinter.Entry(frame,textvariable=self.ev)

		self.entry.pack()

 

		#创建一个text

		self.txt=tkinter.Text(frame,width=8,height=5)

		self.txt.pack()
        
        
class TreeWindows(tkinter.Frame):

	def __init__(self,master,path,otherWin):

		frame = tkinter.Frame(master,width=800,height=500)

		frame.grid(row=0, column=0)


		self.otherWin = otherWin

 

		self.tree = ttk.Treeview(frame)

		self.tree.pack(side=tkinter.LEFT,fill=tkinter.Y)


 

		root = self.tree.insert("","end",text=self.getLastPath(path),open=True,values=(path))

		self.loadTree(root,path)

 

		#滚动条

		self.sy = tkinter.Scrollbar(frame)

		self.sy.pack(side=tkinter.RIGHT,fill=tkinter.Y)

		self.sy.config(command=self.tree.yview)

		self.tree.config(yscrollcommand=self.sy.set)

 

		#绑定事件

		self.tree.bind("<<TreeviewSelect>>",self.func)

 

	def func(self,event):

		#widget触发事件的构建

		self.v = event.widget.selection()

		for sv in self.v:

			file = self.tree.item(sv)["text"]

			self.otherWin.ev.set(file)

			apath = self.tree.item(sv)["values"][0]

			print(apath)

 

 

	def loadTree(self,parent,parentPath):

		for FileName in os.listdir(parentPath):

			absPath = os.path.join(parentPath,FileName)

 

			#插入树枝

			treey = self.tree.insert(parent,"end",text=self.getLastPath(absPath),values=(absPath))

			#判断是否是目录

			if os.path.isdir(absPath):

				self.loadTree(treey,absPath)

 

 

 

 

 

	def getLastPath(self,path):

		pathList = os.path.split(path)

		return pathList[-1]
        
 
win = tkinter.Tk()

win.title("窗体")

win.geometry("1000x700")

 

path = "C:\\Users\\onelor\\game\\benzi"

infoWin = InfoWindows(win)

treeWin = TreeWindows(win,path,infoWin)
