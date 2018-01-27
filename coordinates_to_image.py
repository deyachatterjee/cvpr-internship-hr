#This is the code for getting the image of online handwriting recognition from the coordinates of strokes of the input pen recorded by the computer screen in HDF file.
import h5py
from PIL import Image
from PIL import ImageDraw as id
import numpy as np
#f = h5py.File("data\Test_resamp", "r")

def read(path):
	f=h5py.File(path)
	keys=list(f.keys())
	total=len(keys)
	for t in range(total):        #for all samples
		sample=f.get(keys[t])
		sampleid=sample.attrs["SampleID"]
		box=np.asarray(sample.attrs["Box"],dtype="int16")
		i=box[0]-box[1]+30
		j=box[2]-box[3]+30
		im = Image.new("RGB", (i,j), "white")
		draw = id.Draw(im)
		num_strokes=sample.attrs["Nb_Strokes"]
		for strokes in range(num_strokes):    ##for all strokes in one sample
			stroke=sample.get("S"+str(strokes))   
			stroke=np.array(stroke)
			name=sampleid.decode('utf-8')
			#dset = f.create_dataset("Strokes", (num_strokes,1), dtype='i')

			for ib in range(stroke.shape[0]-1):     ##for all points in one stroke
				a=stroke[ib,0]
				b=stroke[ib,1]
				c=stroke[ib+1,0]
				d=stroke[ib+1,1]
				
				draw.line((a,b, c,d), width=5,fill=0 )
				
			#im.show()
		im.save('/home/cvpr/Deya/results/'+str(name)+'.jpg')
				
read("data/Test_resamp")
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
		
	folder = f.get(dta)
	for strokes in folder:
	#print (data.attrs[strokes])
		stroke=folder.get(strokes)
		stroke=np.array(stroke)
		#print(strokes.attrs["SampleID"])
		for i in range(stroke.shape[0]):
			a=stroke[i,0]
			b=stroke[i,1]
			c=stroke[i+1,0]
			c=stroke[i+1,1]
			draw = id.Draw(im)
			draw.line((a,b, c,d), fill=300)
			#im.show()
			im.save("SampleeID.jpg")
		
"""
