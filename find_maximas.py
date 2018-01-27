import h5py
from PIL import Image
from PIL import ImageDraw as id
import numpy as np
import matplotlib.pyplot as plt


def findmaxima(path):  # THIS FUNCTION INPUTS THE PATH AND RETURNS THE MAXIMA ARRAY i.e.THE MAXIMUM BLACK PIXELS PER COLUMN
    """

    IF PATH IS NOT INPUTTED LIKE IF WE WANT TO TEST ON ALL FILES IN hdf DATASET

    f=h5py.File("data/Test_resamp")
    keys=list(f.keys())
    total=len(keys)
    for t in range(1):        #for all samples . in range(total)
        sample=f.get(keys[t])
        sampleid=sample.attrs["SampleID"]
        name=sampleid.decode('utf-8')
        imgname="/home/cvpr/Deya/results/"+str(name)+".jpg"
        print ("Reading " + imgname)
        imgs = Image.open(imgname).convert("L")
    """
    print("Reading " + path)
    imgs = Image.open(path).convert("L")
    # print (imgs.size)
    pixel = imgs.getdata()
    numarr = np.asarray(pixel, dtype="int16")
    width = imgs.size[0]
    height = imgs.size[1]
    # draw = id.Draw(imgs)
    arr = numarr.reshape(height, width)  # height=rows  width=cols
    maxima = np.zeros(arr.shape[1])
    # print("Array Shape",arr.shape)
    # image created
    rows = arr.shape[0]
    cols = arr.shape[1]
    # print("Rows =",rows," Cols=",cols)
    for i in range(cols):
        for j in range(rows - 1, 0, -1):
            if arr[j][i] != 255:
                maxima[i] = j
                break

    return maxima


def findtrend(maxima):  # find trends in the data at sampling interval s
    cols = len(maxima)
    s = 14
    # print (cols)
    td_arr = []
    for a in range(cols - 15):

        num1 = maxima[a]
        num2 = maxima[a + 1 + s]
        td = num2 - num1
        # print(num1, ",", num2, ",",td)
        if td > 0:
            td = 1
        elif td < 0:
            td = -1
        else:
            td = 0
        # print(num1, ",", num2, ",", td)
        # print (td)
        td_arr.append(td)
    return td_arr


def conv(arr):  # apply convolution to the trend array
    M = [-1, 0, 1]
    length = len(arr)
    mlength = len(M)
    # offset=1            #M/2
    # output = np.zeros(length+1)     #length +mlength -1
    con = np.convolve(arr, M, "valid")
    return con
# filter i.e. remove the zeroes in prev result to get ellipses at peaks.but there are many peaks so this doesnot work as good


#this function has  been written as the principal function 
def filter():
	path = "C:\\CVPR_WORK\\results\\ajaysamanta7_AmtA.txt.jpg"
	imgs = Image.open(path).convert("L")
	draw = id.Draw(imgs)
	maxima = findmaxima(path)
	cols = len(maxima)
	#print("original Maxima array ", list(maxima))

	sd = np.mean(maxima)
	for i1 in range(cols):
		if maxima[i1] <= sd:
			maxima[i1] = 0
	# print("modified maxima array after mean")
	# print(list(maxima))
	td_array = findtrend(maxima)
	convolution = conv(td_array)
	convolution2 = conv(convolution)
	# print("Trend array ")
	# print (td_array)
	#print("final Convolution matrix i.e. y is", list(convolution2))
	sd2 = np.mean(convolution2)
	for i2 in range(len(convolution2)):
		if convolution2[i2] <= sd2:
			convolution2[i2] = 0
	# convolution2 IS THE FINAL MATRIX OF PEAKS. REGRESSION LINE IS DRAWN CONSIDERING IT AS y.
	# y=np.asarray(convolution2)    #this is the y value to get the coeffcients
	x = []
	y = convolution2
	print("y length is", len(y))
	for i3 in range(len(y)):
		x.append(i3)  # this is the x value to get the coeffcients i.e. the column indices
	print("x is ", x)
	#print("y is ", list(y))
	total=len(x)
	#print("Xs=",xs,total)
	x_sum=sum(x)
	y_sum=sum(y)
	x_mean=x_sum/float(total)
	y_mean = y_sum / float(total)
	A=[]
	B=[]
	C=[]
	D=[]
	E=[]
	for t in range(total):
		a=x[t]-x_mean
		b=y[t]-y_mean
		A.append(a)
		B.append(b)
		C.append(a**2)
		D.append(b**2)
		E.append(a*b)
	sum_c=sum(C)
	sum_e=sum(E)
	if(sum_c==0):
		sum_c=0.00001
	b1=float(sum_e)/float(sum_c)
	b0=y_mean-b1*x_mean
	#print("b1=",b1,"b0=",b0)
	#return b0,b1
	#print("the coefficients b1 and b0 are ", b1, b0)
	y_pred = []
	for j in range(len(x)):
		y_pred.append(b0 + b1 * x[j])
	#print("the predicted y is", y_pred)
	for i in range(len(y_pred)):
		num = y_pred[i]
		coord1 = i
		coord2 = num
		coord3 = i + 4
		coord4 = num + 4
		draw.ellipse((coord1, coord2, coord3, coord4), fill=45)
	imgs.show()
	
	
    
