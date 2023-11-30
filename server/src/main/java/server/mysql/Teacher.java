package server.mysql;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Column;
import javax.persistence.OneToMany;
import javax.persistence.JoinColumn;
import javax.persistence.CascadeType;
import javax.persistence.FetchType;
import javax.persistence.Table;
import java.util.HashSet;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;

// 使用@query必须使用table,entity已经废弃
@Entity
@Table (name="teacher")
public class Teacher implements Serializable {  

    @Id
    @Column(name="id")
    private Integer id;  

    @Column(name="teacher")
    private String teacher;

    // fetch有两个类型，LAZY和EAGER　　
    // mappedby是其他表的特殊类字段
    @OneToMany(
        targetEntity = Book.class,
        cascade = CascadeType.ALL, 
        orphanRemoval = true,
        fetch = FetchType.LAZY,
        mappedBy = "teacherid"
    )
    private List<Book> books = new ArrayList<Book>();

    public Teacher() {  
        super();  
    }  

    public Teacher(Integer id, String teacher) {  
        super();  
        this.id = id;
        this.teacher = teacher;
    }  

    public Integer getId() {  
        return id;  
    }  

    public void setId(Integer id) {  
        this.id = id;  
    }  

    public String getTeacher() {  
        return teacher;  
    }  

    public void setTeacher(String teacher) {  
        this.teacher = teacher;  
    }  

    public List<Book> getBooks() {  
        return books;  
    }  

    public void setBooks(List<Book> books) {  
        this.books = books;  
    }  

}  