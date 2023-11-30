package server;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.ExecuteException;
import org.apache.commons.exec.ExecuteWatchdog;
import org.apache.commons.exec.PumpStreamHandler;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
 
import javax.servlet.http.HttpServletResponse;

public class CommandExecute {
	/*
	 * 执行dos命令的方法
	 * @param command 需要执行的dos命令
	 * @param file 指定开始执行的文件目录
	 * 
	 * @return true 转换成功，false 转换失败
	 */
	public static String executeCommand(String command) {
		StringBuffer output = new StringBuffer();
		Process p;
		try{
			p = Runtime.getRuntime().exec(command,null,new File("C:\\Users\\onelor\\Documents\\code\\erokan"));
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
 
}
/**
 * 执行系统命令工具类
 * 
 * @author Storm
 *
 */
class CommandUtils {

    private static final String DEFAULT_CHARSET = "GBK";

    /**
     * 执行指定命令
     * 
     * @param command 命令
     * @return 命令执行完成返回结果
     * @throws IOException 失败时抛出异常，由调用者捕获处理
     */
    public static String exeCommand(String command) throws IOException {
        try (
                ByteArrayOutputStream out = new ByteArrayOutputStream();
        ) {
            int exitCode = exeCommand(command, out);
            if (exitCode == 0) {
                System.out.println("命令运行成功！");
            } else {
                System.out.println("命令运行失败！");
            }
            return out.toString(DEFAULT_CHARSET);
        }
    }

    /**
     * 执行指定命令，输出结果到指定输出流中
     * 
     * @param command 命令
     * @param out 执行结果输出流
     * @return 执行结果状态码：执行成功返回0
     * @throws ExecuteException 失败时抛出异常，由调用者捕获处理
     * @throws IOException 失败时抛出异常，由调用者捕获处理
     */
    public static int exeCommand(String command, OutputStream out) throws ExecuteException, IOException {
        CommandLine commandLine = CommandLine.parse(command);
        PumpStreamHandler pumpStreamHandler = null;
        if (null == out) {
            pumpStreamHandler = new PumpStreamHandler();
        } else {
            pumpStreamHandler = new PumpStreamHandler(out);
        }

        // 设置超时时间为10秒
        ExecuteWatchdog watchdog = new ExecuteWatchdog(1000);

        DefaultExecutor executor = new DefaultExecutor();
        executor.setStreamHandler(pumpStreamHandler);
        executor.setWatchdog(watchdog);

        return executor.execute(commandLine);
    }

    public static void main(String[] args) {
        try {
            String result = exeCommand("ipconfig /all");
            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
