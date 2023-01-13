from pygame import *
from math import *
from random import *
from tkinter import *
from tkinter import filedialog
init()
root=Tk()
root.withdraw()
size=width,height=1280,900
screen=display.set_mode(size)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

start=image.load("images/start1.jpg") #intro image
startRect=Rect(550,380,180,180) #start button

running=True
while running: #intro loop
    for evt in event.get():
        if evt.type==QUIT:
            running=False      
        if evt.type==MOUSEBUTTONDOWN:
            sx,sy=mouse.get_pos()

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    screen.blit(start,(-288,0))
    if startRect.collidepoint(mx,my):
        if (mx-640)**2+(my-472)**2<=89**2:
          draw.circle(screen,BLUE,(640,472),89,1)
          if mb[0]==1:
              break           
    else:
        screen.blit(start,(-288,0))      
    display.flip()

myFont=font.SysFont("Consolas",15) #load font
#several font lines to help user
savetext=myFont.render("Save your masterpiece!",True,BLACK)
loadtext=myFont.render("Load an image.",True,BLACK)
pencil1=myFont.render("Hold down the mouse to",True,BLACK)
pencil2=myFont.render("draw thin lines.",True,BLACK)
brush2=myFont.render("draw thicker lines.",True,BLACK)
eraser2=myFont.render("erase.",True,BLACK)
rect2=myFont.render("draw rectangles.",True,BLACK)
spray2=myFont.render("use the spraypaint.",True,BLACK)
ellipse2=myFont.render("draw ellipses.",True,BLACK)
rectfill1=myFont.render("Use the box above to",True,BLACK)
rectfill2=myFont.render("toggle fill.",True,BLACK)
polygon1=myFont.render("Left click to start a",True,BLACK)
polygon2=myFont.render("polygon. Keep clicking",True,BLACK)
polygon3=myFont.render("to add vertices. Right",True,BLACK)
polygon4=myFont.render("click to close polygon.",True,BLACK)
filltext1=myFont.render("Left click to fill",True,BLACK)
filltext2=myFont.render("the entire canvas.",True,BLACK)
high2=myFont.render("use a translucent brush.",True,BLACK)
size1=myFont.render("Use the box on the left",True,BLACK)
size2=myFont.render("to change thickness.",True,BLACK)
eye1=myFont.render("Left click on an object",True,BLACK)
eye2=myFont.render("to get its color. Right",True,BLACK)
eye3=myFont.render("click to select it as",True,BLACK)
eye4=myFont.render("the secondary color.",True,BLACK)
sizeup1=myFont.render("Increase your tool's",True,BLACK)
sizedown1=myFont.render("Decrease your tool's",True,BLACK)
sizeup2=myFont.render("thickness if available.",True,BLACK)
undotext=myFont.render("Undo your last move.",True,BLACK)
redotext=myFont.render("Redo the recent undo.",True,BLACK)
rewindtext=myFont.render("Rewind the soundtrack.",True,BLACK)
playtext=myFont.render("Play the soundtrack.",True,BLACK)
pausetext=myFont.render("Pause the soundtrack.",True,BLACK)
pal1=myFont.render("Left click to pick the",True,BLACK)
pal2=myFont.render("primary color. Right",True,BLACK)
pal3=myFont.render("click to select it as",True,BLACK)
pal4=myFont.render("a secondary color.",True,BLACK)
colboth1=myFont.render("Left click for primary",True,BLACK)
colboth2=myFont.render("color, right click for",True,BLACK)
colboth3=myFont.render("secondary color.",True,BLACK)
stamptext1=myFont.render("Put an Avenger on your",True,BLACK)
stamptext2=myFont.render("drawing! Use left box",True,BLACK)
stamptext3=myFont.render("for size references.",True,BLACK)
colsecond0=myFont.render("This tool uses the",True,BLACK)
colsecond1=myFont.render("secondary color. Right",True,BLACK)
colsecond2=myFont.render("click on the palette",True,BLACK)
colsecond3=myFont.render("to change its color.",True,BLACK)
savingerror=myFont.render("Error: save failed.",True,BLACK)
loadingerror=myFont.render("Error: load failed.",True,BLACK)

#initializing variables
toolcol=BLACK
col=BLACK #primary color
col2=WHITE #secondary color
tool="none"
fill=0 #fill toggle

#specifing thickness
pencilthicc=2
eraserthicc=30
rectthicc=5
ellipsethicc=5
brushthicc=10
spraythicc=25
stampsize=190

