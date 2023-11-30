package aaa;

//静态导入后把此类设成主类了
import static aaa.Tool.*;

import java.util.Scanner;

import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.LinkedList;

import java.util.concurrent.Callable;

import java.util.function.Function;
import java.util.function.Supplier;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import java.nio.charset.Charset;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.nio.file.StandardCopyOption ;

import java.nio.file.FileVisitOption;
import java.nio.file.FileVisitResult;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Service;

import org.springframework.beans.factory.annotation.Autowired;

@Configuration
//扫描不到,大概是因为直接java运行所以classpath没这个class
@ComponentScan(basePackages="aaa")
class My{

    public static void main(String... args){
        var dl= new Download();
        var list=readline("scrapy.txt");
        for(int i=1;i<=20;i++){
            720
                // dl.addmoeimg(String.valueOf(i*2-1+Integer.valueOf(list.get(0).split(" ")[1])));
                // dl.addmoeimg(String.valueOf(i*2+Integer.valueOf(list.get(0).split(" ")[1])));
                dl.addmomoniji(String.valueOf(i+Integer.valueOf(list.get(1).split(" ")[1])));
                // dl.addnijinchu(String.valueOf(i+Integer.valueOf(list.get(2).split(" ")[1])));
                // dl.addnijifeti(String.valueOf(i+Integer.valueOf(list.get(3).split(" ")[1])));
                // dl.adderokannet(String.valueOf(i*2-1+Integer.valueOf(list.get(4).split(" ")[1])));
                // dl.adderokannet(String.valueOf(i*2+Integer.valueOf(list.get(4).split(" ")[1])));
        }
        // for(int i=1;i<=100;i++){
        //     dl.addindexthumb(String.valueOf(i+Integer.valueOf(list.get(5).split(" ")[1])));
        // }
        //m 10000 10 nijinchu10000 24 nijix1000 16 nijifeti10000 30 momoniji10000 20
        //\0\1是乱码
        //of方法即使路径有错也不会蹦错
        //java编译文件是gkb编码,中文路径会乱码
        //function参数只能用integer,不能用int
        // ApplicationContext ctx = new AnnotationConfigApplicationContext(Mybook.class);
        // 空字符串不是null
        //似乎excutebatch速度比较慢
        //int也可以加""
        //记得加trim()
        //匿名类不能使用外部局部变量
        // String root="C:\\Users\\onelor\\Pictures";
        // var mysql=new Mysql();
        // final int[] i = {0};
        // var ss=mysql.execute("SELECT SUBSTRING_INDEX(description,',',-1) as last FROM test.indexthumb");
        // ss.stream()
        // .forEach(e->{
        //     i[0]++;
        //     if(i[0]>231700){
        //         var book = mybookmatch(MyPatterns.teacherpattern,e);
        //         var teachername= book==null?"[]":book.teacher;
        //         var bookname= book==null?e:book.name==null?"":book.name;
        //         var sql="SELECT id FROM test.teacher where teacher=\""+teachername+"\"";
        //         var teacherid=mysql.execute(sql);
        //         var insertsql = "insert test.book value(null,?,?)";
        //         if(i[0]%100==0)print(String.valueOf(i[0]));
        //         if(teacherid.size()==1){
        //             mysql.executebatch(insertsql,List.of(bookname,teacherid.get(0)));
        //         }
        //     }
        // });
        // distinct()方法对null也去重

        // getallsubpath(pathof(root))
        // .stream()
        // //mypattern只初始化了一次
        // .filter(e->Optional.ofNullable(mybookmatch(MyPatterns.teacherpattern,e.toString())).isPresent())
        // //null的输出是null
        // .forEach(e->{
        //     print("检测到:"+e.toString());
        //     if(inString().equals("1")){
        //         print("123");
        //     }
        // });
    }
}

@Configuration
class Configtest{
    @Bean
    public Function<Integer,Integer> func(){
        return a->1;
    }
    @Bean
    public Function<Integer,Integer> func2(){
        return a->a+2;
    }
}

class Book{
    public String teacher;
    public String name;

    //name用了trim()
    public Book(String teacher,String name){
        this.teacher=teacher;
        this.name=name.trim();
    }

    public String toString(){
        //string类下有很多静态方法,不要用Boolean类的toString方法
        return teacher+" "+name;
    }
}


enum MyPatterns{
    teacherpattern("(\\[.*?\\])(.*)");
    public Pattern pattern;
    MyPatterns(String s){
        pattern=Pattern.compile(s);
    }
}

class FindFileVisitor extends SimpleFileVisitor<Path>{
    private List<Path> result;
    public FindFileVisitor(List<Path> result){
        this.result = result;
    }
    @Override
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs){
        System.out.println("file:" + file);
        System.out.println("1 for add,0 for jump all");
        var s = inString();
        if(s.equals("1")){
            result.add(file);
            return FileVisitResult.CONTINUE;
        }
        if(s.equals("0")){
            return FileVisitResult.SKIP_SIBLINGS;
        }
        return FileVisitResult.CONTINUE;
    }
    // 这四个方法中的每个都返回一个FileVisitResult枚举实例。FileVisitResult枚举包含以下四个选项:
    // CONTINUE继续意味着文件的执行应该像正常一样继续。
    // TERMINATE终止意味着文件遍历现在应该终止。
    // SKIP_SIBLINGS跳过同级意味着文件遍历应该继续，但不需要访问该文件或目录的任何同级。
    // SKIP_SUBTREE跳过子级意味着文件遍历应该继续，但是不需要访问这个目录中的子目录。这个值只有从preVisitDirectory()返回时才是一个函数。如果从任何其他方法返回，它将被解释为一个CONTINUE继续。
    public FileVisitResult visitFileFailed(Path file, IOException exc) throws IOException {
        System.out.println("visit file failed: " + file);
        return FileVisitResult.CONTINUE;
    }

    //在访问任何目录之前调用preVisitDirectory()方法。
    //在访问一个目录之后调用postVisitDirectory()方法。
    public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException {
        return FileVisitResult.CONTINUE;
    }
    public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) throws IOException {
        System.out.println("dir:" + dir);
        System.out.println("1 for add and in,0 for jump all");
        var s = inString();
        //这里不能用var
        //无返回接口可以直接用runnable,有返回用callable
        Map<String,Supplier<FileVisitResult>> map = Map.of("1",()->{
                result.add(dir);
                return FileVisitResult.CONTINUE;
            },"0",()->{
                return FileVisitResult.SKIP_SIBLINGS;
            },"",()->{
                return FileVisitResult.SKIP_SUBTREE;
            });
        return map.get(s).get();
    }

}