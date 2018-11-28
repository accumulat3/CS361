import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;
/**
 * @author Jeremy Rivera & Angela Fong
 * 
 * 
 */
public class ScannerDemo {

	
	private static String file1 = "src\\scannertests\\prog2.jay";
	private static int counter = 1;

	public static void main(String args[]) throws IOException {
		TokenStream tS = new TokenStream(file1);
		
		Token t;
		while(!tS.isEndofFile()) {
			t = tS.nextToken();
			System.out.println("Token " + counter + " - " + t); // For clarity in the Console
			counter ++;	
		}
	}
}