using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Input;

namespace MyWpf
{
    public partial class MyContentControl : Grid{
        public MyContentControl(){
            InitializeComponent();
        }

        private void rect1_MouseDown(object sender, MouseButtonEventArgs e)
        {
            MessageBox.Show("I'm Clicked!");
        }

        private void UserControl_Loaded(object sender, RoutedEventArgs e)
        {
            Height = rect1.ActualHeight;
            Width = rect1.ActualWidth;
        }
        void OnSliderValueChanged(object sender,EventArgs args){
            byte r=(byte)redSlider.Value;
            byte g=(byte)greenSlider.Value;
            byte b=(byte)blueSlider.Value;

            redValue.Text = r.ToString("X2");
            greenValue.Text = g.ToString("X2");
            blueValue.Text = b.ToString("X2");

            brushResult.Color = Color.FromArgb(255,r,g,b);
        }
    }
}