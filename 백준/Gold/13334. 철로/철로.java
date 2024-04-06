import java.io.*;
import java.util.*;

public class Main {
    static long MIN_VALUE = -100000000L;

    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // input
        int n = Integer.parseInt(br.readLine());
        long[][] ho = new long[n][2];
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            ho[i][0] = Long.parseLong(st.nextToken());
            ho[i][1] = Long.parseLong(st.nextToken());
        }
        long d = Long.parseLong(br.readLine());

        // available ranges as starting points
        ArrayList<Long[]> points = new ArrayList<>();
        for (long[] x: ho) {
            long start = Math.min(x[0], x[1]);
            long end = Math.max(x[0], x[1]);
            long newStart = end - d;
            if (newStart > start) continue;
            newStart = Math.max(newStart, MIN_VALUE);
            points.add(new Long[]{newStart, 1L}); // {index, value}
            points.add(new Long[]{start, -1L});
        }

        // find max value
        long curr = 0L;
        long answer = 0L;
        points.sort((a, b) -> !a[0].equals(b[0]) ? Long.compare(a[0], b[0]) : Long.compare(b[1], a[1]));
        for (Long[] x: points) {
            curr += x[1];
            answer = Math.max(answer, curr);
        }

        System.out.println(answer);
    }
}
