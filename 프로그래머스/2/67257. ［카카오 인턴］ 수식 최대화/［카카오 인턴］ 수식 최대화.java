import java.util.*;

class Solution {
    static int N;
    static int[] P;
    static long[] numsCopy;
    static ArrayList<Long> nums = new ArrayList<>();
    static ArrayList<String> opers = new ArrayList<>();

    static int find(int x) {
        if (P[x] != x) {
            P[x] = find(P[x]);
        }
        return P[x];
    }

    static void union(int x, int y, long v) {
        int a = find(x);
        int b = find(y);
        if (a < b) {
            P[b] = a;
            numsCopy[a] = v;
        } else {
            P[a] = b;
            numsCopy[b] = v;
        }
    } 
    
    public long solution(String expression) {
        String word = "";
        for (String x: expression.split("")) {
            if (x.equals("+") || x.equals("-") || x.equals("*")) {
                opers.add(x);
                nums.add(Long.parseLong(word));
                word = "";
            } else {
                word += x;
            }
        }
        nums.add(Long.parseLong(word));
        
        N = nums.size();
        P = new int[N];
        numsCopy = new long[N];
        
        long answer = 0L;
        for (String[] orders: new String[][]{{"*","+","-"}, {"*","-","+"}, {"+","*","-"}, {"+","-","*"}, {"-","*","+"}, {"-","+","*"}}) {
            for (int i=0; i<N; i++) {
                P[i] = i;
            }
            for (int i=0; i<N; i++) {
                numsCopy[i] = nums.get(i);
            }
            for (String order: orders) {
                for (int j=0; j<N-1; j++) {
                    if (!opers.get(j).equals(order)) continue;
                    
                    long result;
                    if (opers.get(j).equals("*")) result = numsCopy[find(j)] * numsCopy[find(j+1)];
                    else if (opers.get(j).equals("+")) result = numsCopy[find(j)] + numsCopy[find(j+1)];
                    else if (opers.get(j).equals("-")) result = numsCopy[find(j)] - numsCopy[find(j+1)];
                    else continue;
                    union(j, j + 1, result);
                }   
            }
            answer = Math.max(answer, Math.abs(numsCopy[0]));
        }
    
        return answer;
    }
}
