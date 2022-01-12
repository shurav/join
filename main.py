import numpy

#takes in two numpy arrays and returns their join by using the concatenate function along the 0th axis
def joining(arr1, arr2):
    return(numpy.concatenate((arr1, arr2)))

#filles both arrays with user specified values based on the shape of the arrays
def arrValuesFiller(arr1, arr2):
    print("Enter the values in sequential order for the first array")
    with numpy.nditer(arr1, op_flags=['readwrite']) as it:
        for x in it:
            while True:
                try:
                    x[...] = int(input("Enter the value "))
                except ValueError:
                    print("Invalid")
                else:
                    break
    print("Enter the values in sequential order for the second array")
    with numpy.nditer(arr2, op_flags=['readwrite']) as it2:
        for y in it2:
            while True:
                try:
                    y[...] = int(input("Enter the value "))
                except ValueError:
                    print("Invalid")
                else:
                    break
    
while True:
    try:
        firstarr = [] # will be used for first array
        secarr = [] # will be used for second array
        shapeList = [] # will be used for iteration to determine shape of arrays
        dimensions = int(input("How many dimensions are the arrays ")) # dimension must be same for both arrays for joining to take place
        print("You will know enter the shape of the array by dimension")
        while(len(shapeList) != dimensions): #iteration serves to append values in each dimension to shapeList to determine the shape of the arrays
            shape = int(input("Enter the number of values in the "+ str(dimensions-len(shapeList)-1) + " dimension "))
            shapeList.append(shape)
        print("This is the shape you entered ", tuple(shapeList))
        # both arrays are initialized to empty arrays with the specified shape
        firstarr = numpy.empty(tuple(shapeList), dtype = int)
        secarr = numpy.empty(tuple(shapeList), dtype = int)
        arrValuesFiller(firstarr, secarr) # call to arrValuesFiller to fill in both arrays with user defined values
        joinedArr = joining(firstarr, secarr) # call to joinedArr to concatenate both arrays
        print("The result of the join of the arrays along the 0th axis is \n", joinedArr)
    except ValueError:
        print("invalid")
    else:
        break
