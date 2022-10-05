import java.util.*;


public class HelloWorld {
    public static void main(String[] args) {
       // Prints "Hello, World" in the terminal window.
       boolean winnerFound = false;
       Scanner scanny = new Scanner(System.in);
       String[][] row1 = new String[5][5];
       initBoard(row1);
       System.out.println("\nWelcome to Conenct 4! First to get 4 in a row wins :D\n\n");
       displayGameBoard(row1);
       while(!winnerFound){
         int columnDrop = retrieveColumn(scanny);
         System.out.println("Dropping your piece in column #" + columnDrop);
         if (columnDrop == 3){
            winnerFound = true;
         }
         
      }

      

       
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
      int retrieved = -1;
      while (retrieved == -1){
         System.out.println("Please give a row number: ");
         if(input.hasNextInt()){
            retrieved=input.nextInt();
         }
         else{
            input.next();
            System.out.println("Not a valid int, try again.");
            continue;
         }
         if (retrieved<5 && retrieved>-1){
            return retrieved;
         }
         else{
            retrieved = -1;
            System.out.println("Out of bounds, please try again.");
         }

      }
      return retrieved;
    }
 }
