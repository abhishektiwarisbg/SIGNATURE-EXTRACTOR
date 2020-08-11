import color_correlation
import cv2
import dewapper
import signature_extractor
import unsharpen


def main_func():
    # img1 = f
    # img2 = cv2.imread('sign2.jpg')
    # a = img1.shape
    # b, c = a[0], a[1]
    # size = (c, b)
    # resized = cv2.resize(img2, size)

    source_image =cv2.imread("input.jpg")
    print("1")
    cv2.imshow("here",source_image)
    print("2")
    try:
        img = signature_extractor.extract_signature(cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY))
        print("3")
    except Exception as e:
        return e
    try:
        unsharpen.unsharpen_mask(img)
        print("4")
    except Exception as e:
        return e
    try:
        img = color_correlation.funcBrightContrast(img)
        print("5")
    except Exception as e:
        return e
    cv2.imwrite('output.jpg', img)



