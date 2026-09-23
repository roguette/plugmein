


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

label ch01_m_cityHallRudeToKurowska:
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
    if not flag("rudeToKurowska"):
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
        "(nie mam więcej pytań)" if any([flag("askedWhereIAmStart"), flag("askedWhoPiotrWas"), flag("accusedPiotrOfKidnapping")]):
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
    you "Then let's get to Kurowska faster."
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
    p "Oczyszczałem las, jak mi kazałeś, a on pojawił się koło mnie i zepsuł mój rytuał, teraz muszę zacząć od nowa."
    you "Jakim cudem to jest moja wina?"
    you "Trzeci raz cię pytam i dalej nie wiem."
    m "No właśnie też bym chciał usłyszeć jakim cudem to jest twoja wina w tej sytuacji."
    m "Coś mi się wydaje, że są rzeczy ważniejsze."
    m "Ty możesz swoje rytuały zrobić nawet jutro. A [name] mógł w tym lesie umrzeć!"
    you "No dokładnie!"
    m "Chodź tu."
    "Podchodzisz trochę bliżej do Filipa, on wstaje i podaje ci rękę."
    "Uśmiechasz się jak w reklamie nieruchomości."
    "Nie wiesz, czy możesz mu ufać, ale on na pewno ma lepsze vibe-y od Piotra."
    you "Tak się wita z ludźmi Panie Piotrze"
    f "Cześć. Nazywam się Filip i witam w naszym małym{w=.6}, pięknym{w=.6}, fajnym{w=.6} i zarazem przytulnym mieście Bratgren. Pewnie masz ogromną ilość pytań?"
    you "No tak."
    f "A czy coś już wiesz o tym mieście?"
    you "No nie."
    "Filip jest uradowany tą informacją z jakiegoś powodu."
    "You tilt your head and lower your eyebrows to signal your confusion, which gets ignored"
    f "No to świetnie. Teraz zaprowadzę cię do Kurowskiej, ona odpowie na wszystkie twoje pytania."
    f "Ona lubi takie rzeczy opowiadać tylko musisz zadać {i}odpowiednie.{/i}"
    you "{i}TFYM ODPOWIEDNIE?!{/i}"
    f "Tylko nie stresuj się. Bądź dla niej miły i ona będzie miła dla ciebie"
    f "Aha powiem ci jeszcze jedną rzecz - nie jesteś jedyny."
    f "Wszyscy pojawiliśmy się przed tym miastem, tak jak ty."
    you "Wszyscy??"
    f "Wszyscy."
    you "Nawet Piotr?"
    f "Nawet Piotr."
    you "Piotr mi tego nie powiedział..."
    f "A to czemu gatekeepujesz, panie Piotrze?"
    p "To jest mój pierwszy raz, kiedy spotykam kogoś w lesie...."
    f "Ma sens, ale proszę następnej osobie takie rzeczy mówić!"
    f "Pan [name] pewnie się stresował przez ciebie."
    you "No właśnie!!!"
    f "No dobra wracając do Kurowskiej."
    f "Najpierw muszę się zapytać czy pana przyjmie."
    f "Ostatnio złapałem ją na robieniu skipu C na stole..., więc przyjemnie nie było i nie pachniało też dobrze..."
    you "Mam tylko jedno pytanie..."
    f "Tak?"
    you "Dlaczego jeszcze nie śpicie? Czy nie jest teraz noc?"
    f "Dzisiaj mieliśmy problem z wodą w mieście i cały dzień byliśmy tym zajęci."
    f "W tym mieście zawsze coś jest"
    "Filip podchodzi do drzwi i grzecznie puka."
    play sound "door_knock.mp3"
    f "Dobry wieczór, mam nową osobę czy mogę ją tutaj wprowadzić?"
    m "Jasne!"
    play sound "audio/sfx_door_open.mp3"
    "Filip otwiera drzwi i wpycha cię do biura, szybko zamykając za tobą drzwi."
    f "No no no idź idź..."

    scene bg office
    stop music

    "..."
    "Przed tobą siedzi Pani Kurowska, która ma taką aurę, że jej wzrok potrafi schłodzić pokój."
    show kurowska normal with dissolve
    you "Dobry wieczór..."
    k "Witam cię w miasteczku Bratgren! Jak cię zwą?"
    you "Zwą...{w=1} mnie [name]."
    k "Okeeej.. Mam na imię Barbara, jestem prezydentem miasta. Sprawuję tutaj władzę od 7 lat. Co cię tutaj sprowadza?"
    you "Właśnie obudziłem się w lesie, nie wiem kim jestem, nie wiem gdzie jestem, znam tylko swoje imie."
    you "Piotr znalazł mnie i zaprowadził mnie do Pani."
    you "No i tyle wiem."
    k "Czyli tak jak wszyscy..."
    "Barbara pisze coś do swojego notatnika."
    k "Jeszcze raz jak masz na imię???"
    you "[name]"
    k "Jakie dziwne imię. Weź mi to przeliteruj."

    $ nameSpelled = '-'.join([f"{letter}{{w=0.5}}" for letter in name])
    you "[nameSpelled]"
    k "Okej mam."


    menu:
        "Docieknij co to znaczy wszyscy.":
            you "Co to znaczy, że \"tak jak wszyscy\"?"
            k "Wszyscy, którzy tutaj mieszkają trafili w ten sam sposób do naszego miasta."
            you "Czyli..??"
            k "Nikt nie wie skąd się tutaj bierzemy"
            k "And, just like you, everyone doesn't know anything you just appear"
            k "Poof and you are in a forest"
        "Milcz":
            you "{i}Chyba nie wiem o co chodzi... ale boję się jej o to pytać.{/i}"
            you "{i}Może jest jeszcze jakaś agresywna.{/i}"
    you "Mam kwerendę!"
    k "Słucham?"
    you "Co jest w lesie poza miastem, i dlaczego to miasto jest w jakichś hebździnkach dolnych?"
    k "Ha ha!"
    k "Jeśli wyjdziesz do lasu zjedzą cię wilki albo umrzesz z powodu jakiejś niszowej choroby."
    you "..."
    "Jesteś w totalnym szoku!"
    k "No właśnie dlatego Piotr robi te rytuały. Wokół tego miasta jest taka tarcza, która odpycha od siebie złą energię."
    you "No piotr mi mówił jak on to robi tym takim onyksem."
    k "Exactly"
    you "That's actually really cool"
    "The concept of magic really intrigues you"
    "What if you too can do these rituals and become a powerful magician"
    you "A może pani ma do mnie jakieś pytania?"
    k "Hmm...."
    k "Czy ty cokolwiek pamiętasz?"
    "Ale ty nie pamiętasz nic. Twoja pamięc jest pusta, jak nowy dysk Samsung SSD T1 2TB Titan Gray USB-C."
    "Your survivor instincts kick in and you think about this question"
    "No, you dont remember most things"
    "Yes, you remember some things, like most of your general knowledge"
    you "{i}Na razie lepiej będzie udawać, że nic nie pamiętam.{/i}"
    you "{i}Bo jeszcze wyczyszczą mi pamięc jeszcze raz!{/i}"
    you "Nic nie pamiętam."
    k "Właśnie nikt w tym mieście nic nie pamięta..."
    k "Wszyscy mają jakieś zaniki pamięci."
    k "Ja też."
    you "Czyli śkończyło się na tym, że wszyscy mamy alzheimera."
    you "Było by to zabawne, gdyby nie było to tak straszne."
    k "Jakoś trzeba sobie radzić."
    jump ch01_kurowskaDialogMenu

