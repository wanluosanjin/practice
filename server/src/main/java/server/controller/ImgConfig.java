package server;

import org.springframework.stereotype.Controller;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;
// @Configuration
@Controller
public class ImgConfig implements WebMvcConfigurer { // 2.实现WebMvcConfigurer接口
//    @Value("${img.path}")
    private String locationPath = "C:/imgs/erokan/"; // 3.本地路径
    private String netPath = "/imgs/**";
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
    	// 目前在本地Win系统测试需要在本地路径前添加 "file:"
    	// 有待确认Linux系统是否需要添加
        registry.addResourceHandler(netPath).addResourceLocations("file:"+locationPath);
        registry.addResourceHandler("/static/**").addResourceLocations("file:C:\\Users\\onelor\\Documents\\code\\static\\");
    }
}