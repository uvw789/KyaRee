import java.io.*;
import java.net.*;

public class MyServer {
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
// PS C:\Users\HP\Desktop\dc\exp1> javac MyServer.java
// PS C:\Users\HP\Desktop\dc\exp1> java MyServer      
// yeh ho jane ke baad client ke commands run karo
// message= Welcome to DC Practicals