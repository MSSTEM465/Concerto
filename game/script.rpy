define e = Character("Eileen")
define q = Character("???")
define allC = Character("Everyone")

define d = Character("Daniel")
define j = Character("Jay")
define ja = Character("Jack")
define a = Character("Alex")
define s = Character("Spencer")
define r = Character("Competition Manager")

image testWhite = Image("white.jpg")
image testTransition = Image("transition.png")
image testBlue = Image("babyblue.png")
image dorm room = Image("danDorm1.png",oversample=1.5)
image 427 = Image("427.png",oversample=1.5)
image outside427 = Image("outside427.png",oversample=1.5)
image beach = Image("beach.png",oversample=1.5)
image pier = Image("pier.png",oversample=1.5)
image ice cream shop = Image("ice cream shop.png",oversample=1.5)
image beach stage = Image("stage.png",oversample=1.5)
image stage = Image("showstage.png",oversample=1.5)
image waiting room = Image("waitingroom.png",oversample=1.5)
image bulletin = Image("bullet.png",oversample=1.5)

#Characters
image jay talking = Image("jaytalk.png", oversample=1.75)
image jay talking flip = Transform(Image("jaytalk.png",oversample=1.75), xzoom=-1)
image jay idle = Image("jay.png", oversample=1.75)
image jay idle flip = Transform(Image("jay.png",oversample=1.75), xzoom=-1)
image jay talk point = Image("jaytalkpoint.png",oversample=1.75)
image jay talk point flip = Transform(Image("jaytalkpoint.png",oversample=1.75), xzoom=-1)
image jay talk tired = Image("jaytalktired.png",oversample=1.75)
image jay talk tired flip = Transform(Image("jaytalktired.png",oversample=1.75), xzoom=-1)

image daniel idle = Image("dan.png", oversample=1.75)
image daniel idle flip = Transform(Image("dan.png",oversample=1.75),xzoom=-1)
image daniel talking = Image("dantalk.png", oversample=1.75)
image daniel talking flip = Transform(Image("dantalk.png",oversample=1.75),xzoom=-1)
image daniel talk confused = Image("dantalkconfused.png",oversample=1.75)
image daniel talk confused flip = Transform(Image("dantalkconfused.png",oversample=1.75),xzoom=-1)
image daniel talk embarrassed = Image("dantalkembarrased.png",oversample=1.75)
image daniel talk embarrassed flip = Transform(Image("dantalkembarrased.png",oversample=1.75),xzoom=-1)
image daniel talk sad = Image("dantalksad.png",oversample=1.75)
image daniel talk sad flip = Transform(Image("dantalksad.png",oversample=1.75),xzoom=-1)
image daniel talk scoff = Image("dantalkscoff.png",oversample=1.75)
image daniel talk scoff flip = Transform(Image("dantalkscoff.png",oversample=1.75),xzoom=-1)
image daniel talk shocked = Image("dantalkshocked.png",oversample=1.75)
image daniel talk shocked flip = Transform(Image("dantalkshocked.png",oversample=1.75),xzoom=-1)
image daniel wave = Image("danwave.png",oversample=1.75)
image daniel wave flip = Transform(Image("danwave.png",oversample=1.75),xzoom=-1)

image alex idle = Image("alex.png", oversample=1.75)
image alex idle flip = Transform(Image("alex.png",oversample=1.75),xzoom=-1)
image alex talk = Image("alextalk.png", oversample=1.75)
image alex talk flip = Transform(Image("alextalk.png",oversample=1.75),xzoom=-1)
image alex talk applaude = Image("alextalkapplaude.png", oversample=1.75)
image alex talk applaude flip = Transform(Image("alextalkapplaude.png",oversample=1.75),xzoom=-1)
image alex talk happy = Image("alextalkhappy.png", oversample=1.75)
image alex talk happy flip = Transform(Image("alextalkhappy.png",oversample=1.75),xzoom=-1)
image alex talk wonder = Image("alextalkwonder.png", oversample=1.75)
image alex talk wonder flip = Transform(Image("alextalkwonder.png",oversample=1.75),xzoom=-1)
image alex wave = Image("alexwave.png", oversample=1.75)
image alex wave flip = Transform(Image("alexwave.png",oversample=1.75),xzoom=-1)

image hostess idle = Image("hostess.png", oversample=1.75)
image hostess idle flip = Transform(Image("hostess.png",oversample=1.75),xzoom=-1)
image hostess talk = Image("hostesstalk.png", oversample=1.75)
image hostess talk flip = Transform(Image("hostesstalk.png",oversample=1.75),xzoom=-1)
image hostess giggle = Image("hostessgiggle.png", oversample=1.75)
image hostess giggle flip = Transform(Image("hostessgiggle.png",oversample=1.75),xzoom=-1)

