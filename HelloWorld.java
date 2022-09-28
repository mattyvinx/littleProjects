import java.util.*;


public class HelloWorld {
    public static void main(String[] args) {
       // Prints "Hello, World" in the terminal window.
       Scanner scanny = new Scanner(System.in);
       String[][] row1 = new String[5][5];
       initBoard(row1);
       System.out.println("\nWelcome to Conenct 4! First to get 4 in a row wins :D\n\n");
       displayGameBoard(row1);
       int columnDrop = retrieveColumn(scanny);
       System.out.println("Dropping your piece in column #" + columnDrop);

       
       //System.out.printf("%-5s %-5s %-5s %-5s %-5s\n", row1[0], row1[1], row1[2], row1[3], row1[4]);
         
      //System.out.printf("%-5s %-5s %-5s %-5s %-5s\n", row1[0], row1[1], row1[2], row1[3], row1[4]);

    }
    public static void initBoard(String[][] gameBoard){
      for (int i =0; i<gameBoard.length; i++){
         gameBoard[i][0] = "O";
         gameBoard[i][1] = "O";
         gameBoard[i][2] = "O";
         gameBoard[i][3] = "O";
         gameBoard[i][4] = "O";
      }
    }
    public static void displayGameBoard(String[][] gameBoard){
      for (int i =0; i<gameBoard.length; i++){
         System.out.printf("%-5s %-5s %-5s %-5s %-5s\n", gameBoard[i][0], gameBoard[i][1], gameBoard[i][2],gameBoard[i][3],gameBoard[i][4]);
      }
      System.out.println("");

      
   }
    public static int retrieveColumn(Scanner input){
      System.out.println("Please give a row number: ");
      int retrieved = input.nextInt();
      return retrieved;
    }
 }
