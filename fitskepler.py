from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def readandplot(path):
	hdu_list = fits.open(path)
	lc=hdu_list[1].data
	flux=[lc[i][3] for i in range(len(lc))]
	time=[lc[i][0] for i in range(len(lc))]

	plt.scatter(time,flux)
	plt.show()

readandplot("/media/petrichor/data/bigdatafiles/public_c1_long_2/ktwo201201917-c01_llc.fits")