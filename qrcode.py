#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qrcode


# In[2]:


from PIL import Image
data = "https://michaelportfolio1.netlify.app/"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_dat(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")
image.save("qr_code.png")
image.open("qr_code.png")


# In[3]:


from PIL import Image
data = "https://michaelportfolio1.netlify.app/"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_dat(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")
image.save("qr_code.png")
image.open("qr_code.png")


# In[4]:


from PIL import Image
data = "https://michaelportfolio1.netlify.app/"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_dat(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")
image.save("qr_code.png")
image.open("qr_code.png")


# In[5]:


get_ipython().system('pip install qrcode[pil]')


# In[8]:


import qrcode

# Define the data you want to encode
data = "https://michaelportfolio1.netlify.app/"

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)

# Add the data to the QRCode
qr.add_data(data)
qr.make(fit=True)

# Create an image using the QRCode instance
image = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
image.save("qr_code.png")

# Open the generated QR code image
image.show()


# In[7]:


get_ipython().system('pip install Pillow')


# In[9]:


import qrcode

# Define the data you want to encode
data = "https://michaelportfolio1.netlify.app/"

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)

# Add the data to the QRCode
qr.add_data(data)
qr.make(fit=True)

# Create an image using the QRCode instance
image = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
image.save("qr_code.png")

# Open the generated QR code image
image.show()


# In[ ]:




