try:
    import simplegui
    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    SIMPLEGUICS2PYGAME = True
import urllib.request as ur
from bs4 import BeautifulSoup
import re

def start():
    frame.set_draw_handler(draw)


#Draw function that will create the frame and draw the necessary text on the frame. 
def draw(canvas):
    data = ur.urlopen("http://www.espncricinfo.com/ci/engine/match/946929.html")
    data1 = data.read()
    data2 = BeautifulSoup(data1)
    tags = data2("title")
    print(tags)
    score = str(tags).split()
    score1 = re.findall('<title>([A-Za-z.]+)', score[0])
    score2 = re.findall('[0-9.]+', score[2])
    #(score1[0], score[1], "overs:", score2[0])
    canvas.draw_text(score1[0], (20,20), 15, "White")
    canvas.draw_text(score[1], (100,20), 15, "White")
    canvas.draw_text("Overs", (20,60), 15, "White")
    canvas.draw_text(score2[0], (70,60), 15, "White")

#Create frame
frame = simplegui.create_frame("NOT vs MID",200,150)
#Create a timer
timer = simplegui.create_timer(1000, start)

frame.set_draw_handler(draw)

#Start the frame and timer
frame.start()
timer.start()