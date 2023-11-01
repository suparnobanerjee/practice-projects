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

TENSOR = torch.tensor([[[1,2,4],[3,4,6],[0,0,0]],[[10,5,6],[0,7,8],[9,9,9]],[[9,10,11],[100,11,12],[10,10,10]],[[0,0,1],[1,2,3],[5,6,10]]])
print(TENSOR)
print(TENSOR.ndim)
print(TENSOR.shape)



