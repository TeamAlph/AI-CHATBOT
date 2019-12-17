# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:35:44 2019
@author: usman
"""

import sys
import time
from termcolor import colored,cprint
import re
import os
import subprocess
import webbrowser
import wx
import wikipedia
import wolframalpha
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
startdoyou='do you remember (.*)'
startiwant='i want (.*)'
stockprice='what (.*) stock prize (.*)'
webbrow='(.*) web browser (.*)'
openapp='(.*) open (.*)' 
playsong='(.*) play song (.*)'
perfect='(.*) efficiency (.*)'
help1='(.*) help (.*)'
time1=[]
memory = []
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
questions = ['How are you?','How are you doing?']
responses = ['Okay','I am fine']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]
f = open("C:\\Users\\usman\\3D Objects\\Ai Jarvis Project\\memory.txt", "a")

class MyFrame(wx.Frame):
  
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="kinlab project")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am kinlab How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
    def replace_pronouns(message):

        message = message.lower()
        if ' me ' in message:
        
            return  re.sub('me', 'you',message)
        if ' my ' in message:
        
            return re.sub('my', 'your',message)
        if ' your ' in message:
        
            return re.sub('your', 'my',message)
        if ' you ' in message:
        
            return re.sub('you', 'me',message)
        if ' wolform' in message:
        
            return re.sub('wolform', '.',message)

        return message
    def OnEnter(self, event):
        start = time.time()
        input = self.txt.GetValue()
        input = input.lower()
        f.write('--'+input + '\n')
    
        try:
            
           
            read=open('C:\\Users\\usman\\3D Objects\\Ai Jarvis Project\\python talk.txt','r')
            list1=[]
            list2=[]
            u=input
            string='''- - '''
            human=string+u
            #print(human)
            
            
            
            for line in read:
                if line.startswith('- - '):
                    list1.append(line)
                elif line.startswith('  - '):
                        list2.append(line)
                        #- - print(line)

            for l in list1:
                
                #print(list1[1])
                break
            for l1 in list2:
                #print(list2[1])
                break

        
            for i in range(0,len(list1)):
                #print(list1[i])
                #cprint(human)
                if list1[i]==human+'\n':
                    #print("*****************************************************")
                    print('bot:'+list2[i])
                    break
                elif human=="- - bye":
                    print("ok bye")
                    time.sleep(5)
                    sys.exit()
                    break
                else:
                    pass
            app_id = "Q3489H-PPHU83PE6L"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print(answer)
            f.write('-'+answer+ '\n')
                
        except:
            
            try:
               print(wikipedia.summary(input))
               f.write('-'+(wikipedia.summary(input))+ '\n')
            except:
             try:
               match=re.search(startdoyou,input).group(1)
               if match:
                   p=MyFrame.replace_pronouns(match)
                   dep=" how i forget "+p
                   print(dep)
                   f.write(dep+ '\n')
               else:
                   pass
               
             except:
                 try:
                     match1=re.search(startiwant,input).group(1)
                     if match1:
                         p=MyFrame.replace_pronouns(match1)
                         dep="then what stopping you "+p
                         print(dep)
                         end = time.time()
                         measure=round(end-start)
                         time1.append(measure)
                         f.write(dep+ '\n')
                     else:
                             pass
                 except:
                    try:
                        match2=re.search(stockprice,input).group(1) 
                        p=MyFrame.replace_pronouns(match2)
                        dep="wait i will show you in browser"
                        print(dep)
                        webbrowser.open('https://dps.psx.com.pk/')
                        end = time.time()
                        measure=round(end-start)
                        time1.append(measure)
                        
                    except:
                        try:
                            match3=re.search(webbrow,input).group(1) 
                            p=MyFrame.replace_pronouns(match3)
                            dep="enjoy the service"
                            print(dep)
                            webbrowser.open('https://www.google.com')
                        except:
                          try:
                            match4=re.search(openapp,input).group(2) 
                            p=MyFrame.replace_pronouns(match4)
                            dep="yah sure "+p
                            mat=re.search('notepad',match4)
                            mat1=re.search('snippingtool',match4)
                            if mat:
                                print(dep)
                                path = r'path/to/your/file.txt'
                                subprocess.Popen(['notepad.exe', path])
                            elif mat1: 
                                print(dep)
                                path = r'path/to/your/file.txt'
                                subprocess.Popen(['snippingtool.exe', path])
                            else:
                                pass
                                    
                                
                            
                          except:
                            try:
                                match5=re.search(playsong,input).group(1)
                    
                                if match5:
                                    p=MyFrame.replace_pronouns(match5)
                                    dep="ya sure enjoy the song "
                                    
                                    print(dep)
                                    os.startfile('C:\\Users\\usman\\Music\\Music Maker Jam Recordings\\Dubstepfinalbest.mp3')
                              
                                else:
                                       pass
                            except:
                                try:
                                    match6=re.search(perfect,input).group(1)
                                    if match6:
                                        p=MyFrame.replace_pronouns(match6)
                                        dep="Now you know my efficiency "
                                        print(time1)
                                        df=pd.DataFrame({'x': time1, 'y': range(0,len(time1)) })
                                        plt.plot( 'x', 'y', data=df, color='skyblue')
                                        plt.show()
                                        plt.plot( 'x', 'y', data=df, color='skyblue', alpha=0.3)
                                        plt.show()
                                    else:
                                        pass
                                except:
                                    pass
                                    
                                


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    frame.SetIcon(wx.Icon("C:\\Users\\usman\\3D Objects\\Ai Jarvis Project\\hvt.ico"))
app.MainLoop()
del app