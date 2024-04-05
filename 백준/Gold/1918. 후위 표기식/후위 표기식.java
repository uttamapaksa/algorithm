import java.io.*;
import java.util.*;

public class Main {
    static int i = 0;
    static String[] input;
    static int N;

    static String solve() {
        StringBuilder sb = new StringBuilder();
        Stack<String> stack = new Stack<>();

        while (i < N) {
            String str = input[i++];

            if (str.equals("(")) {
                sb.append(solve());
            } else if (str.equals(")")) {
                break;
            } else if (str.equals("*") || str.equals("/")) {
                while (!stack.isEmpty() && !(stack.peek().equals("+") || stack.peek().equals("-"))) {
                    sb.append(stack.pop());
                }
                stack.push(str);
            } else if (str.equals("+") || str.equals("-")) {
                while (!stack.isEmpty()) {
                    sb.append(stack.pop());
                }
                stack.push(str);
            } else {
                sb.append(str);
            }
        }

        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine().split("");
        N = input.length;
        String answer = solve();
        System.out.println(answer);
    }
}
