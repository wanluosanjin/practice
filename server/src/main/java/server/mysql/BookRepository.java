package server.mysql;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;


public interface BookRepository extends JpaRepository<Book,Integer> {
    //煞笔pagebale会去count总条目数,贼jr卡
    //使用pageable也可以使用query的countQuery 属性
    //不必用join
    //使用nativequery似乎不能用sort
    @Query(nativeQuery = true,value = "SELECT * FROM test.book limit ?1,10")
    List<Book> find10(Integer num);
}  