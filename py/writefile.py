
#所有的编码都是utf_8

#append写入
def write(text,file):
    with open(file,'a',encoding='utf-8') as f:
        f.write(text)
        
#返回列表

               

        
def writefile():
    dir = 'C:\\Users\\onelor\\game\\benzi'        
    filelist='filelist.txt'
    for subfilename in os.listdir(dir):
        write(subfilename,'filelist.txt')
        print(subfilename)


