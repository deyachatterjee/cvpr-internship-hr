import h5py
from PIL import Image
from PIL import ImageDraw as id
import numpy as np
f = h5py.File("data\Test_resamp", "r")

"""def draw():
	draw = id.Draw(im)
	p=
	q=
	draw.line((p,q), fill=300)
	"""
#def getdata():
"""for data in f:

	folder = f.get(data)
	for strokes in folder:
		stroke=folder.get(strokes)
		stroke=np.array(stroke)
		for i in range(stroke.shape[0]):
			a=stroke[i,0]
			b=stroke[i,1]
			#return a,b
		"""	
		

for dta in f:
	data=f[dta]
	for item in data.attrs.keys():
	#if item=="Box":
		name=data.attrs["SampleID"].decode('utf-8')
		box=np.asarray(data.attrs["Box"],dtype="int16")
		num_strokes=data.attrs["Nb_Strokes"]
		#dset = f.create_dataset("Strokes", (num_strokes,1), dtype='i')
		i=box[0]-box[1]
		j=box[2]-box[3]
		im = Image.new("RGB", (i, j), "white")
		
		
		
		
		
"""		
for dta in f:

	folder = f.get(dta)
	for strokes in folder:
	#print (data.attrs[strokes])
		stroke=folder.get(strokes)
		stroke=np.array(stroke)
		#print(strokes.attrs["SampleID"])
		for i in range(stroke.shape[0]):
			a=stroke[i,0]
			b=stroke[i,1]
			draw = id.Draw(im)
			draw.line((a,b), fill=300)
			im.save("SampleID.jpg")

		#np.concatenate((a, b), axis=0) vertical concatenation
	    #print(item + ":", data.attrs["Box"])
"""

#d = f["anirbanpal7_AmtA.txt"]
#for item in d.attrs.keys():
	#if item=="Box":
#	    print(item + ":", d.attrs[item])
#print(a)
#print(b)
#print(c)
#c=data.attrs["Unicode_Target"].decode('utf-8')"""