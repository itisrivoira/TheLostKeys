import cv2
import numpy as np
from patchify import patchify, unpatchify

path = ""
risoluzione = 48
img = cv2.imread(path+"test.png")
patches_img = patchify(img, (risoluzione, risoluzione, 3), step=risoluzione)  # patches_img.shape = (14, 18, 1, 224, 224, 3)

for i in range(patches_img.shape[0]):
    for j in range(patches_img.shape[1]):
        single_patch_img = patches_img[i, j, 0, :, :, :]
        #cv2.rectangle(single_patch_img, (risoluzione, risoluzione), (0, 0), (0, 0, 255), 3)  # Draw something (for testing).
        if not cv2.imwrite(path+'Tiles/' + 'tile' + str(i).zfill(3) + str(j).zfill(3) + '.png', single_patch_img):  # Save as PNG, not JPEG for keeping the quality.
            raise Exception("Could not write the image") 

# Store an unpatchified reference for testing
# cv2.imwrite("unpatched_ref.png", unpatchify(patches_img, img.shape))

# Unpatchify
################################################################################

# Allocate sapces for storing the patches
#img = cv2.imread(path+"Room_Builder_48x48.png")  # Read test.jpg just for getting the shape
img = np.zeros_like(img)  # Fill with zeros for the example (start from an empty image).

# Use patchify just for getting the size. shape = (14, 18, 1, 224, 224, 3)
# We could have also used: patches = np.zeros((14, 18, 1, 224, 224, 3), np.uint8)
patches = patchify(img, (risoluzione, risoluzione, 3), step=risoluzione)

for i in range(patches.shape[0]):
    for j in range(patches.shape[1]):
        single_patch_img = cv2.imread(path+'Tiles/' + 'tile' + str(i).zfill(3) + str(j).zfill(3) + '.png')  # Read a patch image.
        if single_patch_img is None:
            raise Exception("Could not read the image") 
        patches[i, j, 0, :, :, :] = single_patch_img.copy()  # Copy single path image to patches

reconstructed_image = unpatchify(patches, img.shape)
cv2.imwrite("test1.png", reconstructed_image)