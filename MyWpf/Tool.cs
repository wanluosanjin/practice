using System;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Text.RegularExpressions;
using System.Data;

namespace MyWpf
{
    static class Tool{
        //拓展方法,可以直接对byte[]使用
        public static string ToHexStrFromByte(this byte[] byteDatas)
        {
            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < byteDatas.Length; i++)
            {
                builder.Append(string.Format("{0:x2}", byteDatas[i]));
            }
            return builder.ToString().Trim();
        }

        public static byte[] ToBytesFromHexString(this string hexString)
        {
            //以 ' ' 分割字符串，并去掉空字符
            string[] chars = hexString.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
            byte[] returnBytes = new byte[chars.Length];
            //逐个字符变为16进制字节数据
            for (int i = 0; i < chars.Length; i++)
            {
                returnBytes[i] = Convert.ToByte(chars[i], 16);
            }
            return returnBytes;
        }

        /// <summary>
        /// 16进制格式字符串转普通文本
        /// </summary>
        /// <param name="hexString">16进制格式字符串</param>
        /// <param name="encode">编码规则</param>
        /// <returns></returns>
        // 使用： string hexStr= "%01#abcABCR00051**\r\n".ToHexString(Encoding.ASCII);
        public static string ToStringFromHexString(this string hexString, Encoding encode)
        {
            byte[] _bytes = ToBytesFromHexString(hexString);
            return encode.GetString(_bytes);
        }
        public static void zipfile(string file,string zip)//添加文件似乎会重写整个文件...
        {
            //create删除原有,默认readwrite打开
            using(FileStream fs = new FileStream(zip,FileMode.OpenOrCreate))
            {
                using (ZipArchive archive = new ZipArchive(fs, ZipArchiveMode.Update))
                {
                    //create同名会取代原来的文件
                    ZipArchiveEntry getentry = archive.GetEntry(Path.GetFileName(file));
                    if (getentry == null)
                    {
                        ZipArchiveEntry createntry = archive.CreateEntry(Path.GetFileName(file));
                        using (Stream sr = createntry.Open())
                        {
                            //file不存在报错
                            using (FileStream source = File.Open(file, FileMode.Open))
                            {
                                // Console.WriteLine("Source length: {0}", source.Length.ToString());
                                source.CopyTo(sr);
                            }
                        }
                    }
                    else
                    {
                        Console.WriteLine($"{file}在{zip}中同名文件已存在");
                    }
                }
            }
        }
        //不压缩文件夹
        public static void zipfiles(IEnumerable<string> files,string zip)
        {
            using(FileStream fs = new FileStream(zip,FileMode.OpenOrCreate))
            {
                using (ZipArchive archive = new ZipArchive(fs, ZipArchiveMode.Update))
                {
                    foreach (var file in files)
                    {
                        //我又傻了,不是文件则跳过
                        if (!(isfile(file)??false))
                        {
                            continue;
                        }
                        ZipArchiveEntry getentry = archive.GetEntry(Path.GetFileName(file));
                        if(getentry!=null){
                            Console.WriteLine(file+"文件已存在");
                        } else {
                            ZipArchiveEntry createntry = archive.CreateEntry(Path.GetFileName(file));
                            using (Stream sr = createntry.Open())
                            {
                                using (FileStream source = File.Open(file,FileMode.Open))
                                {
                                    Console.WriteLine("Source length: {0}", source.Length.ToString());
                                    source.CopyTo(sr);
                                }
                            }
                        }
                    }
                }
            }
        }
        //保留原本dir名
        public static void delsingledirwithparentdir(string path){
            var list = Directory.EnumerateFileSystemEntries(path);
            foreach (var item in list)
            {
                if(issingledir(item)??false){
                    Console.WriteLine(item+"is singledir");
                    var subdir=Directory.GetDirectories(item)[0];
                    var dirname=Path.GetFileName(item);
                    Directory.Move(subdir,Path.GetDirectoryName(subdir)+"123");
                    Directory.Delete(Path.GetDirectoryName(subdir));
                    Directory.Move(Path.GetDirectoryName(subdir)+"123",Path.GetDirectoryName(subdir));
                }
            }
        }
        public static void delsingledir(string path){
            var list = Directory.EnumerateFileSystemEntries(path);
            foreach (var item in list)
            {
                if(issingledir(item)??false){
                    Console.WriteLine(item+"is singledir");
                    var subdir=Directory.GetDirectories(item)[0];
                    var subdirname=Path.GetFileName(subdir);
                    Directory.Move(subdir,Path.Combine(Path.GetDirectoryName(item),subdirname));
                    Directory.Delete(item);
                }
            }
        }
        public static Boolean? issingledir(string path){
            if(isfile(path) ?? throw new IOException(path+"不存在")){
                return null;
            }
            var enumerator = Directory.EnumerateFileSystemEntries(path).GetEnumerator();
            if (enumerator.MoveNext())
            {
                return true;
            }
            return false;
            // if(new List<string>(Directory.EnumerateFileSystemEntries(path)).Count==1){
            //     return true;
            // }
        }
        public static void move(string path,string dst){
            try
            {
                Directory.Move(path,dst);
            }
            catch (IOException e)
            {
                if (Directory.GetDirectoryRoot(path) != Directory.GetDirectoryRoot(dst)){
                    CopyDirectory(new DirectoryInfo(path), new DirectoryInfo(dst));
                } else 
                //前缀不存在要建立前缀
                if(!Directory.Exists(Path.GetDirectoryName(dst))){
                    Directory.CreateDirectory(Path.GetDirectoryName(dst));
                    Directory.Move(path,dst);
                } else throw new IOException($"move出错了\n{path}\n{dst}",e);
            }
        }
        public static Boolean? isfile(string path){
            if(File.Exists(path))
            {
                // This path is a file
                return true;
            }
            else if(Directory.Exists(path))
            {
                // This path is a directory
                return false;
            }
            else
            {
                Console.WriteLine("{0} is not a valid file or directory.", path);
                return null;
            }
        }
        public static void delempty(string startPath){
            var list = Directory.EnumerateDirectories(startPath);
            foreach (var path in list)
            {
                if(new List<string>(Directory.EnumerateFileSystemEntries(path)).Count==0){
                    Directory.Delete(path);
                }
            }
        }
        public static void erokanzip(string p1,string p2){
            var list = Directory.GetDirectories(p1);
            foreach (var net in list)
            {
                var netname = Path.GetFileName(net);
                foreach (var net1 in Directory.GetDirectories(net))
                {
                    var net1name = Path.GetFileName(net1);
                    foreach (var net2 in Directory.GetDirectories(net1))
                    {
                        var net2name = Path.GetFileName(net2);
                        var destzip =Path.Combine(p2,netname,net1name,net2name+".zip");
                        if(isfile(destzip)??false){
                            int Entriesnum;
                            using (ZipArchive archive = ZipFile.OpenRead(destzip)){
                                Entriesnum=archive.Entries.Count;
                            }
                            var Filesnum=Directory.GetFiles(net2).Length;
                            if(Entriesnum==Filesnum){

                            } else {
                                Console.WriteLine(destzip+"已存在"+"文件数"+Entriesnum.ToString());
                                Console.WriteLine(net2+"文件数"+Filesnum.ToString());
                                Console.WriteLine("这两个文件数不一样,进行合并");
                                using(FileStream fs = new FileStream(destzip,FileMode.OpenOrCreate))
                                {
                                    using (ZipArchive archive = new ZipArchive(fs, ZipArchiveMode.Update))
                                    {
                                        foreach (var file in Directory.GetFiles(net2))
                                        {
                                            ZipArchiveEntry getentry = archive.GetEntry(Path.GetFileName(file));
                                            if (getentry == null)
                                            {
                                                ZipArchiveEntry createntry = archive.CreateEntry(Path.GetFileName(file));
                                                using (Stream sr = createntry.Open())
                                                {
                                                    //file不存在报错
                                                    using (FileStream source = File.Open(file, FileMode.Open))
                                                    {
                                                        Console.WriteLine("Source length: {0}", source.Length.ToString());
                                                        source.CopyTo(sr);
                                                    }
                                                }
                                            }
                                            else
                                            {
                                                Console.WriteLine($"{file}在{destzip}中同名文件已存在");
                                            }
                                        }
                                        //create同名会取代原来的文件
                                    }
                                }
                            }
                        } else {
                            //确保文件路径存在
                            if(!Directory.Exists(Path.GetDirectoryName(destzip))){
                                Directory.CreateDirectory(Path.GetDirectoryName(destzip));
                            }
                            ZipFile.CreateFromDirectory(net2,destzip);
                        }
                    }
                }
            }
        }

