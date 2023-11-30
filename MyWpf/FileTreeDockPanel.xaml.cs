using System;
using System.IO;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace MyWpf
{
    class FileSystemInfos
    {
        public FileSystemInfo Info { get; set; }
        public IEnumerable<FileSystemInfos> Directories
        {
            get
            {
                //但未在用户代码中进行处理: 'Access to the path 'C:\Documents and Settings' is denied.'
                return Info is DirectoryInfo ?  
                from fi in ((DirectoryInfo)Info).GetFileSystemInfos("*", SearchOption.TopDirectoryOnly)
                    // where fi is DirectoryInfo
                    select new FileSystemInfos { Info = fi } 
                : null;
            }
        }
    }
    class DirectoryRecord
    {
        public DirectoryInfo Info { get; set; }

        public IEnumerable<FileInfo> Files
        {
            get
            {
                return Info.GetFiles();
            }
        }

        public IEnumerable<DirectoryRecord> Directories
        {
            get
            {
                //但未在用户代码中进行处理: 'Access to the path 'C:\Documents and Settings' is denied.'
                return from di in Info.GetDirectories("*", SearchOption.TopDirectoryOnly)
                    select new DirectoryRecord { Info = di };
            }
        }
    }
    public partial class FileTreeDockPanel
    {

        public FileTreeDockPanel(){
            //本来不用后来又需要了??
            InitializeComponent();
            Directory_Load();
            fileInfo.AutoGeneratingColumn += fileInfoColumn_Load;
        }

        private void Directory_Load()
        {
            var directory = new ObservableCollection<DirectoryRecord>();

            foreach (var drive in DriveInfo.GetDrives())
            {
                directory.Add(
                    new DirectoryRecord
                    {
                        Info = new DirectoryInfo(drive.RootDirectory.FullName)
                    }
                );
            }

            directoryTreeView.ItemsSource = directory;
        }

        private void fileInfoColumn_Load(object sender, DataGridAutoGeneratingColumnEventArgs e)
        {
            List<string> requiredProperties = new List<string>
            {
                "Name", "Length", "FullName", "IsReadOnly", "LastWriteTime"
            };

            if (!requiredProperties.Contains(e.PropertyName))
            {
                e.Cancel = true;
            }
            else
            {
                e.Column.Header = e.Column.Header.ToString();
            }
        }
    }
}