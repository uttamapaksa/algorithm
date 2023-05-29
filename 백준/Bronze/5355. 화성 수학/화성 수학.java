import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		
        for (int i=0; i<tc; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			float num = Float.parseFloat(st.nextToken());
			
            while (st.hasMoreTokens()) {
				String oper = st.nextToken();
				if (oper.equals("%")) {
					num += 5;
				} else if (oper.equals("#")) {
					num -= 7;
				} else {
					num *= 3;
				}
			}
			System.out.printf("%.2f%n", num);
		}
	}
}