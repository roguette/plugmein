


# region INTERACTIONS

label ch01_h_entrance:
    scene expression loc_bg("house")
    $ flag("ch01_house_seenEntrance", True)
    "The smell of old, stale things permeates the air"
    "And that is the first thing you noticed when you walked in"
    "For a moment you just stand there, taking in the surroundings"
    "..."
    you "{i}i LOVE it{/i}"
    you "{i}I better lock the door though{/i}"
    "*click*"
    call screen s_House()

label ch01_h_bathroom:
    scene expression loc_bg("house")
    you "{i}Wait{/i}"
    you "{i}Why are there chia seeds near the toilet?{/i}"
    call screen s_House()

label ch01_h_bedroom:
    scene expression loc_bg("house")
    you "{i}The bed is so big and soft{/i}"
    you "{i}I wish i could just never get out of it{/i}"
    you "{i}Wait i actually can{/i}"
    menu:
        "Go to sleep":
            scene black with dissolve
            "You literally jump onto the bed like a hungry animal"
            "Wait.. {w=0.5} you are a hungry animal"
            jump ch02_watch_your_mouth
        "No i want to explore my house first":
            call screen s_House()

label ch01_h_kitchen:
    scene expression loc_bg("house")
    "You can already imagine yourself not using the stove and just eating chinese takeout"
    call screen s_House()

label ch01_h_livingRoom:
    scene expression loc_bg("house")
    "The living room is surprisingly empty"
    "You will have to do some furnishing because right now theres not much living to do in it"
    "Your feet shuffled in place at the sight of the empty room and you heard the sound echoing back to you"
    call screen s_House()

label ch01_h_storageRoom:
    scene expression loc_bg("house")
    "There's a sticky note on one of the shelves"
    "{i}Enjoy - Barbara{/i}"
    you "{i}Enjoy what? Theres nothing to enjoy{/i}"
    you "{i}I mean the house is nice{/i}"
    you "{i}Why would she put the note here though{/i}"
    call screen s_House()

label ch01_m_fountainFirstClick:
    scene expression loc_bg("fountain") with dissolve
    "You spy with your little eye..."
    "and its a fountain..."
    you "{i}No tourists?{/i}"
    "There aren't any coins on the bottom of the fountain"
    you "{i}Well, atleast they dont have to scoop them out{/i}"
    "You look around and there's not a single soul out"
    ".{w=0.5}.{w=0.5}."
    menu:
        "Touch the water":
            you "{i}i HAVE to touch it{/i}"
            "Either there's too little water in the fountain or the edges are way too tall for you"
            "Almost like they dont want random people touching the water"
            ".{w=0.5}.{w=0.5}."
            "!"
            you "{i}Huh{/i}"
            "You now have: {w=0.5}{b}a wet finger{/b}!"

        "Do not":
            you "Why am i even considering this"
            "and you were right to think that"
            "what if this city had more tricks up its sleeve and the water was poisonous"
            you "{i}Hell no{/i}"
    return

label ch01_m_fountainSecondClick:
    scene expression loc_bg("fountain") with dissolve
    "Your attitude towards the fountain is as cold as the water in it"
    "There's nothing to do here at this moment"
    return  

label ch01_m_cityHallRudeToBarbara:
    you "{i}Hell no i'm not going back in there{/i}"
    you "{i}She's gonna eat me alive!{/i}"
    return

label ch01_m_cityHallNormalFirstInteraction:
    you "{i}I have more questions...{/i}"
    scene bg cityhallinside with dissolve
    "Everything here is new to you because i chose this cliche way to start a visual novel"
    "That way i have more control over the lore and what can happen"
    scene bg secretary with dissolve
    show filip normal with dissolve
    if not flag("rudeToBarbara"):
        f "Oh. It's you."
        you "What?"
        f "What do u want"
        # happy meal
        menu:
            "What's her problem":
                "Filip's face contorted"
                "It looks like he's having a nightmare"
                f "Girl i-"
                f "you literally le insulted her hair"
                f "She spends so much money to have maybelline hair and you just..."
                "He waves his hands around due to the lack of words"
                f "That was rude"
                menu:
                    "That was constructive criticism":
                        "It's been a long day and Filip is very tired and you are NOT helping."
                        "He covers his face and pretends to sob dramatically"
                        f "When will you finally understand?"
                        f "She is the president you HAVE to be on good terms with her"
                        f "She has a ton of power over you and you chose to fight her"
                        f "Play stupid games win stupid prizes"

                    "Hmph! I will apologize if you so wish.":
                        f "Good"
                        f "Wait no hold on"
                        f "What are you going to say"
                        f "I dont want you to say something stupid and get into more trouble"
                        "You put your hand on your chin and pretend to think really hard"
                        menu:
                            "I was on drugs and thought you were bald":
                                pass
                            "I had something in my eye":
                                pass
                            "I lied because I'm a pick me":
                                pass
                            "I thought her weave reminded me of my dead hamster":
                                pass
                        "Filip starts giggling uncontrollably"
                        "You arent sure if its your answers which made him laugh or your stupidity"
                        f "Yeah no that is not gonna work. You will have to come up with something better"
                        you "Hmm.."
                        you "Ok i will do something tomorrow"
                        you "I'm too tired for this today"
    else:
        f "Oh hey"
        you "I have a question..."
        menu:
            "Where is my house":
                "Filip rolls his eyes dramatically"
                f "Did you even look at the keys"
                f "Theres an address attached"
                "You take the keys and put them on the table and inspect them closely"
                "Indeed, there is a small keychain with a street name written on it"
                you "But isnt this like dangerous?"
                f "How"
                you "If i lose my keys the person who finds them will be able to unlock my house"
                f "Then rip the tag off and write your name"
                f "If someone finds the keys they will give them to us"
                you "And what if they dont"
                "Filip has clearly had enough and sighs"
                f "Then you will come to me and we will come up with something"
            "Where is everyone":
                f "Its almost midnight and its cold as hell outside"
                f "If you werent \"born\" today you would be asleep right now"
                "You audibly breathe out"
                you "{i}I guess he's right{/i}"
                you "{i}I'd rather be in a warm bed than here{/i}"
                you "Oh."
                f "And yes, we have alot of residents"
                f "It's just that its, you know, late"
                f "Come to the square tomorrow and you will see"
            "What's in the forest":
                f "Ebola"
                "your eyes widen"
                f "Jk its not ebola its bts stans"
                you "Oh! That's cute"
                you "What do i need to do if i see one"
                f "You dont look like you can end bts so you can sing dynamite and pretend you are an army"
                you "I'd rather die"
                you "And piotr was trying to clean the forest?"
                f "Yes"
                f "Now you know why you shouldn't go to the forest"
                you "{i}We will see about that{/i}"
            "Are there any tourist traps?":
                f "No there aren't any"
                f "Because we don't have any tourists"
                you "How"
                f "It's just us here in Bratgren"
                you "So theres literally no one else?"
                f "As far as we are aware, yes"
                f "The forest is way too dangerous so we didnt explore it much"
                you "That's a shame"
                f "Why? Are you already trying to escape?"
                you "I came from a rich family and my bedroom was the size of the square outside soo"
                you "So this feels like prison"
                "Filip giggles"
                f "Yeah right"
                f "If you ever accidentally slip and tumble all the way into the forest and meet the monsters in it"
                f "Sing a bts song"
        you "Okay..."
        you "Well i dont want to take up more of your PRECIOUS time"
        you "Thank you and goodnight"
        f "Bye"
    return

