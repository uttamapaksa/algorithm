import java.io.*;
import java.util.*;

public class Main {
    static int [][] round = new int[4][8];
    static int[] idx = new int[4];

    static void turn(int num, int dir) {
        int[] delta = new int[4];
        delta[num] -= dir;

        // right part
        int nDir = dir;
        for (int i=num; i<3; i++) {
            if (round[i][(idx[i] + 2) % 8] != round[i+1][(idx[i+1] + 6) % 8]) {
                delta[i+1] += nDir;
                nDir = -nDir;
            } else {
                break;
            }
        }
        // left part
        nDir = dir;
        for (int i=num; i>0; i--) {
            if (round[i][(idx[i] + 6) % 8] != round[i-1][(idx[i-1] + 2) % 8]) {
                delta[i-1] += nDir;
                nDir = -nDir;
            } else {
                break;
            }
        }

        // turn
        for (int i=0; i<4; i++) {
            idx[i] = (idx[i] + delta[i] + 8) % 8;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));

        for (int i=0; i<4; i++) {
            String[] input = br.readLine().split("");
            for (int j=0; j<8; j++) {
                round[i][j] = Integer.parseInt(input[j]);
            }
        }

        int time = Integer.parseInt(br.readLine());
        for (int i=0; i<time; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            turn(num - 1, dir);
        }

        int ans = 0;
        for (int i=0; i<4; i++) {
            ans += round[i][idx[i]] * Math.pow(2, i);
        }

        System.out.println(ans);
    }
}