label ch01_kurowskaDialogMenu:
    if flag("askedAboutHousing") and flag("askedAboutCity")  and flag("askedAboutWork"):
        jump ch01_gettingHouseKeysGood

    k "Czy masz jakieś pytania?"
    menu:
        "Zapytaj o miasto" if not flag("askedAboutCity"):
            $ flag("askedAboutCity", True)
            you "So what is this Bratgren"
            k "Its a city founded by Bjork you can see her portrait here, on the wall behind you"
            k "We are a small community built near lake Świtezianka"
            you "And what do you do"
            k "We do everything a city does? I dont understand the question"
            you "No no i understand"
            you "Piotr told me you have to protect the city from some sort of monsters"
            k "Yes.. they are very very dangerous"
            k "Piotr is a hero in here. protecting the city from them is risky"
            you "I see. So i'm guessing you can't really go outside?"
            k "No"
            you "Seems really boring"
            k "What?"
            you "I mean everything you do has to be in this city"
            k "Would you rather go back to the forest?"
            you "{i}Damn it shes right{/i}"
            you "No"
            k "Exactly"
            k "Jak się nie ma co się lubi, to się lubi co się ma"
            jump ch01_kurowskaDialogMenu

        "Zapytaj o nocleg." if not flag("askedAboutHousing"):
            $ flag("askedAboutHousing", True)
            you "Gdzie jest najbliższy hotel czy coś, bo nie mam ani domu ani mieszkania, gdzie ja będę spał?"
            k "Muszę tylko znaleźć klucze do twojego domu..."
            you "Dom?? Za darmo???"
            k "Oczywiście że nie za darmo. Darmowe domy mają tylko ci co pracują."
            k "Powiedzmy że w ten sposób ja inwestuję w ciebie."
            you "Oczywiście że będę pracował!!!"
            k "Mam nadzieję, że mnie nie cyganisz."
            you "{i}I klasa. Dom za darmo? W snach mi się to nie śniło.{/i}"
            jump ch01_kurowskaDialogMenu

        "Zapytaj o pracę." if not flag("askedAboutWork"):
            $ flag("askedAboutWork", True)
            you "A co z pracą?"
            you "Wiem, że filip pracuje w sekretariacie. A co robią inni?"
            you "Inni w sensie przeciętni ludzie."
            k "Powiem ci, że praca to znaczy robić cokolwiek na korzyść miasta."
            k "Są rolnicy, są piekarze, są kurierzy..."
            k "A jest na przykład taki pan Vasilij, który mimo tego że mieszka w mieście i korzysta z naszej ochrony przed złem, nie robi kompletnie nic."
            k "Vasilij tylko siedzi w domu i narzeka na rząd."
            you "Nie no coś tam wymyślę!"
            you "Chyba umarłbym z nudów gdybym był taki jak on."
            k "No ja też nie wiem jak mu się nie nudzi."
            k "Kompletnie nie jestem w stanie wyobrazić takiego życia bez jakichkolwiek czynności..."
            you "{i}Pryszniców on pewnie też nie może wyobrazić.{/i}"
            k "Dobra wracając do twojej pracy..."
            "Barbara przegląda dokumenty na stole, potem w stole, potem za nią."
            "Wydaje się, że ona wie że jest jakaś praca, ale nie może znaleźć tego papieru na stole."
            k "Do jasnej muffinki... Zgubiłam chyba..."
            k "No to w takim razie nie mam nic. Jutro bedę w stanie powiedzieć wiecęj, dlatego dzisiaj jesteś wolny."
            k "Tylko zgłoś się do mnie jutro."
            you "Jasne!!! XOXO"
            jump ch01_kurowskaDialogMenu

        "Powiedz coś o jej wyglądzie." if not flag("commentedOnKurowskasAppearance"):
            $ flag("commentedOnKurowskasAppearance", True)
            menu:
                "Powiedz coś o jej ubiorze":
                    you "Czy każdy może kupić takie ubrania?"
                    you "Bo Pani wygląda jak DIVA!"
                    k "Ha ha, dziękuje. Oczywiście, że można, trzeba się tylko zgłosić do naszej krawcowej."
                    k "Jest na rynku, obok piekarni"
                    $ friendship["Kurowska"] += 1
                    jump ch01_kurowskaDialogMenu
                "Powiedz coś o jej fryzurze":
                    $ telemetry_flag("rudeToKurowska")
                    you "Jakie wydarzenia spłodziły te fryzurę?"
                    k "Masz jakiś problem z moimi lśniącymi włosami z reklamy Maybelline?"
                    you "Nazywanie tego włosami jest dość łaskawym określeniem..."
                    k "Czy ty mnie obrażasz??"
                    you "Myślę, że daję ci coś co nazywa się konstruktywną krytyką!"
                    k "Zaraz ty i twoja konstruktywna krytyka zostaną wywaleni przez to okno."
                    $ flag("rudeToKurowska", True)
                    k "Dobrze w takim razie koniec tego wywiadu. Masz tutaj klucze do twojego domu, a teraz idź zanim cię wywale!"
                    scene bg secretary with vpunch
                    play sound "audio/sfx_door_slam.mp3"
                    you "{i}JESZCZE ŻYJĘ! Byłoby ciężko gdyby mnie wyrzuciła na bruk. Dostałem klucze do domu, o przyjemnych rozmowach nie myślę.{/i}"
                    jump ch01_gettingHouseKeysUniversal

