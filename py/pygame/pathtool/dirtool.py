'''
Created on 2019年6月29日

@author: 宛洛
'''
import os,shutil
def movedir(srcdir,dstdir):
    if not os.path.exists(srcdir):
        print ("%s not exist!"%(srcdir))
    else:
        fpath,fname=os.path.split(dstdir)    #分离文件名和路径
        ensuredir(fpath)
        try:
            shutil.move(srcdir,dstdir)
            #参数为(dir,dstdir)时,dstdir下会有dir(两个文件夹名称相同时不会进行
            #第一个参数为文件时,第二个也为文件
        except:
            print('移动时出现问题,可能是文件名相同,请检查%s'%dstdir)
        else:
            print ('已移动')

def ensuredir(dir):
    if not os.path.exists(dir):
        print('%s不存在,已生成'%dir)
        os.makedirs(dir)

def getfatherdir(dir):
    parent_path = os.path.dirname(dir)
    return parent_path

def getselfname(dir):
    fpath,fname=os.path.split(dir)
    return fname

def getsubdir(dir):
    subdir=[]
    filenamelist=os.listdir(dir)
    for subfilename in filenamelist:
        subdir.append(os.path.join(dir, subfilename))
    return subdir

def replacechar(string,char,index):
    string = list(string)
    string[index] = char
    return ''.join(string)

def getfileformat(file):
    return file.split('.')[-1]