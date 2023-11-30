#! python3
import webbrowser,sys
#argv返回文件名和命令行参数
if len(sys.argv)>1:
    webbrowser.open(''.join(sys.argv[1:]))
else:
    webbrowser.open('https://www.mmgal.com/')
