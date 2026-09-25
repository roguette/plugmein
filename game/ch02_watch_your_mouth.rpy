default piotrFoodPoints = 0
default piotrWritingPoints = 0

#region INTERACTIONS

label ch02_h_bed:
    menu:
        you "{i}I want to...{/i}"

        "Go to sleep (Next day)":
            "You close your eyes and before you know it you drift off to sleep."

        "Explore the house":
            you "{i}I still need to check something...{/i}"
            call screen s_House()
    

label ch02_h_window:
    scene expression loc_bg("house")
    if flag("ch02_seen_bug"):
        "Theres a west conifer seed bug outside the window, crawling, doing whatever its little brain is telling it to."
    else:
        "There's nothing particularly interesting about the window."
        "The bug is gone."

    call screen s_House()


label ch02_h_fridge:
    scene expression loc_bg("house")
    if flag("ch02_opened_fridge"):
        you "{i}No.{/i}"
    else:
        $ flag("ch02_opened_fridge", True)
        "As you open the door the gnome jumps onto his little feet and hurriedly turns on the light in the fridge."
        "Still weirded out by his existence, you smile and notice he is very happy to see you."
        you "Hello!"
        you "{i}Still deaf...{/i}"
        if flag("ch02_ate_at_table"):
            $ flag("ch02_angry_gnome", True)
            you "I'm so sorry i don't have any food..."
            "But the gnome seems to have broken the language barrier this ONE time."
            "He stomps his little foot against the thin shelf, crosses his arms and turns around."
            you "I'll get you food tomorrow i promise!"
            "But he doesn't hear you this time and just stands there."
            "Disgusted by your selfishness, you close the fridge door."
        else:
            $ flag("ch02_fed_gnome", True)
            "You put the rest of your buns on the top shelf, just in case the gnome was hungry and close the door."
            "The little gnome dives into the paper bag."
            "Someone is CLEARLY hungry."

    call screen s_House()


label ch02_h_table:
    scene expression loc_bg("house")
    if flag("ch02_opened_fridge"):
        "You don't have any food."
    else:
        $ flag("ch02_ate_at_table", True)
        "You put the paper bag with Rafał's buns onto the table and devour all of them, leaving zero trace of their existence."
        you "{i}Now to shower and i can go sleep.{/i}"
    call screen s_House()


label ch02_h_suspicious_pot:
    scene expression loc_bg("house")
    $ flag("ch02_seen_suspicious_pot", True)
    "This pot looks identical to the one near it."
    "Its a regular, probably extremely heavy, flower pot."
    "Drawn on it were oriental-style crane drawings."
    "Everything was standing on a very basic nightstand."
    "It's age was made visible by the coffee mug stains on the top surface."
    "The nightstand had two drawers - one bigger, one smaller with two similar metal handles."
    "Everything was supported by four also similar metal legs, which were standing on the..."
    you "{i}Wait what is that{/i}"
    "What you previously thought was a dead bug turned out to be a hole in the floor."
    "And when you inspect it closer, you see a handle further away, under the nightstand."
    "You move the plant before pulling on it, which, unsurprisingly, fails."
    "While getting up your keys fall out, and you take another look at them."
    "None match the round hole."
    you "{i}Tomorrow i'm going to Barbara to ask her about this{/i}"
    "Just in case, you move the plant back where it was."
    call screen s_House()


label ch02_h_normal_pot:
    scene expression loc_bg("house")
    "There's nothing unusual about this pot."
    call screen s_House()


label ch02_h_bathroom:
    scene expression loc_bg("house")
    if flag("ch02_took_a_shower"):
        "The shower wasnt as horrifying as you thought was it?"
    else:
        $ flag("ch02_took_a_shower", True)
        # TODO: When theres a personality quiz at the start only show this if the person knows how to code
        "Everything about the shower seems intimidating."
        "You gather all your courage and step into the shower."
        "..."
        "You are now clean."
    call screen s_House()


label ch02_h_wardrobe:
    scene expression loc_bg("house")
    "This is the only place that, surprisingly, wasnt empty when you arrived"
    "There were some shorts, some pants. All of it looks cheap, almost disposable."
    "Just some clothes to change into before you buy something new."

    call screen s_House()


#endregion



label ch02_watch_your_mouth:
    "You are very hungry, but not so hungry you can't sleep."
    "And before you know it you fall asleep."

    call chapterTransition("Chapter 2", "Hey. It's me.")
    $ time.chapter = 2
    
    ".{w=0.5}.{w=0.5}.{w=0.5}"
    "The sun lined up perfectly with your face, which, in turn, warmed it up just enough to wake you up."
    scene bg houseday with dissolve
    "You instinctively cover yourself but you can still see the sun through the gaps between your fingers."
    "It's time to stop being so lazy and get off the bed."
    "Now that it's not dark anymore you can see the interior of the house better"
    "The house didnt change much, except for the fact that the morning light is making it feel less abandoned."
    "You lazily get off your bed and change your clothes in front of a mirror."
    "It's still you in the reflection, just not smelly and covered in forest dirt."
    $ time.setTime(10,32)
    "When you walk past the clock you notice it mocking you with \"10:32\""
    you "{i}There is no way I slept that long.{/i}"
    show screen s_Clock()
    "If it weren't for your hunger, you would have slept for longer."
    if ch01_f_triedBakery:
        "The only thing you can think of are the pastries you saw at a bakery"
    else:
        "The only thing you can think of is filling your stomach."
    "Luckily, there is a fridge in the kitchen."
    you "{i}Okay what kind of house would this be if I didnt get food?{/i}"
    you "{i}That would be very rude{/i}"
    you "{i}Oh my god what if its magical and can just summon food...{/i}"
    menu:
        "You close your eyes and try to summon..."
        "Caviar":
            "You close your eyes, think of caviar and try your best to channel your inner sorcerer..."
            "This food is going to require the most concentration."
            you "{i}This HAS to work.{/i}"
        "French snails":
            "You close your eyes, think of those slimy things and try your best to channel your inner sorcerer..."
            "This food is going to require the least concentration."
            you "{i}This HAS to work.{/i}"
        "Dead dove":
            "You close your eyes, think of dead doves and try your best to channel your inner sorcerer..."
            "This food is going to require some concentration."
            "Suddenly you remember that you shouldn't eat dead doves."
            you "{i}I need to dream bigger. I want a rotisserie chicken.{/i}"
        "I'm not hungry":
            you "{i}Actually no if i stay hungry i will stay skinny.{/i}"
            you "{i}I'm gonna be so skinny after this! I'll just get something to drink.{/i}"

    "You open the fridge and, to your surprise, there is nothing in it except a gnome who keeps turning the light on and off."
    you "{i}What the hell{/i}"
    you "Hello?"
    you "Who are you?"
    "The little gnome ignores you."
    you "Sprechen sie Deutsch???"
    "While he's ignoring you, you ignore the fact that he could be deaf."
    you "Excuse me young man what are you doing in my fridge?"
    "He looks up at you with a gnarly smile and waves his hand."
    you "{i}I'm not getting paid enough for this.{/i}"
    you "{i}In fact I dont get paid at all.{/i}"
    "You leave the door open just in case he was trapped in there and wants to get out only for him to start dusting the top shelf."
    you "{i}???{/i}"
    "Due to pure confusion you close the fridge door."
    you "{i}Did I summon that?{/i}"
    you "{i}Wait what if he's hungry.{/i}"
    you "{i}I'll get food and share...{/i}"
    "The gnome was only a brief distraction from the calories in your stomach, or lack thereof."
    "As you leave the house, you almost forget to close the door, but at the last moment you remember what kind of neighborhood you live in."
    "You nearly faint from hunger. It seems being skinny wasn't worth it."
    "There is one person in town who can help you right now - Barbara."
    "She is probably at work, so you decide to go straight to her."
    scene bg citysquareday with dissolve
    play music "town_day.mp3"
    play sound "sfx_footsteps_b.mp3"
    "On your way to see Barbara, you admire the buildings and nature, since you couldn't do so the day before."
    "The walk to city hall was very pleasant, though the worst part was ignoring the smells coming from the bakery."
    "Your stomach is growling, but unfortunately you don't have any money to pay for a potential meal."
    you "{i}I CAN'T TAKE IT... I'm so hungry. I should have borrowed money from someone yesterday. Well, I just have to hold out until the end of the day.{/i}"
    you "{i}Or maybe they'll let me put this bread on credit and I'll pay for it later... Although that practice disappeared with the fall of the PRL...{/i}"
    you "I can do this!!!"
    "The streets are now bustling with life, and everyone is hurrying to work."
    "As you approach city hall, it impresses you once again - not as much as yesterday, but it is still very impressive."
    "There is no time to waste, so you enter the building and look for Filip."
    jump ch02_goingToKur

