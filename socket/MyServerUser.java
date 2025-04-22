import java.io.*;
import java.net.*;

public class MyServerUser {
public static void main(String[] args){
try{
ServerSocket ss=new ServerSocket(6666);
Socket s=ss.accept();//establishes connection 

DataInputStream dis=new DataInputStream(s.getInputStream());

String	str=(String)dis.readUTF();
System.out.println("message= "+str);

ss.close();

}catch(Exception e){System.out.println(e);}
}
}

// commands
// pehele server ke commands run karo then client ke
// output
// PS C:\Users\HP\Desktop\dc\exp1> javac MyServerUser.java
// PS C:\Users\HP\Desktop\dc\exp1> java MyServerUser
// yeh ho jane ke baad client ke commands run karo
// message= hii 