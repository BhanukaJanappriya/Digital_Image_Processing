import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])

print(a)
print()
print(b)
print()
# element-wise multiplication
print("Element-wise multiplication--> ")
print(a*b)

# # Dot product
print("Dot product--> ")
print(np.dot(a,b))

# # Matrix multiplication
print("Matrix multiplication--> ")
print(np.matmul(a,b))
