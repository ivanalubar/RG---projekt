from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.WGL import *
import win32ui
import sys

r,g,b=1,1,1
sirina, visina =500,500
polje_sirina=2.0
polje_visina=2.0
x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 = 10,3,-6,-9,17,19,7,13,14,23
y0,y1,y2,y3,y4,y5,y6,y7,y8,y9= 15,25,19,35,18,29,14,39,13,23
x10=40
y10=35
x11,x12,x13,x14,x15,x16,x17,x18,x19 = 15,25,19,35,18,29,14,39,13
y11,y12,y13,y14,y15,y16,y17,y18,y19= 10,33,-6,-9,37,49,47,53,64
i,j = 1, 1
x=b'\170'
y=b'\171'
z=b'\172'
w=b'\167'

def BuildFont():
    global base
    wgldc = wglGetCurrentDC()
    hDC = win32ui.CreateDCFromHandle(wgldc)
    base = glGenLists(96);
    font_properties = { "name" : "Arial",
                        "width" : 10,
                        "height" : 40,
                        "weight" : 900
        }
    font = win32ui.CreateFont(font_properties)
    oldfont = hDC.SelectObject(font)
    wglUseFontBitmaps(wgldc, 32, 96, base)
    hDC.SelectObject(oldfont)

def glPrint(str):
    global base
    glPushAttrib(GL_LIST_BIT);
    glListBase(base - 32);
    glCallLists(str)
    glPopAttrib();

def igraliste2d(sirina,visina, polje_sirina, polje_visina):
    glViewport(0,0,sirina,visina)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,50.0, 0.0, 50.0, 0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def crtajkvadrat(x,y,sirina,visina):
    glBegin(GL_QUADS)
    glVertex2f(x,y)
    glVertex2f(x+sirina,y)
    glVertex2f(x+sirina,y+visina)
    glVertex2f(x,y+visina)
    glEnd()

def crtaj_zvijezde():
    global x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,x10, y10,x11,x12,x13,x14,x15,x16,x17,x18,x19, y11,y12,y13,y14,y15,y16,y17,y18,y19
    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 = 10,3,-6,-9,17,19,7,13,14,23
    y0,y1,y2,y3,y4,y5,y6,y7,y8,y9= 25,35,39,35,28,29,44,39,53,23
    x10=40
    y10=37
    x11,x12,x13,x14,x15,x16,x17,x18,x19 = 15,25,19,35,18,29,14,39,13
    y11,y12,y13,y14,y15,y16,y17,y18,y19= 30,33,46,39,37,49,47,53,64
    glColor3f(1,1,0)
    crtajkvadrat(x0,y0,1,1)
    crtajkvadrat(x1,y1,1,1)
    crtajkvadrat(x2,y2,1,1)
    crtajkvadrat(x3,y3,1,1)
    crtajkvadrat(x4,y4,1,1)
    crtajkvadrat(x5,y5,1,1)
    crtajkvadrat(x6,y6,1,1)
    crtajkvadrat(x7,y7,1,1)
    crtajkvadrat(x8,y8,1,1)
    crtajkvadrat(x9,y9,1,1)
    crtajkvadrat(x10,y10,1,1)
    crtajkvadrat(x11,y11,1,1)
    crtajkvadrat(x12,y12,1,1)
    crtajkvadrat(x13,y13,1,1)
    crtajkvadrat(x14,y14,1,1)
    crtajkvadrat(x15,y15,1,1)
    crtajkvadrat(x16,y16,1,1)
    crtajkvadrat(x17,y17,1,1)
    crtajkvadrat(x18,y18,1,1)
    crtajkvadrat(x19,y19,1,1)

