import cv2
import numpy as np
from matplotlib import pyplot as plt

im=cv2.imread('image/pussi.png')
img=cv2.resize(im,(500,400))
b,g,r=cv2.split(img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Histogram=cv2.calcHist(gray,[0],None,[256],[0,256])
cv2.imshow("image",gray)
plt.plot(Histogram)
plt.title("gray image")
plt.show()
cv2.waitKey(1)
cv2.destroyAllWindows()

hist=cv2.calcHist(b,[0],None,[256],[0,256])
hist1=cv2.calcHist(g,[0],None,[256],[0,256])
hist2=cv2.calcHist(r,[0],None,[256],[0,256])
stk1=np.hstack((b,g,r))
cv2.imshow("spilt",stk1)
plt.plot(hist,'b')
plt.plot(hist1,'g')
plt.plot(hist2,'r')
plt.title("b,g,r:spilt")
plt.show()
cv2.waitKey(1)
cv2.destroyAllWindows()


eqhist=cv2.equalizeHist(gray)
clahe=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clah=clahe.apply(gray)
eqlhist=cv2.calcHist(eqhist,[0],None,[256],[0,256])
eqclah=cv2.calcHist(clah,[0],None,[256],[0,256])
stk2=np.hstack((eqhist,clah))
cv2.imshow("equalize Histogram",stk2)
plt.plot(eqlhist,'b')
plt.plot(eqclah,'g')
plt.title("equalize:Hist,clahe")
plt.show()
cv2.waitKey(1)
cv2.destroyAllWindows()

eqhistB=cv2.equalizeHist(b)
eqhistG=cv2.equalizeHist(g)
eqhistR=cv2.equalizeHist(r)
eqlhistB=cv2.calcHist(eqhistB,[0],None,[256],[0,256])
eqlhistG=cv2.calcHist(eqhistG,[0],None,[256],[0,256])
eqlhistR=cv2.calcHist(eqhistR,[0],None,[256],[0,256])
stk3=np.hstack((eqhistB,eqhistG,eqhistR))
cv2.imshow("EQUALIZE Histogram",stk3)
coleqHist=cv2.merge((eqhistB,eqhistG,eqhistR))
cv2.imshow("cleqhist",coleqHist)
plt.plot(eqlhistB,'b')
plt.plot(eqlhistG,'g')
plt.plot(eqlhistR,'r')
plt.title("BGR EQUALIZE:EQUALIZE")
plt.show()
cv2.waitKey(1)
cv2.destroyAllWindows()

clahB=clahe.apply(b)
clahG=clahe.apply(g)
clahR=clahe.apply(r)
B_G_R=cv2.merge((clahB,clahG,clahR))
eqclhB=cv2.calcHist(clahB,[0],None,[256],[0,256])
eqclhG=cv2.calcHist(clahG,[0],None,[256],[0,256])
eqclhR=cv2.calcHist(clahR,[0],None,[256],[0,256])
stack_p1=np.hstack((clahB,clahG,clahR))
cv2.imshow("BGR:clahe",stack_p1)
cv2.imshow("colorHistClah",B_G_R)
plt.plot(eqclhB,'b')
plt.plot(eqclhG,'g')
plt.plot(eqclhR,'r')
plt.title("B G R EQUALIZE:clahe")
plt.show()
cv2.waitKey(1)
cv2.destroyAllWindows()
