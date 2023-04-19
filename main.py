import cv2
import os
from imgCutting import imgCutting

filepath = "./img/" #檔案路徑
savepath = "./output/" #儲存路徑
saveName = "cutting_img.jpg" #儲存檔案名稱
magnification = 1.4 #放大倍率

#mode 0:顯示圖片 1:儲存圖片
mode = 1

if ".jpg" in filepath or ".png" in filepath:
    img, isCutting = imgCutting(filepath, magnification)
    
    if mode ==0 :
        print("是否檢測到貓臉:" + str(isCutting))
        cv2.imshow("image", img)
        c = cv2.waitKey(10)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        if isCutting == True:
            cv2.imwrite(savepath + saveName ,img )
    
else: 
    fileList = os.listdir(filepath)
    for file in fileList:
        singleFilePath = filepath + file
        saveName = savepath + file
        img, isCutting = imgCutting(singleFilePath, magnification)
        if mode ==0 :
            print("是否檢測到貓臉:" + str(isCutting))
            cv2.imshow("image", img)
            c = cv2.waitKey(10)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            if isCutting == True:
                cv2.imwrite(saveName ,img )
        