label ch02_goingToKur:
    play sound "sfx_footsteps_a.mp3"
    scene bg cityhallinside with dissolve
    "As you walk inside, you smell freshly brewed coffee and warm buns. The smell is driving you insane."
    scene bg secretary with dissolve
    play sound "sfx_door_open.mp3"
    "As Filip leaves Barbara's office carrying an empty tray, you walk up to him."
    show filip normal with dissolve
    you 'Hey...'
    f "Heyy! "
    show filip shocked with vpunch
    f "God, you look awful. What happened?"
    you "Okay this is actually really awkward"
    you "I havent eaten anything since yesterday"
    you "Do you have literally any food here i'm hungrier than a shein worker"
    show filip normal
    f "Yeah. Every day I bring Barbara Rafał's warm buns with coffee."
    you "Could you give me one? I don't have any money, so I can't buy food."
    you "I'm literally about to DIE if I don't eat something!!!"
    f "Sure. I have some stale ones i was too lazy to throw out. Is that okay?"
    you "YES"
    f "Okay"
    show filip normal at offscreenright with move
    "Filip puts the plate down by the sink and disappears into the storage room."
    "You can hear him moving something out of the way just to reach the bun you so desperately crave."
    show filip normal at center with move
    "He comes back and hands you one of Rafał's buns. It's stale, but you don't exactly have a choice."
    "You grab Rafał's bun and devour it. Even though it's expired - just like Tuleja - it still tastes top-tier."
    you "Oh my god, what is this thing made of? It's stale but it's so good that...{w} I have no words."
    f "It tastes that good because you're starving."
    f "But honestly, they are actually really good. You should go to the bakery when they're fresh."
    f "They're even better then."
    f "Everyone in this city loves Rafał's buns."
    you "Where did you buy them?? I want one too when I have money."
    f "At BBB in the town square."
    you "What do you mean BBB???"
    f "You don't get it? {i}{u}Big Buns Bakery{/u}{/i}..."
    f "Anyway, it's right here. The bakery is pretty big, so you'll definitely notice it."
    "Filip points out the bakery's location on the map."
    "You quickly figure out where it is in the town square."
    f "And about the money..."
    f "You should ask Barbara about work. She'll help you."
    you "Thank you! Thank you! Thank you!"
    you "You're literally saving my life right now!"
    play sound "door_knock.mp3"
    "You politely knock on Barbara's door, trying to do it exactly the way Filip did yesterday."
    with vpunch
    k "WHO IS THAT?"
    you "It's me!"
    k "And who's 'me'?"
    you "[name]"
    k "Come in."
    scene bg office with dissolve
    play sound "sfx_door_open.mp3"
    "You enter her office and see that she's once again busy with some documents."
    you "{i}Is she going to be mad at me for just walking in here like this?{/i}"
    you "{i}I hope not.{/i}"
    you "{i}But she literally told me yesterday to come back... So, good morning I guess.{/i}"
    show kurowska normal with dissolve
    you "Good morning. Yesterday you told me to come see you about that job... I think..."
    k "Yes, I remember."
    if flag("rudeToBarbara"):
        jump ch02_goingToKurRude
    else:
        jump ch02_goingToKurNotRude

label ch02_goingToKurRude:
    k "Find yourself a job."
    you "But..."
    k "'But, but, but' - quit trying to weasel your way out of it!"
    k "Get out and go find work!"
    "A furious Barbara throws you out of her office."
    show bg secretary with vpunch
    play sound "sfx_door_slam.mp3"
    you "{i}I didn't even get the chance to apologize...{/i}"
    jump ch02_goingToFindAJob

label ch02_goingToKurNotRude:
    k "You have to find a job yourself. Just ask your friends, I'm sure they'll help you."
    "Barbara starts looking for something on her desk again."
    "..."
    "This time, she actually finds what she was looking for."
    k "Here. This should be enough to keep you alive until you find something."
    "Barbara gives you a pouch full of coins."
    "It's ridiculously heavy..."
    k "Here."
    you "What is this?"
    you "Why are these coins so heavy?"
    k "Because there's alot of them"
    k "I was supposed to give this to Filip to use as change for people but then he raised the prices"
    k "And now i do not need this"
    k "I've kept them in my office for a whole month and wanted to get rid of them anyway, so this is a win-win situation."
    k "Now go find a job and make me proud!"
    you "Thank you so much. I definitely will."
    scene bg secretary with dissolve
    play sound "sfx_door_open.mp3"
    "You leave her office and say goodbye to Filip. Now you finally have some money and can actually do things{w=0.5} without starving to death."
    scene bg citysquareday with dissolve
    play sound "sfx_footsteps_b.mp3"
    "After rush hour, the streets are practically empty apart from a few homeless people and some mildly threatening individuals."
    you "{i}I couldn't have spent THAT long at Barbara's if there's barely a living soul on the street. Everyone's probably at work.{/i}"
    you "{i}And now it's time to buy myself a NUTRITIOUS breakfast.{/i}"
    you "{i}I'm going to BBB.{/i}"
    "As you walk past the fountain, a man attacks you. He's short, but still threatening."
    play music "outfoxingthefox.mp3"
    show kamil normal with vpunch
    m "Give me all the money you have!!!"
    you "WHAT! No, please don't hurt me, but I can't give you this money."
    you "I haven't eaten anything since yesterday. I got this money as a gift. I need it for food and clothes because I'm hungry and basically naked."
    m "Alright, I have a heart, so I'll let you fight for whether or not you have to give me your money."
    you "THAT'S LITERALLY NOT FAIR!"
    m "Life isn't fair."
    m "Now answer my question: 'What's the capital of France?'"
    "Your entire life flashes before your eyes as he asks the question."
    "There is no time to think. Only to act."
    menu:
        "Paris":
            jump ch02_KamilRobberyCorrectChoice

        "Timbuktu":
            jump ch02_KamilRobberyWrongChoice

        "Tell him to smile more":
            m "Why"
            you "Yellow is my favorite color"
            jump ch02_KamilRobberyWrongChoice

