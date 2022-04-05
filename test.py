
import skimage 
import cv2
img = cv2.imread('lena.png',0)
 
 
# shape prints the tuple (height,weight,channels)

row = img.shape[0]
print("Row = ", row)
col = img.shape[1]
print("Col = ", col)
totalPixel = row * col
print("Total Pixel = ", totalPixel)


# img will be a numpy array of the above shape

print("All pixel of image array = \n", img)
print("\n")
 
# finding constrast 

max1 = img.max()
print("Maximum pixel = ", max1)
min1 = img.min()
print("Minimum pixel = ", min1)
dif = max1 - min1
print("Contrast is = ", dif)

# finding Brightness
sum = 0
for row in img:
    for col in row:
        sum = sum + col
       
print("Sum of all pixel = ", sum)        
print("Brightness is = ", round(sum / totalPixel))
        