image jack idle = Image("jack.png", oversample=1.75)
image jack idle flip = Transform(Image("jack.png",oversample=1.75),xzoom=-1)
image jack talk = Image("jacktalk.png", oversample=1.75)
image jack talk flip = Transform(Image("jacktalk.png",oversample=1.75),xzoom=-1)
image jack listen = Image("jacklisten.png", oversample=1.75)
image jack listen flip = Transform(Image("jacklisten.png",oversample=1.75),xzoom=-1)
image jack talk curious = Image("jacktalkcurious.png", oversample=1.75)
image jack talk curious flip = Transform(Image("jacktalkcurious.png",oversample=1.75),xzoom=-1)
image jack talk pumped = Image("jacktalkpumped.png", oversample=1.75)
image jack talk pumped flip = Transform(Image("jacktalkpumped.png",oversample=1.75),xzoom=-1)
image jack talk surprise = Image("jacktalksurprise.png", oversample=1.75)
image jack talk surprise flip = Transform(Image("jacktalksurprise.png",oversample=1.75),xzoom=-1)
image jack wave = Image("jackwave.png", oversample=1.75)
image jack wave flip = Transform(Image("jackwave.png",oversample=1.75),xzoom=-1)
image jack yell = Image("jackyell.png", oversample=1.75)
image jack yell flip = Transform(Image("jackyell.png",oversample=1.75),xzoom=-1)

image spencer idle = Image("spencer.png", oversample=1.75)
image spencer idle flip = Transform(Image("spencer.png",oversample=1.75),xzoom=-1)
image spencer talk = Image("spencertalk.png", oversample=1.75)
image spencer talk flip = Transform(Image("spencertalk.png",oversample=1.75),xzoom=-1)
image spencer talk pumped = Image("spencertalkpumped.png", oversample=1.75)
image spencer talk pumped flip = Transform(Image("spencertalkpumped.png",oversample=1.75),xzoom=-1)
image spencer talk wonder = Image("spencertalkwonder.png", oversample=1.75)
image spencer talk wonder flip = Transform(Image("spencertalkwonder.png",oversample=1.75),xzoom=-1)
image spencer wave = Image("spencerwave.png", oversample=1.75)
image spencer wave flip = Transform(Image("spencerwave.png",oversample=1.75),xzoom=-1)




# define the song titles and their files
init python:
    # must be persistent to be able to record the scores
    # after adding new songs, please remember to delete the persistent data
    #default renpyscore = 0
    newgameplus = True
    rhythm_game_songs = [
    Song('Tutorial Song', 'audio/tutRiff.mp3', 'audio/beatsRiff.txt', "audio/lanesRiff.txt",1),
    Song('Rumble | Vs. Jack', 'audio/Rumble.mp3','audio/Rumble2.beatmap.txt','audio/RumbleNoteMap.txt',1),
    Song('Wherever You Will Go | Vs. Alex', 'audio/WYWG.mp3', 'audio/beatswywg.txt', 'audio/laneswywg.txt',1), #18000
    Song('The Reason | Vs. Spencer', 'audio/Reason.mp3','audio/beatsreason.txt', 'audio/lanesreason.txt',1), #27000
    Song('One Last Breath | Vs. Concrete Chaos', 'audio/OLB.mp3','audio/beatsolb.txt', 'audio/lanesolb.txt',1), #20000
    Song('How You Remind Me | Vs. Riot Circuit', 'audio/HYRM.mp3','audio/beatsremind.txt', 'audio/lanesremind.txt',1), #21000
    Song('Last Resort | Vs. Legendary Four', 'audio/LR.mp3','audio/beatslr.txt', 'audio/laneslr.txt',1), #30000
    Song('Through the Fire and Flames | Vs. The Disenters', 'audio/TTFAF.mp3', 'audio/beatsttfaf.txt', 'audio/lanesttfaf.txt',1)
    ]

    # call screen rhythm_game(RhythmGameDisplayable(rhythm_game_songs[songNumber]))


    # # init
    # if persistent.rhythm_game_high_scores:
    #     for song in songs:
    #         if not song in persistent.rhythm_game_high_scores:
    #             persistent.rhythm_game_high_scores[song] = (0, 0)

# map song name to high scores
default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}

# the song that the player chooses to play, set in `choose_song_screen` below
default selected_song = None

# To do:
# Change the entire GUI! Give menu background, 

label start:
    menu:

        "Skip Tutorial?"

        "Yes":

            jump skip
        
        "No":

            jump tutorial

label musicTesting:
    "Hi me"

    window hide
    $ quick_menu = False
    $ renpy.block_rollback()

    #$ song = Song('Tutorial Song', 'audio/', "audio/", beatmap_stride=2)
    $ rhythm_game_displayable = RhythmGameDisplayable(rhythm_game_songs[6])
    call screen rhythm_game(rhythm_game_displayable) # edited the screen parameters, now allows a second parameter for a background
    show testTransition with None
    hide testTransition
    with easeoutright
    $ renpy.block_rollback()
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    "[rhythm_game_displayable.score]"

label failure:
    "You have failed."

    $ MainMenu(confirm=False)()    

label skip:

    "Huh?"

    "Don't wanna play the tutorial?"

    "Yeah, I guess thats fair."

    window hide
    show testTransition
    with easeinleft

    #hide testTransition
    #scene testBlue with None
    #show testTransition

    jump dormScene1

