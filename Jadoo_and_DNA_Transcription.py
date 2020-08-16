test = input()
out = ''
flag = 'T'
for i in test:
    if i not in ['G','C','T','A']:
        print('Invalid Input')
        flag = 'F'
        break
    else:
        if i == 'G':
            out+= 'C'
        elif i == 'C':
            out += 'G'
        elif i == 'T':
            out += 'A'
        elif i == 'A':
            out += 'U'

if flag == 'T':
    print(out)
