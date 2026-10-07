import cv2
import matplotlib.pyplot as plt

img = cv2.imread('test2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

average = cv2.blur(img, (5,5))
gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 5, 75, 75)

titles = ['Original Image', 'Average','Gaussian','Median','Bilateral Filter']
images = [img, average, gaussian,median,bilateral]

plt.figure(figsize = (12,8))
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()