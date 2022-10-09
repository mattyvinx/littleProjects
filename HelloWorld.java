import java.util.*;


public class HelloWorld {
    public static void main(String[] args) {
       // Prints "Hello, World" in the terminal window.
       boolean player = false;
       //false = red, true = blue
       boolean winnerFound = false;
       Scanner scanny = new Scanner(System.in);
       String[][] row1 = new String[5][5];
       initBoard(row1);
       System.out.println("\nWelcome to Conenct 4! First to get 4 in a row wins :D\n\n");
       displayGameBoard(row1);
       row1[2][4] = "B"; //makes bottom column (4) and 4th row (3) a letter B for blue.
       displayGameBoard(row1);
       while(!winnerFound){
         if (player){
            System.out.println("It's your turn blue.");
            int columnDrop = retrieveColumn(scanny);
            System.out.println("Dropping your piece in column #" + columnDrop);
            if (columnDrop == 3){
               winnerFound = true;
               continue;
            }
            int columnPlacement = findColHeight(columnDrop, row1);
            placePiece(row1, columnDrop, columnPlacement, player);
            displayGameBoard(row1);
            player = !player;
         }
         if (!player){
            System.out.println("It's your turn red.");
            int columnDrop = retrieveColumn(scanny);
            System.out.println("Dropping your piece in column #" + columnDrop);
            
            if (columnDrop == 3){
               winnerFound = true;
               continue;
            }
            int columnPlacement = findColHeight(columnDrop, row1);
            placePiece(row1, columnDrop, columnPlacement, player);
            displayGameBoard(row1);
            player = !player;
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

    public static int findColHeight(int col, String [][] gameBoard){
      /*Gives the location of the height of the current heighest piece.*/
      int heighestPiece = 0;
      for(int i = 0; i<gameBoard.length; i++){
         System.out.println("Checking row "+i+" of "+gameBoard.length);
         if(gameBoard[i][col].equals("B") || gameBoard[i][col].equals("R")){
            heighestPiece = i;
            System.out.println("Found heightest piece to be "+ heighestPiece);
            return heighestPiece;
         }
      }
      heighestPiece = 5;
      return heighestPiece;
    }
    public static void placePiece(String[][] gameBoard, int col, int height, boolean player){
      /*Places current players piece where it would fall*/
      //case where player has chosen a full column
      String playerColor="B";
      if (!player){
         playerColor="R";
      }
      if(height == 0){
         return;
      }
      //empty col case
      else if (height == 5){
         gameBoard[height-1][col]=playerColor;
         return;
      }
      //non-full occupied column
      else{
         gameBoard[height-1][col]=playerColor;
      }
    }
   }
