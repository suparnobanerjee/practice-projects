import java.util.Scanner;
public class arrays {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of array : ");
        int n=sc.nextInt();
//        int arr[]=new int[n];
//        System.out.println("Enter the integers : ");
//        for (int i = 0; i < n; i++) {
//            arr[i]=sc.nextInt();
//        }
//        System.out.println("Your array looks like : ");
//        for (int i = 0; i < n; i++) {
//            System.out.print(arr[i]+" ");
//        }

//        System.out.println("Enter the names : ");
//        String names[]=new String[n];
//        for (int i = 0; i < n; i++) {
//            names[i]=sc.next();
//        }
//        for(String name:names){                     // for-each loop
//            System.out.print(name+"  ");
//        }

        int arr[]=new int[n];
        System.out.println("Enter the integers : ");
        for (int i = 0; i < n; i++) {
            arr[i]=sc.nextInt();
        }
        int max=Integer.MIN_VALUE;
        for(int num:arr){
            if(num>max) max=num;
        }
        System.out.println("The maximum integer is : "+max);
    }
}