label ch01_m_enteringChurch:
    "Walking up to the church you feel a sudden breeze of air graze your back"
    scene bg churchnight with dissolve
    "The building in front of you, which you can only assume is a church, looks very old and a bit dilapidated"
    jump ch01_firstNightTownWalkPartB

# endregion

label ch01_cold_boot:
    $ telemetry_flag("ch01_cold_boot")
    "{cps=1}...{/cps}"
    stop sound fadeout 0.5
    "{cps=25}Congratulations!{w=0.5} You just got hit by a bus.{w=0.5} (MKS #23 to Przybówka).{/cps}"
    "{cps=20}Your screams were only heard by the driver.{/cps}"
    "{cps=15}Who already fled the scene.{/cps}"
    "{cps=2}...{/cps}"
    "Somehow, you are still alive <3"
    "Now that everything has cut to black, you can only feel the pain in your head"
    "You can't even check if you still have it because you are THAT weak"
    "I mean you DID get hit by a bus..."
    call chapterTransition("Akt 1", "So what now?")
    play music "forest.mp3" fadein 2.0
    m "What the..."
    m "Excuse me? Are you alive?"
    "Someone puts their arm onto your shoulder and tries to wake you up, all while his claws are scratching your skin"
    "Wait..."
    "Claws..??"

    scene bg forestnight with vpunch

    you "AAAAA!!!!" 
    you "DON'T TOUCH ME!!!"
    you "Stranger Danger!!!"
    show piotr normal at center with dissolve
    "You gather all your strength to open your eyes to see who the hell woke you up."
    "There's a tall bird guy in front of you, looking at you all weird."
    "Everything in you wants to scoot away from him, but you cant because of the tree behind you."
    "So you just sit there and look at him."
    you "{i}A bird???{/i}"
    "You need a moment to let all this sink in. About ten seconds.\n{w=1.0}1 {w=1.0}2 {w=1.0}3 {w=1.0}4 {w=1.0}5 {w=1.0}6 {w=1.0}7 {w=1.0}8 {w=1.0}9 {w=1.0}10{nw}"
    "Finally calmed down, you cant help but notice his very magical-looking attire."
    "You almost lean in to look closer, but then you snap back to reality."
    "When a bird hatches from its egg, the first thing it sees becomes it's mother. Allegedly."
    "Something similar happens with you, except you think the opposite."
    you "{i}What did he do to me?{/i}"
    you "{i}Did he summoned me???{/i}"
    "You try to do hunter eyes and stare at this mysterious creature."
    you "Who the hell are you?"
    you "And why did you put me here?"
    you "Waking up in the forest and all that?"
    m "Do not yell you are in a forest!!!"
    you "Oh no no no... You are going to answer all of my questions first."
    you "You have 10 seconds until i let you know i had eggs for breakfast."
    p "I won't ask you again."
    p "My name is Piotr and I am a wizard."
    you "Wizard? Like a birthday party wizard?"
    p "???"
    you "Like do you do silly tricks like pulling rabbits out of your huge top hat?"
    with vpnuch
    p "If you don't shut up wolves will hear us and eat us both."
    "Piotr's serious tone finally gets to you."
    you "Okay okay calm down."
    you "You should have started with that."
    "You instinctively try to push yourself away from him one more time, still impossible because of the tree behind you."
    "Maybe you {i}should{/i} be scared of him"
    p "Thank you."
    p "Now get off the dirt you look like a mess."
    "Piotr gives you a hand, and you are unsure how to grab it and not touch his sharp claws"
    p "What?"
    p "I don't bite."
    # https://en.wikipedia.org/wiki/Temperate_broadleaf_and_mixed_forests
    "You reluctantly take his hand and get off the floor, taking time to clean yourself."
    "When you get up a gentle breeze sweeps through the forest, making you shiver a little."
    "Piotr examines you carefully while you are looking for an escape route."
    "First, your gaze turns to the dense forest, covered in even denser fog."
    "Then, you notice the tree crowns covering the night sky."
    "And finally, you notice the forest floor covered in browned birch leaves and pine needles from the pine tree behind you."
    "Amongst those leaves there are countless shrubs, stones, bugs and even more random plants."
    "There's even a small daffodil fighting for its life. {w=0.5}The daffodil is losing."
    "It's leaves had long turned gray and wilted away, leaving just the pretty yellow flower intact."
    "Then, your gaze wanders to Piotr, and more specifically his stuff."
    "His backpack was on the ground, tucked away behind a bush in front of a circle made out of stones."
    you "{i}What is that?{/i}"
    you "{i}Oh my god what if he DID summon me?{/i}"
    you "{i}UGH this is so bad...{/i}"
    "Before running away deep into the unknown, you decide to first test your theory."
    p "What are you looking at?"
    you "Those black stones you have there."
    you "What are those?"
    p "To?"
    "He points with one of his long,{w=.5} black,{w=.5} scary,{w=.5} and even crooked{w=.5} claws at a circle made of black stone."
    you "Yes."
    "Piotr goes to the ritual site to pick up two stones."
    p "This, is onyx. I use it for rituals."
    you "Oh."
    you "So you did summon me?"
    p "What???"
    you "That's actually really cool."
    you "What were you doing before you isekaied me here?"
    p "I did not summon you."
    you "Then what {i}did{/i} you do Mr. Piotr?"
    p "Nothing, {i}yet{/i}."
    you "What do you mean {i}yet{/i}??"
    p "I was cleaning the forest and this had nothing to do with you"
    p "I mean i was going to and then i saw you."
    you "{i}Is he a janitor or something??{/i}"
    you "What do you mean clean?? I don't see your broom."
    "Piotr puts his hand over his forehead, already sick of your impertinence."
    p "I don't sweep the forest. I do spiritual cleanses, not washing trees with a mop."
    you "{i}Whatever that means.{/i}"
    you "And you havent started yet?"
    p "No."
    "You point at the ritual, circling your finger vaguely in its direction."
    you "What if I'm evil and your little ritual kills me?"
    p "You are not evil you're just being rude on purpose."
    p "Im sure you couldnt even hurt a fly."
    you "{i}True. they are way too fast..{/i}"
    you "So when are you gonna answer my questions?"
    "Piotr looks at you with pure confusion."
    p "I have answered all your questions up until this point. How did you manage to answer questions without me noticing?" 
    you "{i}Why is he so rude to me?{/i}"
    you "{i}Fine. This isn't over though.{/i}"
    you "{i}When i find some sort of civilization i will just tell everyone he kept me in his basement{/i}"
    you "{i}Does he have a basement though? What if he doesnt?{/i}"
    you "Do you have a basement?"
    p "What? Yes. Why?{nw}"
    you "{i}Bingo.{/i}"
    jump ch01_piotrIntroductionMenu

