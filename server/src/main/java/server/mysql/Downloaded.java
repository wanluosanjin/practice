package server.mysql;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Column;
import javax.persistence.Table;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.ManyToOne;
import javax.persistence.JoinColumn;
import javax.persistence.CascadeType;
import javax.persistence.FetchType;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table (name="downloaded")
public class Downloaded implements Serializable {  

    @Id
    @Column(name="id")
    private Integer id;  

    public Downloaded() {  
        super();  
    }  

    public Downloaded(Integer id) {  
        super();  
        this.id = id;  
    }  

    public Integer getId() {  
        return id;  
    }  

    public void setId(Integer id) {  
        this.id = id;  
    }  

}  