label ch01_gettingHouseKeysGood:
    k "Jeśli nie masz więcej pytań, masz tutaj klucze do twojego nowego domu.{w} (ps. Kasia Dowbor go remontowała)"
    you "{i}Tam musi być luksusowo{/i}"
    you "Thank you! Thank you! Thank you!"
    jump ch01_gettingHouseKeysUniversal

label ch01_gettingHouseKeysUniversal:
    scene bg cityhallinside with dissolve
    play music "town_night.mp3"
    show piotr normal 
    "Wychodzisz z gabinetu Kurowskiej."
    p "Wyszstko dobrze?! Coś ty długo u niej byłeś..."
    you "Jesteś delulu nie było mnie dosłownie 5 minut."
    p "Jak ci poszło?"
    you "Patrz co mam!! (#flex)"
    "Mówiąc to pokazujesz mu klucze do Twojego własnego domu."
    "Podnosisz klucze do twarzy Piotra i widzisz brelok z adresem"
    "ul. Kolakoka 4"
    "Piotr jest zazdrosny, ponieważ on musiał pracować by dostać swój dom."
    p "Aha. Okej."
    p "W takim razie muszę iść dokończyć rytuał z wcześniej, w którym mi przeszkodziłeś. ŻEGNAM!"
    hide piotr with dissolve
    you "{i}Chyba się na mnie obraził.{/i}"
    if flag("wasRudeToPiotr"):
        you "{i}Chyba przesadziłem w tym sekretariacie.{/i}"
    you "{i}Ale bracie its not that deep. No cóż, nie obchodzi mnie to.{/i}"
    "Przed wyjściem z urzędu miasta patrzysz się na zegar, i widzisz, że jest 23:44."
    $ time.setTime(23,44)
    show screen s_Clock
    scene bg citysquarenight with dissolve
    play sound "sfx_footsteps_a.mp3"
    "Wychodzisz z urzędu miasta i idziesz przed siebie."
    "Czujesz dreszcze przebiegające cię po plecach."
    "Ale{w=0.6} nie wiesz dokładnie, co je spowodowało - to, że nie ma żywej duszy{w=0.6}, czy to, że po prostu jest zimno."
    you "{i}Boże czemu jest tak zimno???{/i}"
    "Łapiesz się za ramiona próbując się jakoś ogrzać."
    you "{i}Jaka to pora roku?{/i}"
    you "{i}Czy oni w ogóle mają tu zimy?{/i}"
    you "{i}Chyba, że to jest wiosna...{/i}"
    you "{i}Nie chcę zimy!{/i}"
    "Mówiąc to, tupnąłeś nóżką jakbyś robił wino."
    "Patrzysz się w górę w poszukiwaniu odpowiedzi, ale widzisz tylko ciemne, puste a nawet nudne niebo."
    "Nie masz pojęcia co teraz robić."
    window hide
    call screen s_walkable_Square()

