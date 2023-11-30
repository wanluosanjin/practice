package aaa;

import java.util.List;
import java.util.ArrayList;

import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.Statement;
import java.sql.SQLException;
import java.sql.ResultSet;
import java.sql.PreparedStatement;

import org.springframework.stereotype.Service;

@Service
class Mysql{

    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost:3306/test?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";

    static final String USER = "root";
    static final String PASS = "onelor998765432";
    static {
        try {
            Class.forName(JDBC_DRIVER);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
    Connection conn;
    public Mysql(){
        //加个钩子关闭连接,精致
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            closeconn();
        }));
        try{
            conn = DriverManager.getConnection(DB_URL,USER,PASS);
        }catch(SQLException e){
            e.printStackTrace();
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    public void closeconn() {
        try {
            if(conn!=null) {
                conn.close();
            }
        } catch (SQLException e) {    
            e.printStackTrace();
        }
    }

    public void insertbooks(List<Book> books){
        try(PreparedStatement pstmt = conn.prepareStatement("insert booklocal value (null,?,?,null)");) {
            for(var book : books){
                pstmt.setString(1,book.teacher);
                pstmt.setString(2,book.name);
                pstmt.addBatch();
            }
            if(pstmt.execute()){
                System.out.println("执行了一条查询语句");
            } else {
                
            }
        } catch (SQLException e) {    
            e.printStackTrace();
        }
    }
    //可能返回null
    public List<String> execute(String preparedSql) {
        //返回失败,try结束resultset就关闭了
        try(PreparedStatement pstmt = conn.prepareStatement(preparedSql);) {
            if(pstmt.execute()){
                var rs = pstmt.getResultSet();
                ArrayList<String> ss=new ArrayList<String>(rs.getFetchSize());
                while(rs.next()){
                    ss.add(rs.getString(1));
                }
                return ss;
            } else {
                return null;
            }
        } catch (SQLException e) {    
            e.printStackTrace();
        }
        return null;
    }
    //这方法感觉很慢
    public int[] executebatch(String preparedSql, List param) {
        try(PreparedStatement pstmt = conn.prepareStatement(preparedSql);) {
            if (param != null) {
                if(param.size() % pstmt.getParameterMetaData().getParameterCount()!=0)throw new RuntimeException("sql参数与所给数据不整除");
                for (int i = 0; i < param.size()/pstmt.getParameterMetaData().getParameterCount(); i++) {
                    for(int j=0;j<pstmt.getParameterMetaData().getParameterCount();j++){
                        pstmt.setObject(j+1, param.get(i*pstmt.getParameterMetaData().getParameterCount()+j)); //j不能是0
                    }
                    pstmt.addBatch();
                }
            }
            return pstmt.executeBatch();
        } catch (SQLException e) {    
            e.printStackTrace();
        }
        return null;
    }

    //废弃方法
    public void connectmysql(){
        try{
            Class.forName(JDBC_DRIVER);
            try(Connection conn = DriverManager.getConnection(DB_URL,USER,PASS);Statement stmt = conn.createStatement();){
                System.out.println("Goodbye!");
            }
        }catch(SQLException e){
            e.printStackTrace();
        }catch(Exception e){
            e.printStackTrace();
        }
    }

}