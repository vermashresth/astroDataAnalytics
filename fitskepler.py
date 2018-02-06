from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import glob
import pickle
from multiprocessing import Pool
import pandas as pd

def readflux(path):
	hdu_list = fits.open(path)
	lc=hdu_list[1].data
	flux=[lc[i][3] for i in range(len(lc))]
	time=[lc[i][0] for i in range(len(lc))]

	return time
	#plt.scatter(time,flux)
	#plt.show()
trainpercent=.8

no=glob.glob("/media/petrichor/data/bigdatafiles/public_c1_long_1/*")
print(len(no))
yes=glob.glob("/media/petrichor/data/bigdatafiles/public_c1_long_2/*")
print(len(yes))

notrain=no[:int(len(no)*trainpercent)]
notest=no[int(len(no)*trainpercent):]

yestrain=yes[:int(len(yes)*trainpercent)]
yestest=yes[int(len(yes)*trainpercent):]
#readandplot("/media/petrichor/data/bigdatafiles/public_c1_long_2/ktwo201201917-c01_llc.fits")

def loopandgetflux(paths):
	fluxlist=[]
	print("start reading")
	with Pool(10) as p:
		fluxlist=p.map(readflux,paths)
	print("end reading")
	return fluxlist

def pickleflux(trutrain,faltrain,trutest,faltest):
	print("trutrain")
	truxtrain=loopandgetflux(trutrain)
	print("faltrain")
	falxtrain=loopandgetflux(faltrain)
	print("done reading train")
	train=pd.DataFrame(truxtrain+falxtrain)
	labeltrain=[[1 if i <len(truxtrain) else 0 for i in range(len(truxtrain+falxtrain))]]
	train.DataFrame.to_pickle("train")

	print("trutest")
	truxtest=loopandgetflux(trutest)
	print("faltest")
	falxtest=loopandgetflux(faltest)
	print("done reading test")
	test=pd.DataFrame(truxtest+falxtest)
	labeltest=[[1 if i <len(truxtest) else 0 for i in range(len(truxtest+falxtest))]]
	test.DataFrame.to_pickle("test")

pickleflux(yestrain,notrain,yestest,notest)





	
