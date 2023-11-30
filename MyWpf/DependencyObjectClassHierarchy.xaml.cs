using System;

using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Text;
using System.Windows.Input;

using System.Collections;
using System.Collections.Generic;

using System.Reflection;

namespace MyWpf
{
    class ClassAndSubclasses
    {
        public Type Type {protected set; get; }
        public List<ClassAndSubclasses> Subclasses {protected set; get; }
        public ClassAndSubclasses(Type parent)
        {
            this.Type = parent;
            this.Subclasses = new List<ClassAndSubclasses>();
        }
    }
    public partial class DependencyObjectClassHierarchy : ScrollViewer
    {
        Type rootType = typeof(Object);
        TypeInfo rootTypeInfo = typeof(DependencyObject).GetTypeInfo();
        List<Type> classes = new List<Type>();
        Brush highlightBrush;
        public DependencyObjectClassHierarchy(){
            InitializeComponent();
            highlightBrush = new SolidColorBrush(Colors.AliceBlue);

            AddToClassList(rootType);
            var rootclass = new ClassAndSubclasses(rootType);
            AddToTree(rootclass,classes);
            Display(rootclass,0);

        }
        void AddToClassList(Type sampleType){
            //输入DependencyObject只有两个类DependencyObject,和freeze
            //得到的时base类
            Assembly assembly = sampleType.GetTypeInfo().Assembly;
            foreach (var type in assembly.ExportedTypes)
            {
                var typeInfo = type.GetTypeInfo();
                //使用object时只有object一个,IsAssignableFrom判定object似乎有例外
                if(typeInfo.IsPublic && rootTypeInfo.IsAssignableFrom(typeInfo)){
                    classes.Add(type);
                }
            }
        }
        void AddToTree(ClassAndSubclasses parentClass, List<Type> classes){
            foreach (var type in classes)
            {
                var baseType = type.GetTypeInfo().BaseType;
                if(baseType == parentClass.Type){
                    var subClass = new ClassAndSubclasses(type);
                    parentClass.Subclasses.Add(subClass);
                    AddToTree(subClass,classes);
                }
            }
        }

        void Display(ClassAndSubclasses parentClass, int indent){
            var typeInfo = parentClass.Type.GetTypeInfo();
            TextBlock txtblk = new TextBlock();
            txtblk.Inlines.Add(new string(' ',8*indent));
            txtblk.Inlines.Add(new string(typeInfo.Name));
            stackPanel.Children.Add(txtblk);
            foreach (var subclass in parentClass.Subclasses)
            {
                Display(subclass,indent+1);
            }
        }
    }
}