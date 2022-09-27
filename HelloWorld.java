import java.util.*;


public class HelloWorld {
    public static void main(String[] args) {
       // Prints "Hello, World" in the terminal window.
       String[][] row1 = new String[5][5];
       initBoard(row1);
       displayGameBoard(row1);
       row1[4][4] = "R";
       row1[2][3] = "R"; 
       displayGameBoard(row1);
       //System.out.printf("%-5s %-5s %-5s %-5s %-5s\n", row1[0], row1[1], row1[2], row1[3], row1[4]);
         
      //System.out.printf("%-5s %-5s %-5s %-5s %-5s\n", row1[0], row1[1], row1[2], row1[3], row1[4]);

    }
    public static void initBoard(String[][] gameBoard){
      for (int i =0; i<gameBoard.length; i++){
         gameBoard[i][0] = "X";
         gameBoard[i][1] = "X";
         gameBoard[i][2] = "X";
         gameBoard[i][3] = "X";
         gameBoard[i][4] = "X";
      }
    }
    public static void displayGameBoard(String[][] gameBoard){
      for (int i =0; i<gameBoard.length; i++){
         System.out.printf("%-5s %-5s %-5s %-5s %-5s\n", gameBoard[i][0], gameBoard[i][1], gameBoard[i][2],gameBoard[i][3],gameBoard[i][4]);
         /*gameBoard[i][1] = "X";
         gameBoard[i][2] = "X";
         gameBoard[i][3] = "X";
         gameBoard[i][4] = "X";*/
      }
      System.out.println("");

      //Just want to see something
      
   }

 }
