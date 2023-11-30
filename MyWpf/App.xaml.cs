using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Threading;
using System.IO;

namespace MyWpf
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        void App_DispatcherUnhandledException(object sender, DispatcherUnhandledExceptionEventArgs e)
        {
            // Process unhandled exception
            using (StreamWriter errorLog = new StreamWriter("error.log",true)){
                errorLog.WriteLine($"Error @ {DateTime.Now.ToString()}");
                errorLog.WriteLine(e.Exception.ToString());
            }
            // Prevent default unhandled exception processing
            e.Handled = true;

            MessageBox.Show("An error occured."+e.Exception.ToString());
        }
    }
}
