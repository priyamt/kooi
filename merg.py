def mergeg



def mergesort(m):
  if len(m)<2:return m
  left=[]
  right=[]
  result=[]
  mid=len(m)/2
  for num in m:
    if m.index(num)<=mid:
      left.append(num)
    else:
      right.append(num)
  left=mergesort(left)
  right=mergesort(right)
  result=merge(left,right)
  return result
