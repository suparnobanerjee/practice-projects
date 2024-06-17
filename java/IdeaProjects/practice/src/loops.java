import java.util.Scanner;
public class loops {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter n : "); // to calculate the sum of first 'n' even natural numbers
        int n=sc.nextInt();
        int sum=0;
//        for(int i=1;i<=n;i++){
//            sum+=2*i;
//        }
        int i=0;
        while(i<=n){
            sum+=2*i;
            i++;
        }
        System.out.printf("Sum : %d",sum);
        sc.close();
    }
}
