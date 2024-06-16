'''Ant on Rail problem
right=+1 left=-1
input format:
1)An integer value N representing the number of moves by the ant
2)An integer array A consisting of the ant's moves towards either side
output;
i/p:-5
1 -1 1 -1 1
'''
n=int(input())
count=0#starting position
ans=0#final answer
a=list(map(int,input().split()))
for i in a:
    count+=i#1-1=0,1+1-1=1
    if count==0:
        ans+=1#1
print(ans)
    

   

