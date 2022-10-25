import speech_recognition as sr
import pyttsx3 as tts
import webbrowser as wbb
import cv2
from PyDictionary import PyDictionary
from time import *

dictionary = PyDictionary()
corpus=[]
str=""

'''import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer'''
import pytesseract
converter=tts.init()
converter.setProperty("rate",150)
s="welcome to nayan.ai"
converter.say(s)
converter.runAndWait()

s1="say google to open google"
converter.say(s1)
converter.runAndWait()


s2="say image to open camera for image recognition"
converter.say(s2)
converter.runAndWait()

s3="say music to play music"
converter.say(s3)
converter.runAndWait()
def getvoice():
   l=[]
   corpus=[]
   v=sr.Recognizer()
   with sr.Microphone() as source:
      voice=v.listen(source)
      said=""

      try:
         said=v.recognize_google(voice)
         print(said)
         converter.say(said)
         converter.runAndWait()
         if said=="Google":
            wbb.open("https://google.com")
         elif said=="music":
            wbb.open("https://www.youtube.com/watch?v=QB9EB8mTKcc&list=RDQB9EB8mTKcc&start_radio=1")
         elif said=="image":
            vid=cv2.VideoCapture(0)
         elif said=="Instagram":
            wbb.open("https://www.instagram.com")
         elif said=="github":
            wbb.open("www.github.com")


        
            while True:
                 ret,frame=vid.read()
                 cv2.imshow("dk",frame)
               
                 cv2.imwrite("imtrying"+".png",frame)
                 img=cv2.imread("imtrying.png")
                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                 thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,3,6)
                 cv2.imshow('threshold',thresh)
                 cv2.waitKey(0)
                 name=pytesseract.image_to_string(thresh,lang='eng',config='--psm 11')
                 print("Name : ",name)
                 l =[]
                 l.append(name)
                 c = cv2.waitKey(1)
                 sleep(5)
                 print(l)
                 
                 #l[0].strip("\n")
                 
                 print(type(l[0]))
                 conv = l[0].replace('\n','')
                 print(conv)
                 break
                 converter.say(conv)
                 converter.runAndWait()
            
               
                  
         vid.release()


         
      except Exception as e:
         
         print("you have an error")


getvoice()

