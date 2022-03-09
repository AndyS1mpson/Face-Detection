import cv2


def template_matching(method) -> None:
      image = cv2.imread("images/img.jpg")
      img = image.copy()
      template = cv2.imread("images/template.jpg", 0)
      img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      meth = eval(method)
      w, h = template.shape[::-1]
      
      # Apply template Matching
      res = cv2.matchTemplate(img_gray,template,meth )
      
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
      # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
      if meth  in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
          top_left = min_loc
      else:
          top_left = max_loc
      bottom_right = (top_left[0] + w, top_left[1] + h)
      cv2.rectangle(img, top_left, bottom_right, 255, 2)
      cv2.imwrite("images/result.jpg", img)


def viola_jones() -> None:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    image = cv2.imread("images/img.jpg")
    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imwrite("images/result.jpg", img)
