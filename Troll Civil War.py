import pygame
import time
import random

grey=(96,96,96)
bright_grey=(160,160,160)
red=(255,0,0)
orange=(255,128,0)

pygame.mixer.init()

Hit_Sound=pygame.mixer.Sound("Images/Hit_Sound.wav")

pygame.mixer.music.load("All Along the Watchtower.mp3")

pygame.mixer.music.play(-1)

screen_w=1900
screen_h=950

pygame.display.init()

info = pygame.display.Info()
screen_w = info.current_w
screen_h = info.current_h
screen=pygame.display.set_mode((screen_w,screen_h),pygame.RESIZABLE)

PlayerReady=pygame.image.load('Images/PlayerTrollRaised.png').convert_alpha()
EnemyReady=pygame.image.load('Images/EnemyTrollRaised.png').convert_alpha()
Player=pygame.image.load('Images/PlayerTroll.png').convert_alpha()
Enemy=pygame.image.load('Images/EnemyTroll.png').convert_alpha()

Float_Height=(screen_h/4)*3
Float_Height=round(Float_Height)
Height=int(Float_Height)

PlayerReady=pygame.transform.scale(PlayerReady,(int(Height/2),Height))
EnemyReady=pygame.transform.scale(EnemyReady,(int(Height/2),Height))
Player=pygame.transform.scale(Player,(int(Height/2),Height))
Enemy=pygame.transform.scale(Enemy,(int(Height/2),Height))

PlayerReady.set_colorkey(grey)
EnemyReady.set_colorkey(grey)
Player.set_colorkey(grey)
Enemy.set_colorkey(grey)

Logo=pygame.image.load('Images/Logo.png')
pygame.display.set_icon(Logo)

Background=pygame.image.load('Images/DungeonPicHigherRes.png').convert()
Background=pygame.transform.scale(Background,(screen_w,screen_h))

Top=''
Med=''
Bot=''

Attack=False
Menu=True
Health=5
Fish=0
Option=0
Level=4
EnemyHealth=5
Dodge=2
Person_Place=0
Player_y=(screen_h/12)*3
Paused=False
OriginalEnemyHealth=EnemyHealth
OriginalPlayerHeath=Health

FirstLetter='a'
SecondLetter='b'
LastLetter='c'

def Draw_Line(LineStartx,LineStarty,LineEndx,LineEndy,color):
    global screen
    LineStart=(LineStartx,LineStarty)
    LineEnd=(LineEndx,LineEndy)
    pygame.draw.line(screen,color,LineStart,LineEnd)
    return

def Draw_Rectangle(Rectx,Recty,Rectw,Recth,color):
    global screen
    pygame.draw.rect(screen,color,[Rectx,Recty,Rectw,Recth])
    return

def Write_Draw(msg,xcord,ycord,size):
    global screen
    global bright_grey
    global grey
    myfont = pygame.font.SysFont("twcencondensed",size)
    if msg=='Health: 1'or msg=='Enemy Health: 1'or msg=='Health: 2'or msg=='Enemy Health: 2'or msg=='Health: 0'or msg=='Enemy Health: 0':
        if msg=='Health: 1'or msg=='Enemy Health: 1'or msg=='Health: 0'or msg=='Enemy Health: 0':
            mytext = myfont.render(msg, True, red)
        if msg=='Health: 2'or msg=='Enemy Health: 2':
            mytext = myfont.render(msg, True, orange)
    else:
        mytext = myfont.render(msg, True, bright_grey)
    mytext = mytext.convert_alpha()
    xchange=mytext.get_width()
    xchange=xchange/2
    ychange=mytext.get_height()
    ychange=ychange/2
    if msg=='Quit' or msg=='Begin':
        Draw_Rectangle((xcord-xchange)-30,ycord-ychange,mytext.get_width()+60,mytext.get_height(),grey)
    else:
        Draw_Rectangle(xcord-xchange,ycord-ychange,mytext.get_width(),mytext.get_height(),grey)
    screen.blit(mytext,(xcord-xchange,ycord-ychange))
    pygame.display.flip()
    return