label ch01_firstNightTownWalk:
    scene bg lanastreetnight with dissolve
    jump ch01_firstNightTownWalkPartB

# ch01_m_enteringChurch goes here and i dont want lanastreet in the bg
label ch01_firstNightTownWalkPartB:
    $ telemetry_flag("choseWiktoriaP")
    "Gdy już postanawiasz spuścić wzrok z tego pięknego zabytku architektury, widzisz...{w=.1} kogoś."
    you "{i}W KOŃCU!{/i}"
    you "{i}Pierwszy raz widzę kogoś na tej ulicy.{/i}"
    "Nie jesteś pewien czy chcesz do tej osoby podejść i porozmawiać czy raczej unikać."
    you "{i}Mam nadzieję, że mnie nie ten ktoś nie pobije.{/i}"
    "Aż w końcu tajemnicza osoba macha do ciebie i gestem zachęca abyś podszedł bliżej."
    you "{i}Czego onx chce???{/i}"
    "Podchodzisz bliżej do tajemniczej sylwetki przed kościołem, zachowując przy tym wszystkie środki bezpieczeństwa."
    show wp normal with dissolve
    $ flag("metWiktoriaP", True)
    you "Hi?"
    m "Oops"
    m "I thought you were someone else"
    you "Really?"
    m "Yeah this is very awkward... Sorry"
    you "Omg there are more people outside?"
    m "What? Yes"
    m "Are you new here or something"
    you "Yes i was born today"
    "She giggles just a tiny bit"
    wp "Well i am Wiktoria and i live down the street"
    wp "And you are ..??"
    you "[name]"
    "Uśmiechasz się jak w reklamie nieruchomości."

    $ newName = name.strip().split(" ")[0].lower()#  "Dupa 3.0" -> "dupa"

    wp "No właśnie miałam mówić, że wyglądasz na [newName]."
    wp "Masz fajne imię."
    wp "[name] [name] [name]"
    "It's your turn to giggle"
    "You lean onto the church's fence and try to be nonchalant"
    you "So where were you going on this fine evening, young lady?"
    wp "I had too much coffee and i couldnt fall asleep"
    you "And you chose to go outside? What if this place is dangerous"
    wp "Like you would know anything about that"
    wp "Actually yes, it is dangerous"
    you "How"
    wp "Vasili might be outside"
    you "Whomstve is vasili"
    wp "Oh my god you dont know?"
    you "No"
    wp "That is a BLESSING you should keep it that way"
    you "What? Why? Is he dangerous"
    wp "No he is worse"
    wp "He is so annoying oh my god"
    $ flag("knowsAboutVasili", True)
    wp "Right behind you theres a bakery right?"
    wp "When rafał, the owner, was closing he had a few buns that were going to go stale"
    wp "So instead of being wasteful he gave them away to people"
    wp "And his high calorie verity shaped ass said that..."
    "wiktoria points her finger up to the sky and starts speaking in a forced, very nerdy voice"
    wp "Boli mnie wszystko co nagłe"
    wp "Chodzi o dyskomfort jaki czuje?"
    wp "Zwracam uwagę na dyskomfort?"
    wp "Domyślam się że macie beke ze mnie"
    wp "Hmph!"
    you "dobra sybau"
    wp "And thats not all!"
    you "And I heard enough"
    you "Now i'm scared of him too"
    you "Where does he live?"
    wp "By the lake. his house is the one with red aura coming off of it"
    you "okay..."
    "you twitch at the thought of coming anywhere near him"
    wp "As you can see I'm his #1 fan"
    you "And my mother is lady gaga"
    "Wiktoria laughs at your sassiness"
    wp "Lets go together"
    wp "You dont want to be alone when {i}he{/i} starts talking to you"
    "You walk to the square talking about how you both hate it when you are trying to open yoghurt and the foil splits in two"
    scene expression loc_bg("square")
    show wp normal at center with dissolve
    wp "So tell me, how were the first few hours in bratgren"
    you "So i woke up in the forest..."
    wp "this is getting interesting"
    you "Piotr was in front of me so i immediately thought its all his fault"
    you "So i was kinda rude to him and you know"
    you "He led me to Kurowska and she gave me a house"
    if flag("rudeToKurowska"):
        you "I was rude to her too"
    "Wiktoria starts laughing uncontrollably"
    wp "What happened to your attitude"
    wp "You weren't rude to me"
    you "Stop it i calmed down now"
    wp "Okay but you have to apologize for being rude"
    you "We will see about that"
    "you both laugh"
    wp "I also appeared in the forest just like you"
    wp "But i didnt have piotr to help me"
    wp "I had to follow my instincts"
    you "And you have been here for how many years?"
    wp "Like 8"
    you "Ohh so like you are a local at this point"
    you "You must know alot about Bratgren"
    wp "Yeah i guess you could say so"
    you "Could you tell me about this city?"
    wp "Is there anything specific you would like to know?"
    you "Well.."
    menu:
        "Where am i":
            pass
    you "Like i know i am IN bratgren but where is this bratgren"
    you "Is that all there is in this world"
    wp "Well no not really"
    wp "I heard there are more cities out there"
    wp "Its that i haven't been outside much"
    you "and where is everyone?"
    wp "I dont really know where the closest one is"
    wp "But it's not like that matters"
    wp "There are gmo wolves in that forest and they will rip you apart if you dare and try to explore"
    you "That's very rude of them"
    you "And no one wanted to explore?"
    wp "Actually i think we can explore the forest"
    wp "Piotr, the guy you were extremely rude to, is in charge of our onyx supply"
    wp "So he is very protective of it"
    wp "He feels very maternal towards it"
    wp "And to explore you need that onyx or else the monsters will try to eat you"
    wp "Piotr is not going to give you any just to wander in the forest"
    wp "Especially with that attitude"
    "You laugh but deep inside you know she is right"
    "There's a moment of silence"
    you "Yeah i have to apologize to him"
    wp "yeah.."
    you "So what do you even do here"
    you "I'll wake up tomorrow and have nothing to do"
    you "Wait no Kurowska told me to get a job"
    wp "You can do anything you just need to get money"
    wp "The goal is to get everyone to chip in a little and improve the city"
    wp "What if more people like you spawn and there are no houses available?"
    wp "Would you rather live with a total stranger or have your own house?"
    you "Seems fair"
    "you yawn very loudly"
    you "I better get going"
    you "It was nice talking to you"
    wp "Goodnight [name]"
    wp "Goodnight"
    hide wp normal with dissolve
    "Zaczynasz iść do domu. Głowa ciąży ci od nadmiaru informacji, które dzisiaj otrzymałeś."
    "Z wiązku z ciężkim dniem, nie myślisz nad niczym innym niż snem."
    call screen s_House()

