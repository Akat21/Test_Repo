import numpy as np
import matplotlib.pyplot as plt

def imgToFloat(img):
    if np.issubdtype(img.dtype, np.float32):
        return img
    else:
        return img/255.0
    
img = plt.imread('./lab4/high_q.jpg', format='jpg')
img = imgToFloat(img)

pallet8 = np.array([
        [0.0, 0.0, 0.0,],
        [0.0, 0.0, 1.0,],
        [0.0, 1.0, 0.0,],
        [0.0, 1.0, 1.0,],
        [1.0, 0.0, 0.0,],
        [1.0, 0.0, 1.0,],
        [1.0, 1.0, 0.0,],
        [1.0, 1.0, 1.0,],
])

pallet16 =  np.array([
        [0.0, 0.0, 0.0,], 
        [0.0, 1.0, 1.0,],
        [0.0, 0.0, 1.0,],
        [1.0, 0.0, 1.0,],
        [0.0, 0.5, 0.0,], 
        [0.5, 0.5, 0.5,],
        [0.0, 1.0, 0.0,],
        [0.5, 0.0, 0.0,],
        [0.0, 0.0, 0.5,],
        [0.5, 0.5, 0.0,],
        [0.5, 0.0, 0.5,],
        [1.0, 0.0, 0.0,],
        [0.75, 0.75, 0.75,],
        [0.0, 0.5, 0.5,],
        [1.0, 1.0, 1.0,], 
        [1.0, 1.0, 0.0,]
])

def colorFit(pixel, pallet):
    if(len(img.shape) < 3):
        pts = np.abs(pallet - pixel)
        return pallet[np.argmin(pts)]
    else:
        pts = np.abs(pallet - pixel)
        pts = np.linalg.norm(pts, axis=1)
        return pallet[np.argmin(pts)]

def kwant_colorFit(img, pallet):
    out_img = img.copy()
    height, width, dim = img.shape

    for i in range(height):
        for j in range(width):
            out_img[i, j] = colorFit(img[i, j], pallet)
    return out_img

q_img = kwant_colorFit(img, pallet8)
plt.imshow(q_img)
plt.show()