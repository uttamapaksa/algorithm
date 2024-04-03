import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int tc = Integer.parseInt(br.readLine());
        for (int t = 0; t < tc; t++) {

            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(br.readLine());

            int[] dp = new int[M+1];
            dp[0] = 1;

            while (st.hasMoreTokens()) {
                int coin = Integer.parseInt(st.nextToken());
                for (int i = coin; i <= M; i++) {
                    dp[i] += dp[i - coin];
                }
            }

            System.out.println(dp[M]);
        }
    }
}