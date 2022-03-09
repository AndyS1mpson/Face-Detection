import cv2
import matplotlib.pyplot as plt
import numpy as np


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
      #plt.subplot(122),plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
