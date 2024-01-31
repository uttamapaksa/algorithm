import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int[] stack = new int[N];
        int[] cnt = new int[N];
        int t = -1;
        long ans = 0;

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N; i++) {
            while (t > -1 && arr[stack[t]] < arr[i]) {
                long tmp = cnt[t--];
                if (t > -1) {
                    ans += (tmp * (tmp + 3)) / 2;
                } else {
                    ans += (tmp * (tmp + 1)) / 2;
                }
            }

            if (t > -1 && arr[stack[t]] == arr[i]) {
                cnt[t]++;
            } else {
                t++;
                stack[t] = i;
                cnt[t] = 1;
            }
        }

        while (t > -1) {
            long tmp = cnt[t--];
            if (t > -1) {
                ans += (tmp * (tmp + 1)) / 2;
            } else {
                ans += (tmp * (tmp - 1)) / 2;
            }
        }

        System.out.println(ans);
    }
}
