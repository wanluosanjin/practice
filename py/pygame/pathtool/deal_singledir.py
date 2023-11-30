import os,shutil
from os import path   
from dirtool import *
def findsingledir(dir):
    filenamelist=os.listdir(dir)
    if(len(filenamelist)==1):
        print("%s文件夹下只有一个文件,移动文件至父目录"%dir)
        dironlyfiledir=dir+'\\'+filenamelist[0]
        if(filenamelist[0]==getselfname(dir)):
            for subfile in getsubdir(dironlyfiledir):
                print(subfile)
                print(dir)
                movedir(subfile, dir)
        else:
            movedir(dironlyfiledir,getfatherdir(dir))
        
def findemptydir(dir):
    dirfile=os.listdir(dir)
    if(len(dirfile)==0):
        print("%s文件夹下没有文件,已转移至:C\图片"%dir)
        movedir(dir,'C:\空文件夹')
        
def removeallzipdir(dir):
    for dirpath, dirnames, filenames in os.walk(dir):
        for dirname in dirnames:
            if(getfileformat(dirname)=='zip'):
                print('%s文件夹以.zip结尾,移除.zip')
                movedir(path.join(dirpath,dirname), path.join(dirpath,dirname.replace('.zip','')))
    
def findsingledirandclean(dir):
    for rootdir, dirnames, filenames in os.walk(dir):
        findsingledir(rootdir)

dir="C:\\Users\\onelor\\Pictures\\doujin.files"
findsingledirandclean(dir)