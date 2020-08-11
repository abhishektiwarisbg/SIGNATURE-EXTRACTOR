"""Adjust the brightness and contrast of an image."""
import cv2

contrast = 0
brightness = 0


def funcBrightContrast(img, bright=0):
    effect = apply_brightness_contrast(img, bright, contrast)
    return effect


def apply_brightness_contrast(input_img, brightness=255, contrast=127):
    brightness = 80
    contrast = 60
    if (brightness != 0):
        if (brightness > 0):
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        # calculating the alpha value
        alpha_c = f
        # set the gamma value
        gamma_c = 127*(1-f)
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
    return buf
