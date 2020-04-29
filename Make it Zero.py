"""
Make it zero.
Given a positive number, print the number of steps to make the given number zero. 
Rules:
If the current number is EVEN, then divide the number by 2, 
If the number is ODD, then subtract 1 from then number.

Input= 14
Output= 
6
14 7 6 3 2 1 0    --- print list of each step value.
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

Input=
15
Output=
7
15 14 7 6 3 2 1 0
----------------------
Input=
4
Output=
3
4 2 1 0
---------------------
Input=
19
Output=
7
19 18 9 8 4 2 1 0
"""
n=int(input())
n1=n
c=0
for i in range(0,n):
    if(n==0):
        break
    elif(n%2==0):
        n=n/2
        c=c+1
    else:
        n=n-1
        c=c+1
print(str(c))
n=n1
print(str(n),end=" ")
for i in range(0,n):
    if(n==0):
        break
    elif(n%2==0):
        print(str(round(n/2)),end=" ")
        n=n/2
    else:
        print(str(round(n-1)),end=" ")
        n=n-1

