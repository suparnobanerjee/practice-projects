package dsa;
import java.util.Scanner;

public class subarrays {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter size : ");
        int n=sc.nextInt();
        int[] arr=new int[n];
        for (int i = 0; i < n; i++) {
            arr[i]=sc.nextInt();
        }
        printSubArray(arr,n);
    }
    public static void printSubArray(int[] arr,int n){
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                for (int k = i; k <= j; k++) {
                    System.out.print(arr[k]+" ");
                }
                System.out.println();
            }
        }
    }
}
