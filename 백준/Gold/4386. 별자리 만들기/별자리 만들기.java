import java.io.*;
import java.util.*;

public class Main {
    static int[]  P;
    static double answer;

    static int find(int x) {
        if (P[x] != x) {
            P[x] = find(P[x]);
        }
        return P[x];
    }

    static void union(double w, int x, int y) {
        int a = find(x), b = find(y);
        if (a == b) {
            return;
        }
        if (a < b) {
            P[b] = a;
        } else {
            P[a] = b;
        }
        answer += w;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        P = new int[N];
        double[][] I = new double[N][2];



        // coordinates of all vertex
        for (int i = 0; i < N; i++) {
            P[i] = i;
            st = new StringTokenizer(br.readLine());
            I[i][0] = Double.parseDouble(st.nextToken());
            I[i][1] = Double.parseDouble(st.nextToken());
        }

        // distances between all vertex
        ArrayList<double[]> G = new ArrayList<>();
        for (int u = 0; u < N-1; u++) {
            double x1 = I[u][0], y1 = I[u][1];
            for (int v = u+1; v < N; v++) {
                double x2 = I[v][0], y2 = I[v][1];
                double w = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
                G.add(new double[]{w, u, v});
            }
        }
        G.sort((a, b) -> Double.compare(a[0], b[0]));

        //  kruskal
        for (double[] edge: G) {
            int u = (int)edge[1];
            int v = (int)edge[2];
            union(edge[0], u, v);
        }

        System.out.println(Math.round(answer * 100.0) / 100.0);
    }
}