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
    img2[:, :, chan] = restoration.wiener(img[:, : , chan], psf, regularization)
    #deconvolved_img, _ = restoration.unsupervised_wiener(img, psf)

print(f"Input range: [{np.min(img)}, {np.max(img)}]")
print(f"Output range: [{np.min(img2)}, {np.max(img2)}]")

clipped = np.clip(img2, 0., 1.)
low = np.min(img2)
high = np.max(img2)
normalized = (img2 - low) / (high - low)

print(f"Normalized output range: [{np.min(img2)}, {np.max(img2)}]")

io.imsave('out.png', normalized)
io.imsave('out_clipped.png', clipped)
io.imsave('out.tiff', normalized)

plt.figure()
plt.title('deconvolved')
plt.imshow(normalized)
plt.title('deconvolved (clipped range)')
plt.imshow(clipped)
plt.figure()
plt.title('input')
plt.imshow(img)

# Comment this out if you don't want see the plots
plt.show()