import java.util.Scanner;
public class Hello {
    public static void main(String[] args){

        Scanner sc=new Scanner(System.in);
        System.out.println("Enter your name : ");
        String name=sc.next();
        System.out.println("Enter you age : ");
        int age=sc.nextInt();
        System.out.printf("%s, your age is %d",name,age);
        sc.close();



    }
}
