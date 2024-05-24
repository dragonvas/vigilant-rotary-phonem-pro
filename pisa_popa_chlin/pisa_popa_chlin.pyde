e=33
ee=33

q=0
w=200
eee=800
r=100

t=200
yy=0
u=20
i=150

o=350
p=0
a=200
s=10

d=420
f=10
g=10
h=90
j=0

k=700
l=400
z=20
xx=100

c=700
v=200
b=100
n=200

m=700
qq=500
ww=100
eeee=150

rr=800
tt=780
yyy=200
uu=20
ii=0

oo=500
pp=730
aa=200
ss=20

dd=400
ff=350
gg=50
hh=450

jj=450
kk=630
ll=100
zz=20

xxx=640
cc=350
vv=20
bb=300

nn=660
mm=400
qqq=40
www=2

eeeee=500
rrr=550
ttt=140
yyyy=20

uuu=450
iii=480
ooo=120
ppp=20

aaa=500
sss=400
ddd=140
fff=20

ggg=70
hhh=350
jjj=380
kkk=50   

lll=0
zzz=450
xxxx=200
ccc=10

vvv=250
bbb=450
nnn=100
mmm=10

qqqq=340
wwww=450
eeeeee=10
rrrr=100

tttt=250
yyyyy=590
uuuu=150
iiii=10

oooo=200
pppp=545
aaaa=140
ssss=5

ffff=250
gggg=550
hhhh=10
jjjj=50

dddd=190
kkkk=450
llll=10
zzzz=50

xxxxx=200
cccc=499
vvvv=100
bbbb=1

nnnn=80
mmmm=510
qqqqq=20
wwwww=220
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter): 
    testX = cx
    testY = cy
    if cx < rx:
        testX = rx
    elif cx > rx+rw:
        testX = rx+rw
    if cy < ry:
        testY = ry
    elif cy > ry+rh:
        testY = ry+rh
    distance = dist(cx,cy,testX,testY)
    if distance <= diameter/2:
        return True
    else:
        return False
def setup():
    size(1000,800)
def draw():
    global e,ee,j,g,h,f,ii,tt
    background(123,234,0)
    j=j+1
    ii=ii+1
    r1 = collideRectCircle(q,w,eee,r, e, ee, 30)
    r2 = collideRectCircle(0,0,1000,2, e, ee, 30)
    r3 = collideRectCircle(0,0,2,1000, e, ee, 30)
    r4 = collideRectCircle(0,798,1000,2, e, ee, 30)
    r5 = collideRectCircle(1000,0,2,1000, e, ee, 30)
    r6 = collideRectCircle(t,yy,u,i, e, ee, 30)
    r7 = collideRectCircle(o,p,a,s, e, ee, 30)
    r8 = collideRectCircle(o,p+100,a,s, e, ee, 30)
    r9 = collideRectCircle(d,f,g,h, e, ee, 30)
    r10 = collideRectCircle(k,l,z,xx, e, ee, 30)
    r11 = collideRectCircle(c,v,b,n, e, ee, 30)
    r12 = collideRectCircle(m,qq,ww,eeee, e, ee, 30)
    r13 = collideRectCircle(k,l+250,z,xx, e, ee, 30)
    r14 = collideRectCircle(rr,tt,yyy,uu, e, ee, 30)
    r15 = collideRectCircle(oo,pp,aa,ss, e, ee, 30)
    r16 = collideRectCircle(dd,ff,gg,hh, e, ee, 30)
    r17 = collideRectCircle(jj,kk,ll,zz, e, ee, 30)
    r18 = collideRectCircle(xxx,cc,vv,bb, e, ee, 30)
    r19 = collideRectCircle(nn,mm,qqq,www, e, ee, 30)
    r20 = collideRectCircle(eeeee,rrr,ttt,yyyy, e, ee, 30)
    r21 = collideRectCircle(uuu,iii,ooo,ppp, e, ee, 30)
    r22 = collideRectCircle(aaa,sss,ddd,fff, e, ee, 30)
    r23 = collideRectCircle(ggg,hhh,jjj,kkk, e, ee, 30)
    r24 = collideRectCircle(lll,zzz,xxxx,ccc, e, ee, 30)
    r25 = collideRectCircle(vvv,bbb,nnn,mmm, e, ee, 30)
    r26 = collideRectCircle(qqqq,wwww,eeeeee,rrrr, e, ee, 30)
    r27 = collideRectCircle(tttt,yyyyy,uuuu,iiii, e, ee, 30)
    r28 = collideRectCircle(oooo,pppp,aaaa,ssss, e, ee, 30)
    r29 = collideRectCircle(ffff,gggg,hhhh,jjjj, e, ee, 30)
    r30 = collideRectCircle(dddd,kkkk,llll,zzzz, e, ee, 30)
    r31 = collideRectCircle(xxxxx,cccc,vvvv,bbbb, e, ee, 30)
    r32 = collideRectCircle(nnnn,mmmm,qqqqq,wwwww, e, ee, 30)
    rect(q,w,eee,r)
    rect(t,yy,u,i)
    rect(o,p,a,s)
    rect(o,p+100,a,s)
    rect(d,f,g,h)
    rect(c,v,b,n)
    rect(k,l,z,xx)
    rect(m,qq,ww,eeee)
    rect(k,l+250,z,xx)
    rect(rr,tt,yyy,uu)
    rect(oo,pp,aa,ss)
    rect(dd,ff,gg,hh)
    rect(jj,kk,ll,zz)
    rect(xxx,cc,vv,bb)
    rect(tttt,yyyyy,uuuu,iiii)
    rect(oooo,pppp,aaaa,ssss)
    noStroke()
    fill(123,234,150)
    rect(nn,mm,qqq,www)
    fill(255,255,255)
    stroke(0,0,0)
    rect(eeeee,rrr,ttt,yyyy)
    rect(uuu,iii,ooo,ppp)
    rect(aaa,sss,ddd,fff)
    rect(ggg,hhh,jjj,kkk)
    rect(lll,zzz,xxxx,ccc)
    rect(vvv,bbb,nnn,mmm)
    rect(qqqq,wwww,eeeeee,rrrr)
    rect(oooo,pppp,aaaa,ssss)
    rect(ffff,gggg,hhhh,jjjj)
    rect(dddd,kkkk,llll,zzzz)
    rect(xxxxx,cccc,vvvv,bbbb)
    rect(nnnn,mmmm,qqqqq,wwwww)
    ellipse(e, ee, 30, 30)
    colide = r1 or r2 or r3 or r4 or r5 or r6 or r7 or r8 or r9 or r10 or r11 or r12 or r13 or r14 or r15 or r16 or r17 or r18 or r19 or r20 or r21 or r22 or r23 or r24 or r25 or r26 or r27 or r28 or r29 or r30 or r31 or r32
    if colide == True:
        e=33
        ee=33
    if j > 150:
        f=110
    if j > 300:
        f=10
        j=0
    if ii > 0:
        tt=tt-3
    if ii > 312:
        tt=780
        ii=0
    if keyPressed:
        if keyCode == UP:
            ee=ee-3
        if keyCode == DOWN:
            ee=ee+3
        if keyCode == LEFT:
            e=e-3
        if keyCode == RIGHT:
            e=e+3
