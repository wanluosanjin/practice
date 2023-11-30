using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Text.RegularExpressions;
using System.Linq;

namespace MyWpf
{
    public enum StoreType{
        game,book,doujin,cg,img,other
    }
    public enum PathType{
        wrong,file,emptydir,allfiledir,hasdir
    }

    class MyButton : Button {
        MyButton(){
            MinHeight = FontSize;
        }
    }
    public partial class MyDialog : Window
    {

        static System.Array enumvalues = System.Enum.GetValues(typeof(StoreType));
        public ListBox listBoxBookType = new ListBox();
        public ListBox listBoxTeacher = new ListBox();

        ListBox showIsStored = new ListBox();
        //不能使用{}初始化???
        public StoreType storeType;

        string storePath;

        WrapPanel wrapPanel=new WrapPanel();
        public MyDialog(string path,string storePath)
        {
            // InitializeComponent();用来解析xaml
            this.Content = wrapPanel;
            this.storePath=storePath;
            this.MaxWidth=500;
            this.SizeToContent=SizeToContent.Width;
            this.WindowStartupLocation=WindowStartupLocation.CenterOwner;
            this.Title="处理book";
            
            listBoxBookType.SelectionMode = SelectionMode.Extended;
            listBoxBookType.ItemsSource = enumvalues;
            //最好设个值,否则在选择之前调用seletitem会出错
            listBoxBookType.SelectedIndex = 0;
            listBoxBookType.MinWidth=this.MaxWidth/2;
            wrapPanel.Children.Add(listBoxBookType);

            // var teachermatch = Regex.Match(path,@"\[.*?\]");
            // var teacher = teachermatch.Success?teachermatch.Value:"[]";
            
            listBoxTeacher.Items.Add("[]");
            var teachersMatch = Regex.Matches(path,@"\[.*?\]");
            //teachersMatch.Select(e=>e.ToString()).toList().Select(listBoxTeacher.Items.Add)无法添加????????
            foreach (var teacher in teachersMatch.Select(e=>e.ToString()))
            {
                listBoxTeacher.Items.Add(teacher);
            }
            listBoxTeacher.SelectedIndex = 0;
            listBoxTeacher.MinWidth=this.MaxWidth/2;
            wrapPanel.Children.Add(listBoxTeacher);

            showIsStored.MinWidth=this.MaxWidth/2;
            wrapPanel.Children.Add(showIsStored);

            var ok=new Button(){Content="ok"};
            ok.Click+=okclick;
            ok.MinHeight=30;
            ok.MinWidth=30;
            wrapPanel.Children.Add(ok);

            var cancel=new Button(){Content="cancel"};
            cancel.IsCancel=true;
            wrapPanel.Children.Add(cancel);

            var showIsStoredButton=new Button(){Content="showIsStored"};
            showIsStoredButton.IsDefault=true;
            showIsStoredButton.Click+=showIsStoredButtonEvent;
            wrapPanel.Children.Add(showIsStoredButton);
        }

        void showIsStoredButtonEvent(object sender, RoutedEventArgs e){
            var selectPath=Path.Combine(storePath,Path.Combine(listBoxBookType.SelectedItem?.ToString(),listBoxTeacher.SelectedItem?.ToString()));
            var exists = Directory.Exists(selectPath);
            if(exists){
                showIsStored.ItemsSource = Directory.GetFileSystemEntries(selectPath);
            } else {
                this.Title="所选路径不存在";
            }
        }
        void okclick(object sender, RoutedEventArgs e){
            this.DialogResult=true;
        }
        
    }
}