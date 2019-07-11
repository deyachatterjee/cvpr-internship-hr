from PIL import Image
import numpy as np
def open_image(path):
 newImage = Image.open(path)
 pixel=newImage.getdata()
 numarr=np.asarray(pixel,dtype="int16")     #
 channel=len(pixel[0])
 width=newImage.size[0]
 height=newImage.size[1]
 arr=numarr.reshape(width,height,channel)                #  print (arr.shape)
 value=int(input("Enter value to increase matrix"))
 for i in range(arr.shape[0]):
  for j in range(arr.shape[1]):
   for k in range(arr.shape[2]):
    arr[i][j][k]+=value
	if arr[i][j][k]>255:
	  arr[i][j][k]=255
 img = Image.fromarray(arr, 'RGB')
 img.save('my.png')
 img.show()
  
open_image("download.jpg")  
  