# a simpler way to launch the minigame 
label tutorial:
    "This is a rhythm game."

    "Hit the notes at the line to score points."

    "The more accurate it is to the line, the more points you score."

    "Your progression is based on the score you achieve."

    "A tutorial song will now play."

    #show testTransition
    #with easeinleft

    window hide
    $ quick_menu = False
    $ renpy.block_rollback()

    #$ song = Song('Tutorial Song', 'audio/', "audio/", beatmap_stride=2)
    $ rhythm_game_displayable = RhythmGameDisplayable(rhythm_game_songs[0])
    call screen rhythm_game(rhythm_game_displayable) # edited the screen parameters, now allows a second parameter for a background
    show testTransition with None
    hide testTransition
    with easeoutright
    $ renpy.block_rollback()
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    if rhythm_game_displayable.score > 1000:
        "You passed the tutorial song. It gets longer and harder from here, so be prepared!"

    else:
        "You failed the tutorial song. It gets harder from here, so..."

        "Yeah, start again."

        $ MainMenu(confirm=False)()
    
    show testTransition
    with easeinleft

    jump dormScene1

    return

label dormScene1:
    scene dorm room with None

    #with None
    #show testBlue
    # Holy moly debugging this transition was a pain in the butt!!!! Next few comments will explain how to do it.

    #Previous scene, put this at end (before jump):
    #show {transition here}, # for now use testTransition, if i decide to change it to a new image ill do it
    #with easeinleft

    #Next scene, put this at beginning
    #scene {next scene background} with None
    
    #show {transition here} with None
    #hide {transition here}
    #with easeoutright

    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show jay talking flip at right
    show daniel idle at left

    j "You're kinda loud, you know that?"

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "Huh?"
    d "Oh, sorry. I get lost in the music."

    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "You know you can take that music else where, right?"

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "Where? Marketing myself is hard, and I don't have any friends who know any other instrument."

    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "{cps=5}...{/cps}{cps=1} {/cps}You seriously don't know?"

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "Know what?"

    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "Theres a competition held in town this week. "

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "You're kidding."

    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "Nope. Could be a good chance for you to put yourself out there. And let me study for once."

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "Yeah, yeah. Sorry."
    
    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "It's fine. Only issue, seems like it's a band only thing. Not solo."

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "Sorry, but you have to suffer with my playing for much longer."

    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "Just ask around man."

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "Fine. How many people counts as a band?"

    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "Don't ask me. The poster and requirements are pinned on the dorm bulletin board. Go there."

    hide jay talking flip
    hide daniel idle
    show daniel talking at left
    show jay idle flip at right

    d "Sure{cps=4}... {/cps}where is it?"

    hide daniel talking
    hide jay idle flip
    show daniel idle at left
    show jay talking flip at right

    j "Follow me."

    show testTransition
    with easeinleft
    
    jump lobby

label lobby:
    scene bulletin with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show jay talk point at left
    show daniel idle flip at right

    j "It's right over here." # jay point

    show jay idle at left
    show daniel talking flip at right

    d "I'm surprised I haven't heard anything about this. Surely I would have heard news about this by now?" # confused dan

    show jay talking at left
    show daniel idle flip at right

    j "It was posted earlier today. Read the qualifications."

    show jay idle at left
    show daniel talking flip at right

    d "It says that a band is composed of 4 members, no exact requirements on the intruments. I probably need a singer, bassist and a drumist."

    show daniel talk embarrased at right

    d "This might be a tough search." # embarrassed dan

    show daniel idle flip at right
    show jay talking at left

    j "To lay some advice on you, I know a drummer in room {b}427{/b}. I'm sure he'll love to compete in the concert."

    show daniel talking flip at right
    show jay idle at left

    d "I'll be heading there now."

    show jay talking at left
    show daniel idle flip at right
    
    j "Good luck! I'm going back to our dorm so I can study. FINALLY!"

    hide jay talking with easeoutleft  
    show daniel talking flip at right


    d "Alright, later Jay." # ease jay hide

    show daniel talking flip at center with easeinleft

    d "{cps=3}...{/cps} how much time do I have?"

    show daniel talk shocked flip at center

    d "IT STARTS TOMORROW??" # shocked dan

    show daniel talk sad flip at center

    d "I'm doomed." # sad dan

    show testTransition
    with easeinleft

    jump outside427

label outside427:
    scene outside427 with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show daniel talking at left

    d "I believe this is it." # dan

    show daniel idle at left
    #Knocking sound

    q "Yeah? Who is it?" # dont show jack yet

    show daniel talking at left

    d "Hey, I heard someone here plays the drums. I wanna ask a question."

    show daniel idle at left

    q "Oh my.. Tell Audrey I don't give a-"

    show daniel talking at left

    d "Dude, I'm not the RA."

    show daniel idle at left
    show jack idle flip at right with easeinright

    # Jack enters the hallway # show jack

    show jack talk curious flip at right

    q "Who are you, then?" # jack curious

    show daniel talking at left
    show jack idle flip at right

    d "You know the concert competition tomorrow?"

    show daniel idle at left
    show jack talk flip at right

    q "No?"

    show daniel talking at left
    show jack idle flip at right

    d "I wanted to ask if you wanted to form a band for it?"

    show daniel idle at left
    show jack talk curious flip at right

    q "Maybe, how'd you find me? You're not a familar face." # jack curious

    show daniel talking at left
    show jack idle flip at right

    d "Daniel. Jay sent me."

    show daniel idle at left
    show jack talk surprise flip at right

    q "Jay sent you? Shoulda said that from the start. Come in." # jack surprise

    show testTransition
    with easeinleft

    jump room427

