package dsa;
import java.util.Scanner;
public class twoDarray {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter row number and column number : ");
        int r=sc.nextInt();
        int c=sc.nextInt();
        int[][] arr=new int[r][c];
        System.out.println("Enter the values of 2D array, to be filled column wise : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                arr[i][j]=sc.nextInt();
            }
        }
        System.out.println("Now enter the row and column number of the value in 2D array you wanna print :");
        int a=sc.nextInt();
        int b=sc.nextInt();
        System.out.printf("Value of 2D array in row %d and column %d is : %d",(a),(b),arr[a-1][b-1]);
    }
}