label ch02_KamilRobberyCorrectChoice:
    play sound "gong.mp3"
    stop music
    "You answer with confidence as every shadow of doubt is swept away by the wind."
    "His ears twitch when he hears your answer, and his eyes widen."
    "In fact, his entire expression changes."
    "You still can't decipher his reaction or tell whether you made the right choice."
    "He stands there staring at you, trying to build suspense."
    m "..."
    m "How did you know?"
    m "Grrr....."
    "The strange man starts growling at you like an alpha."
    m "Heh... Besides, I knew you were going to say that..."
    you "{i}???{/i}"
    you "{i}Is that good or bad{/i}"
    m "Fine, keep your precious finances..."
    you "How do you like that, huh? Now get out of here before I report you somewhere."
    m "But how... fine... you win this time...{w} BUT NEXT TIME IT WON'T BE THIS EASY!!!!"
    play music "town_day.mp3"
    hide kamil with dissolve
    you "{i}I'm not carrying money around with me anymore...{/i}"
    jump ch02_gotMoney

label ch02_KamilRobberyWrongChoice:
    play sound "gong.mp3"
    stop music
    "You answer with confidence as every shadow of doubt is swept away by the wind."
    "His ears twitch when he hears your answer, and his eyes widen."
    "In fact, his entire expression changes."
    "You still can't decipher his reaction or tell whether you made the right choice."
    "He stands there staring at you, trying to build suspense."
    m "..."
    m "I'm not giving your money back."
    you 'Damn it!'
    m "GG FREAKING EZ, NOW GET LOST BEFORE I TAKE EVEN MORE FROM YOU."
    menu:
        "Respond normally":
            you "Buy cheap, buy twice."
            m "???"
            hide kamil with dissolve
            you "{i}I don't think he understood me...{/i}"
        "Be a final girl":
            you "But I don't have anything else."
            m "Ha-ha-ha! You're poor!"
            you "Then why are you robbing people?"
            you "Because you don't have any money of your own?"
            m "You don't even know what you'd spend it on anyway."
            you "I wanted to buy buns at BBB?"
            m "But those have so many calories..."
            you "If you're that worried about calories, think about the ones in your brain."
            you "Because there are none, just like Pepsi Zero."
            hide kamil with dissolve
            "The thief starts crying and runs away."
            you "{i}Not my problem.{/i}"
    play music "town_day.mp3"
    you "{i}Because of that idiot, now I have to go back to Barbara and ask what I'm supposed to do...{/i}"
    you "{i}I'm kind of scared of what she might do, but whatever. I can't think of anything else.{/i}"
    scene bg secretary with dissolve
    play sound "sfx_footsteps_a.mp3"
    "After being robbed there is no other choice but to go back to Barbara"
    "Even if she doesn't have any more money for you, it would be wise to report this"
    "When you enter the city hall, filip is not there, which is confirmed by a cacophony of noises coming from the storage room"
    "With no other choice, you knock on Barbara's door"
    "..."
    you "Good morning! It's me again."
    k "Come in."
    scene bg office with dissolve
    play sound "sfx_door_open.mp3"
    "As you walk in, you can tell she's been practicing skip B."
    show kurowska normal with dissolve
    you "Sorry to bother you again, but I got robbed."
    you "They took all my money. Now I don't know what I'm supposed to do."
    you "Could you help me?"
    "You smile like you're in a real estate commercial."
    k "What am I, a fortune teller?"
    you "No... But I thought you'd help someone in need..."
    k "I gave you everything I had. Nobody else got anything, and they're not complaining."
    k "Find. A. Job."
    hide kurowska normal with dissolve
    jump ch02_goingToFindAJob

label ch02_goingToFindAJob:
    scene bg citysquareday with dissolve
    play sound "sfx_door_open.mp3"
    "You go outside to figure out what you should do next."
    "Like Barbara said, you should pick someone you know and go ask them for work."
    "You stand in the town square looking around like you're about to kiss the ground while holding a cypress cross."
    "Who do you go work for?"
    menu:
        "Vasili (this is the more interesting option)" if flag("metVasili"):
            you "{i}I'll go to him just for the plot.{/i}" 
            you "{i}Besides, I don't think I have a better option.{/i}" 
            $ flag("workedAtVasili", True)
            jump ch02_workingAtVasili
        "Filip":
            you "{i}Barbara doesn't have any work for me, but Filip might.{/i}" 
            $ flag("workedAtFilip", True)
            jump ch02_workingAtFilip

