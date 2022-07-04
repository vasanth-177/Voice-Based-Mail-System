from tkinter import *
import os
from stat import filemode
import time
from uuid import SafeUUID
import playsound
import speech_recognition as sr
import yagmail
from gtts import gTTS
import speech_recognition as sr
import smtplib
# import pyaudio/
# import platform
# import sys
# import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os
import time
from email.header import decode_header
import webbrowser

def speak(t):
    tts = gTTS(text=t, lang='en')
    ttsname=("hello.mp3") 
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

def compose(e):
            print("what is your subject")
            speak("what is your subject ")

            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                s=""
            try:
                s=r.recognize_google(audio)
                print(s)
                
            except Exception as e:
                print("Exception :"+str(e))

            print("what is your message")
            speak("what is your message ")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                m=""
            try:
                m=r.recognize_google(audio)
                print(m)
               
            except Exception as e:
                print("Exception :"+str(e))

            #Getting sender Email
            print("Sender mail address:")
            speak("Sender mail address:")

            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                m1=""
            try:
                m1=r.recognize_google(audio)
                print(m1)
            except Exception as e:
                print("Exception :"+str(e))

            #Modifying Sender Email address
            m1 = m1.lower()
            pos=m1.rindex('at')
            m1 = m1[:pos] + '@' + m1[pos+2:]
            m1=m1.replace(" ","")
            print(m1)
           
        
            sender=yagmail.SMTP('vasanthproj17@gmail.com','wvqouzrjpcfvxils')
            sender.send(to=m1,subject=s,contents=m)
            print("Mail sent Successfully")
            speak("Mail sent successfully")
            disp_tf.insert(0, f'Subject {s} .')
            disp_tf2.insert(0, f'message {m} .')
            disp_tf1.insert(2, f'Sender mail {m1} .')

def check(e):
    server = "imap.gmail.com"
    imap = imaplib.IMAP4_SSL(server)

    # intantiate the username and the password
    username = "vasanthproj17@gmail.com"
    password = "wvqouzrjpcfvxils"

    # login into the gmail account
    imap.login(username, password)

    # select the e-mails
    res, messages = imap.select('"inbox"')

    # calculates the total number of inbox messages
    messages = int(messages[0])

    # determine the number of e-mails to be fetched
    n = 3
    
    dict={}
    l2=[]

    # iterating over the e-mails
    speak("the first  unread messages are @")
    for i in range(messages, messages - n, -1):
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                l2=[]
                m = email.message_from_bytes(response[1])
                # speak("message is from ")
                key=m["From"]
                # disp_tf.insert(0, f'from {f} .')
                # speak(m["From"])
                if (m["Subject"] != ""):
                    # speak("no subject")
                    # m_s=m["Subject"]
                    # disp_tf2.insert(0, f'NO subject .')
                    l2.append(m["Subject"])
                   
                else:
                    # speak(m["Subject"])
                    l2.append(0)
                # speak("The main content is:")
                cont_type = m.get_content_maintype()
                if cont_type == 'multipart':
                    content_1, content_2 = m.get_payload()
                     # print(content_1.get_payload())
                    v=content_1.get_payload()
                    size = len(v)
                        # Slice string to remove last 3 characters from string
                    v = v[:size - 2]
                    l2.append(v)
                    # c=content_1.get_payload()
                    # disp_tf1.insert(0, f'msg {c} .')
                    # speak(content_1.get_payload())
                # else:
                #     t=m.get_payload()
                #     disp_tf1.insert(2, f'msg {t} .')
                #     speak(m.get_payload())
        # break
                dict[key]= l2
        # print(dict)
    i=1
    for users in dict:
                s=str(i)+"."+users
                print(s)
                speak(s)
                i+=1
    print("Choose the user to read their mail:")
    speak("Choose the user to read their mail:")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        c=""
    try:
        c=r.recognize_google(audio)
        print(c)
    except Exception as e:
        print("Exception :"+str(e))

    if c == '1' or c == 'One' or c == 'one':
        c=0
    elif c == '2' or c == 'tu' or c == 'two' or c == 'Tu' or c == 'to' or c == 'To':
        c=1
    else:
        c=2
    res = list(dict.keys())
    l1=list(dict[res[c]])
    print("From")
    speak("From")
    print(res[c])
    speak(res[c])
    disp_tf.insert(0, f'from {res[c]} .')
    for i in range(0,2):
            if(i==0):
                if(l1[0]==0):
                   print("No subject")
                   speak("No subject")
                   disp_tf2.insert(0, f'NO subject .')
                else:
                   print("Subject:")
                   speak("Subject:")
                   print(l1[0])
                   speak(l1[0])
                   disp_tf2.insert(0, f'Subject {l1[0]} .')
            else:
                print("Content:")
                speak("Content:")
                print(l1[1])
                speak(l1[1])
                disp_tf1.insert(2, f'msg {l1[1]} .')

def handler(e):
    print("Options available")
    speak("Options available")
    print("1.To compose a mail kindly press enter ") 
    speak("1.To compose a mail kindly press enter") 
    print("2.To Check Inbox kindly press space bar") 
    speak("2.To Check Inbox kindly press space bar") 
    print("3.Exit")  
    speak("3.Exit")
    return 





ws = Tk()
ws.title('Voice Based Mail System')
ws.geometry('400x300')
ws.config(bg='#0f4b6e')

#name_tf = Entry(ws)
#descipline_tf = Entry(ws)
name_lbl = Label(
    ws,
    text='1.To compose a mail',
    bg='#0f4b6e',
    fg='white'
)


descipline_lbl = Label(
    ws,
    text='2.kindly press space bar to check inbox',
    bg='#0f4b6e',
    fg='white'
)

name_lbl.pack()
#name_tf.pack()
descipline_lbl.pack()
#descipline_tf.pack()

'''btn = Button(
    ws,
    text='read from inbox',
    relief=SOLID,
    command=f
)
btn.pack(pady=10)
'''
disp_tf = Entry(
    ws,
    width=380,
    font=('Arial', 14)
)
disp_tf.pack(padx=10, pady=10)
disp_tf2 = Entry(
    ws,
    width=380,
    font=('Arial', 14)
)
disp_tf2.pack(padx=10, pady=10)
disp_tf1 = Entry(
    ws,
    width=380,
    font=('Arial', 14)
)
disp_tf1.pack(padx=10, pady=10)

ws.bind('<Motion>',handler)
ws.bind('<Return>',compose)
ws.bind('<space>',check)

ws.mainloop()