label ch01_lakeVisit:
    $ telemetry_flag("choseVasili")
    play music "forest.mp3" fadein 1.0
    scene bg lakenighta with dissolve
    "Schodzisz w dół, skręcasz parę razy i docierasz na piękną łąkę."
    "Jest naprawdę ogromna, boagta w różnej barwy i rodzaju kwiaty. Ten widok sprawia, że prawie zapominasz o wszystkich przeżyciach tego dnia."
    "Niestety mocniejszy podmuch wiatru wytrąca cię z tego stanu i zostawia cię samego z powracającymi wydarzeniami tego dnia."
    "Jest też nieopodal jakiś dziwny las, ale nie masz zamiaru tam teraz iść."
    "Zszedłeś z drogi, która prowadziła właśnie do tego lasu, i teraz jedynym światłem jest blask Księżyca{w=.3} ― znaczy, z czegokolwiek co świeci na niebie."
    "Twoja droga nad jezioro powinna być w teorii spokojna ― szelest trawy, przez która się przedostajesz powinien być jedynym dźwiękiem."
    "Jednak los miał inne plany."
    scene bg lakenightb with dissolve
    "Na brzegu jeziora widzisz sylwetkę człowieka{w=.6}, yyy... raczej furasa."
    "Ktokolwiek to jest, próbuje łowić ryby i jest {b}strasznie{/b} głośny."
    you "{i}Do jasnej muffinki! Czy serio ktoś tutaj musi być???{/i}"
    you "{i}Chyba nie mam energii na kolejne konwersacje.{/i}"
    you "{i}Może przemknę się bokiem i mnie na zauważy.{/i}{nw}"
    show vasili normal
    m "Kto tam stoi?!"
    m "{b}HALOOO!!!{/b}"
    you "{i}Yyyyy... nikt? Przestań do mnie gadać.{/i}"
    you "Ja! Yyy... to znaczy, jestem tutaj nowy."
    "Podchodzisz bliżej do postaci. Może jest dziwny, ale to nie znaczy, że musisz od razu być wobec niego niemiły."
    "Ale zanim zdążysz cokolwiek powiedzieć, on wyciąga z kieszeni jakieś urządzenie i puszcza ci muzykę w obcym języku."
    "Muzyka jest dziwna{w=.6}, nawet straszna i niepokojąca."
    m "Bratgren było fajnym miastem...{w=.3} Pamiętam jak surowce miasta nie były gromadzone przez tłuste lwy na szczycie ― wszystko należało do ludu..."
    menu:
        "Udawaj, że za nim jest coś strasznego":
            "Po 5 minutach twojego ragebaitu niedźwiedz się nie odwraca."
            "Po tym jak skończył mówić, kazał ci się nie bać duchów przy tym jeziorze, bo są niegroźne."
            you "Jakie duchy???" 
            m "No a co żeś widział tam?"
            you "Yyy...{w=.3} no ducha widziałem." 
            m "To są duchy zmarłych."
            m "Przychodzę tu w nocy bo czasami pojawia się duch mojego dziadka."
            menu:
                "Jak on miał na imie?":
                    m "Grzegorz Brą z Owy"
    you "Nazywam się [name]."
    $ flag("metVasili", True)
    v "Witaj! Mam na imię Vasili. Warzę eliksiry, w wolnym czasię łowię ryby i lubię też śpiewać."
    you "O jak fajnie, pewnie dużo ludzi zna twój głos?"
    v "No nie wiem...{w=.3} śpiewam tylko jak jestem sam...{w=.3} nie mnie to oceniać."
    "Vasili zaczyna opowiadać ci o tym jeziorze, ale ty nie protestujesz, bo i tak miałeś się pytać."
    v "To jest {i}nasze{/i} jezioro, Świtezianka."
    v "Są bardzo fajne legendy o tym jeziorze i w nich chodzi o to, że właściwie są straszne i to, że są legendami."
    v "Dlatego, w sensie tak ogólnie mówiąc, no to nikt tu nie pływa, tak jakby, wiesz, nikt."
    v "Bo to jest trochę tak, że niby można, ale właściwie to nie bardzo, bo wszyscy jakby uznali, że ten pomysł nie należy do najelpszych."
    you "yyyyyy{nw}"
    v "Znaczy, ja nie mówię, że coś się stanie, ale też nie mówię, że się nic nie stanie, dlatego że właśnie, iż jednak, bo tak to, bo i się nie nic tej z nich stanie."
    v "Więc dlatego, tak podsumowując i reasumując, nikt tu nie pływa, i to tak nie bez powodu, tylko tak specjalnie, że jednak nie pływają."
    v "Dlatego że właśnie, iż jednak, bo tak to, bo i się nie nic tej z nich stanie."
    v "Ale jednocześnie trochę jakby może nie do końca, tylko tak bardziej, że no wiesz o co chodzi."

    menu:
        "Pochwal śpiew":
            you "Świetnie śpiewasz, towarzyszu! Słychać, że masz talent."
            you "Można powiedzieć, że dałeś do {i}naszego{/i} pieca."
            you "Jestem pewny, że kiedyś wylądujesz na wielkiej scenie."
            v "Dzięki wielkie. Nie wiesz jak mi to dzień zrobiło!!!"
            $ friendship["Vasili"] += 1
        
        "Krytykuj śpiew":
            you "Tak szczerze to chyba powinieneś jeszcze troszkę poćwiczyć."
            you "Słychać, że amatorsko śpiewasz."
            you "Trochę ćwiczeń i będzie znacznie lepiej."
            you "Studiowałem w teatrze, więc wiem o czym mówię!"
            v "Kim ty jesteś, żeby tak krytykować mój głos?"
            "Zaczynasz pięknie śpiewać."
            you "la la la la la {w=1.5}la"
            v "No cóż... Mówiłem, że nie jestem specjalistą..."
            $ friendship["Vasili"] -= 1
            $ flag("rudeToVasili", True)
    
    v "To o czym chciałbyś się dowiedzieć? Wiem tutaj praktycznie wszystko ― spędzam całe dnie na ulicy i jeśli się dobrze przysłucha to można dużo informacji uzyskać."
    v "Ja słucham ludzi cały czas."
    v "Wiedziałeś, że kapitalizm jest zły?{nw}"
    jump ch01_vasiliFirstNightMagaMenu