filter()

	
"""
important code snippets that should not be lost
crd1=y_pred[i]
	crd2=y_pred[i+1]
	crd3=
	crd4=
	draw.ellipse((crd1,crd2, crd3,crd4), fill=120)

draw = id.Draw(imgs)
    for j1 in range(len(y_pred) - 1):
        crd2 = y_pred[j1]
        crd4 = y_pred[j1 + 1]
        crd1 = j1
        crd3 = j1 + 1
        print(crd1, crd2, " , ", crd3, crd4)
        draw.line((crd1, crd2, crd3, crd4), width=5, fill=120)
    imgs.show()
	
	for i in range(len(maxima)):
		if maxima[i] != 0:
			num = maxima[i]
			coord1 = i
			coord2 = num
			coord3 = i + 4
			coord4 = num + 4
			draw.ellipse((coord1, coord2, coord3, coord4), fill=120)
	imgs.show()

convolution[i]=1
convolution[i]=np.multiply(convolution[i],maxima[i+2])
num = convolution[i]
coord1 = i
coord2 = num
coord3 = i + 4
coord4 = num + 4

for i1 in range(len(convolution2)):
	if convolution2[i1] <= sd:
		convolution2[i1] = 0

this is the code for showing the points in the image

for i in range(len(convolution2)):
		if convolution2[i]!=0:
			#convolution[i]=1
			#convolution[i]=np.multiply(convolution[i],maxima[i+2])
			num = maxima[i+2+2]
			coord1 = i+2+2
			coord2 = num
			coord3 = i + 4
			coord4 = num + 4
			draw.ellipse((coord1, coord2, coord3, coord4), fill=120)
	imgs.show()

b = maxima1[x+1][y]
d = maxima1[x+1][y+1]
c = maxima1[x][y+1]		

#print("Number of maximas=",len(maxima))
		draw=id.Draw(imgs)
		for a in range(len(maxima)):
			print(maxima[a])

		for a in range(cols):
			num = maxima[a]
			coord1= a
			coord2=num
			coord3=a+4
			coord4=num+4
			draw.ellipse((coord1,coord2, coord3,coord4), fill=120)
		imgs.show()												
#box=np.asarray(sample.attrs["Box"],dtype="int16")
	#i=box[0]-box[1]+30
	#j=box[2]-box[3]+30
	#im = Image.new("RGB", (i,j), "white")
	#draw = id.Draw(im)

regression codes

	def fit(x,y):
	xmean=np.mean(x)
	ymean=np.mean(y)
	sdx=np.std(x)
	sdy=np.std(y)
	r=np.corrcoef(x,y)
	m=r*(sdy/sdx)   #SLOPE
	y_intercept=ymean-(m*xmean)
	return m-y_intercept

    mean_x = np.mean(x)
    mean_y = np.mean(y)
    m = len(x)
    numer = 0
    denom = 0
    for i in range(m):
        numer += (x[i] - mean_x) * (y[i] - mean_y)
        denom += (x[i] - mean_x) ** 2
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)
	
	
	# def getcoeff(x,y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y * x - n * m_y * m_x)
    SS_xx = np.sum(x * x - n * m_x * m_x)
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
 """