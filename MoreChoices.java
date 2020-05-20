import java.util.Scanner;

class MoreChoices{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num; 
		System.out.println("Enter an integer: ");
		num = scan.nextInt();

		if (num<0){
			System.out.println("This number is negative.");
		} else if (num>0){
			System.out.println("This number is positive.");
		} else {
			System.out.println("This number is 0. ");
		}
	}
}