label ch01_piotrIntroductionMenu:
    menu:
        "Who are you?" if not flag("askedWhoPiotrWas"):
            $ flag("askedWhoPiotrWas", True)
            you "I have to know who you really are."
            you "Are you my dad or something?"
            p "My name is Piotr and I am a wizard."
            you "Hi my name is Piotr I am a wizard."
            "You do a very robotic dance while repeating the same phrase over and over again."
            you "Is that your whole personality?"
            p "No?"
            you "Then tell me all about that other side."
            p "Oh you actually care about that? Thats so kind of you!!"
            you "{i}Oh my god.{/i}"
            p "Additionally, I must protect nature from evil, crickets, and tooth decay."
            p "And in the city, I treat residents and help them in all sorts of situations related to their poor physical {b}AND MENTAL{/b} health."
            you "Thats so cute!"
            you "I almost feel bad for being rude to you. You are a doctor!"
            p "Yeah I would have apologized by now."
            you "Hold your horses I said {i}almost{/i}."
            p "So what about you?"
            you "What about me?"
            p "Who are you?"
            you "Oh!"
            "Name one thing. Your city. Your school. Your parents."
            "Nothing."
            "..."
            "What's weird is that you know what you like and what you hate."
            "But you cannot remember why or how that is"
            "Its almost as if you just survived amnesia and became a new person"
            you "I survived cancer but got short and long term memory loss!"
            "Piotr shakes his head in disbelief."
            p "Thats not how it works."
            
            jump ch01_piotrIntroductionMenu
        "I know you kidnapped me!!!" if not flag("accusedPiotrOfKidnapping"):
            $ flag("accusedPiotrOfKidnapping", True)
            $ friendship["Piotr"] -= 1
            you "I can see right through your lies!"
            you "You think I'm not the sharpest tool in the shed!"
            you "But you are wrong!"
            p "What?"
            you "You are trying to play 5d chess with me!"
            p "And how exactly am i doing that?"
            you "I can smell it in the air it has that kidnapping smell!"
            "With every word you say his expression goes more and more grim."
            p "Is this ragebait?"
            you "No."
            p "I did not kidnap anyone."
            you "Thats exactly what a kidnapper would say!"
            p "Ok then prove that I kidnapped you."
            you "Prove that you did not!"
            you "HA!"
            p "Okay, lets go your way."
            p "Even if I did kidnap you and even if I erased your memory,"
            p "You know nothing and you still need my help."
            p "What are you gonna do alone in the forest?"
            you "Larp worms and live underground?"
            "You aren't evil and you aren't stupid either."
            "It's just ragebait. Prankless harm."
            p "Not with that waist."
            you "EXCUSE ME?"
            "You give him a sassy hmph and after little thinking you realize you actually do need his help."
            you "Fine. I guess you are right this once."
            p "Say such nonsense one more time and see what happens."
            jump ch01_piotrIntroductionMenu
        "Where am I?" if not flag("askedWhereIAmStart"):
            $ flag("askedWhereIAmStart", True)
            p "In a forest near Bratgren."
            p "Bratgren is like the city we all live in."
            you "That's so cool! I thought you live up there in the trees."
            "Piotr glares at you menacingly."
            you "And where is this Bratgren?"
            if flag("accusedPiotrOfKidnapping"):
                you "Or did you lie about that too?"
            p "Right behind you actually."
            "Theres a huge wall behind you and you can only assume it guards a city."
            "You try to hide the embarrassment on your face because up until this point you haven't thought of turning around."
            you "How convenient. Are you sure you didnt move it there with magic just to embarrass me?"
            p "Do you ever shut up?"
            jump ch01_piotrIntroductionMenu
        "(I have no more questions)" if any([flag("askedWhereIAmStart"), flag("askedWhoPiotrWas"), flag("accusedPiotrOfKidnapping")]):
            jump ch01_afterPiotrIntroductionMenu

label ch01_afterPiotrIntroductionMenu:
    "You look around the forest one more time, hoping for a change. Nothing grabs your attention - even the huge wall behind you."
    "The wall was really tall, but also really boring."
    p "What?"
    p "Why are you so silent all of a sudden?"
    p "Cat got your tongue?"
    "Piotr is very proud of himself."
    you "What would you do if you woke up in a random forest?"
    you "There's alot to take in."
    you "I dont know anyone, or where I am, or who I am."
    "You look down at your huge paws, which five minutes ago were ordinary human hands, and you should be bamboozled,{w=.5} but you're not."
    p "Come with me, I'll take you to Ms. Barbara. She'll know what to do with you."
    you "Should I be afraid???" 
    p "Yeah..{w=.5} No, just be nice to her and she'll tell you everything."
    p "It would be best if you got a j*b and a home right away, but that can't be predicted."
    you "..."
    you "{i}{b}A J*B??? I DON'T WANT A J*B{/b}{/i}"
    "Piotr seems happy working as a forest janitor. Impossible."
    you "So you are not gonna do the ritual?"
    p "You are more important right now."
    if random.randint(1,100) < 7:
        you "{i}Is he flirting with me right now??{/i}"
        you "I HAVE A GIRLFRIEND!"
        p "No."
        you "{i}Damn it.{/i}"
    else:
        p "You will understand why later."
        p "I can't just leave you here."
        you "Since when are you so kind to me?"
        p "Just because i am nice like that."
        p "Also I would go to jail if someone found out that I didnt help you."
        "You giggle at his joke but deep down you are wondering if Piotr would leave you all alone in this forest, had that law not existed."
        

    "The road from the forest to the city isn't long, although sometimes it can surprise you with some {i}wildlife.{/i}"
    "Together with Piotr, you cross the bridge and make your way toward the city hall. Despite the late hour, the temperature isn't unpleasant. It's actually pretty nice."

    scene bg entrancenight with fade

    "Together, you approach the enormous wooden gate, behind which lies a large{w=.6}, sprawling{w=.6}, fragrant{w=.6}, yet somehow slightly stinky city."
    you "{i}Isn't that bridge a little too old?{/i}"
    you "{i}It could collapse at any moment.{/i}"
    you "{i}I already don't like this place. The people here rely on outdated technology that should've been replaced ages ago.{/i}"
    you "{i}Why do the need such tall walls? Overreaction final boss{/i}"

    show piotr normal with dissolv

    you "Where even are we?"
    p "I already told you! We're about to enter the city of Bratgren."
    you "I mean, I know that, but..."
    you "{i}He doesn't undestand anything. Who am I even talking to?{/i}"
    you "{i}If anyone can answer my questions, it'll definitely be that Barbara.{/i}"
    you "Nevermind..."

    play sound "sfx_footsteps_alot.mp3"
    scene bg citysquarenight with dissolve
    play music "town_night.mp3" fadein 0.5

    "Piotr leads you through the gates of Bratgren, revealing a very picturesque city."
    you "Why is there almost nobody on the streets?"
    p "Because it's cold?"
    you "I'm not cold."
    p "I don't know how you're not cold. I'm about to freeze out here."
    you "Then let's get to  Barbara faster."
    "There is almost nobody on the streets{w}, apart from {i}the two of you{/i}."
    "You notice that the amount of buildings is astronomical. Eventually, you reach the town square, where, despite the late hour, you can still feel a pleasant{w=.6}, warm{w=.6}, welcoming{w=.6}, and an almost friendly atmosphere."
    "You could almost call your little walk romantic{w=1.0}, if it weren't for the fact that Piotr is probably the reason you're here in the first place."
    you "{i}Not a living soul on the streets... It can't be {i}that{/i} late. I hope Barbara's office is still open.{/i}"
    "You approach city hall. You know you've reached your destination thanks to the massive{w=.6}, sprawling{w=.6}, enormous{w=.6}, and simultaneously tiny coat of arms."
    "The building has this...{w=0.5} government aura to it."

    scene bg cityhallinside with dissolve

    "Piotr enters the reception office first, only to immediately lead you back outside."

    show piotr normal at center

    p "Actually, don't come in yet. I still need to talk to Filip."
    you "About what?"
    p "Speech is silver, silence is golden."
    "You're stunned by Piotr's arrogance. You're certain he's about to talk shit about you."
    p "Sit here and behave. I'll be right back."
    you "Okay."
    "{i}What a good boy you are.{nw}{/i}"

    hide piotr

    "You sit down on a nearby chair. It bends slightly beneath your enormous gyatt, but somehow holds together. You completely ignore this, though. Your mind is somewhere else."
    "All of this is so overwhelming. You're thinking about how you got here, who Piotr is, and what you're supposed to do now."
    "Feeling pine needles prick your back, you relax and lean against the wall."
    "They've been stuck to your shirt ever since you were lying in the forest."
    "You feel embarrassed. You walked through the entire city looking like a mess."
    you "{i}I lost so much aura.{/i}"
    you "{i}But nobody was outside. Nobody saw me.{/i}"
    you "{i}Unless someone was watching through a window..??{/i}"
    "You brush off your shirt and return to the most productive activity imaginable: sitting around, completely ignoring the fact that someone is going to have to clean up all those pine needles after you."
    "After a while, Piotr comes back and calls you into the reception office..."

    scene bg secretary with dissolve
    show piotr normal at center with dissolve
    pause 0.5
    show piotr normal at leftish with move 
    show filip normal at rightish with dissolve

    f "Hi! What's your name?"
    "You are startled by the ferret's energy, now that you got used to the lack of it near Piotr."
    you "Me..?"
    p "He literally asked {i}you{/i}."
    menu:
        "Provoke Piotr":
            $ flag("wasRudeToPiotr", True)
            $ friendship["Piotr"] -= 1
            you "You shat yourself when you saw me, Mr. Piotr, so {i}SYBAU!{/i}"
            p "That's not true. Don't tarnish my reputation."
            you "{i}Clock it.{/i}"
            p "..."
            jump ch01_afterPiotrRagebaitMenu            
        "Stay silent":
            you "{i}He is NOT tuff.{/i}" 
            jump ch01_afterPiotrRagebaitMenu

