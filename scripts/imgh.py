from PIL import Image
from PIL import ImageDraw as id
from collections import Counter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
def open_image(path):
	 newImage = Image.open(path).convert("L")
	 pixel=newImage.getdata()
	 numarr=np.asarray(pixel,dtype="int16")
	 #channel=len(pixel[0])
	 width=newImage.size[0]
	 height=newImage.size[1]
	 arr=numarr.reshape(height,width) #important. when reshaping swap the width and height because width=no.o of cols. etc
	 return arr
def brighten(arr,value):
	
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			arr[i][j]+=value
			if arr[i][j]>255:
				arr[i][j]=255
	return arr

def contrast(arr,mul,value):
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			arr[i][j]*=mul
			arr[i][j]+=value
			if arr[i][j]>255:
				arr[i][j]=255
	return arr			

def binarize(arr,threshold1):
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			if arr[i][j]>threshold1:
				arr[i][j]=255
			else:
				arr[i][j]=0
	return arr			
					

def drawonimage(path):
	im = Image.open(path)
	draw = id.Draw(im)
	draw.line((0, 0) + im.size, fill=128)
	im.save("drawimage.jpg")
	im.show()

def drawonnew(i,j,r):
	im = Image.new("RGB", (i, j), "white")
	draw = id.Draw(im)
	a=i/2
	b=j/2	
	draw.line((a-r,b-r, a+r,b-r), fill=300)
	draw.line((a-r,b-r, a-r,b+r), fill=300)
	draw.line((a+r,b-r, a+r,b+r), fill=300)
	draw.line((a-r,b+r, a+r,b+r), fill=300)
	bbox =  (a-r, b-r, a+r, b+r)
	draw.ellipse(bbox, outline=120)
	#draw.rectangle(bbox, outline=120)
	im.save("drawnimage.jpg")
	im.show()	
					

def hist(arr):
	hist=np.zeros([256])
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			hist[arr[i][j]]=hist[arr[i][j]]+1
	
	
	return hist	
	
def save_image(arr,path): 
	 img = Image.fromarray(arr.astype('uint8'))
	 img.save(path)
	 img.show()
	 
def plothist(arr):
	num_bins = 256
	n, bins, patches = plt.hist(arr, num_bins, facecolor='blue', alpha=0.5)
	plt.xlabel('number of pixels')
	plt.ylabel('pixel distribution')
	plt.title('Histogram of pixel distribution')
	
	plt.show()
	
a=open_image("download.jpg") 
#b=contrast(a,1.3,20)
#save_image(b,"contrast.jpg")
#c=binarize(a,200)
#save_image(c,"binarize.jpg")
#d=hist(a)
#plothist(d)
#plt.imshow("download.jpg")
#save_image(a)
#drawonimage("download.jpg")
drawonnew(300,300,40)