def crtaj_snijeg():
    global x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,x10, y10,x11,x12,x13,x14,x15,x16,x17,x18,x19, y11,y12,y13,y14,y15,y16,y17,y18,y19
    glColor3f(1,1,1)
    crtajkvadrat(x0,y0,1,1)
    crtajkvadrat(x1,y1,1,1)
    crtajkvadrat(x2,y2,1,1)
    crtajkvadrat(x3,y3,1,1)
    crtajkvadrat(x4,y4,1,1)
    crtajkvadrat(x5,y5,1,1)
    crtajkvadrat(x6,y6,1,1)
    crtajkvadrat(x7,y7,1,1)
    crtajkvadrat(x8,y8,1,1)
    crtajkvadrat(x9,y9,1,1)
    crtajkvadrat(x10,y10,1,1)
    crtajkvadrat(x11,y11,1,1)
    crtajkvadrat(x12,y12,1,1)
    crtajkvadrat(x13,y13,1,1)
    crtajkvadrat(x14,y14,1,1)
    crtajkvadrat(x15,y15,1,1)
    crtajkvadrat(x16,y16,1,1)
    crtajkvadrat(x17,y17,1,1)
    crtajkvadrat(x18,y18,1,1)
    crtajkvadrat(x19,y19,1,1)
    x0=x0+0.02*0
    y0=y0+0.02* -1
    x1=x1+0.02*0
    y1=y1+0.02* -1
    x2=x2+0.02*0
    y2=y2+0.02* -1
    x3=x3+0.02*0
    y3=y3+0.02* -1
    x4=x4+0.02*0
    y4=y4+0.02* -1
    x5=x5+0.02*0
    y5=y5+0.02* -1
    x6=x6+0.02*0
    y6=y6+0.02* -1
    x7=x7+0.02*0
    y7=y7+0.02* -1
    x8=x8+0.02*0
    y8=y8+0.02* -1
    x9=x9+0.02*0
    y9=y9+0.02* -1
    x10=x10+0.02*0
    y10=y10+0.02* -1
    x11=x11+0.02*0
    y11=y11+0.02* -1
    x12=x12+0.02*0
    y12=y12+0.02* -1
    x13=x13+0.02*0
    y13=y13+0.02* -1
    x14=x14+0.02*0
    y14=y14+0.02* -1
    x15=x15+0.02*0
    y15=y15+0.02* -1
    x16=x16+0.02*0
    y16=y16+0.02* -1
    x17=x17+0.02*0
    y17=y17+0.02* -1
    x18=x18+0.02*0
    y18=y18+0.02* -1
    x19=x19+0.02*0
    y19=y19+0.02* -1

def crtaj_kisu():
    global x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,x10, y10,x11,x12,x13,x14,x15,x16,x17,x18,x19, y11,y12,y13,y14,y15,y16,y17,y18,y19
    glColor3f(0.8,0.9,0.9)
    crtajkvadrat(x0,y0,1,1)
    crtajkvadrat(x1,y1,1,1)
    crtajkvadrat(x2,y2,1,1)
    crtajkvadrat(x3,y3,1,1)
    crtajkvadrat(x4,y4,1,1)
    crtajkvadrat(x5,y5,1,1)
    crtajkvadrat(x6,y6,1,1)
    crtajkvadrat(x7,y7,1,1)
    crtajkvadrat(x8,y8,1,1)
    crtajkvadrat(x9,y9,1,1)
    crtajkvadrat(x10,y10,1,1)
    crtajkvadrat(x11,y11,1,1)
    crtajkvadrat(x12,y12,1,1)
    crtajkvadrat(x13,y13,1,1)
    crtajkvadrat(x14,y14,1,1)
    crtajkvadrat(x15,y15,1,1)
    crtajkvadrat(x16,y16,1,1)
    crtajkvadrat(x17,y17,1,1)
    crtajkvadrat(x18,y18,1,1)
    crtajkvadrat(x19,y19,1,1)
    x0=x0+0.02*0
    y0=y0+0.02* -1
    x1=x1+0.02*0
    y1=y1+0.02* -1
    x2=x2+0.02*0
    y2=y2+0.02* -1
    x3=x3+0.02*0
    y3=y3+0.02* -1
    x4=x4+0.02*0
    y4=y4+0.02* -1
    x5=x5+0.02*0
    y5=y5+0.02* -1
    x6=x6+0.02*0
    y6=y6+0.02* -1
    x7=x7+0.02*0
    y7=y7+0.02* -1
    x8=x8+0.02*0
    y8=y8+0.02* -1
    x9=x9+0.02*0
    y9=y9+0.02* -1
    x10=x10+0.02*0
    y10=y10+0.02* -1
    x11=x11+0.02*0
    y11=y11+0.02* -1
    x12=x12+0.02*0
    y12=y12+0.02* -1
    x13=x13+0.02*0
    y13=y13+0.02* -1
    x14=x14+0.02*0
    y14=y14+0.02* -1
    x15=x15+0.02*0
    y15=y15+0.02* -1
    x16=x16+0.02*0
    y16=y16+0.02* -1
    x17=x17+0.02*0
    y17=y17+0.02* -1
    x18=x18+0.02*0
    y18=y18+0.02* -1
    x19=x19+0.02*0
    y19=y19+0.02* -1

