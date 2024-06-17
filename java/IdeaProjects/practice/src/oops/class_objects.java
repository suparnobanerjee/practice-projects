package oops;
import java.util.Scanner;
public class class_objects {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("How many car entries you want to make? : ");
        int n=sc.nextInt();

        cars[] carArray=new cars[n];
        for (int i = 0; i < n; i++) {
            carArray[i]=new cars();
            System.out.printf("Enter the brand of car %d : ",(i+1));
            carArray[i].brand = sc.next();
            System.out.printf("Enter the model of car %d : ",(i+1));
            carArray[i].model = sc.next();
            System.out.printf("Enter the year of making of car %d : ",(i+1));
            carArray[i].yom = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            System.out.printf("\n\nDetails of car %d",(i+1));
            System.out.printf("\nBrand : %s ",carArray[i].brand);
            System.out.printf("\nModel : %s ",carArray[i].model);
            System.out.printf("\nYear of Making : %d ",carArray[i].yom);
        }
        sc.close();
    }
}
