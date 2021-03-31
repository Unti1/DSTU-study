import cv2

image = cv2.imread('google.png')
# Функция для вывода изображения
def viewImg(image,name_image):
    cv2.imshow(name_image,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

viewImg(image,'1')
cropped = image[10:100,10:250]
viewImg(cropped,'hu')

output = image.copy()
cv2.rectangle(output,(2200,800),(1200,400),(0,255,255),10)
viewImg(output,"r")

cv2.putText(output,"Text",(400,500),cv2.FONT_HERSHEY_SIMPLEX,10,(0,0,250),5)
viewImg(output,'Картинка с текстом')
blur = cv2.GaussianBlur(cropped, (41,41), 0)
image[: cropped.shape[0], :cropped.shape[1]] = blur

viewImg(image,"Blur")

cv2.imwrite('img.png',image)