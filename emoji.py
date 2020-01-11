def emoji():
    emoj = {":)": "🙂", ":(": "☹", ":D": "😃"}
    talk = input("")
    word = talk.split()
    display = word[0:-1]
    for i in word:
        for j in emoj.keys():
            if i == j:
                i = emoj[j]
    for k in display:
        print(k, end=' ')
    print(i, end='')


emoji()
