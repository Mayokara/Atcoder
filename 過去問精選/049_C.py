
def judge(strings):
    s = strings
    t = ''
    patterns = ['dream', 'dreamer', 'erase', 'eraser']
    # patterns = ['dream', 'dreamer', 'erase', 'rerase']
    # strings = dreamererase
    # の場合は探索？再帰関数？
    while len(s) >= 5:
        if s[-5:] == patterns[0]:
            t = s[-5:] + t
            s = s[:-5]

        elif s[-7:] == patterns[1]:
            t = s[-7:] + t
            s = s[:-7]

        elif s[-5:] == patterns[2]:
            t = s[-5:] + t
            s = s[:-5]

        elif s[-6:] == patterns[3]:
            t = s[-6:] + t
            s = s[:-6]

        else:
            print('NO')
            exit()

    if t == strings:
        print('YES')
    else:
        print('NO')

# for文でjudge関数をより汎用的？に
def judge2(strings):
    s = strings
    t = ''
    patterns = ['dream', 'dreamer', 'erase', 'eraser']

    while len(s) >= 5:
        flag = False         
        for i in range(len(patterns)):
            l = len(patterns[i])
            if s[-l:] == patterns[i]:
                t = s[-l:] + t
                s = s[:-l]
                flag = True
                break
        if flag:
            continue
        break
            
    if t == strings:
        print('YES')
    else:
        print('NO')

s_origin = input()
judge(s_origin)
# judge2(s_origin)

# replace()メソッド使うのもあり