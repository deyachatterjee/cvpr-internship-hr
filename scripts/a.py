from PIL import Image
import numpy as np
def open_image():
	 path=input("enter path")
	 newImage = Image.open(path).convert("L")
	 
	 pixel=newImage.getdata()
	 numarr=np.asarray(pixel,dtype="int16")
	 width=newImage.size[0]
	 height=newImage.size[1]
	 arr=numarr.reshape(width,height)
	 rev = arr[::-1]
	 print (rev.shape)
shape=open_image() 	 