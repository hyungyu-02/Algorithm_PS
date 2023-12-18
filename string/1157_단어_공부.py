#String
words = input().upper()
uniq_words = list(set(words))

cnt_list = []

for c in uniq_words :
    cnt = words.count(c)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(uniq_words[max_index])