label ch01_afterPiotrRagebaitMenu:
    you "I... am [name]."
    f "Holy guacamole! What a peculiar name."
    you "Thank you."
    f "So Piotr, tell me, what were you doing when you found [name]?"
    p "I was cleansing the forest like you told me to, and he showed up next to me and ruined my ritual. Now I have to start all over again."
    with vpunch
    you "HOW IS THAT MY FAULT?"
    you "This is the third time I'm asking and I still don't know."
    f "Exactly, I'd also like to hear how any of this is your fault."
    f "I feel like there are more important things right now."
    f "You can do your rituals tomorrow if you have to. [name] could have died in that forest!"
    you "Exactly!"
    f "Come here."
    "You walk a little closer to Filip. He stands up and offers you his hand."
    "You smile like you're in a real estate commercial."
    "You don't know if you can trust him, but his vibes are definitely better than Piotr's."
    you "THAT is how you greet people, Mr. Piotr."
    f "Hi. My name is Filip, and welcome to our small{w=.6}, beautiful{w=.6}, lovely{w=.6}, and at the same time cozy city of Bratgren. You probably have a huge amount of questions?"
    you "Yes!"
    f "Do you already know anything about this city?"
    you "No!"
    "For some reason, Filip is delighted by this information."
    "You tilt your head and lower your eyebrows to signal your confusion, which gets ignored"
    f "Perfect. I'll take you to  Barbara now. She'll answer all your questions."
    f "She likes explaining this stuff, you just have to ask the {i}right{/i} questions."
    you "{i}TFYM THE RIGHT QUESTIONS?!{/i}"
    f "Just don't stress about it. Be nice to her and she'll be nice to you."
    f "Oh, and one more thing - you're not the only one."
    f "All of us appeared outside this city, just like you."
    you "Everyone??"
    f "Everyone."
    you "Even Piotr?"
    f "Even Piotr."
    you "Piotr didn't tell me that..."
    f "Then why are you gatekeeping, Piotr?"
    p "This is the first time I've ever found someone in the forest...."
    f "Fair enough, but please tell the next person things like that!"
    f "[name] was probably stressed because of you."
    you "Exactly!!!"
    f "Okay, back to Barbara."
    f "First I need to ask if she'll see you."
    f "Last time I caught her doing skip B on the desk..., so it wasn't pleasant and it didn't smell good either..."
    you "I only have one question..."
    f "Yes?"
    you "Why are you still awake? Isn't it nighttime?"
    f "We had a problem with the city's water today and spent the whole day dealing with it."
    f "There's always something going on in this city."
    "Filip walks up to the door and politely knocks."
    play sound "door_knock.mp3"
    f "Good evening, I have a new person here. Can I bring him in?"
    m "Sure!"
    play sound "audio/sfx_door_open.mp3"
    "Filip opens the door and shoves you into the office, quickly closing it behind you."
    f "Go, go, go..."

    scene bg office
    stop music

    "..."
    "Barbara is sitting in front of you. Her aura is so intense that one look from her could cool down the whole room."
    show kurowska normal with dissolve
    you "Good evening!"
    k "Welcome to the town of Bratgren! What is your name?"
    you "My name is [name]. Nice to meet you."
    k "Okaaay.. My name is Barbara, I'm the president of this city. I've been in charge here for 7 years. What brings you here?"
    you "I just woke up in the forest. I don't know who I am, I don't know where I am, I only know my name."
    you "Piotr found me and brought me to you."
    you "And that's all I know."
    k "So, just like everyone else..."
    "Barbara writes something in her notebook."
    k "What was your name again???"
    you "[name]"
    k "What a weird name. Spell it for me."

    $ nameSpelled = '-'.join([f"{letter}{{w=0.5}}" for letter in name])
    you "[nameSpelled]"
    k "Okay, got it."


    menu:
        "Ask what she means by everyone.":
            you "What do you mean by \"just like everyone else\"?"
            k "Everyone who lives here arrived in our city the same way."
            you "And that is..??"
            k "No one knows where we come from."
            k "And, just like you, everyone doesn't know anything you just appear."
            k "Poof and you are in a forest."
        "Stay silent":
            you "{i}I don't think I understand what she means... but I'm scared to ask her.{/i}"
            you "{i}What if she's aggressive too.{/i}"
    you "I have a query!!"
    k "Yes?"
    you "What's in the forest outside the city, and why is this place in the middle of nowhere?"
    k "Ha ha!"
    k "If you go out into the forest, wolves will eat you or you'll die from some niche disease."
    you "..."
    "You are in complete shock."
    k "That's exactly why Piotr performs those cleansing rituals."
    you "Yeah, Piotr told me how he does it with that onyx thing."
    k "Exactly."
    you "That's actually really cool."
    "The concept of magic really intrigues you."
    "What if you too can do these rituals and become a powerful magician"
    you "Do you have any questions for me?"
    k "Hmm...."
    k "Do you remember anything at all?"
    "But you remember nothing. Your memory is empty, like a brand new Samsung SSD T1 2TB Titan Gray USB-C drive."
    "Your survivor instincts kick in and you think about this question"
    "No, you dont remember most things"
    "Yes, you remember some things, like most of your general knowledge"
    you "{i}For now, it's probably better to pretend I don't remember anything.{/i}"
    you "{i}What if they wipe my memory again!{/i}"
    you "I don't remember anything."
    k "Everyone has some kind of memory loss."
    k "Me too."
    you "So basically, we all have Alzheimer's."
    k "Let's put it that way."
    jump ch01_kurowskaDialogMenu

