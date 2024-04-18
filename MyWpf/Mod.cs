using System;
using System.Data;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Media.Imaging;
using System.Collections;
using System.IO;
using System.Management.Automation;
using PowerShell = System.Management.Automation.PowerShell;
using System.Diagnostics;
using System.Text.RegularExpressions;
using System.Threading;







namespace MyWpf
{
    class Mod{
        // indexthumb,bookthumb,bookfull
        protected MainWindow mainWindow;
        // Runspace runspace;
        protected DownLoader downloader;
        protected Downloaded downloaded;
        protected MySql mySql;

        public Mod(MainWindow mainWindow){
            this.mainWindow=mainWindow;
            mySql=mainWindow.mySql;
            downloader=mainWindow.downloader;
            downloaded=mainWindow.downloaded;
            
            // var initialSessionState =InitialSessionState.CreateDefault();
            // var runspaceConfiguration = RunspaceConfiguration.Create();
            // runspace = RunspaceFactory.CreateRunspace(runspaceConfiguration);
            // runspace.Open();
            //不支持startjob
            
        }
        public virtual void bookfull(){
        }
        public virtual void bookthumb(){
        }
        public virtual void nextimg(){
            // if(string.IsNullOrEmpty(mainWindow.img.Source)){
            // }
        }
        public virtual void preimg(){}
        public virtual void nextdir(){}
        public virtual void predir(){}
        public virtual void changelist(){}
        public virtual string getbookid(){
            return "";
        }
        public virtual string getteacher(){
            return "";
        }
        public virtual string getPath(){
            return "";
        }
        
        protected void setimg(string path){
            
        try
            {
            mainWindow.img.Source = (new BitmapImage(new Uri(path,UriKind.RelativeOrAbsolute)));
            if(mainWindow.downloaded.ifDownloaded(getbookid()))path+="********************************************缩略图已下载";
            }
            catch (System.IO.FileNotFoundException)
            {
                mainWindow.Title=path+"******not  find";
                downloader.addBookFirstThread(getbookid()); 
                return;
            }
            catch
            {
                
            }
            mainWindow.Title=path;
        
        }

            // Pipeline pipeline = runspace.CreatePipeline();
            // pipeline.Commands.AddScript(script);
            // List<PSObject> results = new List<PSObject>(pipeline.Invoke());
            // if(results.Count==0){
            //     foreach (PSObject obj in results)
            //     {
            //         Console.WriteLine(obj.ToString());
            //     }
            // }
        
    }


    class IndexthumbMod :Mod {//废弃的类
    // const string indexthumbpath = "C:/imgs/indexthumb";
    const string indexthumbpath = "C:/img";
    // IEnumerator<string> booksenumerator;
    // IEnumerator<string> teachersenumerator;
    int teachersmax;
    int booksmax;
    int teachersnum;
    int booksnum;
    List<string> teachers;//需要强制转换 , 或使用list<>,list不用装箱,new list<>
    List<string> books;
        public IndexthumbMod(MainWindow mainWindow) : base(mainWindow){
            DirectoryInfo indexthumbpathDirectoryInfo=new DirectoryInfo(indexthumbpath);
            DirectoryInfo[] teachersDirectoryInfoes = indexthumbpathDirectoryInfo.GetDirectories();
            teachers = new List<string>(teachersmax);
            foreach(var teachersDirectoryInfo in teachersDirectoryInfoes){
                teachers.Add(teachersDirectoryInfo.FullName);
            }
            // teachersenumerator = teachers.GetEnumerator();
            teachersmax=teachers.Count();
            teachersnum=0;
            // if(teachersenumerator.MoveNext()){
            if(!(teachersnum==teachersmax)&&!(teachersnum==-1)){
                DirectoryInfo booksDirectoryInfo=new DirectoryInfo(teachers[teachersnum]);
                FileInfo[] booksFileInfoes = booksDirectoryInfo.GetFiles();
                books = new List<string>(booksFileInfoes.Count());
                foreach(var booksFileInfo in booksFileInfoes){
                    books.Add(booksFileInfo.FullName);
                // booksenumerator = books.GetEnumerator();
                booksmax=books.Count();
                booksnum=-1;
                }
            }
        }
        public override void predir(){
                teachersnum--;
                frashbooks();
                booksmax=books.Count;//刷新books信息
                booksnum=-1;
                preimg();//刷新第一个图片
        }
    // IndexthumbMod(){
    // }写上就无法访问
        public override void nextdir(){
                teachersnum++;
                frashbooks();
                booksmax=books.Count;//刷新books信息
                booksnum=books.Count;
                preimg();//刷新第一个图片
        }
        public override void nextimg(){//用new的话mainwindow里必须使用indexthhumb类而非mod类
            // if(booksenumerator.MoveNext()){
            booksnum++;
            if(!(booksnum==booksmax)&&!(booksnum==-1)){

                setimg(books[booksnum]);
            }
            else
            {
                //进入下一文件夹
                teachersnum++;
                //刷新books
                frashbooks();
                booksmax=books.Count;//刷新books信息
                booksnum=-1;
                nextimg();//刷新第一个图片
            }
        }
        public override void preimg(){
            booksnum--;
            if(!(booksnum==booksmax)&&!(booksnum==-1)){

                setimg(books[booksnum]);
            }
            else
            {
                //进入上一文件夹
                teachersnum--;
                //刷新books
                frashbooks();
                booksmax=books.Count;//刷新books信息
                booksnum=books.Count;
                preimg();//刷新最后的图片
            }
        }

