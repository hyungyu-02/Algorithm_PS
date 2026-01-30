# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):

    tickets.sort()

    used = [False] * len(tickets)

    def dfs(current_airport, path):
        if len(path) == len(tickets) + 1:
            return path

        for i in range(len(tickets)):
            if tickets[i][0] == current_airport and not used[i]:
                used[i] = True
                result = dfs(tickets[i][1], path + [tickets[i][1]])

                if result:
                    return result

                used[i] = False

        return None

    return dfs("ICN", ["ICN"])
