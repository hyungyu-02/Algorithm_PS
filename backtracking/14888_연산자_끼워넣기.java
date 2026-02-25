package baekjoon.silver;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main14888 {
    static int N;
    static int[] A;
    static int[] operators = new int[4];
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("inputs/baekjoon/14888.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 수의 개수 N
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        // 숫자 배열 A
        st = new StringTokenizer(br.readLine());
        A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // 연산자의 개수 + - * /
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            operators[i] = Integer.parseInt(st.nextToken());
        }

        dfs(A[0], 1);

        System.out.println(max);
        System.out.println(min);
    }

    private static void dfs(int current, int index) {
        if (index == N) {
            max = Math.max(max, current);
            min = Math.min(min, current);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (operators[i] > 0) {
                operators[i]--;

                if (i == 0) dfs(current + A[index], index + 1);
                else if (i == 1) dfs(current - A[index], index + 1);
                else if (i == 2) dfs(current * A[index], index + 1);
                else dfs(current / A[index], index + 1);

                operators[i]++;
            }
        }
    }
}
