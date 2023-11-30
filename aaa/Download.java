package aaa;

import static aaa.Tool.*;

import java.io.File;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Date;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import org.springframework.stereotype.Component;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;


@Component
public class Download{
    ExecutorService moeimg;
    ExecutorService momoniji;
    ExecutorService nijifeti;
    ExecutorService nijix;
    ExecutorService nijinchu;
    ExecutorService indexthumb;
    ExecutorService erokan;

    Download(){
        moeimg = Executors.newSingleThreadExecutor();
        momoniji = Executors.newSingleThreadExecutor();
        nijifeti = Executors.newSingleThreadExecutor();
        nijix = Executors.newSingleThreadExecutor();
        nijinchu = Executors.newSingleThreadExecutor();
        indexthumb = Executors.newSingleThreadExecutor();
        erokan = Executors.newSingleThreadExecutor();
    }

	public static String executeCommand(String command,String workdir) {
		StringBuffer output = new StringBuffer();
		Process p;
		try{
			p = Runtime.getRuntime().exec(command,null,new File(workdir));
			p.waitFor();
            try(
                InputStreamReader inputStreamReader = new InputStreamReader(p.getInputStream(), "GBK");
                BufferedReader reader = new BufferedReader(inputStreamReader);
                ) 
                {
                String line = "";
                while ((line = reader.readLine()) != null) {
                    output.append(line + "\n");
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println(output.toString());
		return output.toString();
	}

    public static String adderokan(String name,String num){
        var workdir ="C:\\Users\\onelor\\Documents\\code\\erokan";
        String scrapy="scrapy crawl "+name+" -a num=";
        executeCommand(scrapy+num+" -s LOG_FILE="+name+".log",workdir);
        System.out.println(name+" "+num);
        System.out.println(new Date());
        var list=readline("scrapy.txt");
        int i=0;
        for(int j=0;j<list.size();j++){
            if(list.get(j).startsWith​(name)){
                i=j;
            }
        }
        // list.add(i,name+" "+String.valueOf(Integer.valueOf(num)+1));
        list.set(i,name+" "+num);
        writeline("scrapy.txt",list);
        return num;
    }

    public void addmoeimg(String num){
        // 似乎不会结束
        var future = moeimg.submit(new Callable<String>(){
            @Override
            public String call() throws Exception {
                return adderokan("moeimg",num);
            }
        });
    }
    public void addmomoniji(String num){
        var future = momoniji.submit(new Callable<String>(){
            @Override
            public String call() throws Exception {
                return adderokan("momoniji",num);
            }
        });
    }
    public void addnijinchu(String num){
        var future = nijinchu.submit(new Callable<String>(){
            @Override
            public String call() throws Exception {
                return adderokan("nijinchu",num);
            }
        });
        
    }
    public void addnijifeti(String num){
        var future = nijifeti.submit(new Callable<String>(){
            @Override
            public String call() throws Exception {
                return adderokan("nijifeti",num);
            }
        });
    }
    public void addnijix(String num){
        var future = nijix.submit(new Callable<String>(){
            @Override
            public String call() throws Exception {
                return adderokan("nijix",num);
            }
        });
    }
    public void addindexthumb(String num){
        var future = indexthumb.submit(new Callable<String>(){
            @Override
            public String call() throws Exception {
                return adderokan("indexthumb",num);
            }
        });
    }
    public void adderokannet(String num){
        var future = erokan.submit(new Callable<String>(){
            @Override
            public String call() throws Exception {
                return adderokan("erokan",num);
            }
        });
    }
}




/*
class Command extends Thread{
 private java.lang.Process p; 
 private InputStream is;
 private OutputStream os;
 private BufferedWriter bw;
 private BufferedReader br;
 private ProcessBuilder pb;
 private InputStream stdErr;
 public Command() {
 }


 //获取Process的输入，输出流
 public void setCmd(String cmd) {
  try {
   p = Runtime.getRuntime().exec(cmd);
   os = p.getOutputStream();
   is = p.getInputStream();
   stdErr = p.getErrorStream();
  } catch (IOException e) {
   System.err.println(e.getMessage());
  }
 }
 //向Process输出命令
 public void writeCmd(String cmd) {
  try {
   bw = new BufferedWriter(new OutputStreamWriter(os));
   bw.write(cmd);
   bw.newLine();
   bw.flush();
   bw.close();
  } catch (Exception e) {
   e.printStackTrace();
  }
 }
 //读出Process执行的结果
 public String readCmd() {
  StringBuffer sb = new StringBuffer();
  br = new BufferedReader(new InputStreamReader(is));
  String buffer = null;
  try {
   while ((buffer = br.readLine()) != null) {
    sb.append(buffer + "\n");
   }
   System.out.println(p.waitFor());
  } catch (Exception e) {
   e.printStackTrace();
  }
  return sb.toString();
 }
 //将命令一股脑塞入list中
 public LinkedList<String> doCmd(LinkedList<String> lists) {
  LinkedList<String> list = new LinkedList<String>();
  for (String s : lists) {
   writeCmd(s);
   list.add(readCmd());
  }
  return list;
 }
 public void run(){
    Command cmd = new Command();
    cmd.setCmd("cmd");
    cmd.writeCmd("start cmd /k ping -a -t 43.248.133.79 -l 1000");
    System.out.println(cmd.readCmd());
    //LinkedList<String> list = new LinkedList<String>();
    //list.add("dir/b");
    //list = cmd.doCmd(list);
    //for(String s:list){
    //System.out.print(s);
 }
    public static void main(String[] args) {
        Thread thr1 = new Command();
        Thread thr2 = new Command();
        thr1.start();
        thr2.start();
    }
}
*/