label ch01_kurowskaDialogMenu:
    if flag("askedAboutHousing") and flag("askedAboutCity")  and flag("askedAboutWork"):
        jump ch01_gettingHouseKeysGood

    k "Do you have any questions?"
    menu:
        "Ask about the city" if not flag("askedAboutCity"):
            $ flag("askedAboutCity", True)
            you "So what is this Bratgren?"
            k "We are a small community built near lake Świtezianka."
            you "And what do you do?"
            k "We do everything a city does? I dont understand the question."
            you "No no, i understand."
            you "Piotr told me you have to protect the city from some sort of monsters."
            k "Yes.. they are very very dangerous."
            k "Piotr is like a hero in here. Protecting the city from them is risky."
            you "I see. So i'm guessing you can't really go outside?"
            k "No."
            you "Seems really boring."
            k "What?"
            you "I mean everything you do has to be in this city."
            k "Would you rather go back to the forest?"
            you "{i}Damn it shes right.{/i}"
            you "No."
            k "Exactly."
            jump ch01_kurowskaDialogMenu

        "Ask about housing." if not flag("askedAboutHousing"):
            $ flag("askedAboutHousing", True)
            you "Where's the nearest hotel or something? I don't have a house or an apartment, where am I supposed to sleep?"
            k "About that... I just need to find the keys to your house."
            you "A house?"
            you "For what?"
            k "For free."
            you "And how does that work?"
            k "Free houses are only for people who work."
            k "Let's say I'm investing in you this way."
            you "Obviously I'll work!!!"
            k "You better be telling the truth."
            you "{i}A free house? I wouldn't even dream of this.{/i}"
            jump ch01_kurowskaDialogMenu

        "Ask about work." if not flag("askedAboutWork"):
            $ flag("askedAboutWork", True)
            you "What about work?"
            you "I know Filip works here, with you. What does everyone else do?"
            you "Everyone else as in regular people."
            k "Around here, work basically means doing anything that benefits the city or its people."
            k "There are farmers, bakers, couriers..."
            k "And then there are people who live in the city and benefit from our protection from evil while doing absolutely nothing."
            you "Don't worry. I won't be that kind of person."
            you "How do those people not get bored?"
            k "I don't know either."
            k "I genuinely can't imagine living a life without doing anything at all..."
            k "Okay, back to your work."
            "Barbara looks through the papers on the desk, then inside the desk, then behind herself."
            k "Nooo I think I lost it..."
            k "Well, in that case I have nothing for you. I'll be able to tell you more tomorrow, so you're free today."
            k "Just come see me tomorrow."
            you "Sure!!! XOXO"
            jump ch01_kurowskaDialogMenu

        "Comment on her appearance." if not flag("commentedOnBarbarasAppearance"):
            $ flag("commentedOnBarbarasAppearance", True)
            menu:
                "Comment on her outfit":
                    you "Can anyone buy clothes like that?"
                    you "Because you look stunning!"
                    k "Ha ha, thank you. Of course you can, you just need to go see our tailor."
                    k "She's in the market, next to the bakery."
                    $ friendship["Barbara"] += 1
                    jump ch01_kurowskaDialogMenu
                "Comment on her hairstyle":
                    $ telemetry_flag("rudeToBarbara")
                    you "What series of events gave birth to your hairstyle?"
                    k "Do you have a problem with my shiny Maybelline hair?"
                    you "Calling that hair is pretty generous..."
                    k "Are you insulting me??"
                    you "I think I'm giving you something called constructive criticism!"
                    k "You and your constructive criticism are about to get KICKED OUT."
                    $ flag("rudeToBarbara", True)
                    k "This interview is over. Here are the keys to your house. Now leave before I throw you out!"
                    scene bg secretary with vpunch
                    play sound "audio/sfx_door_slam.mp3"
                    you "{i}Glad she didn't overreact.{/i}"
                    you "{i}Atleast I got a free house..?{/i}"
                    jump ch01_gettingHouseKeysUniversal

label ch01_gettingHouseKeysGood:
    k "If you don't have any more questions, here are the keys to your new house.{w} (Kasia Dowbor renovated it)"
    you "{i}That place must be luxurious.{/i}"
    you "Thank you! Thank you! Thank you!"
    jump ch01_gettingHouseKeysUniversal

label ch01_gettingHouseKeysUniversal:
    scene bg cityhallinside with dissolve
    play music "town_night.mp3"
    show piotr normal 
    "You leave Barbara's office."
    p "Everything okay?! You were in there for a while..."
    you "You are very delulu, I was gone for 5 minutes."
    p "How did it go?"
    you "Look what I got!! (#flex)"
    "As you say this, you show him the keys to your new house."
    "You hold the keys up to Piotr's face and notice an address on the keychain."
    "{i}Colacoca st. 4{/i}"
    "Piotr is jealous because he had to work to get his house."
    p "Wow ok."
    p "In that case, I have to go finish the ritual from earlier that you interrupted. GOODBYE!"
    hide piotr with dissolve
    you "{i}He's just jealous. He will forget about it tomorrow.{/i}"
    if flag("wasRudeToPiotr"):
        you "{i}I think I went a little too far in that office.{/i}"
    you "{i}I mean it's not that deep. Whatever, I don't care.{/i}"
    "Before leaving the city hall, you look at the clock and see that it's 23:44."
    $ time.setTime(23,44)
    show screen s_Clock()
    scene bg citysquarenight with dissolve
    play sound "sfx_footsteps_a.mp3"
    "You leave the city hall and start walking."
    "You feel a shiver run down your spine."
    "But{w=0.6} you can't tell exactly what caused it - the fact that there isn't a living soul around{w=0.6}, or the fact that it's just cold."
    "You wrap your arms around yourself, trying to warm up somehow."
    you "{i}What season even is it?{/i}"
    you "{i}Do they even have winters here?{/i}"
    you "{i}Unless it's spring...{/i}"
    you "{i}I don't want winter.{/i}"
    "You look up for an answer, but all you see is a dark, empty, almost boring sky."
    "You have no idea what to do now."
    window hide
    call screen s_walkable_Square()

label ch01_firstNightTownWalk:
    scene bg lanastreetnight with dissolve
    jump ch01_firstNightTownWalkPartB

