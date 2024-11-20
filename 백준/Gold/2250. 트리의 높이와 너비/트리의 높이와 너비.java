import java.util.*;
import java.io.*;

public class Main {
    static int idx = 0;
    static Map<Integer, int[]> level = new HashMap<>();
    static int[] left, right, par;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        par = new int[N + 1];
        left = new int[N + 1];
        right = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            par[i] = i;
        }

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            if (l != -1) {
                left[n] = l;
                par[l] = n;
            }
            if (r != -1) {
                right[n] = r;
                par[r] = n;
            }
        }

        for (int i = 1; i <= N; i++) {
            if (par[i] == i) {
                inorder(i, 1);
                break;
            }
        }

        int ansLevel = 10001, ansWidth = 0;
        for (Map.Entry<Integer, int[]> entry : level.entrySet()) {
            int levelKey = entry.getKey();
            int width = entry.getValue()[1] - entry.getValue()[0] + 1;
            if (width > ansWidth || (width == ansWidth && levelKey < ansLevel)) {
                ansLevel = levelKey;
                ansWidth = width;
            }
        }

        System.out.println(ansLevel + " " + ansWidth);
    }

    static void inorder(int n, int l) {
        if (n == 0) return;
        inorder(left[n], l + 1);
        idx++;
        if (level.containsKey(l)) {
            level.get(l)[1] = idx;
        } else {
            level.put(l, new int[]{idx, idx});
        }
        inorder(right[n], l + 1);
    }
}
