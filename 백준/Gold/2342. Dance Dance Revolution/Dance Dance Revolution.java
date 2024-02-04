import java.io.*;
import java.util.*;

public class Main {
    static int addend(int c, int x) {
        if (c == 0) return 2;
        else if (c == x) return 1;
        else if (c + x == 4 || c + x == 6) return 4;
        else return 3;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = input.length;

        if (N == 1) {
            System.out.println(0);
        } else {
            int[] arr = new int[N-1];
            for (int i=0; i<N-1; i++) {
                arr[i] = Integer.parseInt(input[i]);
            }

            int[][] dp = new int[5][5];
            int[][] dp2 = new int[5][5];
            int x = arr[0];
            dp[x][0] = 2;
            dp[0][x] = 2;

            for (int i = 1; i < N-1; i++) {
                x = arr[i];
                dp2 = new int[5][5];
                // DP
                for (int l = 0; l < 5; l++) {
                    for (int r = 0; r < 5; r++) {
                        if (dp[l][r] == 0) continue;
                        // left
                        if (dp2[x][r] == 0) dp2[x][r] = dp[l][r] + addend(l, x);
                        else dp2[x][r] = Math.min(dp2[x][r], dp[l][r] + addend(l, x));
                        // right
                        if (dp2[l][x] == 0) dp2[l][x] = dp[l][r] + addend(r, x);
                        else dp2[l][x] = Math.min(dp2[l][x], dp[l][r] + addend(r, x));
                    }
                }
                dp = dp2;
            }

            int ans = 400000;
            for (int[] r: dp) {
                for (int c: r) {
                    if (0 < c && c < ans) {
                        ans = c;
                    }
                }
            }
            System.out.println(ans);
        }
    }
}