# ch01_m_enteringChurch goes here and i dont want lanastreet in the bg
label ch01_firstNightTownWalkPartB:
    $ telemetry_flag("choseWiktoriaP")
    "Just as you decide to look away from this beautiful architectural monument, you see...{w=.1} someone."
    you "{i}FINALLY!{/i}"
    you "{i}This is the first person I've seen on this street.{/i}"
    "You aren't sure whether you want to approach this person and talk or avoid them instead."
    you "{i}I hope this person doesn't beat me up.{/i}"
    "Eventually, the mysterious person waves at you and gestures for you to come closer."
    you "{i}What do they want???{/i}"
    "You approach the mysterious figure in front of the church while taking every possible safety precaution."
    show wp normal with dissolve
    $ flag("metWiktoriaP", True)
    you "Hi?"
    m "Oops."
    m "I thought you were someone else."
    you "Really?"
    m "Yeah this is very awkward... Sorry."
    you "Omg there are more people outside?"
    m "What? Yes."
    m "Are you new here or something?"
    you "Yes I was born today."
    "She giggles just a tiny bit."
    wp "Well my name is Victoria."
    wp "And you are..??"
    you "[name]"
    "You smile like you're in a real estate ad."

    $ newName = name.strip().split(" ")[0].lower()#  "Dupa 3.0" -> "dupa"

    wp "I was literally about to say you look like a [newName]."
    wp "You have a cool name."
    wp "[name] [name] [name]"
    "It's your turn to giggle."
    "You lean onto the random church's fence and try to be nonchalant."
    you "So where were you going on this fine evening, young lady?"
    wp "I had too much coffee and I couldnt fall asleep."
    you "And you chose to go outside? What if this place is dangerou?s"
    wp "Like you would know anything about that."
    wp "Actually yes, it is dangerous."
    you "How?"
    wp "Vasili might be outside."
    you "Whomstve is Vasili>"
    wp "Oh my god you don't know?"
    you "No."
    wp "That is a BLESSING you should keep it that way."
    you "What? Why? Is he dangerous?"
    wp "No he is worse."
    wp "He is SO annoying..."
    $ flag("knowsAboutVasili", True)
    wp "See that bakery behind you?"
    wp "When Rafał was closing he had a few buns that were going to go stale"
    wp "So instead of being wasteful he gave them away to people"
    wp "And his high calorie verity shaped ass said that..."
    "Victoria points her finger up to the sky and starts speaking in a forced, very nerdy voice"
    wp "{i}Everything sudden hurts me.{/i}"
    wp "{i}Do you know the discomfort I feel?{/i}"
    wp "{i}You're just making fun of me.{/i}"
    wp "{i}Hmph!{/i}"
    you "Okay that's enough."
    wp "And thats not all!"
    you "And I heard enough."
    you "Now i'm scared of him too."
    you "Can you tell me where does he live? So that I can avoid him of course."
    wp "I think he lives by the lake..??"
    you "Okay..."
    "You twitch at the thought of coming anywhere near him"
    wp "As you can tell I'm his #1 fan."
    you "And my mother is lady gaga."
    "Wiktoria laughs at your sassiness."
    wp "Lets walk together."
    wp "You dont want to be alone when {i}he{/i} starts talking to you."
    "You walk to the square talking about how you both hate it when you are trying to open yoghurt and the foil splits in two."
    scene expression loc_bg("square")
    show wp normal at center with dissolve
    wp "So tell me, how were the first few hours in Bratgren"
    you "So I woke up in the forest..."
    wp "This is getting interesting."
    you "Piotr was in front of me so I immediately thought its all his fault."
    you "So I was kinda rude to him, you know?"
    you "He led me to Barbara and she gave me a house."
    if flag("rudeToBarbara"):
        you "I was rude to her too."
    wp "What happened to your attitude."
    wp "You weren't rude to me."
    you "Stop it, I calmed down now."
    wp "Okay but you have to apologize for being rude."
    you "We will see about that!"
    "You both giggle at the thought of an apology."
    wp "I appeared in the forest just like you."
    wp "But I didnt have Piotr to help me,"
    wp "I had to follow my instincts."
    you "And you have been here for how many years?"
    wp "Like 8"
    you "Ohh so like you are a local at this point."
    you "You must know alot about Bratgren."
    wp "Yeah i guess you could say so."
    you "Could you tell me about this city?"
    wp "Is there anything specific you would like to know?"
    menu:
        you "Well.."
        "Where am i?":
            pass
    you "Like i know i am IN Bratgren but where is this Bratgren"
    you "Are there other cities?"
    wp "Well no not really."
    wp "I mean... I've heard that there are more cities out there."
    wp "But we don't go outside much."
    you "Oh.."
    wp "But it's not like that matters."
    wp "There are GMO wolves in that forest and they will rip you apart if you dare to try to explore."
    you "That's very rude of them."
    you "And no one {i}wanted{/i} to explore?"
    wp "Actually I think we can explore the forest"
    wp "Piotr, the guy you were extremely rude to, is in charge of all the onyx"
    wp "So he is very protective of it"
    wp "And to explore you need that onyx for protection."
    wp "Piotr is not going to give you any just to wander in the forest."
    wp "Especially after you were rude to him."
    "You laugh but deep inside you know she is right."
    "There's a moment of silence, which kills the mood."
    you "Yeah I have to apologize to him..."
    "..."
    you "So what do you even do here?"
    you "I'll wake up tomorrow and have nothing to do."
    you "Wait no Barbara told me to get a job"
    wp "You can do anything you just need to get money."
    wp "The goal is to get everyone to chip in a little and improve the city."
    wp "What if more people like you spawn and there are no houses available?"
    wp "Would you rather live with a total stranger or have your own house?"
    you "Seems fair."
    "Time didn't suddenly stop, and you still need sleep."
    "You start yawning and immediately think that its past midnight now."
    you "Well, I better get goi ,ng."
    you "It was nice talking to you."
    wp "Goodnight [name]."
    wp "Goodnight."
    hide wp normal with dissolve
    "You start walking home. Your head feels heavy from all the information you've received today."
    "After such a long day, you can't think about anything except sleep."
    call screen s_House()

label ch01_lakeVisit:
    $ telemetry_flag("choseVasili")
    play music "forest.mp3" fadein 1.0
    scene bg lakenighta with dissolve
    "You head downhill, turn a few times, and arrive at a beautiful meadow."
    "It's enormous, filled with flowers of all kinds and colors. The sight almost makes you forget everything that happened today."
    "Unfortunately, a stronger gust of wind snaps you out of it and leaves you alone with the day's events flooding back into your mind."
    "There's also some weird forest nearby, but you have no intention of going there."
    "You stepped off the road that led toward that forest, and now your only light is the glow of the moon{w=.3} - or, well, whatever is shining in the sky."
    "In theory, your walk to the lake should be peaceful. The rustling grass you push through should be the only sound."
    "Unfortunately, fate had other plans."
    scene bg lakenightb with dissolve
    "On the shore of the lake, you see the silhouette of a person{w=.6}, uhh... more like a furry."
    "Whoever it is, they're trying to fish and being {b}extremely{/b} loud."
    you "{i}For crying out loud! Does someone seriously have to be here???{/i}"
    you "{i}I don't think I have the energy for another conversation.{/i}"
    you "{i}Maybe I can sneak past and he won't notice me.{/i}{nw}"
    show vasili normal
    m "Who's standing there?!"
    m "{b}HELLOOO!!!{/b}"
    you "{i}Uhhhh... nobody? Stop talking to me.{/i}"
    you "Me!"
    "You walk closer to the figure. He might be weird, but that doesn't mean you have to be rude to him immediately."
    "Before you can say anything, he pulls some device out of his pocket and plays music in a foreign language."
    "The music is strange{w=.6}, even scary and unsettling."
    m "Bratgren used to be a nice city...{w=.3} I remember when the city's resources weren't hoarded by fat lions at the top - everything belonged to the people..."
    menu:
        "Pretend there's something scary behind him":
            "After 5 minutes of your ragebait, the bear still doesn't turn around."
            "And when he finishes talking, he tells you not to be afraid of the ghosts around this lake because they're harmless."
            you "What ghosts???" 
            m "Well what did you see over there?"
            you "Uhh...{w=.3}Yes yes yes I saw a ghost." 
            m "Those are the ghosts of the dead."
            m "I come here at night because sometimes my grandfather's ghost appears."
            menu:
                "What was his name?":
                    m "Ed Sheeran."
    you "My name is [name]."
    $ flag("metVasili", True)
    v "Hello! My name is Vasili. I brew potions, fish in my free time, and I also like to sing."
    you "Oh, cool. I bet a lot of people know your voice."
    v "I don't know...{w=.3} I only sing when I'm alone...{w=.3} it's not for me to judge."
    you "{i}That wasn't a question{/i}"
    "Vasili starts telling you about the lake, but you don't protest because you were going to ask about it anyway."
    v "This is {i}our{/i} lake, Świtezianka."
    v "There are some really cool legends about this lake, and basically the point is that they're scary and also that they're legends."
    v "So, like, generally speaking, nobody swims here, as in, you know, nobody."
    v "Because it's kind of like, technically you can, but actually not really, because everyone sort of decided that the idea isn't one of the best ones."
    you "Uhhhhhhhh{nw}"
    v "I mean, I'm not saying something will happen, but I'm also not saying that nothing will happen, because precisely, although however, since that is, because and nothing of it to them will happen."
    v "So therefore, to summarize and recap, nobody swims here, and it's not for no reason, it's specifically on purpose that they don't swim."
    v "Because precisely, although however, since that is, because and nothing of it to them will happen."
    v "But at the same time kind of maybe not entirely, more like, you know what I mean."

    menu:
        "Compliment his singing":
            you "You sing really well, comrade! You can tell you have talent."
            you "I'm sure you'll end up on a big stage someday."
            v "Thank you so much. You have no idea how much that made my day, heehee :3!!"
            $ friendship["Vasili"] += 1
        
        "Criticize his singing":
            you "Honestly, I think you should practice a little more."
            you "You can tell you sing like an amateur. Your D major 7 chord is flat."
            you "A bit of practice and you'll get much better."
            you "I studied theater, so I know what I'm talking about!"
            v "Who are you to criticize my voice like that?"
            "You start singing beautifully."
            you "la la la la la {w=1.5}la"
            v "Well... I did say I'm not an expert..."
            $ friendship["Vasili"] -= 1
            $ flag("rudeToVasili", True)
    
    v "So what would you like to know? I know practically everything around here - I spend all day outside, and if you listen closely you can learn a lot."
    v "I listen to people all the time."
    v "Did you know capitalism is bad?"
    jump ch01_vasiliFirstNightMagaMenu