def Start_Menu_Setup():
    global OriginalEnemyHealth
    global OriginalPlayerHeath
    global Health
    global EnemyHealth
    global Level
    global Fish
    global Attack
    global Background
    global Menu
    global mainloop
    global Option
    global FirstLetter
    global SecondLetter
    global LastLetter
    Attack=False
    Menu=True
    mainloop=True
    pygame.init()
    pygame.display.set_caption("Troll Civil War")
    screen.blit(Background, (0,0))
    Write_Draw("Troll Civil War!",screen_w/2,screen_h/4,150)
    Write_Draw("- Begin -",screen_w/2,screen_h/4+screen_h/4,75)
    Write_Draw("Quit",screen_w/2,screen_h/2+screen_h/8,75)
    Write_Draw("Show game Controls (SPACE)",210,50,50)
    FirstLetter='a'
    SecondLetter='b'
    LastLetter='c'
    Health=OriginalPlayerHeath
    EnemyHealth=OriginalEnemyHealth
    Level=4
    Fish=0
    return

def PickingLetter(FeedLetter):
    global screen
    global Background
    global screen_w
    global screen_h
    global FirstLetter
    global SecondLetter
    global LastLetter
    Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    LetterNo=0
    Letter='a'
    LetterDone=False
    FirstLetterX=screen_w/7
    SecondLetterX=(screen_w/7)*3
    LastLetterX=(screen_w/7)*5
    if FeedLetter=='a':
        LetterX=FirstLetterX
    if FeedLetter=='b':
        LetterX=SecondLetterX
    if FeedLetter=='c':
        LetterX=LastLetterX
    screen.blit(Background,(0,0))
    Write_Draw("Name Selector",screen_w/2,screen_h/6,150)
    Write_Draw("press w or s to chose a letter or enter to select",screen_w/2,(screen_h/6)*5,50)
    Write_Draw(FirstLetter,FirstLetterX,screen_h/2,200)
    Write_Draw(SecondLetter,SecondLetterX,screen_h/2,200)
    Write_Draw(LastLetter,LastLetterX,screen_h/2,200)
    while LetterDone==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainloop=False
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    if LetterNo!=0:
                        LetterNo=LetterNo-1
                    else:
                        LetterNo=25
                    Letter=Letters[LetterNo]
                    screen.blit(Background,(0,0))
                    Write_Draw("Name Selector",screen_w/2,screen_h/6,150)
                    Write_Draw("press w or s to chose a letter or enter to select",screen_w/2,(screen_h/6)*5,50)
                    Write_Draw(FirstLetter,FirstLetterX,screen_h/2,200)
                    Write_Draw(SecondLetter,SecondLetterX,screen_h/2,200)
                    Write_Draw(LastLetter,LastLetterX,screen_h/2,200)
                    Write_Draw(Letter,LetterX,screen_h/2,200)
                if event.key==pygame.K_w:
                    if LetterNo!=25:
                        LetterNo=LetterNo+1
                    else:
                        LetterNo=0
                    Letter=Letters[LetterNo]
                    screen.blit(Background,(0,0))
                    Write_Draw("Name Selector",screen_w/2,screen_h/6,150)
                    Write_Draw("press w or s to chose a letter or enter to select",screen_w/2,(screen_h/6)*5,50)
                    Write_Draw(FirstLetter,FirstLetterX,screen_h/2,200)
                    Write_Draw(SecondLetter,SecondLetterX,screen_h/2,200)
                    Write_Draw(LastLetter,LastLetterX,screen_h/2,200)
                    Write_Draw(Letter,LetterX,screen_h/2,200)
                if event.key==pygame.K_RETURN:
                    if FeedLetter=='a':
                        FirstLetter=Letter
                        LetterDone=True
                    if FeedLetter=='b':
                        SecondLetter=Letter
                        LetterDone=True
                    if FeedLetter=='c':
                        LastLetter=Letter
                        LetterDone=True
                if event.key==pygame.K_ESCAPE:
                    mainloop=False
                    pygame.quit()
                    quit()
    return

def SaveNewResults(NewName,Pos):
    global Top
    global Med
    global Bot
    NewName=NewName+','+str(Fish)
    if Pos==4:
        Bot=Med
        Med=Top
        Top=NewName
    if Pos==5:
        Bot=Med
        Med=NewName
    if Pos==6:
        Bot=NewName
    savefile=open('ScoreBoard.txt','w')
    savefile.write(Top)
    savefile.write('\n')
    savefile.write(Med)
    savefile.write('\n')
    savefile.write(Bot)
    savefile.close()
    return