label ch02_workingAtFilip:
    "You go back to city hall and head over to Filip."
    scene bg secretary with dissolve
    show filip normal with dissolve
    "This time he is actually doing his job and not lollygagging in the storage room"
    play sound "sfx_door_open.mp3"
    you "It's me again."
    f "Hii."
    you 'One more question.'
    f 'Yeah?'
    you 'Do you have any work for me?'
    you 'Is there literally anything I can do?'
    f 'Hmm...'
    f "I {i}do{/i} need to move mail from that storage room to Barbara but i am wayy too lazy for that"
    you "I can do it"
    f "Then wait here"
    show filip normal at offscreenright with move
    "Filip gets up and goes into his closet again." 
    "You can hear him moving heavy boxes again, but this time it takes longer." 
    you "{i}How big is that storage room what{/i}"
    show filip normal at center with move
    "Filip finally gets out of the suspiciously large storage room while pulling a huge luggage cart full of paper" 
    "Before you know it, there are four tall stacks of paper in front of you"
    you "Okay i have two questions"
    you "First of all is what the hell is in that storage room?"
    you 'And what the hell is this'
    f 'Oh, that\'s just some paperwork and mail that never made it to Kurowska.'
    f 'I just kept collecting it for years and figured it wasn\'t that important, so I held onto it.'
    f 'And now she wants to see all of it.'
    you 'So what am I supposed to do with this??'
    f 'Take all of it and bring it to Kurowska.'
    you "Cant you just shove the whole luggage cart through the door?"
    f "No because it is too wide"
    you "Oh my god"
    you 'But I can\'t lift all that, are you insane??'
    f 'I\'m not telling you to carry it all at once, dummy.'
    f 'There\'s like 120kg of paper here, I don\'t expect you to lift all of it.'
    f 'Especially with that snatched waist of yours...'
    you 'Okay cool...\n {i}HE NOTICED!!!{/i}'
    "You pick up a stack of paper the size of anna karenina and your spine cracks"
    "Then, with all that paper still in your hand, you take one step and decide against doing a second one"
    "You go back and leave half of your 40cm stack on the luggage cart"
    "Only then your back allows you to move"
    "You knock on Barbara's door"
    if flag("rudeTo Barbara"):
        k "WHO KNOCKS LIKE THAT FOR BEELZEBUB'S SAKE??"
    else:
        k "Come in."
    scene bg office with dissolve
    show kurowska normal at center with dissolve
    "You enter her office and see her knee-deep in documents, like she always is"
    you "{i}Does she really have time to read all this?{/i}"
    you 'Where do I put this?'
    k 'On my desk.'
    you 'Are you sure? This paper is NOT skinny.'
    k 'Fine, leave it on the floor.'
    "You leave the first stack of papers on the floor." 
    scene black with dissolve
    "After a while you get bored, so you start reading what you're carrying."
    "Apparently, you're carrying some complaints."
    "Every headline is worse than the last."
    "The first page is titled 'Report on Noisy Neighbors'."
    if flag("metVasili") or flag("knowsAboutVasili"):
        you "{i}Obviously it\'s about Vasili, pff..{/i}"
    "With every line it gets harder not to laugh because this report is so absurd it barely feels real."
    "No wonder Filip decided it wasn't important - it looks like some kind of fanfic."
    you "{i}\"Shouting 'VAPORIZE THE BOURGEOISIE!!!' while I was working was inappropriate.\" {/i}"
    you "{i}WHO WROTE THIS?{/i}"
    "You bravely carry them one by one, but part of you just wants to keep reading this garbage."
    "The headlines keep getting wilder..."
    "{i}'Rafał's hat is causing drama among Bratgrenians.'{/i}"
    "{i}'Complaint about Colorado bugs attacking tomatoes.'{/i}"
    "{i}'Someone took a shit in front of my house, please remove it.'{/i}"
    scene bg office with dissolve
    show kurowska normal at center with dissolve
    "Before you know it, you've moved everything and run out of headlines to read."
    you 'That\'s a lot of mail...'
    k 'What? What mail?'
    you 'The stuff I\'ve been carrying for the last 40 minutes.'
    k 'MAIL?? Please get it out of here, that\'s Filip\'s job, I have more important things to deal with!'
    you 'Then why did I spend so long carrying it all here?'
    k "You tell me"
    "You dejectedly pick up the pile of mail and go back to Filip."
    scene bg secretary with dissolve
    show filip normal with dissolve
    f 'What are you doing back here with those papers?'
    you 'Barbara said you\'re the one who\'s supposed to answer the mail.'
    you "And that I have to carry it all back."
    f 'WHAT? They\'ll close the vestibule before I finish answering all of these...'
    f 'Fine... bring all of it here.'
    "After another 20 minutes, you finish working for Filip, who is now lying devastated on top of a pile of papers."
    f 'Thanks for the help, even though basically nothing changed.'
    f 'As promised, here\'s some spare change.'
    jump ch02_gotMoney