label ch01_vasiliFirstNightMagaMenu:
    menu:
        "Ask about his knowledge of fish":
            $ ryba = random.choice(["ch01_vasiliFishBrzana", "ch01_vasiliFishKoza", "ch01_vasiliFishWstegorz"])
            jump expression ryba

        "Ask about his political views" if not flag("heardVasiliMonologue"):
            $ flag("heardVasiliMonologue", True) 
            v "I don't believe Barbara is a good president."
            v " Barbara is something worse than evil."
            v "She started tightening the capitalist leash - everyone had to find a j-{w=.6} j-{w=.6} jo...b."
            v "Barbara is efficient, and that is exactly where the real danger lies."
            v "She gives speeches, flashes that Morawiecka-style smile, and waves at children."
            v "She does all of it so people will believe her sentimental little fairy tales."
            v "But I see through the farce."
            v "You think she builds roads?"
            v "NEIN!!!{nw}"
            v "She only makes it easier for you to get to work so you can produce more things."
            v "She banned Piotr from helping Wiktoria on the farm."
            v "Because then she wouldn't have to work."
            you "But then Wiktoria could work somewhere else? That makes no sense."
            "Vasili ignores your argument and continues his rant."
            v "Don't be fooled by the streetlights - the city lighting is actually a surveillance network."
            v "The streetlights have eyes!"
            v "About ten years ago, our water was contaminated."
            v "If you drank it, you turned neon purple and died."
            v "Those were the good times."
            v "Everyone did things together and helped each other."
            v "There was suffering, but it was shared."
            v "Capitalism took that away from us."
            v "Now all we have is oppression, and the proletariat can do nothing."
            v "That's why I'm running for president of Bratgren!"
            v "Under my leadership, the city will enter a new era of anti-capitalist balance."
            v "We will abolish private property."
            "Hearing this insane monologue you cant help it and zone out for god knows how long."
            "Due to sheer luck Vasili doesnt notice you ignoring him and continues his sleep-inducing monologue."
            v "The decadence of the bourgeoisie must be brought to an end."
            v "Vote for me, comrade!!!"
            "Consciousness goes back into you right after he finished the speech."
            menu:
                v "Will you vote for me?"
                "Yes":
                    $ flag("endorsedCommunism", True)
                    $ friendship["Vasili"] += 1
                    v "Thank you, comrade."
                    v "I knew I could count on you."
                    jump ch01_vasiliFirstNightMagaMenu
                "No, thank you":
                    $ friendship["Vasili"] -= 1
                    v "I knew you would support capitalism!"
                    v "In that case, please leave the grounds of our house!!!"
                    you "How does that work? You say it's our house but you're kicking me out?"
                    v "Go support capitalism somewhere else."
                    hide vasili with dissolve
                    "You turn around and walk away from him as fast as possible because you cannot survive another \"comrade\"."
                    jump ch01_goingHomeTiredAfterVasiliFirstNight

        "Ask about his life":
            you "I'm curious about your past. I've heard so many stories about this place, but I know nothing about the people who live here."
            v "You want to know about my life?"
            v "Interesting... Well, I'm not going to gatekeep."
            v "As you already know - I brew potions for myself and other people."
            v "My grandfather opened a shop and made his potions there, so I had to carry on the tradition."
            v "Although after the accident... it was hard to go back to the profession."
            menu:
                "Ask about the accident":
                    you "If I may ask, what happened?"
                    if friendship["Vasili"] < 0:
                        v "You know what, I'd rather not talk about my grandfather..."
                        v "It's a pretty private subject, and I'd rather not talk about things like that."
                        you "That's okay. I understand."
                        you "{i}He said he wasn't going to gatekeep...{/i}"
                    else:
                        v "Sure, no problem. Long story short, my grandfather fell into a cauldron of boiling potion...{w=1} he didn't survive..."
                        you "Oh deer..." # jelito core
                        v "But what's done is done, and now I have to move on."
                "Stay silent":
                    you "{i}I'm a little curious what accident he means, but Vasili seems like a sensitive person.{/i}"
                    if flag("rudeToVasili"):
                        you "{i}Maybe I should leave it alone.{/i}"
                    else:
                        you "{i}If he talks this much anyway, he might as well tell me about his grandfather.{/i}"
                        you "How did your grandfather die?"
                        v "When I was 13, he fell into a cauldron of potion..."
                        you "Yeehaw!"
                        v "That's not funny!"
                        v "The fact that my grandfather stopped being alive is, like, you know, not funny at all, generally speaking, I mean - well - yeah."
                        v "Because it's such an unpleasant, sad, tragic, even unfortunate situation that, like, you can say something, but there really isn't anything to laugh about."
                        v "And generally this is more of a moment for being serious, not for making jokes, because we are, after all, talking about the death of my grandfather!"

            v "As for my hobbies, I love fishing and singing at the same time."
            v "Did I satisfy your curiosity?"
            you "Yes, thank you for sharing your story with me. "
            you "It's getting a little late, I think it's time for me to go. Goodnight!"
            v "Goodnight!"
            
            jump ch01_goingHomeTiredAfterVasiliFirstNight

