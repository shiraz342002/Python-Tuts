// package Fibonacii_Sequence;
import java.util.Scanner;


public class Fibonacci_Recursive{


	static int fibonacci(int n){
		if(n==0){
			return 0;
		}
		if(n==1){
			return 1;
		}
		return fibonacci(n-2) + fibonacci(n-1);
	}

	public static void main(String[] args) {
        
		Scanner sc = new Scanner(System.in);
		System.out.println("How many Fibonacci Numbers?");
		int maxnum=sc.nextInt();
		System.out.println("The fibonacci series of"+maxnum+" ");
		for (int i = 0; i < maxnum; i++) {
			System.out.println(fibonacci(i)+" ");
		}	
		sc.close();
	}
}