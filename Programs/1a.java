import java.util.*;
class Student{
	int age,marks;
	String name,idno,branch,gender;
	double percentage;
	Student(){
		Scanner scan=new Scanner(System.in);
		System.out.println("Enter Name:");
		name=scan.nextLine();
		System.out.println("Enter Id number:");
		idno=scan.nextLine();
		System.out.println("Enter Gender(Male/Female/Other):");
		gender=scan.nextLine();
		System.out.println("Enter Branch:");
		branch=scan.nextLine();
		System.out.println("Enter age:");
		age=scan.nextInt();
		System.out.println("Enter Marks in DS:");
		marks=scan.nextInt();
		System.out.println("Enter percentage of E1-Sem2:");
		percentage=scan.nextDouble();
		System.out.println("Your details recorded and our device will welcomes you");
	}
	public void display(){
		System.out.println();
		System.out.println();
		System.out.println("Welcome to "+idno+" Java Course");
		System.out.println("Name: "+name);
		System.out.println("Gender: "+gender);
		System.out.println("Branch: "+branch);
		System.out.println("Age: "+age);
		System.out.println("Marks in DS: "+marks);
		System.out.println("percentage: "+percentage);
	}

};
public class Question3{
	public static void main(String[] args) {
		Student student1=new Student();
		student1.display();
	}
}
