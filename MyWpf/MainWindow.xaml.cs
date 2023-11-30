using System;
using System.IO;
using System.Data;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

using System.ComponentModel;
using System.Management.Automation;
using System.Diagnostics;
using System.Text;
using System.Text.RegularExpressions;

using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
// using System.Windows.Shapes;

using static MyWpf.Tool;
// using MySql.Data.MySqlClient;
// using PowerShell = System.Management.Automation.PowerShell;

namespace MyWpf
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window//partial拆分定义类,另一个在xaml里定义
    {
        
        // Mod mod;//get set 可以加其他东西
        // public MySql mySql;
        // public DownLoader downloader;
        // public Downloaded downloaded;

        // private void Window_Loaded(object sender, RoutedEventArgs e){
        
        // }
        public MainWindow()
        {
            // mySql=new MySql();
            // // this.WindowState = (WindowState)FormWindowState.Maximized;

            // downloader=new DownLoader(this);
            // mod = new BookthumbMod(this);
            // downloaded=new Downloaded(this);
            InitializeComponent();
            // this.Width = System.Windows.SystemParameters.PrimaryScreenWidth;  
            // this.Height = System.Windows.SystemParameters.PrimaryScreenHeight;
        }

        void dealPath(string path){
            var _isfile=isfile(path)??throw new Exception("路径无效");
            var pathType = _isfile?PathType.file:Directory.EnumerateDirectories(path).GetEnumerator().MoveNext()?PathType.hasdir:Directory.EnumerateFiles(path).GetEnumerator().MoveNext()?PathType.allfiledir:PathType.emptydir;

            var dlg = new MyDialog(path,storePathTextBox.Text);
            dlg.Owner = this;
            var result=dlg.ShowDialog();
            //多选对单选返回第一个
            //
            if(result??false){
                var pathEndWithZipOrRar = path.EndsWith(".zip") || path.EndsWith(".rar");
                var moveTo = Path.Combine(storePathTextBox.Text,Path.Combine(dlg.listBoxBookType.SelectedItem?.ToString(),dlg.listBoxTeacher.SelectedItem?.ToString()),Path.GetFileName(path));
                messageTextBlock.Text=moveTo;

                try
                {
                    switch (pathType)
                    {
                        case PathType.file:
                            //即使也关闭返回ok
                            var filemovechoose=MessageBox.Show($"{Enum.GetName(typeof(PathType),pathType)}\n{path}\n{moveTo}","文件转移,type ok to move");
                            if(filemovechoose==MessageBoxResult.OK)move(path,moveTo);
                        break;
                        case PathType.emptydir:
                            var emptydirchoose = MessageBox.Show($"{path}is a empty dir,wanna del it?","ok for del,close is cancel",MessageBoxButton.OKCancel);
                            if(emptydirchoose==MessageBoxResult.OK)Directory.Delete(path);
                        break;
                        case PathType.allfiledir:
                            //关闭返回cancel
                            var allFileDirChoose = MessageBox.Show($"{path} is a allfiledir dir","ok for zip and cancel for move,close is cancel",MessageBoxButton.OKCancel);
                            if (allFileDirChoose == MessageBoxResult.OK){
                                zip(path,moveTo+".zip");
                            } else if (allFileDirChoose == MessageBoxResult.Cancel){
                                move(path,moveTo);
                            }
                        break;
                        case PathType.hasdir:
                            var hasDirDirChoose = MessageBox.Show($"{path} is a hasDir dir","ok for zip and cancel for move,close is cancel",MessageBoxButton.OKCancel);
                            if (hasDirDirChoose == MessageBoxResult.OK){
                                zip(path,moveTo+".zip");
                            } else if (hasDirDirChoose == MessageBoxResult.Cancel){
                                move(path,moveTo);
                            }
                        break;
                        default:
                        throw new Exception("shouldn't come here,something wrong");
                    }
                }
                catch (IOException e)
                {
                    MessageBox.Show(e.Message,e.Source);
                }
            
            }

        }


        void click1(object sender,RoutedEventArgs args){
            if(isfile(resourcePathTextBox.Text)!=null){
                var entylist = Directory.EnumerateFileSystemEntries(resourcePathTextBox.Text);
                foreach (var path in entylist)
                {
                    var result = MessageBox.Show(path,"处理",MessageBoxButton.YesNoCancel);
                    if(result == MessageBoxResult.Yes){
                        dealPath(path);
                    }else if(result == MessageBoxResult.Cancel){
                        break;
                    }
                }
            } else
            {
                MessageBox.Show(resourcePathTextBox.Text+"不是有效路径");
            }
            //引起一个异常
        }

        void click2(object sender,RoutedEventArgs args){
            dealPath(((FileSystemInfos)my.SelectedItem).Info.FullName);
        }
        void click3(object sender,RoutedEventArgs args){
            if(isfile(resourcePathTextBox.Text)==false){
                my.frash(resourcePathTextBox.Text);
            }
        }

        // 文本输入事件,用最简单的switch
    //     private void txt_input_TextInput(object sender, TextCompositionEventArgs e)
    //     {
    //         // e.text就是键盘值
    //         switch (e.Text)
    //         {
    //             case "d":
    //                 mod.nextimg();
    //                 break;
    //             case "a":
    //                 mod.preimg();
    //                 break;
    //             case "q":
    //                 mod.bookthumb();
    //                 break;
    //             case "w":
    //                 mod.predir();
    //                 break;
    //             case "s":
    //                 mod.nextdir();
    //                 break;
    //             case "p":
    //                 mod.bookfull();
    //                 break;
    //             case "e":
    //                 mod.changelist();
    //                 break;
    //             case "r":
    //                 changemod();
    //                 break;
    //             default:
    //                 string message = "事件：" + e.RoutedEvent + "-值：" + e.Text;
    //                 Console.Out.WriteLine(message);
    //                 break;
    //         }
    //     }
    //     void changemod(){
    //         if (mod is ListMod)
    //         {
    //             mod=new BookthumbMod(this);
    //         }
    //         else
    //         {
    //             mod=new ListMod(this);
    //         }
    //     }
    }




}
