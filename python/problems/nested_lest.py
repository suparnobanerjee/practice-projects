#PROMLEM STATEMENT LINK : https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

a=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    a.append([name,score])

highest = float('-inf')
second_highest = float('-inf')
for _,num in a:
    if num>highest:
        second_highest=highest
        highest=num
    elif num<highest and num>second_highest:
        second_highest=num

# print(f'The second lowest score is {second_highest}')

second_highest_names = [names for names,scores in a if scores == second_highest]



print(second_highest_names)