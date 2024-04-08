import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        StringBuilder answer = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        long[] arr = new long[N+1];
        long[] sums = new long[N+1];
        for (int i=1; i<N+1; i++) {
            arr[i] = Long.parseLong(br.readLine());
            sums[i] = sums[i-1] + arr[i];
        }

        HashMap<Integer, Long> delta = new HashMap<>();
        for (int i=0; i<M+K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (a == 1) {
                long c = Long.parseLong(st.nextToken());
                delta.put(b, c - arr[b]);
            } else {
                int c = Integer.parseInt(st.nextToken());
                long tmp = sums[c] - sums[b-1];
                for (Integer key: delta.keySet()) {
                    if (b <= key && key <= c) {
                        tmp += delta.get(key);
                    }
                }
                answer.append(tmp).append("\n");
            }
        }

        System.out.println(answer.toString());
    }
}