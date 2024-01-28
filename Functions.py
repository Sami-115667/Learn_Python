def averageTuple(*numbers):
    sum=0
    for x in numbers:
        sum=sum+x
    print(sum/len(numbers))
    print(len(numbers))
    print(sum)
    print(type(numbers))


averageTuple(12,13,14)
averageTuple(5,6)




def dict(**name):
    print(name)


name={"fname":"shamsur","mname":"rahman","lname":"sami"}

dict(**name)