label room427:

    scene 427 with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show daniel talking at left
    show jack idle flip at right

    d "Nice dorm. You have a roommate?"

    show daniel idle at left
    show jack talk flip at right

    q "Nah, paid extra to be alone. Knew my drumming would cause more issues if I had a roommate. Doesn't matter with my neighbours sending complaints."

    show daniel talking at left
    show jack idle flip at right

    d "Lucky."

    show daniel idle at left
    show jack talk flip at right

    q "Anyways, I only play with those who play good. Lets play, here and now. Show your skill. Then, I'll see if its worth joining you."

    show daniel talking at left
    show jack idle flip at right

    d "I guess thats fair. Who starts?"

    show daniel idle at left
    show jack talk flip at right

    q "I'll start."

    show daniel talking at left
    show jack idle flip at right

    d "Alright, lets start then."

    show daniel idle at left
    show jack idle flip at right

    "Incase you lose, save here!"

    menu :
        
        "Have you saved?"

        "Yes":

            "Alright, good luck! I wouldn't remind you further, it's on {i}you{/i} to save frequently!"

        "No":

            "Please do!"

    "The song is starting now!"

    window hide
    $ quick_menu = False
    $ renpy.block_rollback()

    #$ song = Song('Tutorial Song', 'audio/', "audio/", beatmap_stride=2)
    $ rhythm_game_displayable = RhythmGameDisplayable(rhythm_game_songs[1])
    call screen rhythm_game(rhythm_game_displayable)
    $ renpy.block_rollback()
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    if rhythm_game_displayable.score > 6000:

        show daniel talking at left
        show jack idle flip at right
        
        d "So, do you think I'm worth joining?"

        show daniel idle at left
        show jack talk surprise flip at right

        q "Heck yeah man, you play good!" # jack surprised

        show daniel talk scoff at left
        show jack idle flip at right

        d "I try my best. Music is everything to me." # dan scoff

        show daniel idle at left
        show jack talk flip at right

        q "Is it just going to be us comepeting?"

        show daniel talking at left
        show jack idle flip at right

        d "No, we need more people, atleast a bassist and a singer."

        show daniel idle at left
        show jack talk flip at right

        q "I know a place we can go. Down by the shore, that's like the musicians hangout spot."

        show daniel talking at left
        show jack idle flip at right

        d "Cool, first, whats your name?"

        show daniel idle at left
        show jack talk flip at right

        ja "Jack."

        show daniel talking at left
        show jack idle flip at right

        d "Alright Jack, lets go."

        show daniel idle at left
        show jack talk flip at right

        show testTransition
        with easeinleft

        jump shore

    else:

        show daniel talking at left
        show jack idle flip at right

        d "So, do you think I'm worth joining?"

        show daniel idle at left
        show jack talk flip at right

        q "You're kidding. You think I would join a loser like you? Train for a couple more years and come back when you can do this properly." # jack angry

        show testTransition
        with easeinleft

        jump failure


label shore:
    scene beach with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show daniel talk shocked at left
    show jack idle at right

    d "Been a while since I've last been here." # dan surprise

    show daniel idle at left
    show jack talk at right

    ja "Yeah, unless you know what goes down here, theres no real reason to visit the shore."

    show daniel talk confused at left
    show jack idle at right

    d "I'm surprised that I never caught wind of this place. I should have went here first, huh?" # dan confused

    show daniel idle at left
    show jack talk at right

    ja "Yeah, it's surprisingly underground nowadays."

    show daniel talking at left
    show jack listen at right

    d "Do you hear that?" # jack listen

    show daniel idle at left
    show jack talk at right

    ja "Yeah, sounds like singing."

    show daniel talking at left
    show jack idle at right

    d "They sound pretty good, maybe we should go over there, see if they're interested."

    show daniel idle at left
    show jack talk at right

    ja "He's getting off the stage, right there! Lets go ask him."

    hide jack talk with easeoutright
    hide daniel idle with easeoutright

    show testTransition
    with easeinleft
    
    jump stage

