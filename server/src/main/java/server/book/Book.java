package server.book;

public class Book
{
    String teacher;
    String bookname;//带bookid
    Boolean downloaded;
    public Book(String teacher,String bookname,Boolean downloaded){
        this.teacher=teacher;
        this.bookname=bookname;
        this.downloaded=downloaded;
    }
    public String getTeacher(){
        return this.teacher;
    }
    public String getBookName(){//数据的大小写似乎是按照get方法判定的
        return this.bookname;
    }
    public Boolean getDownloaded(){
        return this.downloaded;
    }
}