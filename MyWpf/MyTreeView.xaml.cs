using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Globalization;

using System.Windows;
using System.Windows.Data;
using System.Windows.Controls;
using System.Collections.ObjectModel;

namespace MyWpf{
    public class GetFileSystemInfosConverter : IValueConverter {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture){
            try
            {
                if(value is DirectoryInfo info){
                    return ((DirectoryInfo)value).GetFileSystemInfos();
                }
            }
            catch
            {
            }
            return null;
        }
        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture){
            throw new NotImplementedException();
        }
    }
    public partial class MyTreeView : TreeView
    {

        public MyTreeView(){
            //
        InitializeComponent();
        frash(@"C:\Users\onelor\game");
            //template渲染是加载器做的,必须写在xaml里,不然不能为渲染的控件设置binding
            // var temp = new HierarchicalDataTemplate{
            //     DataType=typeof(DirectoryRecord)
            // };
            // var treeViewFactory = new FrameworkElementFactory(typeof(TextBlock));
            // var textBlockBinding = new Binding{Path=new PropertyPath("Info.Name")};
            // treeViewFactory.SetBinding(TextBlock.TextProperty,textBlockBinding);
            // temp.VisualTree=treeViewFactory;
            // var itemsSourceBinding = new Binding{Path=new PropertyPath("Directories")};
            // temp.VisualTree.SetBinding(TreeView.ItemsSourceProperty,itemsSourceBinding);
            // Resources.Add("HierarchicalDataTemplate",temp);
        }

        public void frash(string path){
            //ItemsSource添加其他内容会直接tostring,不会使用模板
            var directory = new ObservableCollection<FileSystemInfos>();
            Directory.GetFileSystemEntries(path).ToList().ForEach(e=>directory.Add(new FileSystemInfos{Info=new DirectoryInfo(e)}));
            ItemsSource = directory;
        }
    }
}