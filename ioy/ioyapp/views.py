from django.shortcuts import render
from django.http import HttpResponse
import cv2
from .yakiniku_camera_capture import capture_camera
from .yakiniku_service import YakinikuService

#import django.views import find_rect_of_target_color,capture_camera
# Create your views here.
"""
import cv2
image = cv2.imread('musume.jpg', 1)
cascade_path =  'C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)
face_cascade = cascade.detectMultiScale(image, 1.1, 3)
"""

#def index(request):
#    return render(request, "index.html")

def index(request):

    return render(request,'index.html',)         # テンプレートに渡すデータ

def cap(request):
    capture_camera()
    return render(request, 'cap.html',)