label stage:
    scene beach stage with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show daniel talking at left
    show jack idle at center
    show alex idle flip at right

    d "Excuse me, my buddy Jack and I think your singing is wonderful, and we were wondering if you would like to join us for the competition that's happening in town tomorrow?"

    show daniel idle at left
    show alex talk wonder flip at right

    q "A contest? I think I've heard about it." # alex wondwer

    q "But, I don't just join random groups. I need to know if you guys are the real deal." # jack curious

    show alex idle flip at right
    show daniel talking at left

    d "Fine then, we can show off our skill here."

    show daniel idle at left
    show alex talk flip at right

    q "That will work. Convince me, and I'll join."

    show daniel talking at left
    show alex idle flip at right

    d "Deal."

    show daniel idle at left
    show alex talk flip at right

    q "Get on stage."
    
    window hide
    $ quick_menu = False
    $ renpy.block_rollback()

    $ rhythm_game_displayable = RhythmGameDisplayable(rhythm_game_songs[2])
    call screen rhythm_game(rhythm_game_displayable)
    $ renpy.block_rollback()
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    if rhythm_game_displayable.score > 1000:

        show daniel idle at left
        show jack talk at center
        show alex idle flip at right

        ja "We were amazing!"
        
        show jack idle at center
        show alex talk applaude flip at right

        a "Thank you, you guys did amazing as well. Seems like a match made in heaven. And by the way, my name is Alex." # alex applaude

        show daniel talking at left
        show alex idle flip at right

        d "Nice to meet you Alex." # handshake dan alex

        show daniel idle at left
        show jack talk at center
    
        ja "Glad to have you on, Alex." # handshake alex jack

        show jack idle at center
        show daniel talk embarrassed at left

        d "Seems we attracted a crowd, huh?" # dan embarrassed

        show jack talk at center
        show daniel idle at left

        ja "Defintely. Lets get off stage, before everyone else starts expecting another song."

        show daniel talking at left
        show jack idle at center

        d "Let's get this over with. Just need one more guy!"

        show daniel idle at left
        show jack talk at center

        ja "Let's split up, so this search can go faster. Remember, we are looking for someone who plays a bass intrument."

        show jack idle at center
        show daniel talking at left

        d "I'll go by the drink stand."

        show daniel idle at left
        show alex talk flip at right

        a "I'll go near the seating area."

        show alex idle flip at right
        show jack talk at center

        ja "I'll look by the pier."

        show testTransition
        with easeinleft

        jump seatingArea

transform leftmost:
    xalign 0
    yalign 0

transform pos20:
    xalign 0.2
    yalign 0

transform pos40:
    xalign 0.4
    yalign 0

transform pos60:
    xalign 0.6
    yalign 0

transform pos80:
    xalign 0.8
    yalign 0

transform leftmiddle:
    xalign 0.333
    yalign 0

transform rightmiddle:
    xalign 0.666
    yalign 0

transform rightmost:
    xalign 1
    yalign 0

label seatingArea:
    scene pier with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show jack talk at left
    show spencer idle flip at right

    ja "Hello, I'm Jack. Me and my friends are looking for someone who plays a bass intrument, and I see you're playing the bass and you play really good. Would you like to join us for a competition happening tomorrow?"

    show jack idle at left
    show spencer talk flip at right

    s "Hey, I'm Spencer. I wanted to go as well, but couldn't find a band. But before I join you guys, I would like to hear you guys play."

    show spencer idle flip at right
    show jack talk at left
    
    ja "Cool, let me just call them over."

    show jack yell flip at left

    ja "DANIEL, ALEX! COME QUICK!" # jack scream

    show jack idle flip at rightmiddle with easeinleft
    show spencer idle flip at right 
    show alex talk at leftmiddle with easeinleft
    show daniel idle at leftmost with easeinleft

    a "What's up Jack?" # alex concerned

    show alex idle at leftmiddle
    show daniel talking at leftmost

    d "Yeah, what happened?" # dan concerned

    show daniel idle at leftmost
    show jack talk flip at rightmiddle

    ja "This is Spencer, he will join us if we show him how well we play, yall down?" # jack point towards spencer

    show daniel talking at leftmost
    show jack idle flip at rightmiddle

    d "Yeah." # dan nod

    show alex talk at leftmiddle
    show daniel idle at leftmost

    a "Of course we are." # alex nod

    show jack talk flip at rightmiddle

    ja "Okay, let's start."

    window hide
    $ quick_menu = False
    $ renpy.block_rollback()

    #$ song = Song('Tutorial Song', 'audio/', "audio/", beatmap_stride=2)
    $ rhythm_game_displayable = RhythmGameDisplayable(rhythm_game_songs[3])
    call screen rhythm_game(rhythm_game_displayable)
    $ renpy.block_rollback()
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    if rhythm_game_displayable.score > 27000:

        show jack idle at rightmiddle
        show spencer talk wonder flip at right
    
        s "You guys are not bad, I think your band is missing something though..." # spencer thinking

        show spencer talk pumped flip at right

        s "A BASS! I'M IN" # spencer pumped

        show spencer idle flip at right
        show daniel talking at leftmost

        d "Awesome!"

        show testTransition
        with easeinleft

        jump campus

label campus: # Shore background
    scene beach with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show daniel talking flip at right
    show jack idle at left
    show alex idle at leftmiddle
    show spencer idle at rightmiddle

    d "Okay see you guys tomorrow, don't forget it starts at 2pm. Let's meet up at the ice-cream shop before then."

    show alex talk at leftmiddle
    show daniel idle flip at right

    a "Good Idea, let's do that."

    show alex wave at leftmiddle
    show spencer wave flip at rightmiddle
    show daniel wave flip at right
    show jack wave at left

    s "See you guys tomorrow!" # all wave

    show testTransition
    with easeinleft
    jump dormScene2

