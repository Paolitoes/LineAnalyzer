import numpy as np

img = np.array([[1,2,3],
               [4,5,6],
                [7,8,9]])
print(img)
print(f"shape of first array is {img.shape}")
img2 = np.ndarray(img.shape+(3,),np.int32)
img2[:,:,0] = img
print(img2)
print(f"shape of second array is {img2.shape}")

img3 = np.zeros(img.shape+(3,))
print(img3)
print(f"shape of thrid array is {img3.shape}")

