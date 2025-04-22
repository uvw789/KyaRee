import java.io.*;
import java.net.*;

public class MyClient {
public static void main(String[] args) {
try{	
Socket s=new Socket("localhost",6666);
	
DataOutputStream dout=new DataOutputStream(s.getOutputStream());

dout.writeUTF("Welcome to DC Practicals");
dout.flush();

dout.close();
s.close();

}catch(Exception e){System.out.println(e);}
}
}

// commands
// pehele MyServer ke commands ek terminal mein run karna aur phir woh terminal waise hi on rakhke, ek naya terminal open karo aur ussmein niche diye huye commands run karo, aur phir server wala joh terminal tha waha jake output dekh lo 
// PS C:\Users\HP\Desktop\dc\exp1> javac MyClient.java
// PS C:\Users\HP\Desktop\dc\exp1> java MyClient      