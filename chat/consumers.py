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

# import json
# from channels.generic.websocket import WebsocketConsumer
# from PIL import Image
# import base64, io, wave
# import face_recognition
# import speech_recognition as sr
# from pydub import AudioSegment
# from pyaudio import PyAudio
# import numpy as np

# r=sr.Recognizer()
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass
 
#     def receive(self, bytes_data):
#         # print(bytes_data)
        
#         # b64=base64.b64encode(bytes_data)
#         filename='audio'+'.wav'
#         data=open(filename,'wb')
#         data.write(bytes_data)
#         data.close

#         r=sr.Recognizer()
#         harvard=sr.AudioFile(filename)
#         with harvard as source:
#             audio = r.record(source)
#             print(r.recognize_google(audio))

#         # data, samplerate = sf.read('existing_file.wav')
#         # sf.write('4.flac', data=bytes_data, samplerate=44100,)
        
#         # print(wave.open("1.wav", 'r').getparams())
#         # with open('3.wav', mode='wb') as f:
#         #     f.write(bytes_data)
#         # stream = ffmpeg.input('2.wav')
#         # stream = ffmpeg.hflip(stream)
#         # stream = ffmpeg.output(stream, 'output.mp4')
#         # ffmpeg.run(stream)
#         # with io.open('3.wav', "rb") as audio_file:
            
#         #     content = audio_file.read()
#             # print(content)
            
        

#         # with sr.WavFile('2.flac') as source: # use "test.wav" as the audio source
        

#         text = speech_recog(bytes_data.decode(''))
#         # self.send(text_data=json.dumps({
#         #     'message': text
#         # }))
# def speech_recog(audio):
#     r=sr.Recognizer()
#     with sr.AudioFile(audio) as source:
#         audio_data = r.record(source)

#         text = r.recognize_google(audio_data)
#         print("You said: {}".format(text))
#         return text

        

