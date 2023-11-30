package server.book;

// import server.mysql.Book;会直接覆盖同类Book
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.File;
import java.io.IOException;
import java.util.stream.Stream;
import java.io.ByteArrayOutputStream;
import java.io.OutputStreamWriter;
import java.nio.charset.Charset;
import java.util.stream.Collectors;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BookPath 
{
    static final String root="C:\\imgs\\erokan\\bookthumb";
    static final Pattern p = Pattern.compile("\\[.*?\\]");
    List<String> teacherlist;
    List<String> booklist;

    public static String getTeacher(String path){
        Matcher m = BookPath.p.matcher(path);
        m.find();
        return m.group();
    }
    public static String getBookName(String path){//返回最后一个名字,数组不能用[-1]极其脑残
        String[] split = path.split("\\\\");
        return split[split.length-1];
    }

    public static Boolean pathExists(Path path){
        return path.toFile().exists();
    }

    public static Boolean exists(String teacher,String bookname){
        try{
            return Path.of(root,teacher,bookname).toFile().exists();
        }catch(Exception e){
            System.out.println(teacher+" "+bookname+"不存在");
            return false;
        }
    }

    public static List<String> list(String teacher,String bookname){
        List<String> list = Arrays.asList(Path.of(root,teacher,bookname).toFile().list());
        list.sort((a,b)->{
            return Integer.valueOf(a.split("\\.")[0])-Integer.valueOf(b.split("\\.")[0]);
            // 注意： . 、 $、 | 和 * 等转义字符，必须得加 \\。
            // 注意：多个分隔符，可以用 | 作为连字符。
        });
        return list;
    }

    public static List<Book> bookToBook(List<server.mysql.Teacher> list){
        return list.stream()
            .flatMap(teacher->teacher.getBooks().stream()
            .map(book->new Book(teacher.getTeacher(),
                String.valueOf(book.getId())+" "+book.getName(),
                exists(teacher.getTeacher(),String.valueOf(book.getId())))))
            .collect(Collectors.toList());
    }

    public static Path bookToBook(Book book){
        return Path.of(root,book.getTeacher(),book.getBookName());
    }

    public static Book pathToBook(String path){
        String teacher = getTeacher(path);
        String bookname = getBookName(path);
        Boolean downloaded = exists(teacher,bookname);
        return new Book(teacher,bookname,downloaded);
    }

    public void frashBooklist(String teacher){
        try{
            //Files.list方法返回全名,File.list返回单名
            teacherlist =Files.list(Path.of(root,teacher)).map(e->e.toString()).collect(Collectors.toList());;
            // booklist=Arrays.asList(Path.of(root,teacher).toFile().list());
        }catch(IOException e){
            e.printStackTrace();
        };
    }
    public List<String> getBookList(){
        return this.booklist;
    }
    public List<String> getTeacherList(){
        return this.teacherlist;
    }
    public static void main( String[] args )
    {
        String path ="C:\\imgs\\bookthumb\\[蛹虎次郎]";
        
        System.out.println(Path.of(root,getTeacher(path)).toFile().exists());

        //println调用tostring,没重写tostring的类返回地址,数组也返回地址
        //数组初始化直接加{}
        // m.results()
        //     .map(e->e.group().toString())
        //     .findFirst()
        //     .ifPresent(System.out::println);
        
    }
    // public static void main(String[] args) {
    //     System.out.println("Default Charset=" + Charset.defaultCharset());
    //     System.out.println("file.encoding=" + System.getProperty("file.encoding"));
    //     System.out.println("Default Charset=" + Charset.defaultCharset());
    //     System.out.println("Default Charset in Use=" + getDefaultCharSet());
    // }

    private static String getDefaultCharSet() {
        OutputStreamWriter writer = new OutputStreamWriter(new ByteArrayOutputStream());
        String enc = writer.getEncoding();
        return enc;
    }
}