import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        long[] arr = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        // left half, right half
        int M = (int) (N / 2);
        long[] left = new long[M];
        long[] right = new long[N-M];
        for (int i=0; i<M; i++) {
            left[i] = arr[i];
        }
        for (int i=M; i<N; i++) {
            right[i-M] = arr[i];
        }

        // sum of elements of subsets
        ArrayList<Long> leftSum = new ArrayList<>();
        ArrayList<Long> rightSum = new ArrayList<>();
        ArrayList<Long> tmp = new ArrayList<>();
        leftSum.add(0L);
        rightSum.add(0L);
        for (Long x: left) {
            tmp.clear();
            for (Long y: leftSum) {
                tmp.add((x + y));
            }
            leftSum.addAll(tmp);
        }
        for (Long x: right) {
            tmp.clear();
            for (Long y: rightSum) {
                tmp.add(x + y);
            }
            rightSum.addAll(tmp);
        }
        rightSum.sort(Comparator.naturalOrder());

        // binary search
        int ans = 0, end = rightSum.size();
        for (Long x: leftSum) {
            int s = 0, m, e = end-1, idx = end;
            Long t = C - x;
            while (s <= e) {
                m = (s+e) / 2;
                if (rightSum.get(m) > t) { // the first position exceeding the target
                    idx = m;
                    e = m - 1;
                } else {
                    s = m + 1;
                }
            }
            ans += idx;
        }

        // output
        System.out.print(ans);
    }
}