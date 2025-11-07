
print("Statistics Data Sorter")
dataset = input("Provide a data set:")
text_to_number = dataset.split(",")#whats happening with this bracket
numbers = []
for x in text_to_number:
    numbers.append(int(x))
    
numbers.sort()
print("New Sorted Version:",numbers)

mean = sum(numbers)/len(numbers)
print("Mean:",mean)
n = len(numbers)
if n % 2 == 1:#check if odd
    calc = n//2#math formula
    median = numbers[calc]     
    print("Median:",median)

elif n % 2 == 0:#if even
    mid1 = numbers[n//2]
    mid2 = numbers[n//2-1]
    median = (mid1 + mid2)/2#math formula
    print("Median:",median)
minimum = min(numbers)
maximum =max(numbers)
print("Minimum:",minimum)
print("Maximum:",maximum)
Range = maximum-minimum#range formula
print("Range:",Range)
 
    


    
    
    

