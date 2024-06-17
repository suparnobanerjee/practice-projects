package dsa;
import java.util.Scanner;
public class transpose {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter how many rows and columns : ");
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] arr = new int[r][c];
        System.out.println("Enter the matrix values : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        System.out.println("The actual matrix looks like : ");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        if(r==c){
            getTransposeOfSqMatrix(arr);
        }
        else{
            getTransposeOfNSqMatrix(arr);
        }
        System.out.println("The transposed matrix looks like :");
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static void getTransposeOfSqMatrix(int[][] arr){

    }
    public static void getTransposeOfNSqMatrix(int[][] arr){

    }
}