label ch01_vasiliFirstNightMagaMenu:
    menu:
        "Zapytaj jaką ma wiedzę na temat ryb":
            $ ryba = random.choice(["ch01_vasiliFishBrzana", "ch01_vasiliFishKoza", "ch01_vasiliFishWstegorz"])
            jump expression ryba

        "Zapytaj o poglądy polityczne" if not flag("heardVasiliMonologue"):
            $ flag("heardVasiliMonologue", True) 
            v "Nie wierzę, że Kurowska jest dobrą prezydentką."
            v "Kurowska to coś gorszego niż zło."
            v "Zaczęła zaciskać kapitalistyczną smycz ― każdy musiał znaleźć pr―{w=.6} pr―{w=.6} pra...cę."
            v "Kurowska jest wydajna i właśnie w tym tkwi prawdziwe niebezpieczeństwo."
            v "Wygłasza przemówienia, pokazuje swój uśmiech à la Morawiecka i macha dzieciom."
            v "Robi to wszystko po to, żeby wierzyli w te jej ckliwe bajeczki."
            v "Ale ja widzę przez tę farsę."
            v "Myślisz, że buduje drogi?"
            v "Nie!!!{nw}"
            v "Ona tylko ci ułatwia dotarcie do pracy, żebyś mógł produkować więcej rzeczy."
            v "Pamiętam, jak próbowała nałożyć podatek na Piotra za to, że nic nie robił."
            v "Nazwała to \"zastojem arkanicznym\"."
            v "Zakazała mu nawet pomagać Wiktorii na farmie."
            v "Bo wtedy by nie musiała pracować."
            you "Ale wtedy wiktoria by mogła pracować gdzieś indziej? To przecież bez sensu"
            "Vasili ignoruje twój argument i kontunuuje swój rant"
            v "Nie daj się zwieść latarniom ― oświetlenie miasta to w rzeczywistości sieć inwigilacji."
            v "Latarnie mają oczy{w=1}.{w=1}.{w=1}."
            v "Jakieś dziesięć lat temu nasze wody zostały zakażone."
            v "Po wypiciu tej cieczy robiłeś się fioletowy i umierałeś."
            v "To były dobre czasy."
            v "Wszyscy robili coś razem i sobie pomagali."
            v "Było cierpienie, ale było ono wspólne."
            v "Kapitalizm nam to odebrał."
            v "Teraz mamy tylko opresję, a proletariat nic nie może zrobić."
            v "Dlatego kandyduję na prezydenta Bratgren!"
            v "Pod moim przewodnictwem miasto wejdzie w nową erę antykapitalistycznej równowagi."
            v "Zniesiemy własność prywatną."
            "Hearing this insane monologue you cant help it and zone out for god knows how long"
            "Due to sheer luck Vasili doesnt notice you ignoring him and continues his sleep-inducing monologue"
            v "Dekadencja burżuazji musi zostać zakończona."
            v "Głosuj na mnie, towarzyszu!!!"
            "Consciousness goes back into you right after he finished the speech"
            menu:
                v "Czy zagłosujesz na mnie?"
                "Tak":
                    $ flag("endorsedCommunism", True)
                    $ friendship["Vasili"] += 1
                    v "Dziękuję towarzyszu."
                    v "Wiedziałem, że mogę na ciebie liczyć."
                    jump ch01_vasiliFirstNightMagaMenu
                "Nie, dziękuję":
                    $ friendship["Vasili"] -= 1
                    v "Wiedziałem, że będziesz popierał kapitalizm!"
                    v "W takim razie proszę opuścić teren naszego domu!!!"
                    you "To jak to działa, że mówisz że to nasz dom ale mnie wyganiasz?"
                    v "Idź popieraj kapitalizm gdzieś indziej."
                    hide vasili with dissolve
                    "Odwracasz się i idziesz jak najszybciej od niego bo nie wytrzymasz kolejnego \"towarzysza\"."
                    jump ch01_goingHomeTiredAfterVasiliFirstNight

            
        "Zapytaj o życie":
            you "Jestem ciekaw twojej przeszłości. Tyle się nasłuchałem historii tego miejsca, a nic nie wiem o ich mieszkańcach."
            v "Chcesz wiedzieć o moim życiu?"
            v "Ciekawe... No ale nie bedę gatekeepował."
            v "Jak już wiesz ― warzę eliksiry dla siebie i innych ludzi."
            v "Mój dziadek stworzył sklep i robił tam swoje mikstury, więc musiałem przejąć tradycję."
            v "Chociaż po wypadku... ciężko było wrócić do zawodu."
            menu:
                "Dopytaj o wypadek":
                    you "Jeśli mogę zapytać, to co się stało?"
                    if friendship["Vasili"] < 0:
                        v "Wiesz co, wolę nie mówić o moim dziadku..."
                        v "Ten temat jest dość prywatny, i wolę nie opowiadać o takich rzeczach."
                        you "Wszystko w porządku. Rozumiem cię."
                        you "{i}Mówił że nie będzie gatekeepował...{/i}"
                    else:
                        v "Jasne, nie ma problemu. To w skrócie mój dziadek wpadł do kotła z wrzącym eliksirem...{w=1} nie przeżył..."
                        you "O jeju" # jelito core
                        v "Ale było minęło i teraz trzeba żyć dalej."
                "Milcz":
                    you "{i}Jestem trochę ciekawy o jaki wypadek chodzi, ale Vasili wydaję się być wrażliwym człowiekiem.{/i}"
                    if flag("rudeToVasili"):
                        you "{i}Może lepiej zostawię to w spokoju.{/i}"
                    else:
                        you "{i}Skoro tyle gada to równie dobrze może mi opowiedzieć o swoim dziadku.{/i}"
                        you "W jaki sposób twój dziadek umarł?"
                        v "Kiedy miałem 13 lat wpadł do kotła z eliksirem..."
                        you "Wow, ale heca."
                        v "To nie jest śmieszne!"
                        v "Sam fakt tego, że mój dziadek przestał żyć, to jakby no, wiesz, nie jest ani trochę zabawne, tak w ogóle w sensie ― no ― tak."
                        v "Bo to jest taka niefajna, smutna, tragiczna a nawet nieszczęśliwa sytuacja, że niby można coś powiedzieć, ale właściwie to nie ma z czego się śmiać."
                        v "I że ogólnie to jest bardziej taki moment na bycie poważnym, a nie na jakieś żarty, bo to jednak mówimy właśnie o śmierci mojego dziadka!"

            v "Natomiast jeśli chodzi o moje pasje to kocham łowić ryby i śpiewać w tym samym momencie."
            v "Czy zaspokoiłem twoją ciekawość?"
            you "Tak, dziękuję że się ze mną podzieliłeś swoją historią. "
            you "Trochę późno, chyba na mnie czas. Dobranoc!"
            v "Dobranoc!"
            
            jump ch01_goingHomeTiredAfterVasiliFirstNight