#defining rects
saveRect=Rect(20,20,40,40)
loadRect=Rect(70,20,40,40)
pencilRect=Rect(20,80,40,40)
eraserRect=Rect(70,80,40,40)
rectRect=Rect(20,130,40,40)
ellRect=Rect(70,130,40,40)
brushRect=Rect(20,180,40,40)
polyRect=Rect(70,180,40,40)
sprayRect=Rect(20,230,40,40)
fillRect=Rect(70,230,40,40)
highRect=Rect(20,280,40,40)
eyeRect=Rect(70,280,40,40)
sizeRect=Rect(15,360,100,100)
sizedownRect=Rect(15,470,44,30)
sizeupRect=Rect(70,470,44,30)
undoRect=Rect(20,550,40,40)
redoRect=Rect(70,550,40,40)
textRect=Rect(1050,460,210,240)
canvasRect=Rect(130,80,910,620)
palRect=Rect(width-220,80,200,200)
fillRect0=Rect(width-165,400,40,40)
fillRect1=Rect(width-115,400,40,40)
rewindRect=Rect(1170,20,40,40)
pauseRect=Rect(1220,20,40,40)
colRect=Rect(width-150,320,40,40)
col2Rect=Rect(width-130,300,40,40)
stamp1Rect=Rect(130,710,180,180)
stamp2Rect=Rect(320,710,180,180)
stamp3Rect=Rect(510,710,180,180)
stamp4Rect=Rect(700,710,180,180)
stamp5Rect=Rect(890,710,180,180)
stamp6Rect=Rect(1080,710,180,180)

#initializing highlighter tool variables
r,g,b=0,0,0
marker=Surface((brushthicc*2,brushthicc*2),SRCALPHA)
draw.circle(marker,(r,g,b,10),(brushthicc,brushthicc),brushthicc)

polyPoints=[] #initializing polygon tool list

#undo and redo lists
undo=[]
redo=[]

#loading and resizing images
palPic=image.load("images/pal.png")
bg=image.load("images/bg2.png")
bg2=transform.scale(bg,(1307,989))
screen.blit(bg2,(-27,-89))
draw.rect(screen,WHITE,textRect)
save=image.load("images/save.png")
save=transform.scale(save,(34,34))
load=image.load("images/load.png")
load=transform.scale(load,(30,30))
pencil=image.load("images/pencil.png")
pencil=transform.scale(pencil,(28,28))
eraser=image.load("images/eraser.png")
eraser=transform.scale(eraser,(46,46))
brush=image.load("images/brush.png")
brush=transform.scale(brush,(28,30))
spray=image.load("images/spray.png")
spray=transform.scale(spray,(36,36))
fillPic=image.load("images/fill.png")
fillPic=transform.scale(fillPic,(38,38))
high=image.load("images/high.png")
high=transform.scale(high,(30,30))
eye=image.load("images/eye.png")
eye=transform.scale(eye,(32,32))
up=image.load("images/up.png")
up=transform.scale(up,(20,20))
down=transform.rotate(up,180)
undoPic=image.load("images/undo.png")
undoPic=transform.scale(undoPic,(34,34))
redoPic=transform.flip(undoPic,True,False)
rewind=image.load("images/rewind.png")
rewind=transform.scale(rewind,(40,40))
play=image.load("images/play.png")
play=transform.scale(play,(40,40))
thor=image.load("images/thor.png")
thorthumb=transform.scale(thor,(94,160))
bp=image.load("images/blackpanther.png")
bpthumb=transform.scale(bp,(88,180))
captain=image.load("images/captain.png")
captainthumb=transform.scale(captain,(144,160))
iron=image.load("images/iron.png")
ironthumb=transform.scale(iron,(77,160))
spider=image.load("images/spiderman.png")
spiderthumb=transform.scale(spider,(77,160))
strange=image.load("images/strange.png")
strangethumb=transform.scale(strange,(108,180))
draw.rect(screen,WHITE,canvasRect)
screen.blit(palPic,(width-220,80))
logo=image.load("images/logo.png")
logo=transform.scale(logo,(185,80))
screen.blit(logo,(535,0))

undo.append(screen.copy()) #starting with one screenshot in undo list

mixer.music.load("soundtrack.mp3") #music
mixer.music.play() #needs to be commanded twice to start for some reason
mixer.music.play()
playing=True

