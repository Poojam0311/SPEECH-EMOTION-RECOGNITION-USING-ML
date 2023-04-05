import keras
import numpy as np
import librosa
import soundfile as sf
import tkinter as tk
from tkinter.filedialog import askopenfilename
import shutil
import os
import sys
from PIL import Image, ImageTk

import os
import random
import time
window = tk.Tk()

window.title("speech emotion")

window.geometry("500x510")
window.configure(background ="lightgreen")

title = tk.Label(text="Click below to choose audio file for testing the emotion....", background = "lightgreen", fg="Brown", font=("", 15))
title.grid()

def openphoto():
    
    fileName = askopenfilename(initialdir='C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\data-20220606T193218Z-001\\data\\', title='Select audio for analysis ',
                           filetypes=[('wav files', '.wav')])

    
    def audio():
        class modelPredictions:

            def __init__(self, path, file):
                self.path = path
                self.file = file

            def load_model(self):
                self.loaded_model = keras.models.load_model(self.path)
                #return self.loaded_model.summary()

            def predictEmotion(self):
                data, sr = librosa.load(self.file)
                mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sr, n_mfcc=40).T, axis=0)
                x = np.expand_dims(mfccs, axis=1)
                x = np.expand_dims(x, axis=0)
                predictedEmotion = self.loaded_model.predict(x)
                predict_classes=np.argmax(predictedEmotion,axis=1)

                print("The predicted emotion is : ", " ", self.convertclasstoemotion(predict_classes))


            @staticmethod
            def convertclasstoemotion(p):
                #predictions(int) to understandable emotion labeling
                label_conversion = {'0': 'neutral','1': 'calm','2': 'happy','3': 'sad','4': 'angry','5': 'fearful','6': 'disgust','7': 'surprised'}

                for key, value in label_conversion.items():
                    if int(key) == p:
                        label = value
    ##                    global label
                        if label =='neutral':
                            labelb = tk.Label(text='  STATUS : Neutral  ', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                        if label =='calm':
                            labelb = tk.Label(text='  STATUS : calm  ', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                        if label =='happy':
                            labelb = tk.Label(text='  STATUS : happy  ', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                        if label =='sad':
                            labelb = tk.Label(text='  STATUS : sad  ', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                        if label =='angry':
                            labelb = tk.Label(text='  STATUS : angry  ', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                        if label =='fearful':
                            labelb = tk.Label(text='  STATUS : fearful  ', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                        if label =='disgust':
                            labelb = tk.Label(text='  STATUS : disgust ', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                        if label =='surprised':
                            labelb = tk.Label(text='STATUS : surprised', background="white",
                                   fg="black", font=("", 15))
                            labelb.grid(column=0, row=4, padx=20, pady=20)
                            path="C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad"
                            files=os.listdir(path)
                            d=random.choice(files)
                            os.startfile("C:\\Users\\Romes\\Downloads\\speech\\speec to emotion_tkinter\\speec to emotion_tkinter\\sad\\" + d)
                            
                return label


        #Created the object p of class modelPredictions
        p1 = modelPredictions(path='CNN_Model.h5',file=fileName)
        p1.load_model()
        #called predictEmotion function to predict emotion type of input file
        p1.predictEmotion()
    button2 = tk.Button(text="analyse audio", command = audio)
    button2.grid(column=0, row=2, padx=10, pady = 10)



button1 = tk.Button(text="Choose file", command = openphoto)
button1.grid(column=0, row=1, padx=10, pady = 10)



window.mainloop()
