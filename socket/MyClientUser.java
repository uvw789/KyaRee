import java.io.*;
import java.net.*;
import java.util.Scanner;

public class MyClientUser {
    public static void main(String[] args) {
        try {
            // Connect to the server at localhost:6666
            Socket s = new Socket("localhost", 6666);

            // Create output stream to send message
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());

            // Create a scanner to read user input
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter your message: ");
            String message = scanner.nextLine();

            // Send the message to the server
            dout.writeUTF(message);
            dout.flush();

            // Close resources
            dout.close();
            s.close();
            scanner.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}



// commands
// pehele MyServerUser ke commands ek terminal mein run karna aur phir woh terminal waise hi on rakhke, ek naya terminal open karo aur ussmein niche diye huye commands run karo, aur phir server wala joh terminal tha waha jake output dekh lo 
// output
// PS C:\Users\HP\Desktop\dc\exp1> javac MyClientUser.java
// PS C:\Users\HP\Desktop\dc\exp1> java MyClientUser
// Enter your message: hii 

