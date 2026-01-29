# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict

def solution(genres, plays):
    answer = []

    plays_per_genre = defaultdict(int)
    songs_in_genre = defaultdict(list)

    for i in range(len(genres)):
        plays_per_genre[genres[i]] += plays[i]
        songs_in_genre[genres[i]].append((plays[i], i))

    sorted_ppg = sorted(plays_per_genre.items(), key=lambda x: x[1], reverse=True)

    for genre, total_plays in sorted_ppg:
        songs_in_genre[genre].sort(key=lambda x: (-x[0], x[1]))
        top_two = songs_in_genre[genre][:2]

        for p, i in top_two:
            answer.append(i)

    return answer