label ch02_workingAtVasili:
    scene bg lakedaya with dissolve
    play sound "sfx_footsteps_a.mp3"
    "The walk to the lake today is, surprisingly, calmer than yesterday."
    "Despite it being daytime and life bustling all around, it was quieter than last night."
    "All you could hear in the background were birds. The lack of Vasili singing made life better."
    scene bg lakedayb with dissolve
    play sound "sfx_footsteps_a.mp3"
    "When you reach the lake, there's not a soul in sight."
    "The only thing you see is smoke rising from a cabin right next to the lake. You also notice a green aura floating around it."
    "{i}That green aura... Whoever lives there must be completely detached from reality. I'll visit that place another time.{/i}"
    "Unable to find Vasili, you start heading back toward city hall. In the distance, however, you notice a house that looks pretty cozy."
    scene bg vasilihouse with dissolve
    play sound "sfx_footsteps_a.mp3"
    you "{i}Seems safe enough, maybe Vasili lives there...{/i}"
    "As you get closer, the muffled singing grows louder."
    "When you knock on the door, your favorite - also your only - fisherman steps outside."
    show vasili normal with dissolve
    if flag("endorsedCommunism"):
        v "Welcome, comrade."
        you "Uhh? Hi..."
        v "What brings you to {b}OUR{/b} humble abode...{w=.6} HAHAHA because you know...{w=.6} collectivization of property..."
        you "haha.. I get it. But I didn't come here to chat."
        you "Barbara told me to find work, so I figured I'd ask if you had anything for me to do."
        v "Ah, the free market...{w=.3} nothing but problems..."
        v "In a normal workplace you'd get a job immediately, and now you money."
        you "I don't have any for food."
        v "Fine... although this will be the first and {b}LAST{/b} time we give you work - we despise the free market..."
        v "As we said, you must collectivize the tax from the petty bourgeoisie residing within our grand estate." 
        v "We, as nobles, demand your full obedience and indifference toward the pleas and bribes of those beneath us." 
        "In other words, you need to collect the eggs from the chickens in the coop." 
        v "Additionally, we request that you condemn the actions of the bourgeoisie by setting them upon the proper intellectual path, using the biography of our magnificent leader and father of our nation - Ed Sheeran, who ought to rule over our common folk for decades to come." 
        v "So once you've collected the eggs, read the chickens the biography of our {b}FATHER{/b}."
        you "..."
        you "{i}What{w=.6} is happening here???{/i}"
        you "{i}Okay I have an idea...{w=.6} Now watch {b}THIS{/b}!!!{/i}"
        you "That's a lot of information, but if you keep saying all of this is ours..." 
        you "So can I move in with you?"
        v "Unfortunately not." 
        v "Your lineage does not permit such indulgence against your axioms." 
        v "Your actions and obligations are distinct, therefore, within this predicament, under no conceivable circumstance - by the power bestowed upon us by our lord and father Ed Sheeran - are we able to grant you shelter within our modest place of existence." 
        you "{i}{b}WTF IS GOING ON HERE. I DON'T WANT THIS. I WANT TO GO HOME... our HOME???{/b}{/i}"
        you "Okay... I guess I'll go collect the eggs...?"
        v "Collect the tax."
        v "Just remember to be ruthless."
        "As you walk away, you hear Vasili start singing \"The Internationale\"."
        you "{i}I'M NEVER COMING BACK HERE AGAIN...{w=.6} maybe just for the money...{/i}"
        scene bg kurnik with dissolve
        "Just like Vasili said, the chicken coop is right behind the house." 
        "But... he forgot to mention one thing..."
        you "{i}THE CHICKENS ARE RED?!{w=.6} I can't...{/i}"
        you "{i}WHY???{/i}"
        you "How could he do this to you..."
        m "Unfortunately.... y-"
        you "{b}WHAT?! WHO SAID THAT?{/b}"
        show kura with dissolve
        kura "Me.{w=.6} Down here."
        kura "Yes, I am the symbol of the rural people oppressed by the bourgeois eggs of big capital."
        kura "Or a representative of the lower class - because the bourgeoisie sits on the upper shelves - of the valuable commodity known as poultry."
        you "I think I'm hallucinating.... this is all because of his red aura."
        kura"Unfortunately for you...{w=.6} we can talk."
        kura "Vasili taught us because he decided he'd rather listen to the problems of the lower class than deal with them..."
        you "I don't think that explanation helped.{w=.6} Whatever, I need to take your eggs."
        kura "You need to do WHAT???"
        you "Collect the eggs....{w=.6} AHHH{w=.3} collect the tax???"
        kura "Okay, you should've said that from the start."
        kura "Unfortunately, we don't have much to hand over because Vasili collected a tax this morning for sleeping through the night..."
        you "Whatever. I just need to earn enough to eat and you will {b}NOT{/b} see me here again."
        scene bg vasilihouse
        "After collecting all the eggs, you go back to Vasili to hand them over. You knock and he opens the door again."
        show vasili normal with dissolve
        v "So?{w=.3} Was collecting tax from the lower social classes a success?"
        you "Yes...{w=.3} Can I get paid now? I'm starving."
        v "Fine... I just don't know if you'll make it before the bakery closes."
        v "There was a delivery today, so the lines are probably four hours long...{w=.6} Oh wait{w=.3}, free market..."
        v "If you hurry, you can still get Rafał's buns while they're warm."
        you "Thank you! Goodbye." 
        v "Farewell, comrade."
        hide vasili with dissolve
    else:
        v "Hello!"
        you "Hi..."
        v "What brings you to my humble doorstep."
        you "Barbara told me to find work, so I figured I'd ask if you had anything for me to do."
        you "So... do you have anything I could do?"
        you "I really need this. I don't even have money for food."
        v "Sure... let me think...{w=.3} hm...{w=.6} Okay, I know - I need you to feed my foxes."
        v "I haven't had time today, so they're probably a little pissed off."
        v "But I know you can handle it."
        v "Their enclosure is right behind the house."
        v "(If I were you, I'd hurry before they get too angry.)"
        you "{i}Okay... not the hardest job in the world, but I hope those foxes are nice to me.{/i}"
        "Vasili gives you fox food in an IKEA container and you leave the house to feed the hungry little foxes."
        hide vasili with dissolve
        "You go behind his house and see..."
        "Actually, you don't see anything because there are no foxes"
        you "{i}Excusez moi{w=.6} nobody's here!{/i}"
        menu:
            "Make fox noises":
                    "You can't think of a single sound a fox makes."
                    "Foxes don't meow, they don't bark, they don't go into alpha mode."
                    "Maybe foxes are just quiet? All these thoughts race through your head while you stand there like an idiot holding a food container."
        you "{i}What am I supposed to do???{w=.3} I'm about to cry...{/i}"
        you "{i}I KNOW!!!{/i}"
        you "{i}I'll leave the food behind the house and they'll come on their own.{/i}"
        you "{i}They're probably scared of me, that's why I can't see them{/i}"
        "You open the container, leave it on the ground, and go back to Vasili."
        show vasili normal with dissolve
        v "Have you ensured the satisfaction of the basic nutritional needs of my animals originating from outside the local ecosystem?"
        you "{i}Hell no!{/i}"
        you "Actually!{w=.3} There's nothing behind your house."
        v "What do you mean?"  
        you "{i}I said what i said.{/i}"
        you "Yeah, I just left the food you gave me there."  
        you "Now where's the money."
        you "How much do I get for all my hard work?"
        v "What do you mean there are no foxes behind my house?"  
        you "I said what I said because that's how it is?"  
        v "Bruh. maybe they didn't come out because you're new."
        v "You should stay there. Maybe they'll come then."  
        hide vasili with dissolve
        "You go behind his house yet again and see a little fox eating from the container you left there."
        "Its fur is whiter than the teeth in a Colgate ad. It looks very weak..."
        you "{i}Oh{w=.3} my{w=.3} god!{w=.6} Why is it so cute?{/i}"  
        you "{i}I can literally see its ribs through its skin... Does that mean it's dying?{/i}"
        "You go back to Vasili and knock on his door for the third time."
        show vasili normal with vpunch
        v "You again!"
        you "There's a little fox behind your house eating the food."
        you "It's very petite. What do I do??"
        v "I need to see it!"
        "He leaves the house with a red aura trailing behind him."
        "You both go behind the house and watch the little white fox continue eating its food"
        show vasili normal at leftish with move 
        show lis at rightish with dissolve
        if random.randint(1,100) == 1:
            "You're close to the fox, so Vasili starts whimpering."
        else:
            "You're close to the fox, so Vasili starts whispering."
        v "Oh my god, can't you see it's injured?"
        "You whisper back."
        you "How do you know it's injured?"  
        v "Can't you see its leg is bent 90 degrees south?"  
        you "How do you even know where south is?"  
        lis "I can hear you!"  
        you "..."
        "You look at Vasili with pity."
        you "You know what...{w=.3} I've had enough!"  
        you "Give me my money and I'm leaving."
        v "Wait!"  
        "Vasili picks up the little fox."
        "You can't see what he's doing, but you hear ASMR."
        v "There. Better."  
        lis "Thanks!!!"  
        "The little fox does a pirouette and hops off into the forest."
        hide lis with dissolve
        you "What{w=1} just happened..."  
        show vasili normal at center with move 
        v "That idiot is always spraining something."
        you "Okay...{w=.6} I'm not going to ask questions."
        you "Just pay me and I'm leaving."
        v "Fine. Here."
        you "Thanks!"
        v "See you, comrade!"
        hide vasili with dissolve
        you "{i}I'm never coming back here again!{/i}" 
        you "{i}Even if I have to starve!{/i}"
    jump ch02_gotMoney
    
label ch02_gotMoney:
    scene bg citysquareday with dissolve
    "You're sick of being hungry, so you head straight to BBB."
    "(Big Buns Bakery) duhh"
    jump ch02_gotMoneyBakeryEntrance

