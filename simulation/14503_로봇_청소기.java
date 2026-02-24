package baekjoon.gold;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main14503 {
    public static void main(String[] args) throws IOException {
//        System.setIn(new FileInputStream("inputs/baekjoon/14503.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 지도의 크기 N x M
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d
        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        // 지도 정보 (0: 빈 칸, 1: 벽)
        int[][] map = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int count = 0;

        while (true) {
            // 현재 칸이 청소가 안된 경우
            if (map[r][c] == 0) {
                map[r][c] = -1;
                count++;
            }

            // 주변 4칸 중 청소가 안된 칸이 있는 경우
            if (map[r - 1][c] == 0 || map[r][c - 1] == 0 || map[r + 1][c] == 0 || map[r][c + 1] == 0) {
                for (int i = 0; i < 4; i++) {
                    d -= 1;
                    if (d < 0) {
                        d = 3;
                    }

                    if (d == 0 && map[r - 1][c] == 0) {
                        r -= 1;
                        break;
                    } else if (d == 1 && map[r][c + 1] == 0) {
                        c += 1;
                        break;
                    } else if (d == 2 && map[r + 1][c] == 0) {
                        r += 1;
                        break;
                    } else if (d == 3 && map[r][c - 1] == 0) {
                        c -= 1;
                        break;
                    }
                }

            } else { // 현재 칸의 주변4칸 중 청소되지 않은 빈 칸이 없는 경우
                if (d == 0 && map[r + 1][c] != 1) {
                    r += 1;
                } else if (d == 1 && map[r][c - 1] != 1) {
                    c -= 1;
                } else if (d == 2 && map[r - 1][c] != 1) {
                    r -= 1;
                } else if (d == 3 && map[r][c + 1] != 1) {
                    c += 1;
                } else {
                    break;
                }
            }
        }

        System.out.println(count);

//        System.out.println("로봇 위치: (" + r + ", " + c + "), 방향: " + d);
//        System.out.println("지도 크기: " + map.length + "x" + map[0].length);
    }
}