label ch01_goingHomeTiredAfterVasiliFirstNight:
    "Przez zmęczenie droga do domu trwała wieki, ale nic nie było widać, ponieważ oszczędzają przez wyłączanie latarni."
    "Pomimo braku widoczności przejscie do domu nie sprawiło ci dużo trudu."
    call screen s_House()

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
    you "{i}Co ja zrobiłem. Za jakie grzechy...{/i}"
    menu:
        "Spróbuj się wymknąć.":
            "Teraz jest twój time to shine."
            "Czas uciekać."
            "Czujesz się jak jakiś Koreańczyk z północy próbujący uciec do Chin."
            "Podczas gdy Vasili patrzy w drugą stronę i gada o jakichś losowych rybach, zbierasz całą energię w swoje cichobiegi i próbujesz uciec."
            "Problem jest w tym, że za dużo tej energii nie poszło w oczy."
            "Bo nie zauważyłeś puszki z haczykami, walizki z akcesoriami wędkarskimi, jego namiotu i krzesła."
            "Najpierw potykasz się o puszkę, potem lądujesz na walizce, przewracając ją i przy okazji rozwalając mu namiot."
            "To co właśnie się stało było tak głośne, że dało ci dodatkową energię do biegu."
            "I pobiegłeś tak szybko jak tylko mogłeś."
            v "No i gdzie ty się wybierasz?!"
            you "{i}...{/i}"

            menu:
                "Zaprezentuj wymówkę i idź":
                    you "Wiesz co... chyba już muszę iść do domu. Jestem strasznie zmęczony, nie dam rady więcej słuchać."
                    v "Czyli tak jak zawsze... nikt mnie nie lubi."
                    v "Każdy ode mnie ucieka."
                    v "Idź już sobie, nie rań mnie więcej."
                    hide vasili with dissolve
                    you "Nie chciałem...{w=.3} Dobranoc."
                    $ friendship["Vasili"] -= 2
                    you "{i}Przecież nie chciałem, żeby tak wyszło. Nie mam siły (i chęci), by więcej słuchać o tych rybach. Mam dość dzisiejszego dnia!{/i}"
                    "Droga do domu była pełna przemyśleń na temat twojego postępowania w związku z Vasilijem."
                    call screen s_House()
                "Zaprezentuj wymówkę i zostań.":
                    you "Nie... tylko chciałem się przejść, bo mnie nogi bolą."
                    you "Poza tym noc jest tak piękna, że aż szkoda ją przespać."
                    v "Masz rację, ale wiesz co? Jeszcze nie opowiedziałem ci o mojej ULUBIONEJ rybie...."
                    jump ch01_vasiliTalksAboutFavoriteFish

        "Wysłuchaj wykładu.":
            you "Znasz może więcej ryb?"
            v "{b}OCZYWIŚCIE{/b}, opowiem ci o mojej {b}ULUBIONEJ{/b} rybie..."
            jump ch01_vasiliTalksAboutFavoriteFish
    
label ch01_vasiliTalksAboutFavoriteFish:
    you "{i}W co ja się wkopałem... JA JUŻ NIE CHCE...{/i}"
    scene black with dissolve
    "Przez nadmiar emocji i przedne wykłady na temat ryb ― usnąłeś."
    "Ale on to zauważył."
    v "[name]!"
    v "Czy ty mnie słuchasz?" 
    you "Przepraszam. Jest bardzo późno, i chyba powieniem iść spać."
    v "Mi się wydaje, że powienieneś iść spać. Brak snu nie jest zdrowy!"
    v "A wiesz, ja się martwię o twoje zdrowie."
    "Nie wie, że zasnąłeś z nudów, {w=0.6}#delulu"
    you "To w takim razie dobranoc. Kiedyś się jeszcze na pewno spotkamy."
    if friendship["Vasili"] < 0:
        v "Dobranoc."
    else:
        v "Dobranoc, towarzyszu."
    "Droga do domu jest jak przez mgłę. Nie pamiętasz za dużo, ponieważ zostałeś obudzony i jesteś bardzo zaspany."
    "Jednak jakoś doczłapałeś do swojego domu"
    call screen s_House()