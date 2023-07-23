def sum(a,b):
    return a + b

result = sum(5,4)
print (result)




def average (*nums):
     summa = 0
     for num in nums:
      summa += num
      result = summa / len(nums)
     return result

avg = average(10,9,9,9,9,9)
print (avg)