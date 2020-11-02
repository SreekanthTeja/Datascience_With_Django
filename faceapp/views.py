from django.shortcuts import render
from PIL import Image
import io
import base64
import face_recognition
from django.http import HttpResponse
import json
from .forms import UploadImageForm
def home(request):
    print(request.GET)
    return render(request,'index.html')
def imageviewform(request):
    if request.method=='POST':
        form=UploadImageForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            print('This is valid!')
            # print(form.cleaned_data['image'])
            img=form.cleaned_data['image']
            op=facerecognition(img)
            return render(request,'imagesubmit.html',{'op':json.dumps(op)})
        return render(request,'imagesubmit.html',{'form':form})
    form=UploadImageForm()
    return render(request,'imagesubmit.html',{'form':form})
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
    

    

            
            


            


    

        
        
    

        





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    

    


