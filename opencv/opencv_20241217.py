import cv2
img = cv2.imread("LTT.jpg")
print(img.shape)
cv2.imshow("LTT.jpg", img)
cv2.waitKey(0)
for row in range(225):
    for col in range(225):
        if row > 110 and row < 144 and col > 90 and col < 210:
            img[row][col] = [0, 0, 0]
cv2.imshow("LTT.jpg", img)
cv2.waitKey(0)