from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def dct(data):
    M, N, channels = data.shape

    dct_result = np.zeros_like(data, dtype=float)

    for c in range(channels):
        for i in range(0, M, 8):
            for j in range(0, N, 8):
                block = data[i:i + 8, j:j + 8, c]

                dct_block = np.zeros((8, 8), dtype=float)

                for u in range(8):
                    cu = 1 if u == 0 else np.sqrt(2) / 2

                    cos_u = np.cos((2 * np.arange(8) + 1) * u * np.pi / 16)

                    for v in range(8):
                        cv = 1 if v == 0 else np.sqrt(2) / 2

                        cos_v = np.cos((2 * np.arange(8) + 1) * v * np.pi / 16)

                        dct_block[u, v] = cu * cv * np.sum(block * np.outer(cos_u, cos_v))

                dct_result[i:i + 8, j:j + 8, c] = dct_block

    return dct_result


CL = [(1 + sqrt(3)) / (4 * sqrt(2)),
      (3 + sqrt(3)) / (4 * sqrt(2)),
      (3 - sqrt(3)) / (4 * sqrt(2)),
      (1 - sqrt(3)) / (4 * sqrt(2))]

def hpf_coeffs(CL):
    N = len(CL)
    CH = [(-1) ** k * CL[N - k - 1] for k in range(N)]
    return CH


def pconv(data, CL, CH, delta=0):

    assert len(CL) == len(CH)

    N = len(CL)
    M = len(data)
    out = []

    for k in range(0, M, 2):
        sL = 0
        sH = 0

        for i in range(N):
            sL += data[(k + i - delta) % M] * CL[i]

            sH += data[(k + i - delta) % M] * CH[i]

        out.append(sL)
        out.append(sH)

    return out


def wavelet_to_image(image):
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    red_result = pconv(red_channel.flatten(), CL, hpf_coeffs(CL))
    green_result = pconv(green_channel.flatten(), CL, hpf_coeffs(CL))
    blue_result = pconv(blue_channel.flatten(), CL, hpf_coeffs(CL))

    red_result = np.array(red_result).reshape(red_channel.shape)
    green_result = np.array(green_result).reshape(green_channel.shape)
    blue_result = np.array(blue_result).reshape(blue_channel.shape)

    result_image = np.stack([red_result, green_result, blue_result], axis=-1)

    return result_image


matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0, 255, 0, 0],
    [0, 255, 63, 127, 127, 63, 255, 0],
    [0, 0, 127, 0, 0, 127, 0, 0],
    [0, 0, 127, 0, 0, 127, 0, 0],
    [0, 255, 63, 127, 127, 63, 255, 0],
    [0, 0, 255, 0, 0, 255, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
matrix_flattened = [item for row in matrix for item in row]
out = pconv(matrix_flattened, CL,hpf_coeffs(CL))
for i in range(0, len(out), 8):
    print([out[i], out[i + 1], out[i + 2], out[i + 3], out[i + 4], out[i + 5], out[i + 6], out[i + 7]])



#image = Image.open('anime256x256.jpg')

#start_image = np.array(image,dtype=np.uint8)


#dct_image = dct(start_image)
#dct_image_scaled = ((dct_image - dct_image.min()) / (dct_image.max() - dct_image.min()) * 255).astype(np.uint8)
#dct_image_final = Image.fromarray(dct_image_scaled[:, :, 0], 'L')

#wavelet_image=wavelet_to_image(start_image);
#wavelet_image_scaled = ((wavelet_image - wavelet_image.min()) / (wavelet_image.max() - wavelet_image.min()) * 255).astype(np.uint8)
#wavelet_image_final = Image.fromarray(wavelet_image_scaled[:, :, 0], 'L')




#plt.imshow(start_image, cmap='gray')
#plt.axis('off')
#plt.show()

#plt.imshow(dct_image_final, cmap='gray')
#plt.axis('off')
#plt.show()
#dct_image_final.save("dct_image_final.jpg")

#plt.imshow(wavelet_image_final, cmap='gray')
#plt.axis('off')
#plt.show()
#wavelet_image_final.save("wavelet_image_final.jpg")