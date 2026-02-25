// https://school.programmers.co.kr/learn/courses/30/lessons/12932

class Solution {
    public int[] solution(long n) {
        String s = String.valueOf(n);
        int[] answer = new int[s.length()];
        
        int i = 0;
        while (n > 0) {
            answer[i++] = (int)(n % 10);
            n /= 10;
        }
        
        return answer;
    }
}
