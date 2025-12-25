import java.util.Scanner; 

public class MortgageCal{

    public static void main(String[] args) {
    Scanner input = new Scanner(System.in); 
    
    double principalAmount = 0; 
    int annualInterestRate = 0; 
    int yearlyDuration = 0; 
    double monthlyPayment = 0; 

        System.out.println("Enter the Principal Amount: ");
        principalAmount = input.nextDouble(); 
        
        System.out.println("Enter the annual Interest: ");
        annualInterestRate = input.nextInt(); 

        System.out.println("Enter the duration in years: ");
        yearlyDuration = input.nextInt(); 

        monthlyPayment = principalAmount * ((annualInterestRate * Math.pow(1 + annualInterestRate,yearlyDuration)) / (Math.pow(1 + annualInterestRate, yearlyDuration) - 1)); 

        System.out.println("Your monthly payment is " + monthlyPayment); 
        
        
   
    }
}
