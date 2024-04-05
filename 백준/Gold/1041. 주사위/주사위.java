import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        long[] arr = new long[6];
        for (int i = 0; i < 6; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        long max1 = 0L, min1 = 51L, min2 = 101L, min3 = 151L;
        // max1, min1
        for (long x: arr) {
            if (min1 > x) {
                min1 = x;
            }
            if (max1 < x) {
                max1 = x;
            }
        }
        // min2
        for (int i = 1; i < 5; i++) {
            if (min2 > arr[0] + arr[i]) {
                min2 = arr[0] + arr[i];
            }
            if (min2 > arr[5] + arr[i]) {
                min2 = arr[5] + arr[i];
            }
        }
        // min3
        for (int[] row: new int[][]{{1, 2}, {1, 3}, {4, 2}, {4, 3}}) {
            int i = row[0];
            int j = row[1];
            if (min2 > arr[i] + arr[j]) {
                min2 = arr[i] + arr[j];
            }
            for (int k: new int[]{0, 5}) {
                if (min3 > arr[i] + arr[j] + arr[k]) {
                    min3 = arr[i] + arr[j] + arr[k];
                }
            }
        }

        long answer = 0L;
        if (N == 1L) {
            answer += Arrays.stream(arr).sum() - max1;
        } else {
            answer += ((5L * N * N) - (16L * N) + 12L) * min1;
            answer += (2L * N - 3L) * 4L * min2;
            answer += 4L * min3;
        }

        System.out.println(answer);
    }
}
