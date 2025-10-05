S = input()

w, s = S.split('-')

if s == '8':
    print(str(int(w)+1) + '-1')
else:
    print(w+'-'+str(int(s)+1))