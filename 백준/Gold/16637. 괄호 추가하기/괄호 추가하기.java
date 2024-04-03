import java.io.*;
import java.util.*;

public class Main {
    static int answer = Integer.MIN_VALUE;
    static int N;
    static String[] input;

    static int operate(int x, String oper, int y) {
        if (oper.equals("+")) return x + y;
        if (oper.equals("-")) return x - y;
        return x * y;
    }

    static void dfs(int i, int value) {
        if (i == N - 1) {
            answer = Math.max(answer, value);
            return;
        }
        if (i + 2 < N) {
            dfs(i + 2, operate(value, input[i + 1], Integer.parseInt(input[i + 2])));
        }
        if (i + 4 < N) {
            dfs(i + 4, operate(value, input[i + 1], operate(Integer.parseInt(input[i + 2]), input[i + 3], Integer.parseInt(input[i + 4]))));
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        input = br.readLine().split("");

        dfs(0, Integer.parseInt(input[0]));
        System.out.println(answer);
    }
}