def Find_Place(No1,No2,No3):
    global Fish
    global Person_Place
    No1Fish=int(No1[4])
    No2Fish=int(No2[4])
    No3Fish=int(No3[4])
    if Fish>No3Fish:
        Person_Place=6
    if Fish>No2Fish:
        Person_Place=5
    if Fish>No1Fish:
        Person_Place=4
    if Fish<No3Fish:
        Person_Place=8
    return

def ScoreBoard(LuckyName):
    global Top
    global Med
    global Bot
    global Fish
    global Person_Place
    savefile=open('ScoreBoard.txt','r')
    file=savefile.read()
    List=file.split('\n')
    screen.blit(Background, (0,0))
    Write_Draw('Score Board',screen_w/2,screen_h/9*2,100)
    Top=List[0]
    Med=List[1]
    Bot=List[2]
    Find_Place(Top,Med,Bot)
    for item in List:
        Scorer=item.split(',')
        if item==Top:
            Place=4
        if item==Med:
            Place=5
        if item==Bot:
            Place=6
        if Place!=Person_Place:
            Write_Draw(str(Scorer[0])+' : '+str(Scorer[1])+' Fish',screen_w/2,(screen_h/9)*Place,75)
    Write_Draw(str(LuckyName+': '+str(Fish)+' Fish'),screen_w/2,screen_h/9*Person_Place,75)
    time.sleep(3)
    SaveNewResults(LuckyName,Person_Place)
    Start_Menu_Setup()
    return

def Get_Name():
    global FirstLetter
    global SecondLetter
    global LastLetter
    PickingLetter(FirstLetter)
    PickingLetter(SecondLetter)
    PickingLetter(LastLetter)
    Name=FirstLetter+SecondLetter+LastLetter
    Name=Name.upper()
    ScoreBoard(Name)
    return

def Dodgeing_Attack():
    global Dodge
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                Dodge=4
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                Dodge=2
    return

def Attacking(Changeable):
    global screen
    global Background
    global screen_h
    global screen_w
    global PlayerReady
    global Player
    global Enemy
    global EnemyReady
    global Health
    global EnemyHealth
    global Fish
    global Dodge
    global Player_y
    EnemyAttacking=''
    PlayerAttacking=''
    if Changeable==Player:
        PlayerAttacking=Changeable
        EnemyAttacking=EnemyReady
    if Changeable==Enemy:
        Changeable.set_colorkey(grey)
        EnemyAttacking=Changeable
        PlayerAttacking=PlayerReady
    Dodgeing_Attack()
    pygame.display.flip()
    screen.blit(Background, (0,0))
    screen.blit(PlayerReady,(screen_w/Dodge - PlayerReady.get_width(),Player_y))
    screen.blit(EnemyReady,(screen_w/2,Player_y))
    Write_Draw("Health: "+str(Health),100,50,50)
    Write_Draw("Fish: "+str(Fish),100,100,50)
    Write_Draw("Enemy Health: "+str(EnemyHealth),screen_w-150,50,50)
    time.sleep(0.2)
    Dodgeing_Attack()
    pygame.display.flip()
    screen.blit(Background, (0,0))
    screen.blit(PlayerAttacking,(screen_w/Dodge - PlayerReady.get_width(),Player_y))
    screen.blit(EnemyAttacking,(screen_w/2,Player_y))
    Write_Draw("Health: "+str(Health),100,50,50)
    Write_Draw("Fish: "+str(Fish),100,100,50)
    Write_Draw("Enemy Health: "+str(EnemyHealth),screen_w-150,50,50)
    pygame.mixer.Sound.play(Hit_Sound)
    time.sleep(0.2)
    Dodgeing_Attack()
    pygame.display.flip()
    screen.blit(Background, (0,0))
    screen.blit(PlayerReady,(screen_w/Dodge - PlayerReady.get_width(),Player_y))
    screen.blit(EnemyReady,(screen_w/2,Player_y))
    Write_Draw("Health: "+str(Health),100,50,50)
    Write_Draw("Fish: "+str(Fish),100,100,50)
    Write_Draw("Enemy Health: "+str(EnemyHealth),screen_w-150,50,50)
    return

def Enemy_Attack():
    global Level
    global Health
    global Enemy
    YesOrNo=random.randint(0,Level)
    if YesOrNo==1:
        Attacking(Enemy)
        if Dodge==2:
            Health=Health-1
    return

