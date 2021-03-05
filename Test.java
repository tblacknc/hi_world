import java.util.Scanner;
public class Test {


    public static String[] graph = {" ", " ", " ", " "," ", " ", " ",
    							    " "," ", " ", " ", " "};
    public static String[] lines = {"0,1,2","3,4,5","6,7,8","0,4,8",
    							    "2,4,6","0,3,6","1,4,7","2,5,8"};
     
    public static void main(String[] args) { 
       //Initialize variable  
    	int x = 0;
        
        Test.printBoard();
        while (x == 0) {  
        	x = Test.mePick();
        	Test.printBoard();
        	x = Test.checkWin();
        	if (x == 1) {
            	break;
            }
        	x = Test.youPick();
        	Test.printBoard();
        	x = Test.checkWin();
        }
    } 
    public static void printBoard() {
    	
    	System.out.println("");
    	System.out.println("");
    	System.out.println("");
    	System.out.println("");
    	
    	System.out.println(" "+graph[0]+" | "+graph[1]+" | "+graph[2] );
    	System.out.println("------------");
    	System.out.println(" "+graph[3]+" | "+graph[4]+" | "+graph[5] );
    	System.out.println("------------");
    	System.out.println(" "+graph[6]+" | "+graph[7]+" | "+graph[8] );
    	
    }

    public static int mePick() {
    	int i = 0;
    	int box;
    	@SuppressWarnings("resource")
		Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    	System.out.println("Enter Box Number");
    	box = myObj.nextInt();  // Read user input
    	box -= 1;
    	System.out.println("box is: " + box);  // Output user input
    	graph[box] = "X";
    	Test.printBoard();
    	i = i + 1;
    	return 0;
    } 
    public static int checkWin() {
        int[] line = {0,0};
        int count = 0;
        int temp = 0;
        for (String i : lines) {
            String[] cells = i.split(",");
            for (String j : cells) {
            	int intI = Integer.parseInt(j);  
            	String[] entries = {"X","O"};
            	for (String entry : entries){
            		if (count == 1) {
                        count = 0;
            		} else {
                        count += 1;
            		}
            		
            		if (graph[intI] == entry) {
                        temp = temp + 1;
                        line[count] += 1 ;
                        if (line[count] == 3) {
                        	System.out.println ("Game Over "+ entry + " wins!");
                            return 1;
                        }
            		}    		
            	}
            }
        	line[0] = 0;
        	line[1] = 0;
        }
    	return 0;
    }
    public static int checkTwo(String inp) {
        int line = 0;
        for (String x : lines) {
        	String[] cells = x.split(",");
            line = 0;
            for (String cell : cells ) {
            	int intI = Integer.parseInt(cell);
                if (graph[intI] == inp) {
                    line = line + 1;
                    if (line == 2) {
                        for (String cell2 : cells) {
                        	intI = Integer.parseInt(cell2);
                            if (graph[intI] == " ") {
                                graph[intI] = "O";
                                return 1;
                            }
                        }
                    }            		
                }                   		
            }
        }
        return 0;
    }
    
    public static int youPick() {
        int[] corners = {0,2,6,8};
        int[] sides = {1,3,5,7};
        int two = 0;
        two = Test.checkTwo("X");
        if (two == 1) {
            return 1;
        }
        
        two = Test.checkTwo("O");
        if (two == 1) {
            return 1;
        }

        for (int corner : corners) {
            if (graph[corner] == " ") {
                graph[corner] = "O";
                return 1;
            }
        }
        
        if (graph[4] == " ") {
            graph[4] = "O";
            return 1;
        }

        for (int side : sides) {
            if (graph[side] == " "){
                graph[side] = "O";
                return 1;  		
            }
        }
        return 1;  
    }
}