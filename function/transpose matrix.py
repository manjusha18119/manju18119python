print("Enter the matrix...")
row=input("Enter the row number : ")
column=input("Enter the column number : ")
matrix1=[]
matrix=[]
for i in range(row):
	print "Enter element to row : ",i+1 
	for j in range(column):
		matrix1.append(input())
	matrix.append(matrix1)
	matrix1=[]
print matrix
matrix1=[]
matrix1=list(*matrix)
print matrix1


matrix2=[]
for i in matrix1:
	matrix2.append(list(i))
print matrix2
