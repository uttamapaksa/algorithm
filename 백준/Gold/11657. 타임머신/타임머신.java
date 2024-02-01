import java.io.*;
import java.util.*;

public class Main {

    public static void bellmanFord(ArrayList<int[]> graph, int N) {
        long INF = 5000001;
        long[] dist = new long[N + 1];
        Arrays.fill(dist, INF);
        dist[1] = 0;

        for (int i=1; i<N; i++) {
            for (int[] edge: graph) {
                int a = edge[0];
                int b = edge[1];
                int c = edge[2];
                if (dist[a] != INF && dist[b] > dist[a] + c) {
                    dist[b] = dist[a] + c;
                }
            }
        }

        for (int i=1; i<N; i++) {
            for (int[] edge: graph) {
                int a = edge[0];
                int b = edge[1];
                int c = edge[2];
                if (dist[a] != INF && dist[b] > dist[a] + c) {
                    System.out.println(-1);
                    return;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i=2; i<N+1; i++) {
            System.out.println(dist[i] == INF ? -1 : dist[i]);
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<int[]> graph = new ArrayList<>();
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            graph.add(new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
        }

        bellmanFord(graph, N);
    }
}