import json
from channels.generic.websocket import WebsocketConsumer
from PIL import Image
import base64, io
import face_recognition
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data_json)
        b64str = text_data_json['message']
        
        b64str=b64str.strip('data:image/jpeg;base64')
        # print(b64str)
        imgdata = base64.b64decode(b64str)
        im=Image.open(io.BytesIO(imgdata))
        im.save("im.jpeg")
                
        data = facerecognition("im.jpeg")
        self.send(text_data=json.dumps({
            'message': data
        }))


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