        //处理mysql的方法
        public static void imgmove(){
            var sql = new MySql();
            var map= new Dictionary<string,string>();
            map.Add("m2","momoniji");
            // map.Add("m","moeimg");
            // map.Add("ni","nijinchu");
            // map.Add("n2","nijifeti");
            // map.Add("n3","nijix");
            foreach (var m in map)
            {
                var root=$"D:\\img\\erokan\\{m.Value}";
                string qurey=$"SELECT md5,description FROM test.img where description like \"{m.Key} %\"";
                var table=sql.getimg(qurey);
                var contiandir=new List<string>(Directory.EnumerateDirectories(root));
                foreach (DataRow row in table.Rows)
                {
                    // foreach(DataColumn column in table.Columns)
                    if (row["md5"] is Byte[] bytes){
                        var filename=bytes.ToHexStrFromByte()+".jpg";
                        if(row["description"] is string description){
                            switch (m.Value)
                            {
                                case "moeimg":
                                    move(Path.Combine(root,filename),Path.Combine(root,description.Split(" ")[1],description.Split(" ")[2]+".jpg"));
                                    break;
                                case "nijinx":
                                    move(Path.Combine(root,filename),Path.Combine(root,description.Split(" ")[1],description.Split(" ")[2]+".jpg"));
                                    break;
                                case "momoniji":
                                    //第二个参数是substring长度
                                    //不能跨盘移动
                                    try
                                    {
                                        if(File.Exists(Path.Combine(root+"\\有重复",filename))){
                                            move(Path.Combine(root+"\\有重复",filename),Path.Combine(root,description.Substring(3,description.Length-6),description.Substring(description.Length-3)+".jpg"));
                                        }
                                        // zip(Path.Combine(root,filename),Path.Combine(@"D:\img\erokan\momoniji",description.Substring(3,description.Length-6)+".zip"));
                                    }
                                    catch (System.Exception e)
                                    {
                                        Console.WriteLine(e.ToString());
                                        File.Delete(Path.Combine(root+"\\有重复",filename));
                                        Console.WriteLine("del");
                                    }
                                    break;
                                case "nijinchu":
                                    try
                                    {
                                        if(Regex.IsMatch(description.Substring(3),@"^\d{14}\S*")){
                                            if(!contiandir.Contains(Path.Combine(root,description.Substring(3,14)))){
                                                move(Path.Combine(root,filename),Path.Combine(root,description.Substring(3,14),description.Substring(18)+".jpg"));
                                            }
                                        }
                                    }
                                    catch (Exception)
                                    {
                                        Console.WriteLine($"{nameof(m)}");
                                    }
                                    break;
                                case "nijifeti":
                                    var imgnames=description.Substring(3).Split("-");
                                    if(imgnames.Length==3){
                                        move(Path.Combine(root,filename),Path.Combine(root,imgnames[0]+"-"+imgnames[1],imgnames[2]+".jpg"));
                                    }
                                    if(imgnames.Length==4){
                                        move(Path.Combine(root,filename),Path.Combine(root,imgnames[0]+"-"+imgnames[1],imgnames[2]+"-"+imgnames[3]+".jpg"));
                                    }
                                    break;
                                default:
                                break;
                            }
                        }
                    }
                }
            }
        }
        //temp 转 book
        public static void temptobook(){
            var sql = new MySql();
            string qurey="SELECT * FROM temp limit 231000,50000";
            var table=sql.getimg(qurey);
            foreach(DataRow row in table.Rows){
                if (row["id"] is int id){
                    if (row["name"] is string name){
                        var teachermatch = Regex.Match(name,@"\[.*?\]");
                        var teacher = teachermatch.Success?teachermatch.ToString():"[]";
                        insert:
                        var teacheridrow = sql.getone($"SELECT id FROM test.teacher where teacher = ?;",teacher);
                        if(teacheridrow==null){
                            sql.insert($"insert teacher value(null,?)",new string[]{teacher});
                            goto insert;
                        }
                        var teacherid=teacheridrow[0] is int?(int)teacheridrow[0]:throw new Exception("aaa");
                        sql.insert($"insert ignore book value ({id},\"{teacherid}\",?)",name);
                    }
                }
            }
        }
        //zippath不能为非zip结尾且已存在的文件
        public static void zip(string path,string zippath){
            var p1isfile = isfile(path)??throw new IOException($"{path}不存在");
            var p2isfile = isfile(path);
            var p2exist = p2isfile!=null;
            var p2endwithzip = zippath.EndsWith(".zip");
            if(p2exist){
                //p2存在
                if(p2isfile??false){
                    //p2已存在文件
                    Console.WriteLine("对zip添加文件似乎很麻烦");
                    if(p1isfile){
                        zipfile(path,zippath);
                    } else {
                        //逐个添加
                        Console.WriteLine("暂不支持添加文件夹至zip文件");
                        Console.WriteLine(path);
                        Console.WriteLine(zippath);
                    }
                } else {
                    //p2已存在文件夹
                    if(p1isfile){
                        zipfile(path,Path.Combine(zippath,Path.GetFileNameWithoutExtension(path)+".zip"));
                    } else {
                        var newzippath = Path.Combine(zippath,Path.GetFileName(path)+".zip");
                        if(File.Exists(newzippath)){
                            Console.WriteLine($"{newzippath}已存在,如需更新请先删除");
                            Console.WriteLine(path);
                            Console.WriteLine(zippath);
                            return;
                        }
                        ZipFile.CreateFromDirectory(path,newzippath);
                    }
                }
            } else{
                //p2不存在
                if(p2endwithzip){
                    if(!Directory.Exists(Path.GetDirectoryName(zippath))){
                        Directory.CreateDirectory(Path.GetDirectoryName(zippath));
                    }
                    if(p1isfile){
                        zipfile(path,zippath);
                    } else {
                        ZipFile.CreateFromDirectory(path,zippath);
                    }
                }
                else{
                    if(!Directory.Exists(zippath)){
                        Directory.CreateDirectory(zippath);
                    }
                    if(p1isfile){
                        zipfile(path,Path.Combine(zippath,Path.GetFileNameWithoutExtension(path)+".zip"));
                    } else {
                        var newzippath = Path.Combine(zippath,Path.GetFileName(path)+".zip");
                        ZipFile.CreateFromDirectory(path,newzippath);
                    }
                }
            }
        }
        public static void bookmove(string bookpath,string teacherdir){
            if(!bookpath.EndsWith(".zip")){
                Console.WriteLine($"{bookpath}必须是.zip文件");
                return;
            }
            var teacher = Regex.Match(bookpath,@"\[.*?\]");
            //使用success来匹配是否成功
            //如果模式匹配成功，则 Value 属性包含匹配的子字符串， Index 属性指示输入字符串中匹配的子字符串的从零开始的起始位置，而 Length 属性指示输入字符串中匹配的子字符串的长度。
            if (teacher.Success)
            {
                move(bookpath,Path.Combine(teacherdir,teacher.ToString(),Path.GetFileName(bookpath)));
            }else{
                move(bookpath,Path.Combine(teacherdir,"[]",Path.GetFileName(bookpath)));
            }

        }
        public static void combinedir(string p1 ,string p2){
            //p2存在则合并两文件夹
            if(Directory.Exists(p2)){
                var p1list = Directory.EnumerateFileSystemEntries(p1);
                foreach (var item in p1list)
                {
                    var filename = Path.GetFileName(item);
                    if(!File.Exists(Path.Combine(p2,filename))){
                        Directory.Move(item,Path.Combine(p2,filename));
                    }
                }//要记得删除
                if(new List<string>(Directory.EnumerateFileSystemEntries(p1)).Count==0){
                    Directory.Delete(p1);
                }
            } else{
                throw new IOException($"{p2}不存在");
            }
        }
        static void CopyDirectory(DirectoryInfo diSourceDir, DirectoryInfo diDestDir)
            {
                if (!diDestDir.Exists) diDestDir.Create();
                FileInfo[] fiSrcFiles = diSourceDir.GetFiles();
                foreach (FileInfo fiSrcFile in fiSrcFiles)
                {
                    fiSrcFile.CopyTo(Path.Combine(diDestDir.FullName, fiSrcFile.Name));
                }
                DirectoryInfo[] diSrcDirectories = diSourceDir.GetDirectories();
                foreach (DirectoryInfo diSrcDirectory in diSrcDirectories)
                {
                    CopyDirectory(diSrcDirectory, new DirectoryInfo(Path.Combine(diDestDir.FullName, diSrcDirectory.Name)));
                }
            }
    }
}