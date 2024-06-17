import java.util.Scanner;
public class conditionalStatements {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
//        System.out.println("Enter your age : ");
//        int age=sc.nextInt();
//        if(age>=18){
//            System.out.println("Yes, you can vote!");
//        } else {
//            System.out.println("No you can't vote!");
//        }
//
        System.out.println("Enter a number between 1 to 3");
        int n = sc.nextInt();
        switch(n){
            case 1:
                System.out.println("One");
                break;
            case 2:
                System.out.println("Two");
                break;
            case 3:
                System.out.println("Three");
                break;
            default:
                System.out.println("Invalid Number");
        }
        sc.close();
    }
}
