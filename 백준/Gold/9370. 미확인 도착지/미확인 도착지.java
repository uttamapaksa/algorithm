import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static Map<Integer, List<int[]>> graph;

    public static int[] dijkstra(int s) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, 2000001);
        dist[s] = 0;
        PriorityQueue<int[]> priorityQueue = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        priorityQueue.add(new int[]{dist[s], s});

        while (!priorityQueue.isEmpty()) {
            int[] curr = priorityQueue.poll();
            int d = curr[0];
            int u = curr[1];
            if (dist[u] < d) continue;

            for (int[] entry: graph.get(u)) {
                int w = entry[0];
                int v = entry[1];
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    priorityQueue.add(new int[]{dist[v], v});
                }
            }
        }

        return dist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            graph = new HashMap<>();
            for (int j = 1; j <= n+1; j++) {
                graph.put(j, new ArrayList<>());
            }

            for (int j = 0; j < m; j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());

                graph.get(a).add(new int[]{d, b});
                graph.get(b).add(new int[]{d, a});
            }

            List<Integer> destinations = new ArrayList<>();
            for (int j = 0; j < t; j++) {
                destinations.add(Integer.parseInt(br.readLine()));
            }
            destinations.sort(Comparator.naturalOrder());

            int[] dists = dijkstra(s);
            int[] distg = dijkstra(g);
            int[] disth = dijkstra(h);
            int w = 0;
            for (int[] entry: graph.get(g)) {
                int ww = entry[0];
                int vv = entry[1];
                if (vv == h) {
                    w = ww;
                    break;
                }
            }

            for (int x : destinations) {
                if (dists[x] == dists[g] + w + disth[x] || dists[x] == dists[h] + w + distg[x]) {
                    sb.append(x).append(" ");
                }
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }
}