label ch02_gotMoneyBakeryEntrance:
    scene bg bakeryfrontday with dissolve
    play sound "sfx_footsteps_b.mp3"
    "The bakery really is big. The smells drifting through the street are driving you insane."
    "The smell of yeast hangs in the air, and the display window is packed with baked goods."
    scene bg bakeryinside with dissolve
    play sound "sfx_footsteps_a.mp3"
    "The first thing you notice inside is the Taylor Spit posters."
    "But.{w=0.5} There's a line."
    "This leaves you with time to take in the surroundings"
    "From the brick walls to the warm glow of incandescent light bulbs, every piece of the interior was deliberately chosen by the owner"
    "Every little detail, even the posters made the bakery feel premium - a word your wallet is not ready to hear"
    show wp normal at leftish with moveinleft
    show fraucrusty normal at center with moveinleft
    show rafal normal at rightish with moveinright
    "There are two people in front of you."
    "First in line is Frau Crusty."
    if flag("metWiktoriaP"):
        you "Oh, hey."
        wp "Hey! What's up?"
        
        if flag("workedAtFilip"):
            you "It was awful... I had to work..."
            wp "Who did you go to?"
            you "Filip."
            you "He made me carry documents to Kurowska."
            you "And when I finished, Barbara made me carry all the letters back."
            you "Because he's the one who's supposed to read them."
            wp "You should've demanded money and left after that."
            wp "And skibidi."
        elif flag("workedAtVasili"):
            you "It was awful... I had to work..."
            wp "Who did you go to?"
            you "Vasili."
            if flag("endorsedCommunism"):
                you "You know what, it wasn't bad."
                you "We have similar political views."
                "Wiktoria gives you a bombastic side eye."
            else:
                you "Jesus, it was awful, he kept talking about communism the entire time."
            you "Don't even get me started."
            you "You know him better than I do, so you can probably imagine what it was like."
            wp "Let me guess."
            wp "Was he singing \"The Internationale\"?"
            you "Yeah..."
            wp "My condolences..."
        else:
            you "Can you believe Kurowska gave me money"
            wp "Just like that??"
            you "Yep!"
            you "Just like that."
            wp "Aren't things going a little too well for you?"
            you "No."
    else:
        "Right in front of you is Wiktoria P."
    jump ch02_gotMoneyBakeryCustomer

label ch02_gotMoneyBakeryCustomer:
    frau "What kind of outrageous question is that?"
    frau "Of course I have money."
    frau "I'm just 23 forints short today."
    frau "Can I bring them tomorrow???"
    m "I'm not a bank. That's not how this works. I'm not giving you the cake unless someone pays for it."
    frau "But it's my birthday today!!!"
    menu:
        "Give her some coins":
            you "Here."
            frau "My gyatt is staying here for good!"
            frau "Thank you, kind furry."
            with vpunch
            show fraucrusty normal at offscreenleft with move
            "Frau Crusty leaves the bakery with the cake using a C-skip."

        "Pretend you didn't hear anything":
            frau "You're all rude and aggressive."
            with vpunch
            show fraucrusty normal at offscreenleft with move
            "Frau Crusty leaves the bakery without the cake using a C-skip."
    hide fraucrusty
    jump ch02_gotMoneyBakeryTea

label ch02_gotMoneyBakeryTea:
    wp "Okaaay."
    m "Hii."
    wp "Hey, what's up?"
    m "Nothing really, I've been delirious all day."
    wp "Sounds pretty standard for you."
    "They both start laughing."
    wp "I'll have 3 Rafał buns."
    m "Sure."
    "You can see entire baskets full of Rafał buns in the back."
    "You stare at those buns like they're luxury single-serve desserts from Los Angeles."
    "Except Rafał's buns don't cost $15 for 150g."
    "You have absolutely no idea what currency this city uses - this is the first time you've seen it."
    "You have some money, but you don't know whether it's enough for one bun or a hundred."
    you "{i}These buns are insanely popular here.{/i}"
    you "{i}I would destroy one of those right now..{/i}"
    m "Here you go."
    "Suddenly, another man you don't recognize walks in."
    "He looks like some kind of pimp."
    show niuniu normal at leftish
    show wp normal at rightish
    show rafal normal at right 
    with move
    m "Jesus, you again."
    m "Yes, Rafał, it's me!"
    r "What do you want from me this time?"
    m "Show me what's under your hat."
    "Wiktoria starts whispering to you so she doesn't draw attention to herself."
    wp "That's Niuniu."
    wp "He's the guy who comes up with conspiracy theories around town."
    wp "And this time Rafał is the victim."
    wp "He was at a Taylor Spit concert, and during the show she threw her hat at him."
    wp "He's worn it ever since."
    wp "And Niuniu decided he's hiding something underneath it."
    show rafal normal at center 
    show wp normal at rightish 
    with move
    r "Nope, okay, I've had enough."
    "Rafał grabs a broom and hits Niuniu."
    with vpunch
    n "AAAAA"
    r "Sharp or dull"
    n "Sharp?"
    r "No. Try again."
    with vpunch
    "He hits him again."
    n "Yeah, that's sharp."
    r "Get out of my bakery before I play sharp or dull with a brick."
    n "Okay, okay."
    show niuniu normal at offscreenleft with move
    show wp normal at leftish with move
    show rafal normal at rightish with move
    you "My condolences."
    you "Do you actually have a brick somewhere in here?"
    r "Yes. I'm prepared."
    'He pulls out a huge red brick with both paws and proudly shows it to you like it\'s his child.'
    'The brick was old. Really old.'
    menu:
        "Skip the brick":
            $ telemetry_flag("skippedBrickDescription")
            jump ch02_brickDescriptionEnd
        "No i want to hear all about it":
            pass
    'At first glance, you can tell that there\'s no way to tell exactly how old it is - the countless chips and scratches make that obvious.'
    'In fact, it was so old that assigning any number to its age felt insulting not only to the brick, but also to whoever made it.'
    "Calling it simply 'old' would erase the centuries it had survived."
    'The brick had long since lost its sharp edges and become rounded, as if it had been used many times.'
    'One corner was especially worn down, and even the smartest person in town couldn\'t tell you why it was chipped or where exactly that corner even was.'
    'Only Rafał could know - assuming he knows or remembers what happened to it.'
    'The brick\'s only purpose was being thrown, so you try not to jump to conclusions about who will be, or already has been, its victim.'
    'Looking at the chipped corner, it becomes clear that it is the result of some airborne event.'
    'You could almost call it a miracle that the brick hasn\'t split in half yet.'
    "That it hasn\'t split in half like a watermelon falling onto a knife from 100m in some YouTube video"
    'Its amorphous porcelain structure had remained strong all these years, which is more than can be said for some relationships.'
    'The brick was old enough to pass for the oldest object on this planet - or wherever you are now.'
    'You don\'t know exactly where you are, but one thing is certain - this brick is older than the ground you\'re standing on.'
    'Old age was no longer an adjective for it, but an inherent property.'
    'No matter where Rafał touches the brick with his little paws, some dust and crumbled clay falls off, like the brick has dandruff.'
    'Rafał completely ignores the mess he just made, as if he\'s used to it.'
    'He also ignores the dust on his soft paws because he knows he\'ll put this delicate clay product away in a moment anyway, so there\'s no point washing them.'
    'At this point, any reasonable person would stop thinking about the brick.'
    'You don\'t.'
    show wp normal at offscreenright with move
    'One side of the brick was darker than the others - as if it had been exposed to the elements while the rest sat safely inside a wall.'
    "Real scientists could spend their entire lives studying this difference and still never reach an agreement."
    "That was how mysterious this brick was."
    'There\'s no way to tell whether Rafał removed the brick or whether it fell out on its own.'
    'You can tell, however, that the brick {i}belongs{/i} to this bakery because of its distinctive but faded red color, duller than the rest of the bricks in the bakery.'
    'Looking closer, you see all its imperfections - marks left behind by time.'
    'The cracks are filled with dust so old and so deeply embedded that not even water could reach it.'
    'They\'ve become part of the time capsule that is this brick.'
    'This brick was probably older than you and had been in this city long before you were born.'
    'It has witnessed hundreds, if not thousands, of people and millions of spoken words.'
    'The brick knows all the city\'s secrets, but it cannot speak or reveal the truth.'
    'It also had a clearly designated spot under Rafał\'s counter, where he kept the register and handled daily business.'
    'Not every customer knew - or could even suspect - that this brick existed.'
    'If Rafał pulls it out in front of you, it means you\'re either a victim or a close friend.'
    'You also notice small multicolored stains scattered across its surface - each one different, each with its own shape, size, and story.'
    'One might be two days old while the one next to it could be over two years old, with no way to tell which is which.'
    'Because carbon dating hasn\'t been invented in this universe.'
    "Despite the apparent ordinariness of this 'random brick', you can't shake the feeling that the everyday lives of Bratgren's residents are somehow embedded in its amorphous structure."
    'From the oblivious footsteps of people too busy to notice an ordinary brick, to the heavy rain that simply happened to soak everyone.'
    'All of those events didn\'t just leave stories behind - they became sediment.'
    'A thin, fragile layer of tiny things that changed this brick, brick by brick, step by step.'
    "You stare at the little holes in the brick when suddenly something starts to dawn on you."
    "The brick makes you feel something you haven't felt before."
    "At least not in this city."
    "For reasons you can't explain, looking at it fills you with determination."
    "Determination so strong that all your plans, the ones you've postponed forever, suddenly seem not only possible but necessary."
    'You can no longer stop the whirlwind of thoughts this ancient piece of architecture has caused in your head, so you let out a long, dramatic sigh.'
    'You want every other brick in this cozy café to know that you understand its history.'
    'This brick and its past inspire you to keep going and never give up.'
    'To an ordinary person it was just a brick, but your eyes see something else - a source of inspiration and determination inside such a simple object.'
    "Helen Keller once said - \"Alone we can do so little; together we can do so much\" - and nothing could describe this brick better."
    jump ch02_brickDescriptionEnd
