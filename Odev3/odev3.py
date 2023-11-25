import cv2
import numpy as np

image = cv2.imread('image/pirinc.jpeg')

# Görüntü gri seviyeye dönüştürüldü.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#eşikleme
ret, thresh = cv2.threshold(gray_image, 150,255, cv2.THRESH_BINARY)

#morfolojik işlemler
kernel = np.ones((2,2), dtype=np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
background = cv2.erode(opening,kernel,iterations=1)

#Sayma ve etiketleme fonksiyonları
_, markers = cv2.connectedComponents(background)
count = np.max(markers)


cv2.imshow("Orijinal Goruntu", image)
cv2.imshow("Esiklenmis Goruntu", background)


print(f"Pirinç sayısı: {count}")

cv2.waitKey(0)
cv2.destroyAllWindows()


