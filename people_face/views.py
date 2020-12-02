from django.shortcuts import render
from .forms import ImageForm
import cv2
import numpy as np
from PIL import Image
import face_recognition
import json
import io
import base64

def imageform(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        # print(request.POST)
        if form.is_valid():
            # print('This is valid!')
            # print(form.cleaned_data['image'])
            img1=form.cleaned_data['image1']
            img2=form.cleaned_data['image2']
            stiching=merge_images(img1,img2)
            stiching.save("fc1.jpg")
            pic="fc1.jpg"
            dp=facerecognition(pic)
            # print(dp)
            return render(request,'face.html',{'dp':json.dumps(dp)})
        return render(request,'face.html',{'form':form})
    form=ImageForm()
    return render(request,'face.html',{'form':form})

def merge_images(file1,file2):

    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result
    
img="fc1.jpg"
def facerecognition(img):
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(image)
    # print("I found {} face(s) in this photograph.".format(len(face_locations)))
    img_list=[]
    for face in face_locations:
        top, right, bottom, left = face
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        blob=io.BytesIO()
        pil_image.save(blob,format='JPEG')
        # pil_image.show()
        img_byte=base64.b64encode(blob.getvalue())
        img_str=img_byte.decode(encoding='utf-8')
        img_list.append(img_str)
    return img_list
    









