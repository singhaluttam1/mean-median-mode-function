def mean(list_of_nums):
    total=0
    for num in list_of_nums:
        total=total+num
    return total/len(list_of_nums)

def mode(list_of_nums):
    max_count=(0,0)
    for num in list_of_nums:
        occurances=list_of_nums.count(num)
        if occurances>max_count[0]:
            max_count=(occurances,num)
    return max_count[1]
def median(list_of_nums):
    list_of_nums.sort()
    x=len(list_of_nums)
    if x%2!=0:
        return (list_of_nums[int((x-1)/2)])
    elif x%2==0:
        middle_index1=list_of_nums[int((x/2))-1]
        middle_index2=list_of_nums[int(x/2)]
        
    return (middle_index1,middle_index2)
print(median([12,33,32,34,2,11,21,14]))
