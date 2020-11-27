"""
=========================================
Build Clear images from Distorted images
=========================================

"""

from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float, img_as_ubyte
from skimage import io
import numpy as np


image = img_as_float(io.imread("Lena-Noisy-image.png")).astype(np.float32)

# estimate the noise standard deviation from the noisy image
sigma_est = np.mean(estimate_sigma(image, multichannel=True))

print("estimated noise standard deviation = {}".format(sigma_est))

#Defining a dictionary for the input parameters to Denoising Algorithm
patch_kw = dict(patch_size=5,      # 5x5 patches
                patch_distance=6,  # 13x13 search area
                multichannel=True)


denoise_image = denoise_nl_means(image, h=1.15 * sigma_est, fast_mode=False,
                                **patch_kw)

denoise_image_as_8byte = img_as_ubyte(denoise_image)

#Save the output to current directory
io.imsave("Denoised-Output-Image.png", denoise_image_as_8byte)

