using System;
using System.Diagnostics;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Data;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using System.Reflection;
using static csharp.Tool;

using Microsoft.Win32;
// #nullable enable

namespace csharp
{
    class Program
    {
        //解压zip可能需要导入gbk,要先项目添加dll,再在zipfile的解压方法参数里添加
        // System.Text.Encoding.RegisterProvider (System.Text.CodePagesEncodingProvider.Instance);
        // var gbk=Encoding.GetEncoding("GB2312");
        // var list = Directory.EnumerateFileSystemEntries(startPath,"*.jpg",SearchOption.AllDirectories);
        // string qurey="SELECT book.id,teacher,name FROM test.book,teacher where teacher.id=book.teacherid LIMIT 0, 50";


        public static void combineteacher(string p1){
            var list = Directory.GetDirectories(p1);
            for (int i = 0; i < list.Length; i++)
            {
                var name=Path.GetFileName(list[i]);
                if(name.Contains('(')){
                    var name2=Path.GetFileName(list[i+1]);
                    if(name2.Contains('(')){
                        var prename = name.Split('(')[0];
                        var prename2 = name2.Split('(')[0];
                        if(prename.Equals(prename2)){
                            var dest=prename.Trim()+"]";
                            try
                            {
                                combinedir(list[i],Path.Combine(p1,dest));
                                combinedir(list[i+1],Path.Combine(p1,dest));
                            }
                            catch (IOException)
                            {
                                Console.WriteLine(list[i]);
                            }
                        }
                    }
                }
            }
        }

        public class Forecast{
            public DateTime Date {get;set;}
            public string Summary {get;set;}
        }

        record Data(string a,string b,string c);
        
        static void Main(string[] args)
        {
            // var p1=@"C:\imgs\erokan";
            // var p2=@"D:\img\erokan";
            // erokanzip(p1,p2);
            Action<string> a = Console.WriteLine;
            a+=Console.WriteLine;
            Action<string,string> b = Console.WriteLine;
            Func<string,Action> f=(string s)=>{
                return  ()=>a(s);
            };
            f("a")();
            foreach (var item in Directory.GetDirectories(@"C:\Users\onelor\Documents\book\英文"))
            {
                isSingleDirAndDel(item,KeepParentDirOrSubDir.Sub);
            }

        }
    }
}