def crtaj_krov():
    glColor3f(1,0,0)
    crtajkvadrat(29,19,1,1)
    crtajkvadrat(30,20,1,1)
    crtajkvadrat(31,21,1,1)
    crtajkvadrat(32,22,1,1)
    crtajkvadrat(33,23,1,1)
    crtajkvadrat(34,24,1,1)
    crtajkvadrat(35,25,1,1)
    
    crtajkvadrat(36,24,1,1)
    crtajkvadrat(37,23,1,1)
    crtajkvadrat(38,22,1,1)
    crtajkvadrat(39,21,1,1)
    crtajkvadrat(40,20,1,1)
    crtajkvadrat(41,19,1,1)

def crtaj_kucu():
    glColor3f(1,0,1)
    
    crtajkvadrat(30,19,1,1)
    crtajkvadrat(31,20,1,1)
    crtajkvadrat(32,21,1,1)
    crtajkvadrat(33,22,1,1)
    crtajkvadrat(34,23,1,1)
    crtajkvadrat(35,24,1,1)
    crtajkvadrat(36,23,1,1)
    crtajkvadrat(37,22,1,1)
    crtajkvadrat(38,21,1,1)
    crtajkvadrat(39,20,1,1)
    crtajkvadrat(40,19,1,1)

    crtajkvadrat(30,18,1,1)
    crtajkvadrat(31,19,1,1)
    crtajkvadrat(32,20,1,1)
    crtajkvadrat(33,21,1,1)
    crtajkvadrat(34,22,1,1)
    crtajkvadrat(35,23,1,1)
    crtajkvadrat(36,22,1,1)
    crtajkvadrat(37,21,1,1)
    crtajkvadrat(38,20,1,1)
    crtajkvadrat(39,19,1,1)
    crtajkvadrat(40,18,1,1)

    crtajkvadrat(30,17,1,1)
    crtajkvadrat(31,18,1,1)
    crtajkvadrat(32,19,1,1)
    crtajkvadrat(33,20,1,1)
    crtajkvadrat(34,21,1,1)
    crtajkvadrat(35,22,1,1)
    crtajkvadrat(36,21,1,1)
    crtajkvadrat(37,20,1,1)
    crtajkvadrat(38,19,1,1)
    crtajkvadrat(39,18,1,1)
    crtajkvadrat(40,17,1,1)

    crtajkvadrat(30,16,1,1)
    crtajkvadrat(31,17,1,1)
    crtajkvadrat(32,18,1,1)
    crtajkvadrat(33,19,1,1)
    crtajkvadrat(34,20,1,1)
    crtajkvadrat(35,21,1,1)
    crtajkvadrat(36,20,1,1)
    crtajkvadrat(37,19,1,1)
    crtajkvadrat(38,18,1,1)
    crtajkvadrat(39,17,1,1)
    crtajkvadrat(40,16,1,1)

    crtajkvadrat(30,15,1,1)
    crtajkvadrat(31,16,1,1)
    crtajkvadrat(32,17,1,1)
    crtajkvadrat(33,18,1,1)
    crtajkvadrat(34,19,1,1)
    crtajkvadrat(35,20,1,1)
    crtajkvadrat(36,19,1,1)
    crtajkvadrat(37,18,1,1)
    crtajkvadrat(38,17,1,1)
    crtajkvadrat(39,16,1,1)
    crtajkvadrat(40,15,1,1)

    crtajkvadrat(30,14,1,1)
    crtajkvadrat(31,15,1,1)
    crtajkvadrat(32,16,1,1)
    crtajkvadrat(33,17,1,1)
    crtajkvadrat(34,18,1,1)
    crtajkvadrat(35,19,1,1)
    crtajkvadrat(36,18,1,1)
    crtajkvadrat(37,17,1,1)
    crtajkvadrat(38,16,1,1)
    crtajkvadrat(39,15,1,1)
    crtajkvadrat(40,14,1,1)

    crtajkvadrat(31,14,1,1)
    crtajkvadrat(32,15,1,1)
    crtajkvadrat(33,16,1,1)
    crtajkvadrat(34,17,1,1)
    crtajkvadrat(35,18,1,1)
    crtajkvadrat(36,17,1,1)
    crtajkvadrat(37,16,1,1)
    crtajkvadrat(38,15,1,1)
    crtajkvadrat(39,14,1,1)

    crtajkvadrat(32,14,1,1)
    crtajkvadrat(33,15,1,1)
    crtajkvadrat(34,16,1,1)
    crtajkvadrat(35,17,1,1)
    crtajkvadrat(36,16,1,1)
    crtajkvadrat(37,15,1,1)
    crtajkvadrat(38,14,1,1)
    
    crtajkvadrat(33,14,1,1)
    crtajkvadrat(34,15,1,1)
    crtajkvadrat(35,16,1,1)

    crtajkvadrat(34,14,1,1)
    crtajkvadrat(35,15,1,1)
    crtajkvadrat(35,14,1,1)

