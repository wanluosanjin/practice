'''
Created on 2019年6月29日

@author: 宛洛
'''
from os import path   
from dirtool import *
import zipfile
import re,time
import webbrowser

#除了move外的所有方法的目标目录如果不存在都会报错!!!!!!!!!!



def add方括号(dir):
    old_name=getselfname(dir)
    new_name='['+old_name+']'
    os.rename(dir,os.path.join(getfatherdir(dir),new_name))
    print (old_name,"has been renamed successfully! New name is: ",new_name)   #输出提示
def 消去方括号(dir):#其实就是消去前后俩字符
    old_name=getselfname(dir)
    new_name=old_name[1:-1]
    os.rename(dir,os.path.join(getfatherdir(dir),new_name))
    print (old_name,"has been renamed successfully! New name is: ",new_name)   #输出提示

def 检测方括号(dir):  #检测第一个字符是否为[
    if (getselfname(dir)[0]=='['):
        return 1
    else:
        return 0
    
def detectionImgdir(dir):
    pagenum=0
    filelist=os.listdir(dir)
    for subfilename in filelist:
        fileformat=getfileformat(subfilename)
        if(fileformat=='png' or fileformat=='jpg'):
            pagenum+=1
        
    if (pagenum>0):
        return {dir:pagenum}#返回的是包含页数的字典!!!
    else:
        return 0
        
def findAllImgdir(dir):
    imgdirdict={}
    for dirpath, dirnames, filenames in os.walk(dir):
        a=detectionImgdir(dirpath)
        if(a):
            imgdirdict.update(a)
    return imgdirdict #返回的是包含页数的字典

def findAllzipfile(dir):
    zipdirlist=[]
    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            if (getfileformat(file)=='zip' or getfileformat(file)=='rar'):
                zipdirlist.append(path.join(dirpath,file))
    return zipdirlist

def zip_dir(dir):
    file_news = dir +'.zip'
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(dir):
        fpath = dirpath.replace(dir,'') #fpath是写入zip文件内的相对文件路径
        fpath = fpath and fpath + os.sep or ''#path存在则加\,不存在则返回''!!!!!!!!!
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()
    print('%s已压缩至根目录')
    
def zip_todir(dir,dstdir):#zip文件名为dir的名字,创建在dstdir目录下
    ensuredir(dstdir)
    file_news = os.path.join(dstdir, getselfname(dir)) +'.zip'
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(dir):
        fpath = dirpath.replace(dir,'') #fpath是写入zip文件内的相对文件路径
        fpath = fpath and fpath + os.sep or ''#path存在则加\,不存在则返回''!!!!!!!!!
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    z.close()
    print('%s已压缩至%s'%(dir,dstdir))
    

def matchteacher(name):
    pattern = re.compile(r'\[.*?\]')
    teachers=pattern.findall(name)

    return teachers
过滤表=['DL版','化','中国','chinese','翻译','彩頁','彩页','嵌字','全彩','中文','黑街','百度','MB']
def sendbenzi(zipdir,dstdir):#两参数一样则重命名
    fdir,zipname=os.path.split(zipdir)
    teachers=matchteacher(zipname)
    for teacher in teachers:
        send=1
        for 过滤词 in 过滤表:
            if (过滤词 in teacher):
                send=0
                continue
        if (send):
            print('检测到'+teacher+'在'+zipname)
            dstdir=path.join(dstdir,teacher,zipname)#根目录为dstdir,只能移动一次
            movedir(zipdir, dstdir) 
            zipdir=dstdir
            fdir,zipname=os.path.split(zipdir)
            '''
            if (input('检测到'+teacher+'在'+zipname+'按回车或输入任何')==''):
                dstdir=path.join(dstdir,teacher,zipname)#根目录为dstdir,只能移动一次
                movedir(zipdir, dstdir) 
                zipdir=dstdir
                fdir,zipname=os.path.split(zipdir)
            else:#删除名字
                zipname=zipname.replace(teacher,'')
                newpath=path.join(fdir,zipname)
                movedir(zipdir,newpath)
                zipdir=newpath
                fdir,zipname=os.path.split(zipdir)'''


#返回字典,项为第一层,值为第二层的列表
def getteacherdic(dir):
    dic={}
    teachernamelist=os.listdir(dir)
    for teachername in teachernamelist:
        teacherpath=path.join(dir, teachername)
        dic[teachername]=os.listdir(teacherpath)
    return dic