label ch02_brickDescriptionEnd:
    'The brick was a part of something bigger, but its impossible to tell what.'
    "Bricks can be used to build anything - from a small wall during a protest in France to a huge villa that can withstand a tornado."
    'Just like one of those bricks, you are a part of this city'
    'A city that welcomed you with open arms.'
    r "Why are you staring like that"
    "The sudden question catches you off-guard, interrupting your delusions"
    you "I got inspired?"
    "When you snap back to reality you notice Wiktoria had already left the bakery"
    r "Weirdo"
    "Rafał puts the brick back where it belongs - below the register"
    r "Okay so what do you want"
    you "Uhhh"
    "There are many buns laid out in front of you"
    "Each one was deliberately laid out to appear different"
    "when in reality its the same exact thing"
    you "I'll have four buns"
    "Rafał wipes his dirty paws and assembles your order"
    r "Anything else?"
    you "Do you have any cold drinks i could buy?"
    r "Yes i sell bottled performative-ness"
    you "what"
    r "Its an iced matcha latte"
    you "No thank you"
    "The black cat eagerly taps the buttons on the cash register"
    r "That will be $80"
    you "Uhh.. i have a really stupid question"
    r "Yes?"
    you "Is $80 alot of money?"
    you "You know, i was born yesterday"
    r "Its not alot but its not spare change"
    r "There's cheaper food across the street if you want that"
    r "In here you are also paying for the skills needed to make such a bun"
    "BBB is the equivalent of a millenial burger place with black gloves, fake brick walls and food served on a cutting board"
    you "Here you go"
    r "Thank you and BON APPETIT"
    you "Bye"
    "You look at the bag of coins in your hand and start thinking"
    "Would you still be holding money right now if Piotr didnt come to help?"
    "And to think that you were so rude to him"
    you "{i}I really do need to apologize to him{/i}"
    you "Wait"
    you "Where does Piotr live?"
    r "He has a potions shop down the street"
    r "Piotr lives in the same building"
    r "You wont miss it theres a sign outside"
    you "Okay thanks"
    you "But... i'm not done"
    you "I have an unusual request"
    you "I want to get something for Piotr. What should i get?"
    r "Well.. I dont know how to describe him BUT if he was a color he would be blue"
    r "And not the sky blue because that has too much sky"
    r "Also he wouldnt be navy blue either bc its blue with responsibilities"
    r "Its the kind of blue you think of when looking at something green"
    r "Maybe get something.. rectangular..??"
    "With every word Rafal says your confidence quickly gets replaced with confusion"
    "They say that a smile goes a long way when trying to be polite"
    "That is exactly why you keep smiling even though you have absolutely no idea what he is saying"
    menu:
        you "Okay that makes sense"
        "3 cups of coffee in a paper bag":
            $ flag("gotCoffeeForPiotr", True)
            $ piotrFoodPoints = 2
        "Bread in a paper bag":
            $ flag("gotBreadForPiotr", True)
            $ piotrFoodPoints = 0
        "A slice of red velvet cake (in a paper bag)":
            $ flag("gotCakeForPiotr", True)
            $ piotrFoodPoints = 1

    r "Okay give me just a moment!"
    "Rafał twirls on his right foot and assembles your order with pride"
    "You watch him swiftly assemble your order, and when he comes back you are already ready to pay"
    "He puts your apology gift on the table, and the plain paper bag gives you an idea"
    you "Can i have a pen i want to write something"
    r "Yes sure"
    menu:
        you "{i}I want to write...{/i}"
        "Sorry :(":
            $ piotrWritingPoints = 2
        "Sorry but be more fun next time":
            $ piotrWritingPoints = 0
        "Sorry i forgot your name":
            $ piotrWritingPoints = 1
        "Sorry, i forgot your name":
            $ piotrWritingPoints = 0
    "You scribble away trying to keep every letter steady and even with the rest"
    you "{i}Perfect{/i}"
    you "Okay that should be it. Thank you very much"
    r "No problem senorita"
    you "Bye"
    r "Byee"
    scene expression loc_bg("lanastreet") with dissolve
    "Finally happy, you leave the bakery and head straight to Piotr"
    scene expression loc_bg("cityexit") with dissolve
    "Rafał was right - it {i}was{/i} hard to miss the shop"
    "Especially the HUGE wooden door which was blocking half the pavement"
    scene bg potionshop with dissolve
    you "HELLO EVERYONE"
    "Your impatience knows no bounds. You are ready to jump over the counter just to apologize to piotr"
    you "{i}Where is this bird{/i}"
    you "PIooooOTR come here"
    "Piotr emerges from the back of the shop"
    show piotr normal at center with dissolve
    you "{i}Why does he leave his shop open if he spends most of the time there{/i}"
    you "{i}Thats like sooo dangerous gurl i-{/i}"
    "Piotr opens his mouth to start speaking but before he can mutter a single word you overpower him with your proclamation"
    you "I've come to announce that i am a different [name]"
    you "I am no longer [name] i am now [name] version TWO"
    you "You hear me? I am version DOS."
    you "I can even be version three but i dont even know how to say that in spanish"
    you "And to prove how much i've changed i hereby bequeath you a little treat"
    "You put on a smug grin before placing the paper bag directly onto the table, and sliding it over the countertop, careful not to scratch it"
    you "Enjoy"

    if flag("gotCakeForPiotr"):
        "Piotr carefully looks inside the oil-staned paper bag before noticing the message"
    elif flag("gotBreadForPiotr"):
        "Piotr carefully looks inside the extremely rectangular paper bag before noticing the message"
    elif flag("gotCoffeeForPiotr"):
        "Piotr smells the aroma of fresh coffee and quickly tears the bag apart, before noticing the message"
        "The message you wrote with great care and precision stayed intact due to sheer luck"

    "His eyes quickly skim the text"
    if piotrWritingPoints == 2:
        "He exhales and lowers his guard"
        "Piotr cant possibly be mad at you"
    if piotrWritingPoints == 1:
        "Piotr ignores the message and moves on"
    elif piotrWritingPoints == 0:
        "Piotr's eyes widen"
        p "what the"
        p "WHAT IS THIS"
    you "Now don't be so shy. Please indulge in this Bratgrenian delicacy"

    if flag("gotCakeForPiotr"):
        "Piotr decided that taking the cake out was too risky so he ripped the bag"
        "Which revealed a slightly-smooshed cake"
        "The cake doesn't look very presentable anymore but its still edible"
        you "Like i said, Enjoy"

    elif flag("gotBreadForPiotr"):
        "Piotr lifts the bag because he has had enough and does not want to deal with this right now"
        "When suddenly..."
        "The bag rips and the bread falls out onto the tabletop, leaving a dent"
        "you start laughing very loudly and very obnoxiously"
        you "WHY DID IT FALL OUT LIKE THAT"
        "You are the only one laughing"
        you "I haven't laughed this much in a while"
        p "Great. You ruined my table"
        you "okay okay wait"
        you "Here's the receipt. You can go back to the store and return it for store credit"
        "Piotr rolls his eyes"
        you "i'm actually really sorry this was supposed to be an actual gift but i didnt check the bread"
    elif flag("gotCoffeeForPiotr"):
        you "One is poisoned by the way"
        p "WHAT"
        p "No thank you"
        you "Just kidding"
        you "żarcik kosmonaucik"
        "piotr looks suspiciously at the coffees and exhales"
    
    you "Apology accepted?"

    if piotrFoodPoints + piotrWritingPoints > 2:
        $ flag("piotrApologyAccepted", True)
        p "Yes."
        p "Thank you"
        you "And thank {i}you{/i} for being as cool as a cucumber"
        p "Don't push it"
    elif piotrFoodPoints + piotrWritingPoints > 1:
        $ flag("piotrApologyAccepted", True)
        p "Yeah i guess"
        you "I can hear the doubt in your voice that is extremely rude"
        you "Where are your manners young man"
        p "That's exactly what i'm talking about you are NEVER serious"
        you "{i}Hmph!{/i}"
        you "{i}This isn't the end of it{/i}"
    else:
        jump ch02_piotrApologyDenied

    you "Okay okay fine"
    you "Ignore the food i just wanted to say sorry"
    you "Yes i can be rude but I'm not rude because i have tofu with you its just because I'm sassy like that"
    p "..."
    "Piotr inspects you top to bottom, his gaze landing on your eyes and piercing you"
    p "Fine"
    p "You will change"
    you "{i}???{/i}"
    you "{i}No YOU will change{/i}"
    jump ch02_piotrApologyAccepted

