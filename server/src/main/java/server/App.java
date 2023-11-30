package server;

import java.util.List;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.ui.Model;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.beans.factory.annotation.Autowired;
import server.mysql.BookRepository;
import server.mysql.TeacherRepository;
import server.mysql.DownloadedRepository;
import server.book.Book;
import server.mysql.Teacher;
import server.book.BookPath;
import java.util.stream.Collectors;

@Controller
@SpringBootApplication
public class App 
{
    @Autowired
    BookRepository bookRepository;

    @Autowired
    TeacherRepository teacherRepository;

    @Autowired
    DownloadedRepository downloadedRepository;

    @Autowired
    Thread1 thread1;

    // @ResponseBody
	@RequestMapping("/")
	String home() {
		return "static/html.html";
	}

    @ResponseBody
	@RequestMapping("/next")
    //@RequestParam(required = false, defaultValue = "10") String pageSize
	List<Book> next(Integer pagenum) {
        if (pagenum == null){
            pagenum = 0;
        }
        // Pageable pageable = PageRequest.of(pagenum,10);
        // Sort sort = Sort.by(Sort.Direction.DESC,"id");
        List<server.mysql.Book> list = bookRepository.find10(pagenum*10);
		return list.stream().map(book->new Book(book.getTeacherid().getTeacher(),
                String.valueOf(book.getId())+" "+book.getName(),
                book.getTeacherid().getTeacher()=="[]"?downloadedRepository.findById(book.getId()).isPresent():false))
                .collect(Collectors.toList());
	}

    @ResponseBody
	@RequestMapping("/exists")
    //这里的bookname要包括bookid
	Boolean exists(String teacher,String bookname) {
        return BookPath.exists(teacher,bookname);
        //两个参数必须都要有,不能是null,但可以是空字符,''则跳过哪个路径
	}

    @ResponseBody
	@RequestMapping("/book")
	List<String> book(String teacher,String bookid) {
        return BookPath.list(teacher,bookid);
	}

    @ResponseBody
	@RequestMapping("/teacher")
	List<Book> teacher(String teacher) {
        if (teacher == null){
            return null;
        }
        List<Teacher> teacherlist = teacherRepository.findByTeacher(teacher);
        return teacherlist.stream()
            .flatMap(teacher1->teacher1.getBooks().stream()
                .map(book->new Book(teacher1.getTeacher(),
                    String.valueOf(book.getId())+" "+book.getName(),
                    downloadedRepository.findById(book.getId()).isPresent())))
            .collect(Collectors.toList());
		// List<Integer> bookidlist = new List<Integer>();
        // for(Book book:booklist){
        //     bookidlist.add(book.getId());
        // }
	}

    @ResponseBody
	@RequestMapping("/bookthumb")
	void bookthumb(Integer bookid) {
        thread1.addBookThumb(String.valueOf(bookid));
        // downloadedRepository.save(new Downloaded(bookid));
	}

    public static void main( String[] args )
    {
        // Thread1 thread1 = new Thread1();
        // thread1.addBookThumb("31630");
        SpringApplication.run(App.class,args);
    }
}
