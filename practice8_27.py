# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')
#####################################################
# a = int(input())

# if 90 <= a:
#     print('A')
# elif 80 <= a:
#     print('B')
# elif 70 <= a:
#     print('C')
# elif 60 <= a:
#     print('D')
# else:
#     print('F') 
#######################################################
# 윤년문제
# 연도가 주어졌을때 윤년이면 1, 아니면 0을 출력하는 프로그램
# 윤년 = 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일때

# year = int(input())
# if year % 4 == 0:
#     if year % 100 != 0:
#         print('1')
#     elif year % 400 == 0:
#         print('1')
#     else:
#         print('0')
# else: 
#     print('0') 

#######################################################
# 사분면 고르기
# 어떠한  점이 어느 사분면에 속하는지 알아보자

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print('1')
# elif x > 0 and y < 0:
#     print('4')
# elif x < 0 and y < 0:
#     print('3')
# else:
#     print('2')

######################################################
# 알람시계
# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것.
# 현재 상근이가 설정한 알람시각이 주어졌을 때, 시간을 당겨서
# 설정한다. 
# H, B = map(int, input().split())
# if B < 45:
#     if H == 0:
#         H1 = 23
#     else: 
#         H1 = H -1
#     B1 = B +60 - 45
#     print(H1, B1, sep=' ')
# else:
#     B1 = B - 45
#     print(H, B1, sep=' ')
#############          구구단             #################
'''
N을 입력받은 뒤에 구구단 N단을 출력하는 프로그램을 작성
'''
# N = int(input())
# for i in range(1,10):
#     print(N, '*', i, '=', N*i)
#     # print (N * i)

###################################################
#10950
# case = int(input())
# add = sum(i for i in range(0, case+1))
# print(add)    

# 15552
# import sys

# input = sys.stdin.readline
# case = int(input())
# for i in range(0,case):
#     num1, num2 = map(int, input().split())
#     add = num1 + num2
#     print(add)

##################################################
# 2741
# n이 주어졌을때 1부터 n까지 한줄에 하나씩 출력하는 프로그램을 작성하시오
# num = int(input())
# for i in range(num):
#     print(num-i)
#     i += 1

##################################################
# 11021
# case = int(input())
# for i in range(1, case+1):
#     a, b = map(int, input().split())
#     print('Case #%d: %d' % (i, a+b))