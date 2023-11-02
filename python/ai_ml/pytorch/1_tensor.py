import torch 
import numpy as np

# a = np.array([[[1,2,3],[4,5,6],[2,4,5]],[[4,5,6],[7,8,9],[10,11,12]]])
# print(a)
# print(np.ndim(a))
# print(np.shape(a))

# b = torch.tensor(a)
# print(b)
# print(np.ndim(b))
# print(np.shape(b))

# scalar = torch.tensor(2) # 0-D Tensor

# vector = torch.tensor([1,2,3]) # 1-D Tensor

# MATRIX = torch.tensor([[1,2,3],[4,5,6]]) # 2-D Tensor

# TENSOR = torch.tensor([[[1,2,4],[3,4,6]],[[0,7,8],[9,9,9]],[[9,10,11],[100,11,12]],[[0,0,1],[1,2,3]]])
# print(TENSOR)
# print(TENSOR.ndim)
# print(TENSOR.shape)

# random = torch.rand(4,3) # Random tensors are important in the sense that neural nets tends to learn from tensors full of random numbers and adjust those random numbers to better represent the data.
# print(random)
# print(random.ndim)

# zeros = torch.zeros(2,3) # same for ones
# print(zeros)
# print(zeros.dtype)

# zero_to_ten = torch.arange(1,10)
# zero_to_ten = torch.arange(start=1,end=10,step=2)
# print(zero_to_ten)
# to_zeros = torch.zeros_like(input=zero_to_ten)
# print(to_zeros)

 