from skimage import io, img_as_float
import bm3d
import cv2 as cv
import numpy as np

img_ruim = img_as_float(io.imread('ruim.png', as_gray=True))

dm3d_ruido = bm3d.bm3d(img_ruim, sigma_psd=0.2,
                       stage_arg=bm3d.BM3DStages.ALL_STAGES)
cv.imshow('img_ruim', img_ruim)
cv.imshow('dm3d_ruido_clean', dm3d_ruido)
dm3d_ruido = dm3d_ruido.astype(np.uint8)
cv.imwrite('boa.png', dm3d_ruido)
cv.waitKey(0)
cv.destroyAllWindows()

