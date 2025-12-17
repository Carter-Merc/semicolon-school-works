import java.util.Scanner; 

public class CreditLimitCalculator{

	public static void main(String[] args){
	Scanner input = new Scanner(System.in); 



	int accountNumber, beginningBalance, totalCharges, totalCredits, creditLimit, newBalance; 

	

	System.out.println("Enter Your Account Number: ");
	accountNumber = input.nextInt(); 

	
	while (accountNumber != -1){

	   System.out.println("Enter Your Beginning Balance: "); 
	   beginningBalance = input.nextInt(); 

	   System.out.println("Enter Your total charges: "); 
	   totalCharges = input.nextInt(); 

	   System.out.println("Enter Your Total Credits: "); 
	   totalCredits = input.nextInt(); 

	   System.out.println("Enter Your Credit Limit: "); 
	   creditLimit = input.nextInt(); 


	   newBalance = beginningBalance + totalCharges - totalCredits; 
		System.out.println("Your New Balance: " + newBalance);

	   if (newBalance > creditLimit){
	      System.out.println("Credit Limit exceeded");
	   }

	System.out.println("Enter next account number (or -1 to end)");
	accountNumber = input.nextInt();
	}  
	
	
	


	}
}