#列表不能和值对比
def dealbenziname(name):
    teacherlist=matchteacher(name)
    print('处理'+name)
    teacherlistcopy=teacherlist.copy()#其实可以不用copy直接循环remove
    for teacher in teacherlist:
        if('DL版'in teacher):
            teacherlistcopy.remove(teacher)
    for teacher in teacherlistcopy:
        print('检测到'+teacher, end='')  
        if (input('回车确认老师(至少选一个老师,否则崩错)')==''):
            teachername=teacher
    return teachername
    
def sendallbenzi(dir,dstdir):#只处理zip格式的本子
    for zipdir in findAllzipfile(dir):  
        sendbenzi(zipdir,dstdir)
                
def zipsubdir(dir,dstdir):#压缩子文件至dstdir
    for subdir in getsubdir(dir):
        zip_todir(subdir, dstdir)
        
def zipallimgdir(dir,dstdir):#压缩子文件至dstdir,必需保证符合格式
    for imgdir in list(findAllImgdir(dir)):
        zip_todir(imgdir, dstdir)    
        
def zipallsubimgdir(dir,dstdir):
    for subdir in getsubdir(dir):
        zipallimgdir(subdir,path.join(dstdir,getselfname(subdir)))

def smoothdir(dir):#已整理的本子专用严禁对文件数多的文件夹使用此方法!!!!!
    for subdir in getsubdir(dir):
        if(path.isdir(subdir)):
            for dirpath, dirnames, filenames in os.walk(dir):
                for filename in filenames:
                    movedir(path.join(dirpath,filename),path.join(dir,filename))

def readlist(file):
    with open(file,'r',encoding='utf-8') as f:
        list=f.readlines()#末尾有\n,最后一个\n不读取
    return list

def detectionformat(list):
    for i in range(len(list)//9):
        if(not list[i*9+8]=='\n'):
            return 0
    return 1
def getresourcedic(list):
    dic={}
    #检测是否符合要求
    if detectionformat(list):
        print('表符合要求')
        for i, element in enumerate(list):
            if(i%9==0):
                name=list[i+1]
                diclist=list[i:i+9]#变量名不能太通用
                dic[name]=diclist
        return dic
    else:
        print('list不符合规范')
        

#resourcedir=r'C:\\Users\\onelor\\AppData\\Local\\Programs\\Python\\Python37\\text全new.txt'
resourcedir=r'C:\\Users\\onelor\\AppData\\Local\\Programs\\Python\\Python37\\[ぴよころた].txt'
#teacherdir='E:\本子\散装饼干'
teacherdir='D:\图片\本子'
#storedir='C:\\Users\\onelor\\AppData\\Local\\Programs\\Python\\Python37\\text全new.txt'
storedir='C:\\Users\\onelor\\AppData\\Local\\Programs\\Python\\Python37\\[ぴよころた].txt'
resourcelist=readlist(resourcedir)#变量名不能太通用,否则会覆盖关键方法名
#historylist=readlist(historydir)
teacherdic=getteacherdic(teacherdir)
resourcedic=getresourcedic(resourcelist)
#num=int(input('从第几本开始?'))
resourcelist=list(resourcedic.keys())#在 python 3 dict.keys() 中，返回一个iteratable但不可索引的对象。
for name in resourcelist:
    if (not input('输入任何则储存')==''):
        with open(storedir,'w',encoding='utf-8') as f:
            writelist=[]
            for diclist in resourcedic.values():
                writelist.extend(diclist)
            f.writelines(writelist)
    teacher=dealbenziname(name)
    print('资源的老师为'+teacher)
    if(teacher in teacherdic):
        print(teacher+'老师作品如下')
        for benziname in teacherdic[teacher]:
            print(benziname)
        if (input('回车下载')==''):
        #本子不存在时下载本子
            webbrowser.open_new(resourcedic[name][2][:-1])
            if (teacher in teacherdic):
                teacherdic[teacher].append(name)
            else:
                teacherdic[teacher]=[name]
    else:
        if (input('老师不存在,回车下载')==''):
            webbrowser.open_new(resourcedic[name][2][:-1])
            if (teacher in teacherdic):
                teacherdic[teacher].append(name)
            else:
                teacherdic[teacher]=[name]
    resourcedic.pop(name)