        public override void bookthumb(){
            ThreadStart childref = new ThreadStart(runscript);
            Thread childThread = new Thread(childref);
            childThread.Start();
            Console.WriteLine("线程开始");
        }

        void frashbooks(){
            // if(teachersenumerator.MoveNext()){
            if(!(teachersnum==teachersmax)&&!(teachersnum==-1)){
                DirectoryInfo booksDirectoryInfo=new DirectoryInfo(teachers[teachersnum]);
                FileInfo[] booksFileInfoes = booksDirectoryInfo.GetFiles();
                books = new List<string>(booksFileInfoes.Count());
                foreach(var booksFileInfo in booksFileInfoes){
                    books.Add(booksFileInfo.FullName);
                }
            }
        }
        protected void runscript(){
            string[] pathsplit = books[booksnum].Split("\\");
            var num = pathsplit[pathsplit.Count()-1].Split(" ")[0];
            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.UseShellExecute = false;//是否使用操作系统shell启动
            process.StartInfo.RedirectStandardInput = true;//接受来自调用程序的输入信息
            // process.StartInfo.RedirectStandardOutput = true;//由调用程序获取输出信息
            // process.StartInfo.RedirectStandardError = true;//重定向标准错误输出
            // process.StartInfo.CreateNoWindow = true;//不显示程序窗口
            process.Start();//启动程序
            string cd="cd C:\\Users\\onelor\\Documents\\myscrapy";
            string scrapy="scrapy crawl bookthumb -a num=";
            string script=cd+" && "+scrapy+num+" &exit";
            process.StandardInput.WriteLine(script);
            process.StandardInput.AutoFlush=true;
            process.WaitForExit();//等待程序执行完退出进程
            process.Close();
            Console.WriteLine(num+"完成");
        }
    }



