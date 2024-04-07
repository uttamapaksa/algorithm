import java.io.*;
import java.util.*;

public class Main {
    static long MOD = 1000000007L;

    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] arr = new long[n];
        for (int i=0; i<n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        // cumulative sum
        Arrays.sort(arr);
        for (int i=1; i<n; i++) {
            arr[i] = (arr[i] + arr[i-1]) % MOD;
        }

        // power. number of cases by the diff
        long[] power = new long[n];
        power[0] = 1L;
        for (int i=1; i<=n-2; i++) {
            power[i] = (power[i-1] << 1) % MOD;
        }

        // group by same diff pair. count * power
        long answer = 0L;
        for (int diff=1; diff<n; diff++) {
            long count = arr[n-1] - arr[n-1-diff];
            if (count < 0) count += MOD;
            count -= arr[diff-1];
            if (count < 0) count += MOD;
            answer = (answer + (count * power[diff-1]) % MOD) % MOD;
        }

        // output
        System.out.println(answer);
    }
}