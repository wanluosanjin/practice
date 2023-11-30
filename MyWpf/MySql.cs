using System;
using System.Data;
using MySql.Data.MySqlClient;

namespace MyWpf
{
    public class MySql{//不用框架直接写死
        MySqlConnection conn;
        string constr="server=localhost;User Id=root;password=onelor998765432;Database=test";
        DataSet ds;
        public MySql(){
            
            //两列名间不加逗号视为as
            conn=new MySqlConnection(constr);
            ds = new DataSet();
            try
            {
                conn.Open();
                Console.WriteLine("已经建立连接");
            }
            catch (MySqlException e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                // conn.Close();
            }
        }

        ~MySql(){
            conn?.Close();
        }

        public DataTable get(string qurey){
            string tablename="get";
            MySqlCommand cmd = new MySqlCommand(qurey, conn);
            MySqlDataAdapter da = new MySqlDataAdapter(cmd);
            da.Fill(ds, tablename);
            return ds.Tables[tablename];
        }
        public Object[] getone(string qurey,params object[] param){
            MySqlCommand cmd = new MySqlCommand(qurey, conn);
            var parameters=getparameter(param);
            cmd.Parameters.AddRange(parameters);
            using (var reader = cmd.ExecuteReader(CommandBehavior.SingleRow)){
                if(reader.Read()){
                    var list = new Object[reader.FieldCount];
                    for (int i = 0; i < reader.FieldCount; i++)
                    {
                        list[i]=reader[i];
                    }
                    return list;
                }
                return null;
            }
        }

        public static MySqlParameter[] getparameter(params object[] list){
            var parameters=new MySqlParameter[list.Length];
            for (int i = 0; i < list.Length; i++)
            {
                MySqlParameter parameter = new MySqlParameter();
                if(list[i].GetType()==typeof(string)){
                    parameter.MySqlDbType = MySqlDbType.VarChar;
                }else if(list[i].GetType()==typeof(int)){
                    parameter.MySqlDbType = MySqlDbType.UInt32;
                }else throw new Exception("不支持的类型");
                parameter.Value = list[i];
                parameters[i]=parameter;
            }
            return parameters;
        }

        public void insert(string nonqurey,params object[] param){
            MySqlCommand cmd = new MySqlCommand(nonqurey, conn);
            var parameters=getparameter(param);
            cmd.Parameters.AddRange(parameters);
            cmd.ExecuteNonQuery();
        }
        public DataTable getimg(string qurey){
            string tablename="img";
            if (ds.Tables.Contains(tablename))
            {
                return ds.Tables[tablename];
            }
            MySqlCommand cmd = new MySqlCommand(qurey, conn);
            MySqlDataAdapter da = new MySqlDataAdapter(cmd);
            da.Fill(ds, tablename);
            return ds.Tables[tablename];
        }

        public void close(){
            conn.Close();
        }
        public DataTable getTankoubonPathTable(){
            string tablename="TankoubonPath";
            if (ds.Tables.Contains(tablename))
            {
                return ds.Tables[tablename];
            }
            string qurey="select imgpath from(SELECT  indexthumb.bookid as indexid,imgpath from indexthumb join tankoubon on tankoubon.bookid=indexthumb.bookid order by indexid desc) as tankoubonpath ";
            MySqlCommand cmd = new MySqlCommand(qurey, conn);
            MySqlDataAdapter da = new MySqlDataAdapter(cmd);
            da.Fill(ds, tablename);
            return ds.Tables[tablename];
        }
        public DataTable getChineseTankoubonPathTable(){
            string tablename="ChineseTankoubonPath";
            if (ds.Tables.Contains(tablename))
            {
                return ds.Tables[tablename];
            }
            string qurey="select imgpath from(SELECT  indexthumb.bookid as indexid,imgpath from indexthumb join tankoubon on tankoubon.bookid=indexthumb.bookid,chinese where indexthumb.bookid=chinese.bookid  order by indexid desc) as chinesetankoubonpath";
            MySqlCommand cmd = new MySqlCommand(qurey, conn);
            MySqlDataAdapter da = new MySqlDataAdapter(cmd);
            da.Fill(ds, tablename);
            return ds.Tables[tablename];
        }
        public void downloadThumbDone(string num){
            string qurey=$"insert ignore into downloaded value({num});";
            MySqlCommand cmd = new MySqlCommand(qurey, conn);
            cmd.ExecuteNonQuery();
        }
        public DataTable getDownloadedBookids(){
            string tablename="DownloadedBookids";
            if (ds.Tables.Contains(tablename))
            {
                return ds.Tables[tablename];
            }
            string qurey="SELECT * FROM test.downloaded;";
            MySqlCommand cmd = new MySqlCommand(qurey, conn);
            MySqlDataAdapter da = new MySqlDataAdapter(cmd);
            da.Fill(ds, tablename);
            return ds.Tables[tablename];
        }
    }
}