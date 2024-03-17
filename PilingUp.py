import collections
for _ in range (int(input())):
  n= int(input())
  side_lengths=collections.deque(map(int,input().split()))
  horizontal_row=[]
  while len(side_lengths)>0:
    if side_lengths[-1]>side_lengths[0]:
      horizontal_row.append(side_lengths[-1])
      side_lengths.pop()
    else:
      horizontal_row.append(side_lengths[0])
      side_lengths.popleft()
  if all(horizontal_row[i+1]<=horizontal_row[i] for i in range (len(horizontal_row)-1)):
    print ("Yes")
  else :
    print("No")