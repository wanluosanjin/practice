package com.loger.md5;
 
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
 
public class Md5 {
   public static String bytesToHexString(byte[] src){
       StringBuilder stringBuilder = new StringBuilder("");
       if (src == null || src.length <= 0) {
           return null;
       }
       for (int i = 0; i < src.length; i++) {
           int v = src[i] & 0xFF;
           String hv = Integer.toHexString(v);
           if (hv.length() < 2) {
               stringBuilder.append(0);
           }
           stringBuilder.append(hv);
       }
       return stringBuilder.toString();
   }
   /**利用MD5进行加密*/
  public String EncoderByMd5(String str) throws NoSuchAlgorithmException, UnsupportedEncodingException{
    //确定计算方法
    MessageDigest md5=MessageDigest.getInstance("MD5");
    //加密后的字符串
    String newstr=bytesToHexString(md5.digest(str.getBytes("utf-8")));
    return newstr;
  }
  public static void main(String[] args){    
    Md5 md5 = new Md5();  
    String str = "apple";
    try {
      String newString = md5.EncoderByMd5(str);
      System.out.println(newString);
    } catch (NoSuchAlgorithmException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    } catch (UnsupportedEncodingException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }

     
  }
}