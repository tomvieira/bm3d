from skimage import io, img_as_float, img_as_uint
import bm3d
import cv2 as cv
import numpy as np
img = io.imread('ruim.png', as_gray=True)
img_ruim = np.array(img.copy(), dtype=float)

img_sem_ruido = bm3d.bm3d(img_ruim, sigma_psd=0.2,
                          stage_arg=bm3d.BM3DStages.ALL_STAGES)
io.imsave('boa.png', img_sem_ruido)
cv.imshow('Ruim', img_ruim)
cv.imshow('Sem ruido', img_sem_ruido)
cv.waitKey(0)
cv.destroyAllWindows()