def AttackMovment():
    global Health
    global Fish
    global EnemyHealth
    global Background
    global screen
    global screen_h
    global screen_w
    global Player
    global PlayerReady
    global EnemyReady
    global Attack
    pygame.display.flip()
    if Attack==True:
        Attacking(Player)
        Attack=False
        EnemyHealth=EnemyHealth-1
        if EnemyHealth==0:
            Health=OriginalPlayerHeath
            Fish=Fish+1
            EnemyHealth=OriginalEnemyHealth+Fish
            Write_Draw("Next Round!",screen_w/2,screen_h/2,200)
            time.sleep(2)
            pygame.display.flip()
            Game_loop()
    else:
        pygame.display.flip()
        Enemy_Attack()
    return

def Game_loop():
    global screen
    global screen_h
    global screen_w
    global Background
    global PlayerReady
    global EnemyReady
    global Fish
    global Health
    global EnemyHealth
    global Level
    global Player_y
    screen.blit(Background, (0,0))
    screen.blit(PlayerReady,(screen_w/2 - PlayerReady.get_width(),Player_y))
    screen.blit(EnemyReady,(screen_w/2,Player_y))
    Write_Draw("Health: "+str(Health),100,50,50)
    Write_Draw("Fish: "+str(Fish),100,100,50)
    Write_Draw("Enemy Health: "+str(EnemyHealth),screen_w-150,50,50)
    pygame.display.flip()
    if Fish!=0:
        Level=3
    if Fish!=0 and Fish!=1:
        Level=2
    if Fish>2:
        Level=1
    if Health !=0:
        AttackMovment()
    else:
        Write_Draw("Defeated",screen_w/2,screen_h/2,200)
        time.sleep(3)
        Get_Name()
    return

def Pause():
    global mainloop
    global Paused
    global Background
    global screen
    global screen_h
    global screen_w
    screen.blit(Background,(0,0))
    pygame.mixer.music.pause()
    Write_Draw("Paused",screen_w/2,screen_h/2,200)
    while Paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
                Paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
                    Paused = False
                if event.key == pygame.K_SPACE:
                    Paused = False
                    pygame.mixer.music.unpause()
                    Game_loop()
    return

Start_Menu_Setup()

mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            if Menu:
                if Option==0:
                    if event.key == pygame.K_s:
                        Option=Option+1
                        screen.blit(Background, (0,0))
                        Write_Draw("Troll Civil War!",screen_w/2,screen_h/4,150)
                        Write_Draw("Begin",screen_w/2,screen_h/4+screen_h/4,75)
                        Write_Draw("- Quit -",screen_w/2,screen_h/2+screen_h/8,75)
                        Write_Draw("Show game Controls (SPACE)",210,50,50)
                    if event.key == pygame.K_RETURN:
                        Menu=False
                        Game_loop()
                else:
                    if event.key == pygame.K_w:
                        Option=Option-1
                        screen.blit(Background, (0,0))
                        Write_Draw("Troll Civil War!",screen_w/2,screen_h/4,150)
                        Write_Draw("- Begin -",screen_w/2,screen_h/4+screen_h/4,75)
                        Write_Draw("Quit",screen_w/2,screen_h/2+screen_h/8,75)
                        Write_Draw("Show game Controls (SPACE)",210,50,50)
                    if event.key == pygame.K_RETURN:
                        mainloop = False
                if event.key==pygame.K_SPACE:
                    screen.blit(Background, (0,0))
                    pygame.mixer.Sound.play(Hit_Sound)
                    Write_Draw("Game Controls",screen_w/2,screen_h/10,100)
                    Write_Draw("W/S - Up/Down",screen_w/2,(screen_h/10)*3,50)
                    Write_Draw("Escape - Quit",screen_w/2,(screen_h/10)*4,50)
                    Write_Draw("ENTER - Attack/Select",screen_w/2,(screen_h/10)*5,50)
                    Write_Draw("A - Dodge",screen_w/2,(screen_h/10)*6,50)
                    Write_Draw("Exit (W/S)",screen_w/4*3,(screen_h/10)*8,75)
                    Write_Draw("SPACE - Toggle Pause",screen_w/2,(screen_h/10)*7,50)
            else:
                if event.key == pygame.K_RETURN:
                    Attack = True
                    Game_loop()
                if EnemyHealth!=10:
                    Enemy_Attack()
                if event.key == pygame.K_SPACE:
                    if Health != 0:
                        Paused = True
                        Pause()
    pygame.display.flip()
pygame.quit()