label ch02_piotrApologyDenied:
    p "No."
    you "Why?"
    "But Piotr doesn't even reply. He just shakes his head while staring directly at you."
    "No words come out of his angry beak, and none have to."
    "Even your apology was rude."
    "..."
    p "Get out."
    you "Fine!{i}Hmph!{/i}"
    scene expression loc_bg("cityexit") with dissolve
    you "{i}I did exactly what Rafał told me to and he got mad{/i}"
    you "{i}Wow.{/i}"
    "You head straight to Rafał. After all, you think it's all his fault"
    "Before going back to the bakery, you wipe your feet on Piotr's cute welcome mat."
    scene bg bakeryinside with dissolve
    show rafal normal with dissolve
    r "Good m- You're back!"
    you "Yes."
    r "Is there anything i can help you with?"
    you "I bought the thing you told me to apologize to Piotr and now he is mad at me."
    you "Why did you even suggest that?"
    "For a moment, Rafał lowers his eyebrows and just stares at you."
    r "What do you mean \"apologize\"?"
    r "You didn't tell me you wanted to apologize."
    you "I didn't?"
    r "No."
    "..."
    r "How bad is it?"
    you "Its not THAT bad, I guess. It's simple and very stupid."
    you "When I woke up in that forest, I immediately assumed that it was Piotr who summoned me there."
    you "So, naturally, I was angry at him and I was very rude."
    "Rafał doesn't say anything and just exhales."
    you "So what do i do?"
    r "The best apology would be to leave him alone for now."
    "..."
    you "Okay."
    you "Thank you for the advice."
    r "No problem."
    "You leave the bakery while thinking about Piotr."
    jump ch02_afterPiotrApologyOutcome


label ch02_piotrApologyAccepted:
    "There's a moment of silence that makes everything very awkward. Someone HAS to start the conversation."
    you "So what do you sell here?"
    p "A lot of things actually."
    p "Look around, if something piques your interest i will tell you all about it"
    "You stop leaning on the countertop and walk around the small store."
    "Every single shelf is covered in various bottles, trinkets, baubles, feathers, sticks and other magic-adjacent paraphernalia."
    "Despite the store's small size, there is everything a wizard would need."
    "You turn to the table behind you and pick up a stone covered in bright orange spikes, the color of a wet construction cone."
    p "Don't touch that"
    you "What is \"that\"?"
    p "What you are holding is a very big piece of ortamite. It's heavy but very brittle."
    p "You could crush it in your hands if you wanted to. Please don't do that."
    you "It looks so pretty..."
    "Careful not to break it, you grab one of the thicker spikes and inspect it closer."
    "Up close it looks like a neon sea urchin."
    you "Where do you even get all these?"
    you "Do you just dig something like this up?"
    p "No. Well yes but not everything."
    p "While yes, you can just find stuff, I craft like 2/3rds of the things I sell here."
    you "You can just make these??"
    p "No i dont \"just\" make things, it takes alot of time and alot of effort."
    you "Why would someone even want this?"
    p "Well... not many people. People often come here to buy medicine."
    you "{i}He dodged my question. Wow.{/i}"
    p "If you ever become sick come to me."
    you "I definitely will."
    p "Now, if you dont mind, I have other matters to tend to."
    you "It's totally fine. Thank you for showing me around."
    p "Goodbye."
    jump ch02_afterPiotrApologyOutcome
    
    
label ch02_afterPiotrApologyOutcome:
    scene expression loc_bg("cityexit") with dissolve
    