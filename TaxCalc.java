import java.util.Scanner;

class TaxCalc{
	public static void main(String[] args) {
		final double tax_rate = 0.05;
		double cost,tax;
		Scanner scan = new Scanner(System.in); 
		System.out.println("Enter the price: ");
		cost = scan.nextDouble();

		if (cost >= 100){
			tax = cost * tax_rate;
			System.out.println("The tax on this is: " + tax);
			System.out.println("So the total is: " + (tax + cost));
		} else {
			System.out.println("This is tax free.");
		}
	}
}