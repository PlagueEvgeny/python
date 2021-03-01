import numpy as np
from PIL import Image, ImageFilter

image_name = 'Zamok.jpg'
image = Image.open(image_name)
image_np = np.array(image)
print(image_np.size, image_np.shape, image.format, image.mode)
image_np_conv = image_np
print(image_np_conv[:, :, 0].mean(), image_np_conv[:, :, 1].mean(),
      image_np_conv[:, :, 2].mean())
image_np_conv[:, :, 2][image_np_conv[:, :, 2] <= 215] += 40
# image_np_conv[:, :, 0][image_np_conv[:, :, 0] <= 200] += 55
# image_np_conv[:, :, 0] = 196
# image_np_conv[:, :, 1] = 139
# image_np_conv[:, :, 2] = 175

# new_image = image.filter(ImageFilter.SHARPEN)


new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'Zamok_conv.jpg'
new_image.save(save_name)

new_image_filter = image.filter(ImageFilter.DETAIL)
save_name = 'Zamok_filter.jpg'
new_image_filter.save(save_name)