def crtaj_vrata():
    glColor3f(0,0,0.1)
    crtajkvadrat(36,16,1,1)
    crtajkvadrat(37,15,1,1)
    crtajkvadrat(38,14,1,1)
    crtajkvadrat(36,14,1,1)
    crtajkvadrat(37,14,1,1)
    crtajkvadrat(36,15,1,1)
    crtajkvadrat(37,16,1,1)
    crtajkvadrat(38,16,1,1)
    crtajkvadrat(38,15,1,1)
    crtajkvadrat(36,17,1,1)
    crtajkvadrat(37,17,1,1)
    crtajkvadrat(38,17,1,1)
    crtajkvadrat(36,18,1,1)
    crtajkvadrat(37,18,1,1)
    crtajkvadrat(38,18,1,1)
    
def crtaj_prozor():
    glColor3f(0,1,1)
    crtajkvadrat(32,18,1,1)
    crtajkvadrat(33,18,1,1)
    crtajkvadrat(32,17,1,1)
    crtajkvadrat(33,17,1,1)

def crtaj_proljece():
    glColor3f(0,1,0)
    for i in range(50):
        for j in range(17,-1,-1):
            crtajkvadrat(i,j,1,1)
    crtaj_cvijet()
    crtaj_bor()

def crtaj_ljeto():
    glColor3f(0,0.7,0)
    for i in range(50):
        for j in range(17,-1,-1):
            crtajkvadrat(i,j,1,1)
    crtaj_cvijet()
    crtaj_bor()
    crtaj_zvijezde()
    

def crtaj_jesen():
    glColor3f(0,0.9,0)
    for i in range(50):
        for j in range(17,-1,-1):
            crtajkvadrat(i,j,1,1)
    crtaj_bor()
    crtaj_kisu()
            
