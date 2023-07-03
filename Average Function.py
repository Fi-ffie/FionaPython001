#create a function that gives you the average of a list of items.
def Calculate_Average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total/count
    return average

dataset = [2, 3, 5, 7, 11, 2,]
answer = Calculate_Average(dataset)
print("The average is ", answer)