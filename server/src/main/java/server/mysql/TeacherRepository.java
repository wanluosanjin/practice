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


public interface TeacherRepository extends JpaRepository<Teacher,Integer> {
    //语句里有括号会出错...他会自己添加括号,十分弱智  
    //方法的参数个数必须和@Query里面需要的参数个数一致,十分弱智
    //使用@query就会出错,十分弱智
    //nativequery不是语法错误就是类型转换错误
    // @Query(nativeQuery = true,value = "")

    // @PersistenceContext
    // private EntityManager entityManager;
    //   @Query("select distinct s from Store s inner join s.shops where s.id = ?1")
    //   List<Store> findByShopList(Integer id);
    
    // @Query("select distinct t FROM Teacher t inner join t.books WHERE t.teacher = ?1")
    //似乎不能用join
    @Query(value = "SELECT t FROM Teacher t where t.teacher = ?1")
    List<Teacher> findByTeacher(String teacher);
}  