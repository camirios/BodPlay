#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:25:46 2018

@author: Rey
"""

import os
#import ./nowplaying.py as tunes

#keyboard.press_and_release('play')
#pyautogui.press('f119')

#for i in (15,17):
    #pyautogui.keyDown('shift')  # hold down the shift key
    #pyautogui.press('f'+str(i))     # press the left arrow key
    #pyautogui.keyUp('shift')

#pyautogui.press('f6')
#pyautogui.press('enter')
#pyautogui.press('f17')


#play='python ./nowplaying.py play'
#tunes="echo "+play

#os.system(tunes)


#-----------------------------------------------------------------------


import subprocess;
import os;
import random;
import sys;
#args=sys.argv[1]
artist=subprocess.getoutput("osascript -e 'tell application \"iTunes\" to artist of current track as string'");
track=subprocess.getoutput("osascript -e 'tell application \"iTunes\" to name of current track as string'");
state=subprocess.getoutput("osascript -e 'tell application \"iTunes\" to player state as string'");
currentvolume=subprocess.getoutput("osascript -e 'tell application \"iTunes\" to sound volume as integer'")



def status():
  if (state=="playing"):
   print ("Itunes is: %s" % state)
   print ("Currently playing: '%s' by '%s'") % (track, artist)
  else:print ("Itunes it not playing, type 'itunes play' to start playing music")

def play():
 if(state=="paused"):
  print ("Playing iTunes")
  subprocess.getoutput("osascript -e 'tell application \"iTunes\" to play'")
  print ("Currently playing: '%s' by '%s'" % (track, artist))
 else: print ("Itunes is currently playing")

def pause():
 if(state=="playing"):
  print ("Pausing iTunes")
  subprocess.getoutput("osascript -e 'tell application \"iTunes\" to pause'")
  print ("iTunes paused")
 else:print ("iTunes is currently paused")

def nsong():
 print("Skipping to next song")
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to next track'")
 print ("Currently playing: '%s' by '%s'") % (track, artist)

def psong():
 print("Rewinding to previous song")
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to previous track'")
 status()
#Jesse, we need to fix that shit... it runs to quickly

def iquit():
 print ("Quitting iTunes")
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to quit'")

def mute():
 print ("Muting iTunes")
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set mute to true'")

def unmute():
 print ("Unmuting iTunes")
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set mute to false'")

def volup():
 increaseby=10
 if (currentvolume=="100"):increaseby=0;
 elif(currentvolume>"90"):increaseby=100-int(currentvolume);
 elif(currentvolume<"90"):increaseby=10;
 newvolume=int(currentvolume)+increaseby
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set sound volume to "+str(newvolume)+"'");
 print ("Your current volume is: %d" % (int(subprocess.getoutput("osascript -e 'tell application \"iTunes\" to sound volume as integer'"))))


def voldown():
 decreaseby=10
 if (currentvolume=="0"):decreaseby=0;
 elif(currentvolume<"10"):decreaseby=int(currentvolume)
 elif(currentvolume>"10"):decreaseby=10;
 newvolume=int(currentvolume)-decreaseby
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set sound volume to "+str(newvolume)+"'");
 print ("Your current volume is: %d" % (int(subprocess.getoutput("osascript -e 'tell application \"iTunes\" to sound volume as integer'"))))

def volexact():
 newvolume=sys.argv[2]
 subprocess.getoutput("osascript -e 'tell application \"iTunes\" to set sound volume to "+str(newvolume)+"'");
 print ("Your current volume is: %d" % (int(subprocess.getoutput("osascript -e 'tell application \"iTunes\" to sound volume as integer'"))))


#status()


#PARSE ARGS
'''
if (args=="status"):status();
elif (args=="play"):play();
elif (args=="pause"):pause();
elif (args=="next"):nsong();
elif (args=="quit"):iquit();
elif (args=="prev"):psong();
elif (args=="mute"):mute();
elif (args=="unmute"):unmute();
if (args=="vol"):volexact();
#I just realized I should have only looked for "up" or "down" .... too late I did all of the below code :\
#voldu = sys.argv[1:len(sys.argv)-1][0]+" "+sys.argv[1:len(sys.argv)-1][1]
elif(args=="up"):volup();
elif(args=="down"):voldown();

'''
