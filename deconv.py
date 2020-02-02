import sys
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, data, restoration, io

if len(sys.argv) < 4:
    print("Usage: deconv.py INPUT_IMAGE POINT_SPREAD_IMAGE REGULARIZATON_WEIGHT")
    print("out.png and out.tiff will be written")
    sys.exit(1)

input_path = sys.argv[1]
psf_path = sys.argv[2]
regularization = float(sys.argv[3])

psf = color.rgb2gray(io.imread(psf_path))
psf /= np.sum(psf)

plt.figure()
plt.title('psf')
plt.imshow(psf)

img = io.imread(input_path) / 255.

img2 = np.zeros_like(img)

for chan in range(img.shape[2]):
    print(f"Channel {chan}...")
    img2[:, :, chan] = restoration.wiener(img[:, : , chan], psf, .0025)
    #deconvolved_img, _ = restoration.unsupervised_wiener(img, psf)

print(f"Input range: [{np.min(img)}, {np.max(img)}]")
print(f"Output range: [{np.min(img2)}, {np.max(img2)}]")

low = np.min(img2)
high = np.max(img2)
img2 = (img2 - low) / (high - low)

print(f"Normalized output range: [{np.min(img2)}, {np.max(img2)}]")

io.imsave('out.png', img2)
io.imsave('out.tiff', img2)

plt.figure()
plt.title('deconvolved')
plt.imshow(img2)
plt.figure()
plt.title('input')
plt.imshow(img)

# Comment this out if you don't want see the plots
plt.show()