while running: #program loop
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            click=True
            
            sx,sy=mouse.get_pos() #starting position at click

        if evt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(sx,sy) or canvasRect.collidepoint(mx,my):
                undo.append(screen.copy()) #add screenshot to undo list when something is drawn
                redo=[] #clear redo list

    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    #drawing tool rects and blitting images
    draw.rect(screen,WHITE,(10,70,110,260)) #white backgrounds for some
    screen.blit(save,(23,23))
    screen.blit(load,(75,25))
    screen.blit(pencil,(26,86))
    screen.blit(eraser,(68,75))
    screen.blit(brush,(26,185))
    screen.blit(spray,(23,232))
    screen.blit(fillPic,(72,231))
    screen.blit(high,(25,285))
    screen.blit(eye,(74,284))
    screen.blit(down,(27,475))
    screen.blit(up,(82,475))
    draw.rect(screen,WHITE,undoRect)
    draw.rect(screen,WHITE,redoRect)
    screen.blit(undoPic,(23,553))
    screen.blit(redoPic,(73,553))
    draw.rect(screen,WHITE,(1160,10,110,60))
    screen.blit(rewind,(1170,20))
    screen.blit(play,(1220,20))
    draw.line(screen,col,(80,185),(105,185),2)
    draw.line(screen,col,(105,185),(95,215),2)
    draw.line(screen,col,(95,215),(75,215),2)
    draw.line(screen,col,(75,215),(90,200),2)
    draw.line(screen,col,(90,200),(75,200),2)
    draw.line(screen,col,(75,200),(80,185),2)
    draw.rect(screen,WHITE,saveRect,2)
    draw.rect(screen,WHITE,loadRect,2)
    draw.rect(screen,toolcol,pencilRect,2)
    draw.rect(screen,toolcol,eraserRect,2)
    draw.rect(screen,toolcol,rectRect,2)
    draw.rect(screen,toolcol,ellRect,2)
    draw.rect(screen,toolcol,brushRect,2)
    draw.rect(screen,toolcol,polyRect,2)
    draw.rect(screen,toolcol,sprayRect,2)
    draw.rect(screen,toolcol,fillRect,2)
    draw.rect(screen,toolcol,highRect,2)
    draw.rect(screen,toolcol,eyeRect,2)
    draw.rect(screen,WHITE,(sizeRect))
    draw.rect(screen,WHITE,(sizedownRect),2)
    draw.rect(screen,WHITE,(sizeupRect),2)
    draw.rect(screen,WHITE,(width-170,395,100,50))
    draw.rect(screen,col,fillRect0,2)
    draw.rect(screen,col,fillRect1)
    draw.rect(screen,col2,col2Rect)
    draw.rect(screen,BLACK,col2Rect,2)
    draw.rect(screen,col,colRect)
    draw.rect(screen,BLACK,colRect,2)
    draw.rect(screen,(50,100,255),undoRect,2)
    draw.rect(screen,(50,100,255),redoRect,2)
    #stamp rects and thumbnails
    draw.rect(screen,WHITE,stamp1Rect,2)
    screen.blit(thorthumb,(173,720))
    draw.rect(screen,WHITE,stamp2Rect,2)
    screen.blit(bpthumb,(366,710))
    draw.rect(screen,WHITE,stamp3Rect,2)
    screen.blit(captainthumb,(528,720))
    draw.rect(screen,WHITE,stamp4Rect,2)
    screen.blit(ironthumb,(752,720))
    draw.rect(screen,WHITE,stamp5Rect,2)
    screen.blit(spiderthumb,(947,720))
    draw.rect(screen,WHITE,stamp6Rect,2)
    screen.blit(strangethumb,(1116,710))
    
    if fill==0: #if fill turned off, highlight "no fill box" and draw tools thumbnails without fill
        draw.rect(screen,RED,(1113,398,44,44),2)
        draw.rect(screen,col,(25,140,30,20),2)
        draw.ellipse(screen,col,Rect(74,138,32,24),2)
    if fill==1: #if off, highlight fill box abd draw filled tools
        draw.rect(screen,RED,fillRect1,2)
        draw.rect(screen,col,(25,140,30,20))
        draw.ellipse(screen,col,Rect(74,138,32,24))
        
    #if tool is selected
    if tool=="pencil":
        draw.rect(screen,RED,pencilRect,2) #highlight box
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col,(65,410),pencilthicc) #draw appropriate circle in preview box
        draw.rect(screen,WHITE,textRect)
        screen.blit(pencil1,(1060,480)) #blit relecant help text
        screen.blit(pencil2,(1060,500))
        screen.blit(size1,(1060,550))
        screen.blit(size2,(1060,570))
        screen.blit(colboth1,(1060,620))
        screen.blit(colboth2,(1060,640))
        screen.blit(colboth3,(1060,660))
    if tool=="eraser":
        draw.rect(screen,RED,eraserRect,2)
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col2,(65,410),eraserthicc)
        draw.rect(screen,WHITE,textRect)
        screen.blit(pencil1,(1060,480))
        screen.blit(eraser2,(1060,500))
        screen.blit(size1,(1060,545))
        screen.blit(size2,(1060,565))
        screen.blit(colsecond0,(1060,610))
        screen.blit(colsecond1,(1060,630))
        screen.blit(colsecond2,(1060,650))
        screen.blit(colsecond3,(1060,670))
    if tool=="rect":
        draw.rect(screen,RED,rectRect,2)
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col,(65,410),rectthicc)
        draw.rect(screen,WHITE,textRect)
        screen.blit(pencil1,(1060,470))
        screen.blit(rect2,(1060,490))
        screen.blit(rectfill1,(1060,523))
        screen.blit(rectfill2,(1060,543))
        screen.blit(size1,(1060,577))
        screen.blit(size2,(1060,597))
        screen.blit(colboth1,(1060,630))
        screen.blit(colboth2,(1060,650))
        screen.blit(colboth3,(1060,670))
    if tool=="ellipse":
        draw.rect(screen,RED,ellRect,2)
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col,(65,410),ellipsethicc)
        draw.rect(screen,WHITE,textRect)
        screen.blit(pencil1,(1060,470))
        screen.blit(ellipse2,(1060,490))
        screen.blit(rectfill1,(1060,523))
        screen.blit(rectfill2,(1060,543))
        screen.blit(size1,(1060,577))
        screen.blit(size2,(1060,597))
        screen.blit(colboth1,(1060,630))
        screen.blit(colboth2,(1060,650))
        screen.blit(colboth3,(1060,670))
    if tool=="brush":
        draw.rect(screen,RED,brushRect,2)
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col,(65,410),brushthicc)
        draw.rect(screen,WHITE,textRect)
        screen.blit(pencil1,(1060,480))
        screen.blit(brush2,(1060,500))
        screen.blit(size1,(1060,550))
        screen.blit(size2,(1060,570))
        screen.blit(colboth1,(1060,620))
        screen.blit(colboth2,(1060,640))
        screen.blit(colboth3,(1060,660))
    if tool=="polygon":
        draw.rect(screen,RED,polyRect,2)
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col,(65,510),1)
        draw.rect(screen,WHITE,textRect)
        screen.blit(polygon1,(1060,480))
        screen.blit(polygon2,(1060,500))
        screen.blit(polygon3,(1060,520))
        screen.blit(polygon4,(1060,540))
    if tool=="spray":
        draw.rect(screen,RED,sprayRect,2)
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col,(65,410),spraythicc)
        draw.rect(screen,WHITE,textRect)
        screen.blit(pencil1,(1060,480))
        screen.blit(spray2,(1060,500))
        screen.blit(size1,(1060,550))
        screen.blit(size2,(1060,570))
        screen.blit(colboth1,(1060,620))
        screen.blit(colboth2,(1060,640))
        screen.blit(colboth3,(1060,660))
    if tool=="fill":
        draw.rect(screen,RED,fillRect,2)
        draw.rect(screen,col2,(sizeRect))
        draw.rect(screen,WHITE,textRect)
        screen.blit(filltext1,(1060,490))
        screen.blit(filltext2,(1060,510))
        screen.blit(colsecond0,(1060,580))
        screen.blit(colsecond1,(1060,600))
        screen.blit(colsecond2,(1060,620))
        screen.blit(colsecond3,(1060,640))
    if tool=="highlighter":
        draw.rect(screen,RED,highRect,2)
        draw.rect(screen,WHITE,(sizeRect))
        draw.circle(screen,col,(65,410),brushthicc)
        draw.rect(screen,WHITE,textRect)
        screen.blit(pencil1,(1060,510))
        screen.blit(high2,(1060,530))
        screen.blit(size1,(1060,600))
        screen.blit(size2,(1060,620))
    if tool=="eyedropper":
        draw.rect(screen,RED,eyeRect,2)
        if canvasRect.collidepoint(mx,my):
            draw.rect(screen,screen.get_at((mx,my)),(sizeRect)) #previewing color
        draw.rect(screen,WHITE,textRect)
        screen.blit(eye1,(1060,480))
        screen.blit(eye2,(1060,500))
        screen.blit(eye3,(1060,520))
        screen.blit(eye4,(1060,540))
    if tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6":
        draw.circle(screen,BLACK,(65,410),stampsize//10,1)
        draw.rect(screen,WHITE,textRect)
        screen.blit(stamptext1,(1060,480))
        screen.blit(stamptext2,(1060,500))
        screen.blit(stamptext3,(1060,520))
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
        draw.rect(screen,WHITE,textRect)
        screen.blit(savetext,(1060,480))
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,RED,loadRect,2)
        draw.rect(screen,WHITE,textRect)
        screen.blit(loadtext,(1060,480))

    #highlighting boxes when hovering over them
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,RED,pencilRect,2)
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,RED,eraserRect,2)
    if rectRect.collidepoint(mx,my):
        draw.rect(screen,RED,rectRect,2)
    if ellRect.collidepoint(mx,my):
        draw.rect(screen,RED,ellRect,2)
    if brushRect.collidepoint(mx,my):
        draw.rect(screen,RED,brushRect,2)
    if polyRect.collidepoint(mx,my):
        draw.rect(screen,RED,polyRect,2)
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,RED,sprayRect,2)
    if fillRect.collidepoint(mx,my):
        draw.rect(screen,RED,fillRect,2)
    if highRect.collidepoint(mx,my):
        draw.rect(screen,RED,highRect,2)
    if eyeRect.collidepoint(mx,my):
        draw.rect(screen,RED,eyeRect,2)
    if fillRect0.collidepoint(mx,my):
        draw.rect(screen,RED,(1113,398,44,44),2)
    if fillRect1.collidepoint(mx,my):
        draw.rect(screen,RED,fillRect1,2)
    if stamp1Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp1Rect,2)
    if stamp2Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp2Rect,2)
    if stamp3Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp3Rect,2)
    if stamp4Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp4Rect,2)
    if stamp5Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp5Rect,2)
    if stamp6Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp6Rect,2)
    if sizeupRect.collidepoint(mx,my):
        draw.rect(screen,RED,sizeupRect,2)
        draw.rect(screen,WHITE,textRect)
        screen.blit(sizeup1,(1060,480)) #some buttons provide text when hovering
        screen.blit(sizeup2,(1060,500))
    if sizedownRect.collidepoint(mx,my):
        draw.rect(screen,RED,sizedownRect,2)
        draw.rect(screen,WHITE,textRect)
        screen.blit(sizedown1,(1060,480))
        screen.blit(sizeup2,(1060,500))
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
        draw.rect(screen,WHITE,textRect)
        screen.blit(undotext,(1060,480))
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect,2)
        draw.rect(screen,WHITE,textRect)
        screen.blit(redotext,(1060,480))
    if rewindRect.collidepoint(mx,my):
        draw.circle(screen,RED,(1190,40),21,2)
        draw.rect(screen,WHITE,textRect)
        screen.blit(rewindtext,(1060,480))
    if pauseRect.collidepoint(mx,my):
        draw.circle(screen,RED,(1240,40),21,2)
        draw.rect(screen,WHITE,textRect)
        #different text based on what the play/pause button will do
        if playing:
            screen.blit(pausetext,(1060,480))
        else:
            screen.blit(playtext,(1060,480))
    #highlighting hovering stamp outlines
    if tool=="stamp1":
        draw.rect(screen,RED,stamp1Rect,2)
    if tool=="stamp2":
        draw.rect(screen,RED,stamp2Rect,2)
    if tool=="stamp3":
        draw.rect(screen,RED,stamp3Rect,2)
    if tool=="stamp4":
        draw.rect(screen,RED,stamp4Rect,2)
    if tool=="stamp5":
        draw.rect(screen,RED,stamp5Rect,2)
    if tool=="stamp6":
        draw.rect(screen,RED,stamp6Rect,2)

    #resizing stamps for use in canvas
    thorstamp=transform.scale(thor,(int(0.587*stampsize),stampsize))
    bpstamp=transform.scale(bp,(int(0.49*stampsize),stampsize))
    captainstamp=transform.scale(captain,(int(0.8*stampsize),stampsize))
    ironstamp=transform.scale(iron,(int(0.48*stampsize),stampsize))
    spiderstamp=transform.scale(spider,(int(0.48*stampsize),stampsize))
    strangestamp=transform.scale(strange,(int(0.6*stampsize),stampsize))

    #selecting the tool
    if mb[0]==1 and click:
        if pencilRect.collidepoint(mx,my):
            tool="pencil"
        if eraserRect.collidepoint(mx,my):
            tool="eraser"
        if rectRect.collidepoint(mx,my):
            tool="rect"
        if ellRect.collidepoint(mx,my):
            tool="ellipse"
        if brushRect.collidepoint(mx,my):
            tool="brush"
        if polyRect.collidepoint(mx,my):
            tool="polygon"
        if sprayRect.collidepoint(mx,my):
            tool="spray"
        if fillRect.collidepoint(mx,my):
            tool="fill"
        if highRect.collidepoint(mx,my):
            tool="highlighter"
        if eyeRect.collidepoint(mx,my):
            tool="eyedropper"
        #using size up button
        if sizeupRect.collidepoint(mx,my):
            if tool=="pencil":
                if pencilthicc<4:
                    pencilthicc+=1
            if tool=="eraser":
                if eraserthicc<50:
                    eraserthicc+=2
            if tool=="rect" and fill==0:
                if rectthicc<15:
                    rectthicc+=1
            if tool=="ellipse" and fill==0:
                if ellipsethicc<30:
                    ellipsethicc+=1
            if tool=="brush" or tool=="highlighter":
                if brushthicc<48:
                    brushthicc+=2
                    marker=Surface((brushthicc*2,brushthicc*2),SRCALPHA) #creating a blank surface
                    draw.circle(marker,(r,g,b,10),(brushthicc,brushthicc),brushthicc)
            if tool=="spray":
                if spraythicc<100:
                    spraythicc+=1
            if tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6":
                if stampsize<490:
                    stampsize+=30
        #size down button
        if sizedownRect.collidepoint(mx,my):
            if tool=="pencil":
                if pencilthicc>1:
                    pencilthicc-=1
            if tool=="eraser":
                if eraserthicc>10:
                    eraserthicc-=2
            if tool=="rect" and fill==0:
                if rectthicc>1:
                    rectthicc-=1
            if tool=="ellipse" and fill==0:
                if ellipsethicc>1:
                    ellipsethicc-=1
            if tool=="brush" or tool=="highlighter":
                if brushthicc>6:
                    brushthicc-=2
                    marker=Surface((brushthicc*2,brushthicc*2),SRCALPHA) #creating a blank surface
                    draw.circle(marker,(r,g,b,10),(brushthicc,brushthicc),brushthicc)
            if tool=="spray":
                if spraythicc>5:
                    spraythicc-=1
            if tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6":
                if stampsize>50:
                    stampsize-=30
        #selecting fill state
        if fillRect0.collidepoint(mx,my):
            fill=0
        if fillRect1.collidepoint(mx,my):
            fill=1
        if undoRect.collidepoint(mx,my) and click: #undo
            if len(undo)>1: #undo not possible if there is only one screenshot in the list
                redo.append(undo.pop()) #move last screenshot to redo list
                ss=undo[-1] #define ss as the current screenshot
                screen.blit(ss,(0,0))   #blitting screenshot
        if redoRect.collidepoint(mx,my) and click:
            if len(redo)>0:
                undo.append(redo.pop())
                ss=undo[-1]
                screen.blit(ss,(0,0))
                
        #selecting stamps
        if stamp1Rect.collidepoint(mx,my):
            tool="stamp1"
        if stamp2Rect.collidepoint(mx,my):
            tool="stamp2"
        if stamp3Rect.collidepoint(mx,my):
            tool="stamp3"
        if stamp4Rect.collidepoint(mx,my):
            tool="stamp4"
        if stamp5Rect.collidepoint(mx,my):
            tool="stamp5"
        if stamp6Rect.collidepoint(mx,my):
            tool="stamp6"
        #saving
        if saveRect.collidepoint(mx,my):
            try:
                fname=filedialog.asksaveasfilename(defaultextension=".png")
                #if the user clicks CANCEL, don't save the picture
                image.save(screen.subsurface(canvasRect),fname)
            except:
                tool=="none" #no tool so msg can be shown till a new tool is chosen
                draw.rect(screen,WHITE,textRect)
                screen.blit(savingerror,(1060,480)) #showing error msg
        #loading
        if loadRect.collidepoint(mx,my):
            f=filedialog.askopenfilename()
            loadpic=image.load(f)
            w=loadpic.get_width() #grabbing height and width to see how to blit
            h=loadpic.get_height()
            screen.set_clip(canvasRect)
            try:
                if w<=910 and h<=620: #if the pic is smaller than the canvas
                    screen.blit(loadpic,(130+(910-w)//2,80+(620-h)//2)) #center pic
                else:
                    if h*1.467>w: #1.467=ratio of my canvas. seeing if the pic is wider or taller than canvas and
                                  #blitting accordingly so I have the biggest possible size without cropping anything out 
                        draw.rect(screen,WHITE,canvasRect)
                        smallPic=transform.scale(loadpic,(int((w/h)*620),620)) #top and bottom touching canvas border

                    else:
                        draw.rect(screen,WHITE,canvasRect)
                        smallPic=transform.scale(loadpic,(910,int((h/w)*910))) #sides touching canvas border

                    w=smallPic.get_width()
                    h=smallPic.get_height()
                    screen.blit(smallPic,(130+(910-w)//2,80+(620-h)//2)) #center pic

                undo.append(screen.copy()) #adding to undo list since nothing is drawn
                screen.set_clip(None)
            except:
                tool="none"
                draw.rect(screen,WHITE,textRect)
                screen.blit(loadingerror,(1060,480)) #loading error msg
                
        if rewindRect.collidepoint(mx,my):
            mixer.music.play()
        if pauseRect.collidepoint(mx,my):
            if playing:
                mixer.music.pause()
                playing=False
            else:
                mixer.music.unpause()
                playing=True 
    if palRect.collidepoint(mx,my):
        if (mx-1160)**2+(my-180)**2<=99**2: #circular palette
            if mb[0]==1 and click:
                col=screen.get_at((mx,my))
                r,g,b,a=screen.get_at((mx,my)) #color including alpha for highlghter
                draw.circle(marker,(r,g,b,10),(brushthicc,brushthicc),brushthicc) #updating highlighter surface
            if mb[2]==1 and click:
                col2=screen.get_at((mx,my)) #right click for secondary color
            draw.rect(screen,WHITE,textRect)
            screen.blit(pal1,(1060,480))
            screen.blit(pal2,(1060,500))
            screen.blit(pal3,(1060,520))
            screen.blit(pal4,(1060,540))
            draw.rect(screen,screen.get_at((mx,my)),colRect) #preview
            draw.rect(screen,BLACK,colRect,2)
    #kept this with the palette because the code is similar
    if tool=="eyedropper":
        if canvasRect.collidepoint(mx,my):
            if mb[0]==1 and click:
                col=screen.get_at((mx,my))
                r,g,b,a=screen.get_at((mx,my))
                draw.circle(marker,(r,g,b,10),(brushthicc,brushthicc),brushthicc)
            if mb[2]==1 and click:
                col2=screen.get_at((mx,my))
                
    #defining the current screenshot before it's used
    ss=undo[-1]
    #previewing stamps on canvas
    if mb[0]==0:
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            if tool=="eraser":
                screen.blit(ss,(0,0))
                draw.circle(screen,col2,(mx,my),eraserthicc)
            if tool=="stamp1":
                screen.blit(ss,(0,0))
                screen.blit(thorstamp,(mx-0.587*stampsize//2,my-stampsize//2))
            if tool=="stamp2":
                screen.blit(ss,(0,0))
                screen.blit(bpstamp,(mx-0.49*stampsize//2,my-stampsize//2))
            if tool=="stamp3":
                screen.blit(ss,(0,0))
                screen.blit(captainstamp,(mx-0.8*stampsize//2,my-stampsize//2))
            if tool=="stamp4":
                screen.blit(ss,(0,0))
                screen.blit(ironstamp,(mx-0.48*stampsize//2,my-stampsize//2))
            if tool=="stamp5":
                screen.blit(ss,(0,0))
                screen.blit(spiderstamp,(mx-0.48*stampsize//2,my-stampsize//2))
            if tool=="stamp6":
                screen.blit(ss,(0,0))
                screen.blit(strangestamp,(mx-0.6*stampsize//2,my-stampsize//2))
            screen.set_clip(None)
        else:
            screen.set_clip(canvasRect)
            screen.blit(ss,(0,0))
            screen.set_clip(None)

    #using the tool
    if mb[0]==1:
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect) #only the canvas can be "updated"
            if tool=="pencil":
                                    #previous  current
                draw.line(screen,col,(omx,omy),(mx,my),pencilthicc)
            if tool=="eraser":
                draw.circle(screen,col2,(mx,my),eraserthicc)
            if tool=="rect" or tool=="ellipse":
                screen.blit(ss,(0,0))
                dx=(mx-sx) #distance from start to current
                dy=(my-sy)
                if tool=="rect":
                    if fill==0:
                        for i in range(0,rectthicc): #drawing 1 thickness rectangles
                            if dx>0 and dy>0:
                                draw.rect(screen,col,(sx-i,sy-i,dx+i*2,dy+i*2),1)
                            if dx>0 and dy<0:
                                draw.rect(screen,col,(sx-i,sy+i,dx+i*2,dy-i*2),1)
                            if dx<0 and dy<0:
                                draw.rect(screen,col,(sx+i,sy+i,dx-i*2,dy-i*2),1)
                            if dx<0 and dy>0:
                                draw.rect(screen,col,(sx+i,sy-i,dx-i*2,dy+i*2),1)
                            if dx==0:
                                draw.rect(screen,col,(sx-i,sy-i,dx+i*2,dy+i*2),1)
                            if dy==0:
                                draw.rect(screen,col,(sx-i,sy-i,dx+i*2,dy+i*2),1)
                    if fill==1:
                        draw.rect(screen,col,(sx,sy,dx,dy))
                if tool=="ellipse":
                    if fill==0: #drawing 8 ellipses around to avoid cutting at corners
                        ellipseRect=Rect(sx,sy,dx,dy)
                        ellipseRect1=Rect(sx-1,sy,dx,dy)
                        ellipseRect2=Rect(sx,sy-1,dx,dy)
                        ellipseRect3=Rect(sx+1,sy,dx,dy)
                        ellipseRect4=Rect(sx,sy+1,dx,dy)
                        ellipseRect5=Rect(sx-2,sy,dx,dy)
                        ellipseRect6=Rect(sx,sy-2,dx,dy)
                        ellipseRect7=Rect(sx+2,sy,dx,dy)
                        ellipseRect8=Rect(sx,sy+2,dx,dy)
                        ellipseRect.normalize()
                        ellipseRect1.normalize()
                        ellipseRect2.normalize()
                        ellipseRect3.normalize()
                        ellipseRect4.normalize()
                        ellipseRect5.normalize()
                        ellipseRect6.normalize()
                        ellipseRect7.normalize()
                        ellipseRect8.normalize()
                        try:
                            draw.ellipse(screen,col,ellipseRect,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect1,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect2,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect3,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect4,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect5,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect6,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect7,ellipsethicc)
                            draw.ellipse(screen,col,ellipseRect8,ellipsethicc)
                        except: #drawing filled ellipse when it's smaller than its thickness
                            ellipseRect9=Rect(sx,sy,dx,dy)
                            ellipseRect9.normalize()
                            draw.ellipse(screen,col,ellipseRect9)
                    if fill==1:
                        ellipseRect=Rect(sx,sy,dx,dy)
                        ellipseRect.normalize()
                        try:
                            draw.ellipse(screen,col,ellipseRect)
                        except:
                            pass
            if tool=="brush":
                dx=mx-omx
                dy=my-omy
                dist=int(sqrt(dx**2+dy**2))
                for i in range(1,dist+1): #drawing between mouse locations
                    dotX=int(omx+i*dx/dist)
                    dotY=int(omy+i*dy/dist)
                    draw.circle(screen,col,(dotX,dotY),brushthicc)
            if tool=="spray":
                sprayx=randint(mx-spraythicc,mx+spraythicc) #random location for dots
                sprayy=randint(my-spraythicc,my+spraythicc)
                if ((mx-sprayx)**2+(my-sprayy)**2)<=spraythicc**2: #draw if the dot is in the circle
                    draw.rect(screen,col,(sprayx,sprayy,1,1),1)
                sprayx=randint(mx-spraythicc,mx+spraythicc) #drawing more speeds up the process
                sprayy=randint(my-spraythicc,my+spraythicc)
                if ((mx-sprayx)**2+(my-sprayy)**2)<=spraythicc**2:
                    draw.rect(screen,col,(sprayx,sprayy,1,1),1)
                sprayx=randint(mx-spraythicc,mx+spraythicc)
                sprayy=randint(my-spraythicc,my+spraythicc)
                if ((mx-sprayx)**2+(my-sprayy)**2)<=spraythicc**2:
                    draw.rect(screen,col,(sprayx,sprayy,1,1),1)
            if tool=="fill":
                draw.rect(screen,col2,canvasRect)
            if tool=="highlighter":
                if mx!=omx or my!=omy: #there is movement
                    screen.blit(marker,(mx-brushthicc,my-brushthicc))
            screen.set_clip(None)

    #using dual-color tools with right click, only color is changed
    if mb[2]==1:
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            if tool=="pencil":
                draw.line(screen,col2,(omx,omy),(mx,my),pencilthicc)
            if tool=="rect" or tool=="ellipse":
                screen.blit(ss,(0,0))
                dx=(mx-sx)
                dy=(my-sy)
                if tool=="rect":
                    if fill==0:
                        for i in range(0,rectthicc):
                            if dx>0 and dy>0:
                                draw.rect(screen,col2,(sx-i,sy-i,dx+i*2,dy+i*2),1)
                            if dx>0 and dy<0:
                                draw.rect(screen,col2,(sx-i,sy+i,dx+i*2,dy-i*2),1)
                            if dx<0 and dy<0:
                                draw.rect(screen,col2,(sx+i,sy+i,dx-i*2,dy-i*2),1)
                            if dx<0 and dy>0:
                                draw.rect(screen,col2,(sx+i,sy-i,dx-i*2,dy+i*2),1)
                            if dx==0:
                                draw.rect(screen,col2,(sx-i,sy-i,dx+i*2,dy+i*2),1)
                            if dy==0:
                                draw.rect(screen,col2,(sx-i,sy-i,dx+i*2,dy+i*2),1)
                    if fill==1:
                        draw.rect(screen,col2,(sx,sy,dx,dy))
                if tool=="ellipse":
                    if fill==0:
                        ellipseRect=Rect(sx,sy,dx,dy)
                        ellipseRect1=Rect(sx-1,sy,dx,dy)
                        ellipseRect2=Rect(sx,sy-1,dx,dy)
                        ellipseRect3=Rect(sx+1,sy,dx,dy)
                        ellipseRect4=Rect(sx,sy+1,dx,dy)
                        ellipseRect5=Rect(sx-2,sy,dx,dy)
                        ellipseRect6=Rect(sx,sy-2,dx,dy)
                        ellipseRect7=Rect(sx+2,sy,dx,dy)
                        ellipseRect8=Rect(sx,sy+2,dx,dy)                    
                        ellipseRect.normalize()
                        ellipseRect1.normalize()
                        ellipseRect2.normalize()
                        ellipseRect3.normalize()
                        ellipseRect4.normalize()
                        ellipseRect5.normalize()
                        ellipseRect6.normalize()
                        ellipseRect7.normalize()
                        ellipseRect8.normalize()
                        try:
                            draw.ellipse(screen,col2,ellipseRect,ellipsethicc)                            
                            draw.ellipse(screen,col2,ellipseRect1,ellipsethicc)
                            draw.ellipse(screen,col2,ellipseRect2,ellipsethicc)
                            draw.ellipse(screen,col2,ellipseRect3,ellipsethicc)
                            draw.ellipse(screen,col2,ellipseRect4,ellipsethicc)
                            draw.ellipse(screen,col2,ellipseRect5,ellipsethicc)
                            draw.ellipse(screen,col2,ellipseRect6,ellipsethicc)
                            draw.ellipse(screen,col2,ellipseRect7,ellipsethicc)
                            draw.ellipse(screen,col2,ellipseRect8,ellipsethicc)
                        except:
                            ellipseRect9=Rect(sx,sy,dx,dy)
                            ellipseRect9.normalize()
                            draw.ellipse(screen,col2,ellipseRect9)
                    if fill==1:
                        ellipseRect=Rect(sx,sy,dx,dy)
                        ellipseRect.normalize()
                        try:
                            draw.ellipse(screen,col2,ellipseRect)
                        except:
                            pass
            if tool=="brush":
                dx=mx-omx
                dy=my-omy
                dist=int(sqrt(dx**2+dy**2))
                for i in range(1,dist+1): #1,2,3,4.....
                    dotX=int(omx+i*dx/dist)
                    dotY=int(omy+i*dy/dist)
                    draw.circle(screen,col2,(dotX,dotY),brushthicc)
            if tool=="spray":
                sprayx=randint(mx-spraythicc,mx+spraythicc)
                sprayy=randint(my-spraythicc,my+spraythicc)
                if ((mx-sprayx)**2+(my-sprayy)**2)<=spraythicc**2:
                    draw.rect(screen,col2,(sprayx,sprayy,1,1),1)
            screen.set_clip(None)

    if tool=="polygon":
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            if mb[0]==1 and click:
                polyPoints.append(mx) #adding coordinated to list
                polyPoints.append(my)
                if len(polyPoints)>3: #draw line if 2 pairs of coordinates are available
                    draw.line(screen,col,(polyPoints[-4],polyPoints[-3]),(polyPoints[-2],polyPoints[-1]),2)
            if mb[2]==1 and click: #right click connects last dot to first
                if len(polyPoints)>3:
                    screen.blit(ss,(0,0))
                    draw.line(screen,col,(polyPoints[-2],polyPoints[-1]),(polyPoints[0],polyPoints[1]),2)
                    polyPoints=[]
            if mb[0]==0 and mb[2]==0: #preview of next line
                screen.blit(ss,(0,0))
                if len(polyPoints)>1:
                    draw.line(screen,col,(polyPoints[-2],polyPoints[-1]),(mx,my),2)
        else:
            if click: #clicking outside canvas resets list
                polyPoints=[]
            screen.set_clip(None)
            
    omx=mx #old mouse positions
    omy=my 
    display.flip()
quit()
