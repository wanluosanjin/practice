package server.mysql;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Column;
import javax.persistence.Table;
import javax.persistence.OneToMany;
import javax.persistence.ManyToOne;
import javax.persistence.JoinColumn;
import javax.persistence.CascadeType;
import javax.persistence.FetchType;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table (name="book")
public class Book implements Serializable {  

    @Id
    @Column(name="id")
    private Integer id;  

    // joincolumn本事就是一列,name为列的名字,默认int,也可以指定其他string列
    // @JsonIgnore，生成Json时不生成StudentEntity 的属性
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "teacherid",insertable = false,updatable = false,referencedColumnName = "id")
    private Teacher teacherid;

    // private Integer teacherid;

    @Column(name="name")
    private String name;


    public Book() {  
        super();  
    }  

    public Book(Integer id, Teacher teacherid, String name) {  
        super();  
        this.id = id;  
        this.name = name;
        this.teacherid = teacherid;
    }  

    public Integer getId() {  
        return id;  
    }  

    public void setId(Integer id) {  
        this.id = id;  
    }  

    public String getName() {  
        return name;  
    }  

    public void setName(String name) {  
        this.name = name;  
    }  

    public Teacher getTeacherid() {  
        return teacherid;  
    }  

    public void setTeacherid(Teacher teacherid) {  
        this.teacherid = teacherid;  
    }  

    // public Teacher getTeacher() {  
    //     return teacher;  
    // }  

    // public void setTeacher(Teacher teacher) {  
    //     this.teacher = teacher;  
    // }  

}  