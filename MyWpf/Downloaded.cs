using System;
using System.Data;
using System.Collections.Generic;

namespace MyWpf{
    public class Downloaded{
        MySql mySql;
        List<string> bookids;//似乎可以不用转list
        public Downloaded(MainWindow mainWindow){
            mySql=mainWindow.mySql;
            var bookidsTable=mySql.getDownloadedBookids();
            bookids=new List<string>(bookidsTable.Rows.Count);
            for(int i=0;i<bookidsTable.Rows.Count;i++)
            {
                bookids.Add(bookidsTable.Rows[i]["id"].ToString());
            }
        }
        public bool ifDownloaded(string bookid){
            return bookids.Contains(bookid);
        }
    
    }
}
