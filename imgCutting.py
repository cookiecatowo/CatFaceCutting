import cv2


def imgCutting(filepath, magnification): 
    
    img = cv2.imread(filepath)
    isCutting = False
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    classifier = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
    color = (0, 255, 0)  # 定义绘制颜色
    
    faceRects = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1, minSize=(75, 75))

    if len(faceRects):  # 大于0则检测到猫脸
        # print ("檢測到貓臉")
        isCutting = True
        for faceRect in faceRects:  # 单独框出每一张猫脸
            x, y, w, h = faceRect
            centerX = x + 0.5*w
            centerY = y + 0.5*h
            w = int(w*magnification)
            h = int(h*magnification)
            x = int(centerX-0.5*w)
            y = int(centerY-0.5*h)
            if x <0 : x = 0
            if y <0 : y = 0
            # 框出猫脸
            # cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
            cut_img = img[y:y+h, x:x+w]

    if isCutting == True:
        return cut_img, isCutting
    else:
        return img, isCutting
