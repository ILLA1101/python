n = int(input()) #줄 입력

for i in range(n) : #줄
    for j in range(n-(i+1)) : #빈칸을 채움
        print(' ',end = '') # 빈칸을 채우면서 ,end = ' '  < 를 사용하여 줄바꿈을 안함
    for j in range(i+1) : # 별을 출력
        print('*',end = '') # '*'을 출력 하면서 ,end = ' ' < 를 사용하여 줄바꿈을 안함
    print() # 줄바꿈
'''
0000*
000**
00***
0****
*****
'''