    class BookthumbMod :Mod {
        class Node{
            string name;
            List<Node> subnode;
            Node fathernode;
            int nodenum;
            public Node(string name){
                if(name!=null){
                    this.name=name;
                }
            }
            void initsubnode(){//对比fullanme比较浪费空间
            //初始化subnode,father和num,,,dir,file要各装各的
                if(subnode==null){
                    DirectoryInfo folder = new DirectoryInfo(getsubnodepath());
                    var dirs = folder.GetDirectories();
                    var files = folder.GetFiles();
                    subnode = new List<Node>(dirs.Count()+files.Count());
                    foreach (DirectoryInfo file in dirs){
                        subnode.Add(new Node(file.Name));
                        subnode.Last().fathernode=this;
                    }
                    foreach (FileInfo file in files){
                        subnode.Add(new Node(file.Name));
                        subnode.Last().fathernode=this;
                    }
                    Regex r = new Regex("\\d+");
                    subnode.Sort((a,b)=>{
                        if(a.name.EndsWith(".jpg")&&b.name.EndsWith(".jpg")){
                            MatchCollection mc = r.Matches(a.name+b.name);
                            return int.Parse(mc[0].Value).CompareTo(int.Parse(mc[1].Value));
                        }
                        return a.name.CompareTo(b.name);
                        });
                    nodenum=0;
                }
            }
            public string getprefile(bool overflow = false){//不能至上一文件夹
                if(isfile()){
                    return getsubnodepath();
                }
                if(nodenum!=-1){
                    if(subnode[nodenum].isfile()){
                        if (overflow)
                        {
                            return subnode[nodenum].getprefile();
                        }
                        nodenum--;
                        if(nodenum!=-1){
                            return subnode[nodenum].getprefile();
                        }
                        else
                        {
                            nodenum++;
                            fathernode.nodenum--;
                            return fathernode.getprefile(true);
                        }
                    }
                    else
                    {
                        if(overflow)return subnode[nodenum].getprefile(true);
                        return subnode[nodenum].getprefile();
                    }
                }
                else
                {
                    nodenum++;
                    fathernode.nodenum--;
                    return fathernode.getprefile(true);
                }
            }
            public string getnextfile(bool overflow = false){//用while也可以写,此处用迭代,占内存高
                if(isfile()){
                    return getsubnodepath();
                }
                if(subnode==null){
                    initsubnode();
                }
                if(nodenum!=subnode.Count){

                    if(subnode[nodenum].isfile()){//这里崩错,需要两次越界检测
                        if (overflow)
                        {
                            return subnode[nodenum].getnextfile();
                        }
                        nodenum++;
                        if(nodenum!=subnode.Count){//是我傻逼了//先加1后判断
                            return subnode[nodenum].getnextfile();
                        }
                        else
                        {
                            nodenum--;
                            fathernode.nodenum++;
                            return fathernode.getnextfile(overflow = true);
                        }
                    }
                    else
                    {
                        if(overflow)return subnode[nodenum].getnextfile(true);
                        return subnode[nodenum].getnextfile();
                    }
                }
                else
                {
                    nodenum--;
                    fathernode.nodenum++;
                    return fathernode.getnextfile(overflow = true);
                }
            }

            public string getnextdir(bool overflow = false){//需要用overflow传递是否溢出
                if(!hasdrection()){
                    return subnode[nodenum].getsubnodepath();
                }
                if(subnode==null){
                    initsubnode();
                }
                if(nodenum!=subnode.Count){
                    
                    if(!subnode[nodenum].hasdrection()){
                        if (overflow)
                        {
                            return subnode[nodenum].getnextdir();
                        }
                        nodenum++;//原本是0,+1直接走了
                        if(nodenum!=subnode.Count){
                            return subnode[nodenum].getnextdir();
                        }
                        else
                        {
                            nodenum--;
                            fathernode.nodenum++;
                            return fathernode.getnextdir(true);
                        }
                    }
                    else
                    {
                        if(overflow)return subnode[nodenum].getnextdir(true);
                        return subnode[nodenum].getnextdir();
                    }
                }
                else
                {
                    nodenum--;
                    fathernode.nodenum++;
                    return fathernode.getnextdir(true);
                }
            }
            public string getpredir(bool overflow = false){//需要用overflow传递是否溢出
                if(!hasdrection()){
                    return subnode[nodenum].getsubnodepath();
                }
                if(subnode==null){
                    initsubnode();
                }
                if(nodenum!=-1){
                    
                    if(!subnode[nodenum].hasdrection()){
                        if (overflow)
                        {
                            return subnode[nodenum].getpredir();
                        }
                        nodenum--;//原本是0,+1直接走了
                        if(nodenum!=-1){
                            return subnode[nodenum].getpredir();
                        }
                        else
                        {
                            nodenum++;
                            fathernode.nodenum--;
                            return fathernode.getpredir(true);
                        }
                    }
                    else
                    {
                        if(overflow)return subnode[nodenum].getpredir(true);
                        return subnode[nodenum].getpredir();
                    }
                }
                else
                {
                    nodenum++;
                    fathernode.nodenum--;
                    return fathernode.getpredir(true);
                }
            }
            public string getsubnodepath(){
                if(fathernode!=null){
                    return System.IO.Path.Join(fathernode.getsubnodepath(),name);
                }
                else
                {
                    return name;
                }
            }
            public string getPath(){
                if(subnode!=null){
                    return System.IO.Path.Join(name,subnode[nodenum].getPath());
                }
                else
                {
                    return name;
                }
            }
            public bool hasdrection(){//有不是文件的则返回t
                if(isfile()){
                    return false;
                }
                initsubnode();//要确保有subnode
                foreach(var file in subnode){
                    if(!file.isfile())return true;
                }
                return false;
            }
            public bool isfile(){
                if(File.Exists(getsubnodepath())){
                    return true;
                }
                return false;
            }
        }
        const string bookthumbpath = "C:/imgs/bookthumb";
        Node teachers;
        public BookthumbMod(MainWindow mainWindow) : base(mainWindow){
            teachers=new Node(bookthumbpath);
        }

