#!/usr/bin/env python
# coding: utf-8

# # Image to Pencil Sketch with Python:
# 
# We need to read the image in RBG format and then convert it to a grayscale image. This will turn an image into a classic black and white photo. Then the next thing to do is invert the grayscale image also called negative image, this will be our inverted grayscale image. Inversion can be used to enhance details. Then we can finally create the pencil sketch by mixing the grayscale image with the inverted blurry image. This can be done by dividing the grayscale image by the inverted blurry image. Since images are just arrays, we can easily do this programmatically using the divide function from the cv2 library in Python

# In[ ]:


import cv2
import matplotlib.pyplot as plt


img_Dog=cv2.imread("C:\\Users\\Dorababu Pudi\\Desktop\\Dog.jpg")



# In[4]:


plt.figure(figsize=(6, 8))
plt.imshow(img_Dog)
plt.axis("off")
plt.title("Original Image (BGR format)")
plt.show


# In[5]:


img_rgb = cv2.cvtColor(img_Dog, cv2.COLOR_BGR2RGB)


# In[6]:


gray = cv2.cvtColor(img_Dog, cv2.COLOR_BGR2RGB)
cv2.imshow('mycat',gray)
plt.imshow(img_Dog)


# In[7]:


invert_img = cv2.bitwise_not(gray)
plt.imshow(img_Dog)


# In[8]:


blur_img = cv2.GaussianBlur(invert_img,(21,21),0)
plt.imshow(img_Dog)


# In[9]:


invertedblur = cv2.bitwise_not(blur_img)
plt.imshow(img_Dog)


# In[10]:


sketch_filter=cv2.divide(gray,invertedblur,scale=256.0)
plt.imshow(img_Dog)


# In[ ]:


cv2.imshow('cat.jpg',sketch_filter)
cv2.waitKey(0)
plt.imshow(img_Dog)


# In[ ]:





# In[ ]:




