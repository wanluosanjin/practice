using System;
using System.Data;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Media.Imaging;
using System.Collections;
using System.Threading;
using System.Diagnostics;

namespace MyWpf{
    public class DownLoader{
        List<string> thumbnums;
        List<string> fullnums;
        bool thumbfirst;
        bool fullfirst;
        int thumbnum;
        int fullnum;
        MySql mySql;
        string bookfirstid;
        public DownLoader(MainWindow mainWindow){
            thumbnums=new List<string>();
            thumbnum=0;
            thumbfirst=true;
            fullnums=new List<string>();
            fullnum=0;
            fullfirst=true;
            this.mySql=mainWindow.mySql;
        }
        public void addThumbThread(string bookid){
            thumbnums.Add(bookid);
            if (thumbfirst==true){
                ThreadStart childref = new ThreadStart(scrapybookthumb);
                Thread childThread = new Thread(childref);
                childThread.Start();
            }
            thumbfirst=false;
        }
        public void addFullThread(string bookid){
            fullnums.Add(bookid);
            if (fullfirst==true){
                ThreadStart childref = new ThreadStart(scrapybookfull);
                Thread childThread = new Thread(childref);
                childThread.Start();
            }
            fullfirst=false;
        }
        public void addBookFirstThread(string bookid){
            bookfirstid=bookid;
            ThreadStart childref = new ThreadStart(scrapybookfirst);
            Thread childThread = new Thread(childref);
            childThread.Start();
            
        }
        public void downLoadThumbDone(){
            mySql.downloadThumbDone(thumbnums[thumbnum]);//下载完成后添加数据库
            thumbnum++;
            if(thumbnum==thumbnums.Count){
                thumbnums=new List<string>();
                thumbnum=0;
                thumbfirst=true;
            }
            else{
                ThreadStart childref = new ThreadStart(scrapybookthumb);
                Thread childThread = new Thread(childref);
                childThread.Start();
            }
        }
        public void downLoadfullDone(){
            fullnum++;
            if(fullnum==fullnums.Count){
                fullnums=new List<string>();
                fullnum=0;
                fullfirst=true;
            }
            else{
                ThreadStart childref = new ThreadStart(scrapybookfull);
                Thread childThread = new Thread(childref);
                childThread.Start();
            }
        }
        Process getProcess(){
            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.UseShellExecute = false;//是否使用操作系统shell启动
            process.StartInfo.RedirectStandardInput = true;//接受来自调用程序的输入信息
            return process;
        }
        protected void scrapybookthumb(){//进程调用函数是实时的,不会储存函数
            var process = getProcess();
            process.Start();
            string cd="cd C:\\Users\\onelor\\Documents\\myscrapy";
            string scrapy="scrapy crawl bookthumb -a num=";
            string script=cd+" && "+scrapy+thumbnums[thumbnum]+" -s LOG_FILE=all.log"+" &exit";
            process.StandardInput.WriteLine(script);
            process.StandardInput.AutoFlush=true;
            process.WaitForExit();
            process.Close();
            downLoadThumbDone();
        }
        protected void scrapybookfull(){
            var process = getProcess();
            process.Start();
            string cd="cd C:\\Users\\onelor\\Documents\\myscrapy";
            string scrapy="scrapy crawl bookfull -a num=";
            string script=cd+" && "+scrapy+fullnums[fullnum]+" -s LOG_FILE=all.log"+" &exit";
            process.StandardInput.WriteLine(script);
            process.StandardInput.AutoFlush=true;
            process.WaitForExit();//等待程序执行完退出进程
            process.Close();
            downLoadfullDone();
        }
        protected void scrapybookfirst(){
            var process = getProcess();
            process.Start();
            string cd="cd C:\\Users\\onelor\\Documents\\myscrapy";
            string scrapy="scrapy crawl bookfirst -a num=";
            string script=cd+" && "+scrapy+bookfirstid+" -s LOG_FILE=all.log"+" &exit";
            process.StandardInput.WriteLine(script);
            process.StandardInput.AutoFlush=true;
            process.WaitForExit();//等待程序执行完退出进程
            process.Close();
        }
    }
}