label dormScene2:
    scene dorm room with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show daniel idle at left
    show jay talking flip at right

    j "Hey Daniel, did you find a band?"

    show daniel talking at left
    show jay idle flip at right

    d "Yes, I did!"

    d "You will be there right?"

    show jay talking flip at right
    show daniel idle at left

    j "That's great man! I will be there to watch you guys play."

    show daniel talking at left
    show jay idle flip at right

    d "Great! I owe you for this man."

    show daniel idle at left
    show jay talking flip at right

    j "True, you know I got you man."

    show daniel talking at left
    show jay idle flip at right

    d "I should get some rest for tomorrow."

    show jay talking flip at right
    show daniel idle at left

    j "Your right, rest up."
    window hide
    show testTransition
    with easeinleft

    hide testTransition
    with easeoutright
    window show

    show daniel talking at left
    show jay idle flip at right

    d "Today is finally the day I show off my talent!"

    show jay talk tired flip at right
    show daniel idle at left

    j "You seem full of energy, excited?" # jay tired

    show daniel talking at left
    show jay idle flip at right

    d "Yes, very! As a matter of fact, I'm going to head out right now to meet with my band."

    show jay talking flip at right
    show daniel idle at left

    j "Alright, good luck!"

    show testTransition
    with easeinleft
    
    jump icecreamShop

label icecreamShop:
    scene ice cream shop with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    show daniel talking at left
    show spencer idle flip at leftmiddle
    show alex idle flip at rightmiddle
    show jack idle flip at right

    d "Are you guys ready?"

    show daniel idle at left
    show spencer talk flip at leftmiddle
    show alex talk flip at rightmiddle
    show jack talk flip at right

    allC "Yeah!" # group celebrate

    show daniel talking at left
    show spencer idle flip at leftmiddle
    show alex idle flip at rightmiddle
    show jack idle flip at right

    d "Great, let's go!"

    show testTransition
    with easeinleft

    jump waitingRoom


label waitingRoom:
    scene waiting room with None
    show testTransition with None
    hide testTransition
    with easeoutright
    window show

    r "Hi! Are you guys here for the competition held today?"

    d "Yeah, where do we go?"

    r "Have a seat anywhere, and fill out the top page. Place it beneath and give it to your teammates after. How many of you are there?"

    ja "Just 4."

    r "Perfect! Take this clipboard and give it to me after you have filled out everything."

    d "Alright, thank you."
    show testTransition
    with easeinleft

    jump waitingRoom2

label waitingRoom2:
    # Special Pre Rendered images
    a "Comfy chairs, huh?"

    d "True."

    "Reading out the form, Daniel realizes one thing. One very, very important thing."

    d "Hey, uhh.. what do we put as our band name?"

    ja "Didn't we discuss that at the pier?"

    a "No, I don't think so."

    s "Yeah, I don't remember anything about naming."

    a "I think it's fair to give Dan the choice."

    ja "Yeah, Dan has come a far way to round us up. It's fair to give him the privilege to name the group."

    s "I agree aswell."

    d "You guys sure?"

    allC "Yep."

    d "Alright..."

    $ group_name = renpy.input("What will be the group name?",default = "Concerto")
    $ group_name = group_name.strip() # Removes leading white space just in case user accidently pressed space

    d "Our group name will be [group_name]!"

    a "Yeah!"

    s "Lets win this, [group_name]!"

    ja "Good luck, guys!"
    show testTransition
    with easeinleft
    jump waitingRoom3


label waitingRoom3:
    scene waiting room with None
    show testTransition with None
    hide testTransition
    with easeoutright
    
    r "[group_name]!"

    d "Thats us!"

    r "You are up next, rivalling the.."

    window hide
    $ showCard("cc")
    window show

    r "Wouldn't be surprised if you beat them, but I wouldn't be surprised if you lose against them. They are a resilent band, but I've seen you around, and you seem good enough to compete against them."

    ja "We stand a chance, atleast." # jack pumped

    s "This will be easy!"

    r "Seems they are finishing up. Get ready!"

    # play song vs. cc

    show testTransition
    with easeinleft

label waitingRoom4:
    scene waiting room with None
    show testTransition with None
    hide testTransition
    with easeoutright

    if True:

        a "We did it!" # alex celebrate

        d "What do you think? We passed them in the bracket?" 

        s "Oh yeah, 100 percent. No way they won against us." 

        ja "Not to toot my own horn, but their drummist clearly had no experience with the drums. No way we lose against those guys!" # jack scoff

        r "Great job, [group_name]. You did great out there! Listen from the curtains to hear the results."

        s "Lets go!" # spencer pumped

        #Fade to black

        "Incredible performances from our bands.. but only one can proceed..."

        "The winner is..."

        "{size=+20}{font=BlackCasper.ttf}[group_name]{/font}!!!{/size}"

        s "Woo!"

        a "Three more to go!"

        ja "Let's not celebrate early, we need that energy for our next few!"

        d "Exactly. Lets watch the next few, we got alot of time to our next battle."

        jump waitingRoom5
    
    else:

        d "That wasn't good."

        s "That really sucked."

        a "Lets, not do that again."

        jump failure