def crtaj_zimu():
    crtaj_borZ()
    crtaj_snijeg()
    glColor3f(1,1,1)
    for i in range(50):
        for j in range(17,-1,-1):
            crtajkvadrat(i,j,1,1)
    crtaj_borZ()
    



def crtaj_cvijet():
    glColor3f(1,0,0)
    crtajkvadrat(10,10,1,1)
    crtajkvadrat(11,11,1,1)
    crtajkvadrat(10,12,1,1)
    crtajkvadrat(9,11,1,1)
    glColor3f(1,1,0)
    crtajkvadrat(10,11,1,1)

    glColor3f(1,0,0)
    crtajkvadrat(15,13,1,1)
    crtajkvadrat(16,14,1,1)
    crtajkvadrat(15,15,1,1)
    crtajkvadrat(14,14,1,1)
    glColor3f(1,1,0)
    crtajkvadrat(15,14,1,1)

    glColor3f(1,0,0)
    crtajkvadrat(20,3,1,1)
    crtajkvadrat(21,4,1,1)
    crtajkvadrat(20,5,1,1)
    crtajkvadrat(19,4,1,1)
    glColor3f(1,1,0)
    crtajkvadrat(20,4,1,1)

    glColor3f(1,0,0)
    crtajkvadrat(4,4,1,1)
    crtajkvadrat(5,5,1,1)
    crtajkvadrat(4,6,1,1)
    crtajkvadrat(3,5,1,1)
    glColor3f(1,1,0)
    crtajkvadrat(4,5,1,1)

    glColor3f(1,0,0)
    crtajkvadrat(34,7,1,1)
    crtajkvadrat(35,8,1,1)
    crtajkvadrat(34,9,1,1)
    crtajkvadrat(33,8,1,1)
    glColor3f(1,1,0)
    crtajkvadrat(34,8,1,1)

    glColor3f(1,0,0)
    crtajkvadrat(44,10,1,1)
    crtajkvadrat(45,11,1,1)
    crtajkvadrat(44,12,1,1)
    crtajkvadrat(43,11,1,1)
    glColor3f(1,1,0)
    crtajkvadrat(44,11,1,1)

