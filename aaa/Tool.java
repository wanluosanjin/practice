package aaa;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.LinkedList;

import java.util.Scanner;

import java.util.concurrent.Callable;

import java.util.function.Function;
import java.util.function.Supplier;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.nio.file.StandardCopyOption ;

import java.nio.charset.Charset;

class Tool{
    public static File file(String path){
        File f = new File(path);
        if(f.exists()){
            return f;
        }
        try{
            f.getParentFile().mkdirs();
            f.createNewFile();
        } catch (Exception e) {
            throw new RuntimeException("创建文件出错",e);
        }
        return f;
    }

    public static void zip(Path srcDir,Path outfile){
        try(FileOutputStream fos1 = new FileOutputStream(file(outfile.toString()))){
            toZip(srcDir.toString(),fos1);
        } catch (Exception e) {
            throw new RuntimeException("zip方法出错",e);
        }
    }

    public static void toZip(String srcDir, OutputStream out){
        long start = System.currentTimeMillis();
        ZipOutputStream zos = null ;
        try {
            zos = new ZipOutputStream(out);
            File sourceFile = new File(srcDir);
            compress(sourceFile,zos,sourceFile.getName(),true);
            long end = System.currentTimeMillis();
            // System.out.println("压缩完成，耗时：" + (end - start) +" ms");
        } catch (Exception e) {
            throw new RuntimeException("zip error from ZipUtils",e);
        }finally{
            if(zos != null){
                try {
                    zos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }


    private static void compress(File sourceFile, ZipOutputStream zos, String name,
            boolean KeepDirStructure) throws Exception{
        byte[] buf = new byte[2 * 1024];
        if(sourceFile.isFile()){
            // 向zip输出流中添加一个zip实体，构造器中name为zip实体的文件的名字
            zos.putNextEntry(new ZipEntry(name));
            // copy文件到zip输出流中
            int len;
            FileInputStream in = new FileInputStream(sourceFile);
            while ((len = in.read(buf)) != -1){
                zos.write(buf, 0, len);
            }
            // Complete the entry
            zos.closeEntry();
            in.close();
        } else {
            File[] listFiles = sourceFile.listFiles();
            if(listFiles == null || listFiles.length == 0){
                // 需要保留原来的文件结构时,需要对空文件夹进行处理
                if(KeepDirStructure){
                    // 空文件夹的处理
                    zos.putNextEntry(new ZipEntry(name + "/"));
                    // 没有文件，不需要文件的copy
                    zos.closeEntry();
                }
            }else {
                for (File file : listFiles) {
                    // 判断是否需要保留原来的文件结构
                    if (KeepDirStructure) {
                        // 注意：file.getName()前面需要带上父文件夹的名字加一斜杠,
                        // 不然最后压缩包中就不能保留原来的文件结构,即：所有文件都跑到压缩包根目录下了
                        compress(file, zos, name + "/" + file.getName(),KeepDirStructure);
                    } else {
                        compress(file, zos, file.getName(),KeepDirStructure);
                    }
                }
            }
        }
    }
    public static String getClassPath(){
        return Thread.currentThread().getContextClassLoader().getResource("").getPath();
    }

    //这里返回ascii码值
    //这方法会读取三次,带上回车和换行
    //废弃方法
    public static int getint(){
        // try{
            //readAllBytes()会永远持续下去
            //read(byte[])方法似乎会在字符串最后加\0
            //当byte长度n大于3时,输入n-1或n个字符,连续的两次read第二次会输出\nbyte[1:]
            // byte[] b=new byte[5];
            // System.in.read(b);
            // System.out.println("your char is :"+new String(b)); 
            // System.in.read(b);
            // System.out.println("your char is :"+new String(b)); 
            //\n是换行10,\r是回车13
            // for(int i =System.in.read();System.in.read()==13&&System.in.read()==10;i =System.in.read())
            // return System.in.read();
        // }catch(IOException e){
        //     e.printStackTrace();
        //     throw new RuntimeException("getint出错");
            return 0;//无法访问
        // }
    }
    // 返回的字符串不在字符池,回车返回空字符串
    public static String inString(){
        Scanner sc = new Scanner(System.in);
        return sc.nextLine();
    }
    //也可以用files.list(),原理相同
    //此方法不检查路径是否有错
    public static List<Path> getsubpath(Path path) {
        List<Path> list=new ArrayList<Path>();
        try(DirectoryStream<Path> stream = Files.newDirectoryStream(path)){
            //可以用newDirectoryStream(Path dir, String glob)
                for(Path e : stream){
                    list.add(e);
                }
            }catch(IOException e){
                e.getStackTrace();
            }
        return list;
    }

	public static List<Path> getallsubpath(Path path){
        //		按名称顺序访问所有根节点,存在dir则访问
		List<Path> result = new LinkedList<Path>();//不能用arraylist,列表要经常插入
	    try {
			Files.walkFileTree(path, new FindFileVisitor(result));
	    	// Stream<Path> results = Files.walk(path, FileVisitOption.FOLLOW_LINKS);
	    	// result.addAll(results.collect(Collectors.toList()));
		} catch (IOException e) {
			e.printStackTrace();
		}
	    System.out.println(result.toString());
	    return result;
	}
    //正常状态下assert不阻拦程序运行
    public static Path pathof(String s){
        Path p = Path.of(s);
        if (p.toFile().exists())return p;
        throw new RuntimeException(s+"此路径下无文件");
    }

    public static Path tailpath(Path p,Path root){
        if(p. startsWith(root)){
            return Path.of(p.toString().substring(root.toString().length()));
        }
        throw new RuntimeException("tailpath方法两参数无联系");
    }

    public synchronized static void appendline(String filename,List<String> list){
        try{
        Files.write(Path.of(filename),list,StandardOpenOption.valueOf("APPEND"),StandardOpenOption.CREATE);
        }catch(IOException e){
            print("appendline出错");
            e.printStackTrace();
        }
    }
    public static void sleep(int time){
        try{
            Thread.sleep(2000);
        } catch (InterruptedException e) {
			e.printStackTrace();
		}
    }

    public synchronized static List<String> readline(String filename){
        try{
            //System.getProperty("line.separator")
            return Files.readAllLines(Path.of(filename));
        } catch (IOException e) {
            print("readline出错");
			e.printStackTrace();
            return null;
		}
    }

    public synchronized static void writeline(String filename,List<String> ss){
        try{
            //System.getProperty("line.separator")
            Files.write(Path.of(filename),ss,Charset.forName("UTF-8"),StandardOpenOption.CREATE,StandardOpenOption.WRITE);
        } catch (IOException e) {
            print("writeline出错");
			e.printStackTrace();
		}
    }
    public synchronized static void writestring(String filename,String s){
        try{
            //System.getProperty("line.separator")
            Files.writeString(Path.of(filename),s,Charset.forName("UTF-8"),StandardOpenOption.CREATE,StandardOpenOption.WRITE);
        } catch (IOException e) {
            print("writestring出错");
			e.printStackTrace();
		}
    }

    public synchronized static String readstring(String filename){
        try{
            //System.getProperty("line.separator")
            return Files.readString(Path.of(filename));
        } catch (IOException e) {
            print("readstring出错");
			e.printStackTrace();
            return null;
		}
    }

    public static Book mybookmatch(MyPatterns p,String s){
        Matcher m = p.pattern.matcher(s);
        if (m.find( )) {
            return new Book(m.group(1),m.group(2));
        } else {
            return null;
        }
    }

    public static void print(Object o){
        System.out.println(o.toString());
    }

    //p1为文件夹时原方法p2不能是非空文件夹
    public synchronized static void move(Path p1,Path p2){
        if(p2.toFile().exists()){
            print(p2.toString()+"已存在,1 for continue");
            if(!inString().equals("1")){
                print("已取消");
                return;
            }
        }
        try {
            Files.move(p1,p2, StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}