        public override void preimg(){
            setimg(teachers.getprefile());
        }
        public override void nextimg(){
            setimg(teachers.getnextfile());
        }
        public override void nextdir(){
            setimg(teachers.getnextdir());
        }
        public override void predir(){
            setimg(teachers.getpredir());
        }
        public override void bookfull(){
            downloader.addFullThread(getbookid());
        }
        public override string getPath(){
            return teachers.getPath();
        }
        public override string getbookid(){
            //join方法
            string[] pathsplit = teachers.getPath().Split("\\");
            return pathsplit[pathsplit.Count()-2].Split(" ")[0];
        }
    }

    class ListMod :Mod {
        DataTable imgPathTable;
        int num;
        public ListMod(MainWindow mainWindow):base(mainWindow){
            imgPathTable=mySql.getTankoubonPathTable();
            num=-1;            
        }
        public override string getPath(){
            return "C:\\imgs\\"+imgPathTable.Rows[num]["imgpath"].ToString()+".jpg";
        }

        public override void nextdir(){//改为后移十位
            num=num+10;
            setimg(getPath());
        }
        public override void nextimg(){
            num++;
            setimg(getPath());
        }
        public override void preimg(){
            num--;
            setimg(getPath());
        }
        public override void changelist(){

        }
        public override void bookthumb(){
            downloader.addThumbThread(getbookid());
        }
        public override void bookfull(){
            downloader.addFullThread(getbookid());
        }
        public override string getteacher(){
            Regex r = new Regex("\\[.*?\\]");
            var teacher=r.Match(getPath()).Value;
            return teacher;
        }
        Process getProcess(){
            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.UseShellExecute = false;//是否使用操作系统shell启动
            process.StartInfo.RedirectStandardInput = true;//接受来自调用程序的输入信息
            return process;
        }
        // private readonly object scrapybookfullLock = new object();不需要锁了
        public override string getbookid(){
            string[] pathsplit = getPath().Split("\\");
            return pathsplit[pathsplit.Count()-1].Split(" ")[0];
        }

    }

    class bookfullMod :Mod {
        const string bookfullpath = "C:/imgs/bookfull";
        public bookfullMod(MainWindow mainWindow) : base(mainWindow){}
    }
    

    
    // public class ImgModel : INotifyPropertyChanged
    // {
    //     public event PropertyChangedEventHandler PropertyChanged;
    //     private string _imageSource = null;
    //     public string ImgSource
    //     {
    //         get{return _imageSource;}
    //         set
    //         {
    //             if (value == _imageSource)
    //             {
    //                 return;
    //             }
    //             _imageSource = value;
    //             this.PropertyChanged.Invoke(this,new PropertyChangedEventArgs("ImgSource"));
    //         }

    //     }
    // }
}