label ch01_goingHomeTiredAfterVasiliFirstNight:
    "Because of how tired you are, the walk home feels like it takes forever, and you can barely see anything because they save money by turning off the streetlights."
    "Despite the poor visibility, getting home isn't too difficult."
    call screen s_House()

# TODO: COPY PASTE AN ENGLISH WIKIPEDIA ARTICLE NOT POLISH ??
label ch01_vasiliFishBrzana:
    v "Brzana (łac. Barbus barbus) to średniej wielkości, typowa rzeczna ryba z rodziny karpiowatych."
    v "Występuje w dorzeczach Loary, Rodanu, Renu, Dunaju, Łaby, Odry i Wisły."
    v "Można ją też spotkać w Tamizie, Niemnie, Dniestrze i Dnieprze oraz na Półwyspie Iberyjskim."
    v "Została introdukowana we Włoszech i Maroku."
    v "Osiąga przeciętnie około 70 cm długości."
    v "Maksymalnie dorasta do 120 cm i może ważyć do 12 kg."
    v "Brzana ma długie, niskie i walcowate ciało."
    v "Jest ono przystosowane do życia w nurcie rzeki."
    v "Grzbiet ma oliwkowozielony lub ciemnoszary."
    v "Boki są jaśniejsze, a brzuch biały."
    v "Płetwy grzbietowa i ogonowa są szare z ciemniejszym obrzeżeniem."
    v "Pozostałe płetwy mają czerwonawy kolor."
    v "Głównym pokarmem są larwy owadów wodnych, takie jak muchówki, chruściki, widelnice i jętki."
    v "Zjada też kiełże, mięczaki i skąposzczety."
    v "Rzadziej poluje na małe ryby."
    jump ch01_vasiliAfterFishMonologue

label ch01_vasiliFishKoza:
    v "Koza [[1] to gatunek małej ryby [[2] słodkowodnej z rodziny piskorzowatych [[3]."
    v "Zamieszkuje Europę [[4][[5] z wyjątkiem Irlandii [[6], Szkocji, Norwegii i północnej Szwecji."
    v "Nie występuje też w Finlandii, północnej Rosji oraz południowych[[3.5] półwyspach."
    v "Chodzi o Półwysep Iberyjski[[7][[8], Apeniński[[67] i Bałkański."
    v "Osiąga przeciętnie ok. 10[[10]] cm[[9]."
    v "Maksymalnie dorasta do 13,5[[13,5]] cm długości[[123]."
    v "Ma wydłużone ciało[[10]."
    v "Posiada obronne, ruchome kolce[[11] w okolicy oka[[12][[13]."
    v "Grzbiet jest brązowoszary[[14] i pokryty[[1] ciemnymi plamkami."
    v "Wzdłuż boków biegną dwa[[2], rzadziej jeden[[1], rzędy plam."
    v "Jest ich zwykle 10-20, są duże, okrągłe i ciemne[[15]."
    v "U nasady płetwy ogonowej znajduje się jedna duża ciemna plama[[2650]."
    v "Brzuch jest biały lub żółtawy[[6]."
    v "Żywi się bezkręgowcami dennymi..."
    jump ch01_vasiliAfterFishMonologue

label ch01_vasiliFishWstegorz:
    v "Wstęgor królewski to gatunek dużej, morskiej ryby strojnikokształtnej z rodziny Regalecidae."
    v "Jest zwierzęciem kosmopolitycznym — występuje w wodach Oceanu Indyjskiego, Pacyfiku, Atlantyku."
    v "Można go też spotkać w Morzu Północnym i Morzu Śródziemnym."
    v "Wstęgor osiąga zazwyczaj do 8 metrów długości."
    v "Maksymalna potwierdzona długość wynosi 11 m."
    v "Istnieje jednak doniesienie o osobniku, który miał aż 17 metrów."
    v "Maksymalna potwierdzona masa ciała wynosiła 272 kg."
    v "Ma bardzo wąskie, taśmowate i mocno bocznie spłaszczone ciało."
    v "Wzdłuż niego ciągnie się płetwa grzbietowa, od głowy do ogona."
    v "Służy ona też do napędu."
    v "Płetwa ma ponad 300 promieni, co jest rekordową liczbą."
    v "Pierwszych kilkanaście jest wysokich i zakończonych ozdobnymi zgrubieniami."
    v "Przypominają one koronę, stąd nazwa \"królewski\"."
    v "Przypuszcza się, że płetwy w wodzie mają jaskrawoczerwoną barwę."
    v "Na powietrzu szybko blakną."
    v "Ciało jest jasne i srebrzyście połyskujące..."
    jump ch01_vasiliAfterFishMonologue

label ch01_vasiliAfterFishMonologue:
    you "{i}What have I done. What did I do to deserve this...{/i}"
    menu:
        "Try to sneak away.":
            "Now is your time to shine."
            "Time to escape."
            "You feel like some North Korean trying to escape into China."
            "While Vasili looks the other way and rambles about some random fish, you put all your energy into your sneak mode and try to escape."
            "The problem is that not enough of that energy went into your eyes."
            "Because you failed to notice a can of hooks, a case full of fishing gear, his tent, and his chair."
            "First you trip over the can, then land on the case, knocking it over and destroying his tent in the process."
            "What just happened was so loud that it gives you extra energy to run."
            "And you run as fast as you possibly can."
            v "And where do you think you're going?!"
            you "{i}...{/i}"

            menu:
                "Give an excuse and leave":
                    you "You know what... I think I need to go home. I'm exhausted, I can't listen anymore."
                    v "So, just like always... nobody likes me."
                    v "Everyone runs away from me."
                    v "Just go. Don't hurt me anymore."
                    hide vasili with dissolve
                    you "I didn't mean to...{w=.3} Goodnight."
                    $ friendship["Vasili"] -= 2
                    you "{i}I didn't want it to end like this. But I don't have the energy to hear any more about those fish. I've had enough!{/i}"
                    "The walk home is full of thoughts about how you treated Vasili."
                    call screen s_House()
                "Give an excuse and stay.":
                    you "No... I just wanted to walk around because my legs hurt."
                    you "Besides, the night is so beautiful it would be a shame to sleep through it."
                    v "You're right, but you know what? I still haven't told you about my FAVORITE fish...."
                    jump ch01_vasiliTalksAboutFavoriteFish

        "Listen to the lecture.":
            you "Do you know any more fish?"
            v "{b}OF COURSE{/b}, I'll tell you about my {b}FAVORITE{/b} fish..."
            jump ch01_vasiliTalksAboutFavoriteFish
    
label ch01_vasiliTalksAboutFavoriteFish:
    you "{i}What have I gotten myself into... I DON'T WANT THIS ANYMORE...{/i}"
    scene black with dissolve
    "Overwhelmed by emotion and the endless fish lectures - you fall asleep."
    "But Vasili notices."
    v "[name]!"
    v "Are you listening to me?" 
    you "Sorry. It's really late, and I think I should go to sleep."
    v "I think you should go to sleep. Lack of sleep isn't healthy!"
    v "You know, I care about your health."
    "He doesn't know you fell asleep out of boredom, {w=0.6}#delulu"
    you "In that case, goodnight. I'm sure we'll meet again sometime."
    if friendship["Vasili"] < 0:
        v "Goodnight."
    else:
        v "Goodnight, comrade."
    "The walk home is a blur. You don't remember much because you were just woken up and you're extremely sleepy."
    "Somehow, you manage to drag yourself home."
    call screen s_House()