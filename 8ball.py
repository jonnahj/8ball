import time
import speech_recognition as sr
from playsound import playsound
import random
import pyttsx3
import re

def speak(data):
    import pyttsx3
    converter = pyttsx3.init()
    converter.setProperty('rate', 200)
    converter.setProperty('volume', 1)
    converter.say(data)
    converter.runAndWait()

def record():
    r = sr.Recognizer()
    speak("What do you wanna know today?")
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            data = r.recognize_google(audio)
    except:
        return ""
    return data

def answer(count):
        i = count
        question = record()
        print(question)
        if(question == "shut up"):
            return "done"
        if(re.search("nice$",question)!=None):
            nice= ["I love the way your eyes smile.","Jesus Loves you!","You are amazing just the way you are.","I love you."]
            n = random.randint(0,3)
            speak(nice[n])
            return "continue"
        if(question == ""):
            speak("I'm sorry, can you please repeat that?")
            return "continue"
        replies = ["Oh yeah!", "I'm gonna leave this up to you.", "You deserve it.","I'll kill you.", "Girl! Are you drunk?","That would look good on you.",
          "Don't even think about it.","Dont get me started on that.","Nope, nay, no and noooooooooooooooo"]
        replies_next = ["Roses are red violets are blue did i stutter when I already answered you!","Din't you hear me the first time.","You are a nice person and you deserve all the love in the world."
            ,"Oh yeah!", "I'm gonna leave this up to you.", "You deserve it.","I'll kill you.", "Girl! Are you drunk?","That would look good on you.",
          "Don't even think about it.","Dont get me started on that.","Nope, nay, no and noooooooooooooooo"]
        if(i == 0):
            n = random.randint(0,8)
            i += 1
            speak(replies[n])
        else:
            n = random.randint(0,11)
            speak(replies_next[n])
        return "continue"
    
import pygame
pygame.init()
background_colour = (255,255,255)
bg = pygame.image.load("ready.png")
(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('8Ball')
screen.fill(background_colour)
screen.blit(bg,(0,0))
pygame.display.flip()
running = True
i=0
while running:
    result = answer(i)
    if(i == 0):
        i = 1
    if(result == "done"):
        event=pygame.event.Event(pygame.QUIT, attr1='event')
        pygame.event.post(event)
        pygame.quit()
        exit()
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()