def crtaj_bor():
    glColor3f(0,0.6,0)
    for i in range(3,8,1):
        for j in range(16,23,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(5,15,1,1)
    
    glColor3f(0,0.6,0)
    for i in range(19,24,1):
        for j in range(15,22,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(21,14,1,1)
    glColor3f(0,0.6,0)
    for i in range(43,48,1):
        for j in range(16,23,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(45,15,1,1)
    glColor3f(0,0.6,0)
    for i in range(11,16,1):
        for j in range(17,24,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(13,16,1,1)

def crtaj_borZ():
    glColor3f(0,0.6,0)
    for i in range(3,8,1):
        for j in range(16,22,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(1,1,1)
    crtajkvadrat(3,22,1,1)
    crtajkvadrat(4,22,1,1)
    crtajkvadrat(5,22,1,1)
    crtajkvadrat(6,22,1,1)
    crtajkvadrat(7,22,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(5,15,1,1)
    
    glColor3f(0,0.6,0)
    for i in range(19,24,1):
        for j in range(15,22,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(1,1,1)
    crtajkvadrat(19,22,1,1)
    crtajkvadrat(20,22,1,1)
    crtajkvadrat(21,22,1,1)
    crtajkvadrat(22,22,1,1)
    crtajkvadrat(23,22,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(21,14,1,1)
    glColor3f(0,0.6,0)
    for i in range(43,48,1):
        for j in range(16,23,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(1,1,1)
    crtajkvadrat(43,23,1,1)
    crtajkvadrat(44,23,1,1)
    crtajkvadrat(45,23,1,1)
    crtajkvadrat(46,23,1,1)
    crtajkvadrat(47,23,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(45,15,1,1)
    glColor3f(0,0.6,0)
    for i in range(11,16,1):
        for j in range(17,24,1):
            crtajkvadrat(i,j,1,1)
    glColor3f(1,1,1)
    crtajkvadrat(11,24,1,1)
    crtajkvadrat(12,24,1,1)
    crtajkvadrat(13,24,1,1)
    crtajkvadrat(14,24,1,1)
    crtajkvadrat(15,24,1,1)
    glColor3f(0,0.2,0)
    crtajkvadrat(13,16,1,1)

def crtaj_sunce():
    glColor3f(1,1,0)
    crtajkvadrat(34,44,1,1)
    crtajkvadrat(35,45,1,1)
    crtajkvadrat(36,45,1,1)
    crtajkvadrat(37,44,1,1)
    crtajkvadrat(38,44,1,1)
    crtajkvadrat(39,44,1,1)
    crtajkvadrat(40,44,1,1)

    crtajkvadrat(35,44,1,1)
    crtajkvadrat(36,44,1,1)
    crtajkvadrat(37,45,1,1)
    crtajkvadrat(38,45,1,1)
    crtajkvadrat(39,45,1,1)

    crtajkvadrat(36,46,1,1)
    crtajkvadrat(37,46,1,1)
    crtajkvadrat(38,46,1,1)

    crtajkvadrat(35,43,1,1)
    crtajkvadrat(36,43,1,1)
    crtajkvadrat(37,43,1,1)
    crtajkvadrat(38,43,1,1)
    crtajkvadrat(39,43,1,1)

    crtajkvadrat(36,42,1,1)
    crtajkvadrat(37,42,1,1)
    crtajkvadrat(38,42,1,1)

    crtajkvadrat(37,41,1,1)
    crtajkvadrat(37,47,1,1)

def keyPressed(*args):
        
    if args[0] == x:
        glutDisplayFunc(drawProljece)
        glutIdleFunc(drawProljece)

    if args[0] == y:
        glutDisplayFunc(drawZimu)
        glutIdleFunc(drawZimu)
        
    if args[0] == z:
        glutDisplayFunc(drawJesen)
        glutIdleFunc(drawJesen)
        
    if args[0] == w:
        glutDisplayFunc(drawJesen)
        glutIdleFunc(drawLjeto)
        

def drawZimu():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 1.0, 1.0)
    glLoadIdentity()
    igraliste2d(sirina,visina,polje_sirina,polje_visina)
    crtaj_krov()
    crtaj_zimu()
    crtaj_kucu()
    crtaj_prozor()
    crtaj_vrata()
    glRasterPos2f(40, 5)
    glPrint(b'Zima')
    glutSwapBuffers()

def drawProljece():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.9, 0.0)
    glLoadIdentity()
    igraliste2d(sirina,visina,polje_sirina,polje_visina)
    crtaj_krov()
    crtaj_proljece()
    crtaj_kucu()
    crtaj_prozor()
    crtaj_vrata()
    crtaj_sunce()
    glRasterPos2f(40, 5)
    glPrint(b'Proljece')
    glutSwapBuffers()

def drawJesen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.8, 0.0)
    glLoadIdentity()
    igraliste2d(sirina,visina,polje_sirina,polje_visina)
    crtaj_krov()
    crtaj_jesen()
    crtaj_kucu()
    crtaj_prozor()
    crtaj_vrata()
    glRasterPos2f(40, 5)
    glPrint(b'Jesen')
    glutSwapBuffers()

def drawLjeto():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.5, 0.0)
    glLoadIdentity()
    igraliste2d(sirina,visina,polje_sirina,polje_visina)
    crtaj_krov()
    crtaj_ljeto()
    crtaj_kucu()
    crtaj_prozor()
    crtaj_vrata()
    glRasterPos2f(40, 5)
    glPrint(b'Ljetna noc')
    glutSwapBuffers()
    
    

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(sirina,visina)
glutInitWindowPosition(0,0)
window=glutCreateWindow(b'Racunalna grafika- Projekt')
glutDisplayFunc(drawProljece)
glutIdleFunc(drawProljece)
glutKeyboardFunc(keyPressed)
BuildFont()
glutMainLoop()