label waitingRoom5:

    r "[group_name]!"

    d "Yeah?"

    r "If you haven't have heard, you proceeded further into the competition. Great job!"

    r "Welcome to the semi-semi finales! Next up is you and..."

    window hide
    $ showCard("rc")
    window show

    r "The Riots are on a winning streak, and made semi finales in nearly all competitions they participated it. I would be surprised if you beat them, being a newcomer and all."

    ja "Sooo... easy peazy lemon squeezy?"

    a "Don't push our luck."

    r "You're up next. Have fun out there!"

    # play song vs. rc

label waitingRoom6:

    if True:

        d "Woo! That was so fun!"

        a "Yeah! That was great!"

        ja "Riot Circuit's are worse than our circuits!"

        s "Dumb joke, but yeah!"

        r "Congratulations you guys! Crowd reactions were insane! I haven't heard that many cheers for a rival against the Riots."

        r "Safe to say, you won! You are now in the semi-finals! Haven't seen a newcomer up here for nearly 7 years!"

        r "Winner for the next battle will be the ones you will be fighting in the semi-finals. Come watch!"

        d "That would be smart, yeah?"

        s "Lets go see who we are rivaling against!"

        # Fade to black

        "And the winner is..."

        window hide
        $ showCard("lf")
        window show

        d "Legendary Four, huh?"

        a "Familar name. Where do I remember that name from?"

        s "They won last competition. Beat me and my team, caused us to disband."

        ja "Really? That sucks."

        s "Eh, morale was at an all time low. They beat us first round. Bound to happen anyways."

        s "But, I haven't gotten this far before. Glad to have gotten the experience with them, but I'm happy to be here! Seems like we all are destined to work together."

        a "True."

        s "Lets prepare, I gotta show these four whose boss."

        # play song

    else:

        d "Yeah, they were tough."

        ja "There's no way we won against them."
    
label waitingRoom7:

    if True:

        s "Yes! Woo!"

        d "That was incredible Spencer. We knocked the four right off the board!"

        r "Indeed you have, guys! Haven't seen the judges more surprised ever." 
        r "The most emotion I have ever seen on their face! " # manager giggle
        r "But, uhh.. the hardest part of this isn't over."
        r "The newcomer who was in the semi-finals? 7 years ago? They are up next, against you guys."
        window hide
        $ showCard("td")
        window show
        r "They also won that competition. Make a miracle happen."

        d "You heard her, lets perform a miracle!"
        allC "Yeah!"

        #play song vs. the disenters

label results:

    d "Gosh, that was difficult."

    if True:

        a "You went ham on the guitar, dude! Insane performance from you."

        ja "Exactly! It's insane how you haven't contested before."

        s "Same here, dude. I wouldn't be surprised if you were a member of The Disenters or something."

        d "Ha, thanks guys. You all did incredible yourselves."
        d "Hey, what if we keep this up? Don't let this become a one time gig and become a real band or something?"
        
        s "I'd love to continue playing with you all."

        a "I have never gotten this far with others. My singing has never sounded this good. I'm in."

        ja "I'm so glad I lucked out and Jay recommended me to you. I would have never gotten this far playing the drums if it wasn't for you knocking on my door."
        ja "So, you are now looking at your band's drumist."

        d "Thank you so much guys. Cheers to [group_name]!"
        allC "[group_name]!"

    else:

        "I dont wanna write this one out rn remind me later"
        jump failure

        # Stage view
    show testTransition
    with easeinleft
    scene stage
    hide testTransition
    with easeoutright

    "Incredible performances from everyone tonight! Give a big round of applause to everyone who tried their best at todays competition."
    # round of applause
    # pause until applause ends

    "But, there can be only one winner from the 16 teams."

    "We have [group_name], the incredible newcomer, the first newbie to reach finals in 7 years..."
    "And we have The Disenters, the band who set that record 7 years ago..."
    "Two incredible fierceless forces battling eachother, with only one winning..."
    "The winner is..."
    if True:
        "{size=+20}{font=BlackCasper.ttf}[group_name]{/font}!!!{/size}"

        d "Woo!"

        a "We did it!"

        s "We won!"

        ja "Congrats guys! We did incredible!"
        show testTransition
        with easeinleft
        jump credits
    else:
        "{size=+20}{font=BlackCasper.ttf}The Disenters{/font}!!!{/size}"
        jump failure
    


label credits:
    scene black
    show screen creditscreen
    pause 100 # or however long it takes to scroll through in a reasonable speed
    pause
    hide screen creditscreen
    $ newgameplus = True
    return

    # Below is how to call the introduction screens. The band names are the bands names abbreviated

    #window hide
    # $ showCard(-bandname-) # Example: showCard("td")
    #window show

