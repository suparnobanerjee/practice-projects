import java.util.Scanner;
public class method {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter two numbers : ");
        int a = sc.nextInt();
        int b = sc.nextInt();
//        System.out.println("The maximum of 2 numbers is : "+Math.max(a,b));
//        System.out.println("The maximum of 2 numbers is : "+ getMax(a,b));
        System.out.printf("Random number between %d and %d is : %d ",a,b,getRandom(a,b));
    }
//    public static int getMax(int a, int b){
//        return a>b ? a : b;
//    }
    public static int getRandom(int a, int b){
        return (int)((Math.random()*(b-a+1))+a);
    }
}
