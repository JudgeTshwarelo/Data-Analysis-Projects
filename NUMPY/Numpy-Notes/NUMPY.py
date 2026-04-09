import numpy as np

#Introduction to numpy
array = np.array([1, 2, 3, 4])
array *= 2

#print(array)

#-----------------------------------------------------------------------------------------------------------------------
#multidimensional arrays (2D arrays)

array = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],  #layer
                  [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],  #layer
                  [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]]) #layer
                    #row                #row            #row
                    #column - down

#print(array.ndim)   #it checks the number of dimensions in an array
#print(array.shape) #check the depth(layers), row and column
#print(array[layer][row][colum])
#print(array[0][1][0])   #chain indexing - accessing certain element
#print(array[0, 0, 0])    #multidimensional indexing

#excercise (3 letters word using string concatenation)
word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]

#print(word)

#-----------------------------------------------------------------------------------------------------------------------
#slicing

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

#array[start:end:step]

#selecting rows
#print(array[0:4:2])
#       0r
#print(array[::2])

#selecting columns
#print(array[:, 1: 4])

#selecting both rows and columns
#print(array[0:2, 0:2])

#-----------------------------------------------------------------------------------------------------------------------
#Scalar arithmetic

array_sa = np.array([1, 2, 3])

# scalar (linear) arithmetic
'''
print(array_sa + 1)
print(array_sa - 2)
print(array_sa * 3)
print(array_sa / 4)
print(array_sa ** 5)'''

#vectorized (single dimension) math funcs :
'''print(np.sqrt(array_sa))
print(np.round(array_sa))
print(np.floor(array_sa)) #round down
print(np.ceil(array_sa)) #round up
print(np.pi)'''

#exercise (scalar + vectorized  arithmetic)
radii = np.array([1, 2, 3])
circumference = np.pi * radii ** 2
#print(circumference)

#element wise arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

#print(array1 + array2)
#print(array1 - array2)
#print(array1 * array2)
#print(array1 / array2)
#print(array1 ** array2)

#comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])

#print(scores == 100)
#print(scores >= 60)
#print(scores < 60)

scores[scores < 60] = 0
#print(scores)

#-----------------------------------------------------------------------------------------------------------------------
#Broadcasing allows NumPy to perform operation on arrays
#with different shapes by virtually expanding dimensions
#so they match the layer array's shape

#the dimensions have the same size
#OR
#One of the dimensions have a size of 1

array_1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9,10, 11, 12],
                   [13, 14, 15, 16]])
array_2 = np.array([[1], [2], [3], [4]])

#print(array_1.shape)
#print(array_2.shape)

#print(array_1 * array_2)   #broadcasting the array shapes

#exercise : create multiplication table via broadcasting
array__1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array__2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

#print(array__1.shape)
#print(array__2.shape)

#print(array__1 * array__2)

#-----------------------------------------------------------------------------------------------------------------------
#aggregate functions = summarize data and typically
#                       returns a single value

array3 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

#print(np.sum(array3))
#print(np.mean(array3))
#print(np.std(array3))    #standart deviation
#print(np.var(array3))    #variance
#print(np.min(array3))
#print(np.max(array3))
#print(np.argmin(array3)) #position of a min value
#print(np.argmax(array3)) #position of a max value

#select an axis
#print(np.sum(array3, axis = 0)) #sum all columns
#print(np.sum(array3, axis = 1)) #sum all rows

#-----------------------------------------------------------------------------------------------------------------------
#filtering = refers to the process of selecting elements
#               from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenager = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65) ]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

#where function
adult = np.where(ages >= 18, ages, 0) #keeps the original shape of the data

#print(adult)

#-----------------------------------------------------------------------------------------------------------------------
#random numbers

rng = np.random.default_rng()
#print(rng.integers(low=1, high=7, size=(3, 2)))

#floating numbers
#print(np.random.uniform(low=-1, high=1, size=(3, 3)))

#shovel an array
array4 = np.array([1,2,3,4,5])
rng.shuffle(array4)
print(array4)

#random choice
fruits = np.array(['apple', 'orange', 'banana', 'coconut', 'pineapple'])
fruits = rng.choice(fruits, size=(2, 2))
print(fruits)