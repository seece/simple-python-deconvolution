# Python deconvolution example


First install dependencies with

	pip install numpy scikit-image matplotlib
	
and then run

	python deconv.py jazz.png psf5.png 0.0025

![](psfplot.png)

*The point spread function (PSF).*

![](jazz.png)
![](out.png)
![](out_clipped.png)

*Input image (left) and deconvolution output (middle) and clipped output (right.)*




