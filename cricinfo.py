#Import the libraries needed.
try:
    import simplegui
    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    SIMPLEGUICS2PYGAME = True
import urllib.request as ur
from bs4 import BeautifulSoup
import re

# this function calls the Draw function
def start():
    frame.set_draw_handler(draw)
    
#Draw function that will create the frame and draw the necessary text on the frame. 
def draw(canvas):
    #The URL is provided and the program crawls the data from this website. Just change the location below for required score.
    data = ur.urlopen("http://www.espncricinfo.com/ci/engine/match/946929.html")
    
    #The required data is converted into a traversable tree using BeautifulSoup and read using the XML tags. 
    data1 = data.read()
    data2 = BeautifulSoup(data1)
    tags = data2("title")
    print(tags)
    
    # The required information is extracted from the retrieved data and written to a frame.
    score = str(tags).split()
    score1 = re.findall('<title>([A-Za-z.]+)', score[0])
    score2 = re.findall('[0-9.]+', score[2])
    #(score1[0], score[1], "overs:", score2[0])
    canvas.draw_text(score1[0], (20,20), 15, "White")
    canvas.draw_text(score[1], (100,20), 15, "White")
    canvas.draw_text("Overs", (20,60), 15, "White")
    canvas.draw_text(score2[0], (70,60), 15, "White")

#Create a data frame
frame = simplegui.create_frame("NOT vs MID",200,150)

#Create a timer which will perform the start function every 10 secs
timer = simplegui.create_timer(1000, start)

frame.set_draw_handler(draw)

#Start the frame and timer
frame.start()
timer.start()