init python:
    def showCard(band):
        renpy.show_screen(band)
        renpy.pause(5)
        renpy.hide_screen(band)


screen td:
    vbox:
        xsize 1000
        ysize 720
        xalign 0.5

        text "YOU vs.":
            color "#ffffff"
            size 50
            yalign 0.1
            xalign 0.5

        text "The DISSENTERS":
            font "BlackCasper.ttf"
            color "#ffffff"
            size 150
            xalign 0.5
            yalign 0

        text "The Dissenters haven't lost any championship they have participated in. Good luck...":
            font "Harting_plain.ttf"
            color "#918f8f"
            size 30
            xalign 0.5

screen rc:
    vbox:
        xsize 1000
        ysize 720
        xalign 0.5

        text "YOU vs.":
            color "#ffffff"
            size 50
            yalign 0.1
            xalign 0.5

        text "RIOT CIRCUIT":
            font "BlackCasper.ttf"
            color "#ffffff"
            size 150
            xalign 0.5
            yalign 0

        text "The Riots have won half their championships and on a winning streak...":
            font "Harting_plain.ttf"
            color "#918f8f"
            size 30
            xalign 0.5

screen lf:
    vbox:
        xsize 1000
        ysize 720
        xalign 0.5

        text "YOU vs.":
            color "#ffffff"
            size 50
            yalign 0.1
            xalign 0.5

        text "LEGENDARY FOUR":
            font "BlackCasper.ttf"
            color "#ffffff"
            size 150
            xalign 0.5
            yalign 0

        text "The Four have won more than eight championships, and you aren't confident in winning...":
            font "Harting_plain.ttf"
            color "#918f8f"
            size 30
            xalign 0.5

screen cc:
    vbox:
        xsize 1000
        ysize 720
        xalign 0.5

        text "YOU vs.":
            color "#ffffff"
            size 50
            yalign 0.1
            xalign 0.5

        text "CONCRETE CHAOS":
            font "BlackCasper.ttf"
            color "#ffffff"
            size 150
            xalign 0.5
            yalign 0

        text "The Concrete Chaos won 2 out of eight championships. Even if they seem easy, they won't back down...":
            font "Harting_plain.ttf"
            color "#918f8f"
            size 30
            xalign 0.5


screen creditscreen:
    vbox:
        xsize 1000 # horizontal size of the credits
        ysize 5500 # how much vertical space your rolling credits take.
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            easein 100: # or however long it takes to scroll through in a reasonable speed
                yalign 1.0
        vbox:
            ysize 720 # enter vertical resolution, so that it starts with an empty screen
        text "Concerto":
            font "BlackCasper.ttf"
            color "#ffffff"
            size 100
            xalign 0.5
        text "Created for the AP CSP Practice Create Task":
            font "SF_Cartoonist_Hand.ttf"
            color "#ffffff"
            size 25
            xalign 0.5
        text ""

        text "Primary Writer: E'Myla":
            color "#ffffff"
        text "Secondary Writer: Maximillian Siewior":
            color "#ffffff"
        text ""
        text "Main Programmer: Maximillian Siewior":
            color "#ffffff"
        text "Secondary Programmer: E'Myla":
            color "#ffffff"
        text "Concept Art: E'Myla":
            color "#ffffff"
        text "3D Scenery: Maximillian Siewior":
            color "#ffffff"
        text ""
        text "Music:\n{size=-8}Tutorial:{/size} 80's style guitar shredding by Straten Marshall\n{size=-8}Vs. Jack:{/size} Rumble by Link Wray\n{size=-8}Vs. Alex:{/size} Wherever You Will Go by The Calling\n{size=-8}Vs. Spencer:{/size} The Reason by Hoobastank\n{size=-8}Vs. Concrete Chaos:{/size} One Last Breath by Creed\n{size=-8}Vs. The Riot:{/size} How You Remind Me by Nickelback\n{size=-8}Vs. The Four:{/size} Last Resort by Papa Roach\n{size=-8}Vs. The Dissenters:{/size} Through the Fire and Flames by DragonForce":
            color "#ffffff"
        text "Fonts:\nHarting from Font Squirrel\nBlackCasper from Font Squirrel\nCartoonist Hand from Font Squirrel":
            color "#ffffff"
        text "Characters created with VRoid Studio":
            color "#ffffff"
        text "Rhythm Game Template: RuolinZheng08":
            color "#ffffff"
        text "Made with Ren'Py.":
            font "Harting_plain.ttf"
            color "#ffffff"
            bold True
            xalign 0.5

label test:
    e "Welcome to the Ren'Py Rhythm Game! Ready for a challenge?"
    window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    $ song = Song('Isolation', 'audio/Isolation.mp3', 'audio/Isolation.beatmap.txt', beatmap_stride=2)
    $ rhythm_game_displayable = RhythmGameDisplayable(song)
    call screen rhythm_game(rhythm_game_displayable)

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    return

"""
* Title: Ren'py Rhythm
* Author: RuolinZheng08
* Date: September 16, 2025
* Code Version: Ren'Py Python
* Availability: https://github.com/RuolinZheng08/renpy-rhythm
"""