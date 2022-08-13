define KrtkusOut = 0
define FifiOut = 0
define ZlevOut = 0
define MysOut = 0
define day = 1
define krtkus = Character("Velký Krtkus")
define me = Character("já")
define mis = Character("Myškuska")
define lev = Character("Český Zlev")
define fifi = Character("Velká Fifinka")
define everyone = Character("Všichni")
define walter = Character("Waldemar Bílý")
define debug = Character("E̷̞̖̻̗̤̘̎r̴̡͉̭̩͖̗̈́̔͛͊̐͒r̷̨̰͍̤̈̈o̷͉̤̦̻͚͈͌͑̆r̵̖̦̂́͝")
define rock = Character("Šutrák")
define info = Character("")
define babicaAfranta = Character("Jirka Babica a Špinavej František")
define franta = Character("Špinavej František")
define babica = Character("Jirka Babica")
define zagur = Character("Zagur")
define KrtkusLove = 0
define FifiLove = 0
define MisLove = 0
define LevLove = 0
define SutrakLove = 0
define HasMoney = 1
define Lunch = 0
define Mineralka = 0
define SutrakActive = 1
define PeroCisty = False
define olda = Character("Olda")
define Event1 = 0
define Event2 = 0
define marek = Character("Marek Vašut")
define pavouk = Character("Teplý Pavouk")

define SittingWith = 0 

label start:
    jump den1


label den1: 
    stop music
    scene black
    play sound "<from 0 to 2>audio/Alarm-ringtone.mp3" volume 0.4
    
    me "O né, nesmím přijít na můj první den školy pozdě!"
    me "Musím rychle!"

    scene background1

    show krtek at center

    me "*Vrazíš do někoho*"
    krtkus "Jauvajs, Dávej trochu pozor!"
    menu:
        "promiň, neviděl jsem tě.":
            $ KrtkusLove = KrtkusLove + 2
        "Kam Koukáš ty Kopáči??":
            $ KrtkusLove = KrtkusLove - 2

    $ player_name = renpy.input("Tebe neznám, jak se jmenuješ??")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Dušan"

  
    krtkus "{b}%(player_name)s {/b} Radši pojď, ať nepříjdeme pozdě."
    
    hide krtek
    scene background2
    show krtek:
        xpos 0 ypos 400
    show fifi:
        xpos 350 ypos 400
    show lev:
        xpos 700 ypos 400 zoom 2
    show myskus:
        xpos 1300 ypos 300
    everyone "takže ty seš tady taky nový??"
    hide fifi
    hide lev 
    hide myskus
    with dissolve
    krtkus "už jsme se potkali ale nepředstavil jsem se, jsem Velký Krtkus"
    show myskus
    hide krtek
    with dissolve
    mis "Ahoj, já jsem Myškuska, moc mě těší"
    show fifi
    hide myskus
    show krtek:
        xpos 0 ypos 400
    with dissolve
    fifi "Co na mě tak blbě civíš. O tebe bych si ani kolo neopřela a na moje jméno můžeš úplně zapomenout"
    krtkus "Tohle je Fifinka, má spadeno na populární holkokluky ze školy… ty žel zatím plníš jen jednu predispozici, aby o tebe jevila zájem"
    hide fifi
    hide krtek
    show lev:
        ypos 300 zoom 2
    with dissolve
    lev "Vítej u nás ve třídě. Lepšího průvodce bys nenašel, jsem totiž Český Zlev. Pokud by ses ztratil, a nebo bys nevěděl do čeho píchnout, hehe, tak jsem tady vždy k dispozici *mrk*."
    play sound "<from 0 to 3>audio/School-bell.mp3" volume 0.25
    lev "ehh už začíná hodina, myslím že teď máme chemii? tento rok máme zase pana Waldemara Bílého"
    hide lev
    show walter:
        xpos 1150 ypos 305 zoom 0.25
    with dissolve
    walter "Dobrý den třído, posaď se {b} %(player_name)s {/b} , vítám vás v prvním školním dni... "
    menu:
        "Sednout si za krtkusem":
            $ KrtkusLove = KrtkusLove + 1
            $ SittingWith = 1
        "Sednout si za Myškou":
            $ MisLove = MisLove + 1
            $ SittingWith = 2
        "Sednout si za fifi":
            $ FifiLove = FifiLove + 1
            $ SittingWith = 3
        "Sednout si za lvem":
            $ LevLove = LevLove + 1
            $ SittingWith = 4
    walter "Hned vám rozdám nové učebnice ať můžeme začít s vyučováním ale ještě předtím..."
    walter "vám musím představit našeho nového studenta, jmenuje se {b} %(player_name)s {/b} "
    if SittingWith == 1:
        show krtek at left
        krtkus "Tohle je náš učitel chemie Waldemar. Jednou postnul meme, co byl tak velkej cancer až z toho dostal opravdovou rakovinu varlat. Čas od času kvůli tomu nedorazí na hodinu, ale někdy si nejsem jistý, jestli fakt chybí kvůli té jeho rakovině varlat."
        krtkus "Podívej na tento meme, co jsem vytvořil. Účinkuji v něm já a zpívám v něm: Vel-ký Krtkus, Velký Krtkus Velký Krtkus několikrát za sebou. Přijde ti to také k popukání?"
        menu:
            "Ano, Velký krtkusi. Ty jsi vždy byl a navždy budeš vtipný!":
                krtkus "OMB děkuji, já věděl že jsem mega vtipný!"
                $ KrtkusLove = KrtkusLove + 1
            "Ani ne, tenhle vtip je už dávno ohranej":
                krtkus "COŽE? tak teďs mě nasral"
                $ KrtkusLove = KrtkusLove - 1
    if SittingWith == 2:
        show myskus at left
        mis "To pan Bílý, učil nás chemii i minulý rok. Ale něco se mi na něm nezdá, má takovou nezdravou barvu, je bílý jak stěna. Jak jsi na tom byl na minulé škole s chemií?"
        menu:
            "Nic moc":
                mis "Tak to jsme dva"
            "Jo, celkem mi to šlo":
                mis "Tak to doufám že mě někdy necháš něco opsat"
                $ MisLove = MisLove + 1 
    if SittingWith == 3:
        show fifi at left
        fifi " Proč si zamnou vůbec sedáš? nikdo se tě o to neprosil! achjo zase máme chemii s tím retardem kterej vypadá jako by měl každou chvílí zemřit…"
    if SittingWith == 4:
        show lev:
                zoom 2
                xpos 100
                ypos 230
        lev "Vidím že sis zvolil dobře, právě sis sedl s nejlepším průvodcem historií této školy, věděl jsi že náš učitel má testikulární rakovinu? ano je to tak, jednou postnul jeden meme kterej byl takovej cancer až z toho dostal opravdou rakovinu!"
    info "Hodina Chemie s panem Waldemarem bílým byla docela nuda, no prostě chemie"
    info "bylo velice zvláštní že měl celou dobu takovou divnou barvu, asi je nemocný..."
    info "a nebo že by to byla ta rakovina jak o ní povídali? idk jestli se tomu dá věřit"
    play sound "<from 0 to 3>audio/School-bell.mp3" volume 0.25
    scene background3
    show sutrak_2 at right:
        zoom 0.8
    with dissolve
    rock "Tak ty seš ten novej student?"
    menu:
        "A-ano":
            show sutrak_2 at right:
                zoom 0.8
        "Co ti je do toho??":
            hide sutrak_2
            show sutrak_1 at right:
                zoom 0.8
    rock "Naval prachy nebo ti ukážu proč mi říkají Šutrák!"
    menu:
        "D-dobrá *dá mu peníze*":
            show sutrak_2 at right:
                zoom 0.8
            $ HasMoney = 0

        "Soráč, ale když ti je dám, tak tvoje máma nedostane zaplaceno":
            $ SutrakLove = SutrakLove - 1
            hide sutrak_2
            show sutrak_1 at right:
                zoom 0.9
            with dissolve
            rock "Co jsi to řekl o mojí mámě?!"
            show walter:
                xpos -500
            with dissolve
            walter "Nemáte už dávno být na obědě?"
            rock "Ještě se uvidíme!"
    scene background4
    show babica at left
    with dissolve
    babica "Tak gejmře, co to bude?"
    menu:
        "Co si dám k obědu?"
        "Vepřo Knedlo Zelo":
            babica "dobrá volba"
            $ Lunch = 1
        "Ravioli":
            if HasMoney == 0:
                babica "to je za připlatek 30kč"
                me "ale já mám jen na klasicej oběd"
                babica "tak to si musíš vzít knedlo vepřo zelo..."
            else:
                babica "Vepřo Knedlo Zelo je lepší ale dobře no"
                $ HasMoney = 0
                $ FifiLove = FifiLove + 1
                $ Lunch = 2
    hide babica
    show jirka_a_franta at left
    
    babicaAfranta "Dobrou chuť!"
    scene background5
    menu:
        "Za kým si sednu?"
        "Za Krtkusem":
            scene background4
            show krtek:
                zoom 1.5
                ypos 300
            me "Je tu volno?"
            krtkus "No jasně ale ty sem nesmíš..."
            krtkus "hahahah jen vtípkuju, pojď si sednout. Co to máš?"
            if Lunch == 2:
                krtkus "co to máš za sračku, podporuj tradiční českou kuchyni ne?!"
                $ KrtkusLove = KrtkusLove - 1
            else:
                krtkus "no to je pořádný jídlo, nechápu jak by si někdo mohl dát to druhý 'jídlo'"
            krtkus "No a jak se ti tady zatím líbí?"
            menu:
                "Jak se mě tady líbí?"
                "Pohoda":
                    krtkus "Tak to je dobrý, Já to tady občas docela nesnáším, hlavně když musíme jíst něco hnusnýho, dneska naštěstí bylo něco jedlýho..."
                "Nesnáším to tady":
                    krtkus "Tak to mě mrzí, snad se to tu brzo zlepší, přecejen to je první den školy tak hned nebreč + průměr + nikdo se neptal"
        "Za Miškusem":
            scene background16
            show myskus:
                zoom 1.25
                ypos 200
            me "Je tu volno?"
            mis "Jasně."
            menu:
                "Jak ti chutná?":
                    mis "je to dobrý, ale radši nechtěj vědět, jak to v té kuchyni vypadá."
                "Vaří tu dobře?":
                    mis "Levný, ale dobrý jídlo. Jen si nikdy nedávej koláč, budou v něm vlasy."
        "Za Fifi":
            scene background14
            show fifi:
                zoom 1.5
                ypos 200

            if FifiLove < 2:
                fifi "vážně tu chceš sedět?"
            else:
                fifi "jestli chceš, tak se tady klidně posaď"
            if Lunch == 2:
                fifi "ty jsi taky vegan? tak to je úžasný!!! konečně nejsem ve škole jediná. Z těch kteří dokážou sníst maso je mi špatně, pokud teda nejsou populární ovšem, potom jim to prominu, každý ma nějakou chybičku že ano "
                menu:
                    "Nejsem Vegan, prostě jen mě toto přišlo lepší...":
                        fifi "no aspoň o 1 míň zvířat přišlo o život..."
                        $ FifiLove = FifiLove + 2
                    "jo, nesnáším tento řízený zločin proti zvířatům!!!":
                        fifi "konečně si někdo uvědomuje vážnost této situace, konečně nebudu jediná která bojuje za práva zvířat!"
                        $ FifiLove = FifiLove + 3
            if Lunch == 1:
                fifi "Další masožrout? je mi z vás blbě, nepřijde ti blbé že aby jen kvůli tvému potěšení z jídla ublížit nevinným zvířatům??"
                menu:
                    "jo, ale já si nemůžu pomoct, jsem nemocnej":
                        $ FifiLove = FifiLove + 3
                        fifi "můžu tě skusit napravit, vypada to že nejsi ještě uplně ztracený případ"
                    "ne, je mi to jedno, klidně ať umřou, mě maso chutná":
                        fifi "OKAMŽITĚ odejdi od tohoto stolu!!!"
                        $ FifiLove = FifiLove - 3
        "Za Zlvem":
            scene background15
            show lev:
                zoom 2
                xpos 100
                ypos 230
            me "je tu volno?"
            lev "Si Kuř."
            lev "Dneska jsem  viděl jednoho muže s gigantickým penisem, hned jsem na něho měl chuť, rozhodně víc než na tohle “jídlo“"
            menu:
                "Kde jsi proboha dnes viděl muže s gigantickým penisem?":
                    lev "na hlaváku, cestou do školy"
                "Taky bych si dal":
                    lev "je vidět že máme stejný názor!"
                    $ LevLove = LevLove + 1
    play sound "<from 0 to 3>audio/School-bell.mp3" volume 0.25
    me "konečně konec školy, dneska byl dlouhý den. Ještě bych šel s někým ven, ale s kým?"
    scene background1
    menu:
        "s kým půjdu ven?"
        "S krtkusem":
            $ KrtkusOut = KrtkusOut + 1
            jump KrtkusOut1
        "S Myškusem":
            $ MysOut = MysOut + 1
            jump MyskusOut1
        "S Fifi":
            $ FifiOut = FifiOut + 1
            jump FifiOut1
        "Se Zlvem":
            $ ZlevOut = ZlevOut + 1
            jump ZlevOut1
jump den2

label den2:
    scene black
    play sound "<from 0 to 2>audio/Alarm-ringtone.mp3" volume 0.4
    me "dneska jsem si už nastavil budík správně takže dneska už nepříjdu pozdě (snad)"
    scene background1
    show lev:
        zoom 2
        ypos 300
    with dissolve
    lev "Brý ráno, vidím, že dneska jdeš už na čas."
    menu:
        "Jo, už si davám bacha":
            lev "Jdeme tedy?"
        "Jak vůbec víš že jsem ráno nestíhal?":
            lev "Vím toho spoustu… Ale o tom někdy jindy, teď bychom už měli jít."
    scene background2
    if SittingWith == 1:
        show krtek
        krtkus "Ahoj, vyspinkanej do růžova?"
        menu:
            "Vž-vždyť já na sobě růžovou nemám":
                krtkus "Ale vždyť víš, to se tak přece říká…"
            "Jo, dokonce se mi ani nezdálo nic o někom ze třídy, nebo tak…":
                krtkus "Zvláštní, neříkáš to moc přesvědčivě."
    if SittingWith == 2:
        show miskus
        mis "Ahoj, doufám že sis po včerejšku pořádně odpočinul."
        menu:
            "Ne… musel jsem na tebe pořád myslet.":
                mis "…A-ano, t-taky jsem o včerejšku přemýšlela… "
            "Ano, proč se ptáš?":
                mis "No, včera to byla pohodička, ale teď už nás pan Bílý nebude šetřit."
    if SittingWith == 3:
        show fifi
        fifi "No nazdárek, tak už konečně na čas?!"
        menu:
            "Ano, dal jsem si brzo budíka.":
                fifi "To je dobře, když sám nedokázeš vstát."
            "Jo, ale ne díky tobě.":
                fifi "Tak si trhni nohou."
    if SittingWith == 4:
        show lev:
            zoom 2
            ypos 300
        lev "Brý ráno, vidím, že jsi to po prvním dni nevzdal, to jsem rád."
        menu:
            "Proč bych to měl vzdávat?":
                lev "No, v takové třídě retardů nevydrží úplně každej, možná to chce ještě čas…"
            "Mě se jen tak nezbavíte.":
                lev "Máš kuráž, to se mi líbí."
    play sound "<from 0 to 3>audio/School-bell.mp3" volume 0.25
    info "začíná hodina"
    scene background2
    show walter:
        xpos 1150 ypos 305 zoom 0.25
    play sound "<from 0 to 18>audio/BB-Intro.mp3" volume 0.1
    if Event1 == 1:
        walter "Žáci, měl by k vám pár slov pan ředitel."
        show marek with dissolve
        marek "Studenti, vyskytl se nám tady takový nešvar… Včera mi někdo propíchal gumy, pokud nevíte, mám tu tmavou, modrozelenou felicii, co vždy parkuje úplně u zdi."
        marek "Jestli jste u toho včera někoho viděli, tak mi to prosím nahlaste.  Nemusím snad ani zmiňovat, že za případné dopadení pachatele dostanete odměnu."
        marek "je možné, že to nikdo od nás nebyl, ale mám obavu, či spíše, důvodné podezření, že šlo o někoho odsud."
        marek "Abychom zde mohli fungovat, musíme se vyvarovat takových nepříjemností a držet pospolu. Z mých benefitů získáváte i vy. Nyní pokračujte ve výuce, nashledanou."
        hide marek with dissolve

    walter "Tak, můžeme začít s výukou, připravte si učebnice."
    walter "Nejdřív si ale proklepnu, kolik si toho pamatujete."
    walter "Aha, {b}%(player_name)s {/b} by nám mohl ukázat, jak dobře učí chemii na Czechmemes. Tak tedy: Které látky mají identické atomy?"
    menu:
        "Které látky mají identické atomy?"
        "Uhlík a dusík.":
            walter "To neděláš své bývalé škole dobré jméno… to právě unikátní skladba atomu přece odlišuje jednu látku od druhé. "
        "Železo a dusík.":
            walter "To neděláš své bývalé škole dobré jméno… to právě unikátní skladba atomu přece odlišuje jednu látku od druhé. "
        "Železo a rtuť.":
            walter "To neděláš své bývalé škole dobré jméno… to právě unikátní skladba atomu přece odlišuje jednu látku od druhé. "
        "Žádné":
            walter "Ano, velmi správně."
    walter "A druhá otázka: Co zapříčiňuje díry v ozonové vrstvě?"
    menu:
        "Co zapříčiňuje díry v ozonové vrstvě?"
        "Přílišné využívání skla v městské zástavbě.":
            walter "Špatně, jde o freony."
        "Tání ledovců.":
            walter "Ne, jsou to freony"
        "Freony":
            walter "Naprosto správně"
        "Ozonové díry jsou hoax vyprodukovaný nosáči, aby zpomalili energetický průmysl.":
            walter "No, podle učebních osnov to sice správně není, ale jsem mile překvapen, že někdo takto červenopilulkován. Na Czechmemes bych tě vskutku netipoval."
    
    walter "Kohopak bychom… Krtkusi, ty jsi nám minulý rok trochu pokulhával."
    show krtek at left with dissolve

    walter "Proč se při lámání a navazování chemických vazeb uvolňuje energie?"
    krtkus "Uuuuuh, noooo…"
    menu:
        "mlčet":
            walter "no tak to nebude dobrá známka..."
            $ KrtkusLove = KrtkusLove -1
            $ Event1 = 1
        "Napovědět správnou odpověď":
            $ KrtkusLove = KrtkusLove +2
            $ Event1 = 2
            krtkus "Protože samotné vazby jsou energie"
            walter "Správně, máš za jedna"
        "napovědět špatně":
            $ KrtkusLove = KrtkusLove -4
            $ Event1 = 3
            krtkus "Protože to tu energii vyleká a chce emmm… rychle utéct"
            walter "Špatně, protože jsem milosrdný tak dostaneš čtyřku a ne pětku"
    hide krtek with dissolve
    walter "Tak, dneska se budeme učit o jaderných elektrárnách, k tomu vám pustím video a pak si uděláte zápis z učebnice, stránky 16"
    info "Pan Bílý pustí NEZkreslenou vědu o jaderných elektrárnách"
    walter "Na toto téma si připravte domácí úkol, zítra jej budu kontrolovat, jinak máte přestávku."
    play sound "<from 0 to 3>audio/School-bell.mp3" volume 0.25
    scene background5 with dissolve
    show babica
    with dissolve

    babica "Tak co to bude dneska gejmře?"
    menu:
        "Moravský vrabec s divokou rýží":
            $ Lunch = 1
            babica "No to je vono, moravská klasika, nech si chutnať"
        "ovocný Salát":
            $ Lunch = 2
            hide babica
            show franta
            franta "Další vegan… vem si ten salát a drž hubu."
    hide franta
    hide babica
    menu:
        "s kým si sednu na oběd?"
        "Krtkus":
            scene background4
            show krtek at left
            if Event1 == 2:
                krtkus "Kámo Mega dík za tu radu zachránil si mě"
                menu:
                    "Nemáš zač. Nemohl jsem tam jen tak sedět mezitím co se Waldemar připravoval ti dát kouli. ":
                        $ KrtkusLove = KrtkusLove + 1
                        krtkus "Na tohle nikdy nezapomenu"
                    "Máš zač. Dej mi kus své porce a máš dluh zplacenej":
                        $ KrtkusLove = KrtkusLove - 2
                        krtkus "No to snad nemyslíš vážně?"
                        krtkus "*Povzdychne si*"
                        krtkus "Nuže dobrá fakt si mi pomohl."
                        $ SutrakActive = 1
            if Event1 == 1:
                krtkus "Tos mě nemohl poradit??"
                menu:
                    "nevěděl jsem odpověď tak sem ti nechtěl poradit špatně":
                        krtkus "no tak aspoň jsi mi neporadil špatně"
                        $ KrtkusLove = KrtkusLove + 1
                    "chtěl jsem aby jsi dostal za 5":
                        krtkus "idiote rodiče mě zabijou"
                        $ KrtkusLove = KrtkusLove - 3
            if Event1 == 3:
                krtkus "No tak to ti teda děkuji za tu radu. Teď mám kouli z Chemie."
                menu:
                    "Fakt se omlouvám myslel jsem si, že je to dobrá odpověď":
                        krtkus "Hmmm no aspoň si to myslel dobře…"
                        if KrtkusLove < 0:
                            $ SutrakActive = 1
                    "Furt nemůžu uvěřit že si mi na to skočil :trolak:":
                        krtkus "Jdi do prdele"
                        $ KrtkusLove = KrtkusLove - 10

        "Fifi":
            scene background14
            show fifi at left
            if FifiLove >= 7:
                fifi "ahoj, ty si tu chceš sednout? tak pojď!"
            if FifiLove < 7:
                fifi "ok no, sedni si sem jestli chceš i guess"
                if Lunch == 2:
                    fifi "veganská pochutina, salát!"
                    $ FifiLove = FifiLove + 1
                    fifi "je viděť že máš vkus, jediný důvod že se s tebou bavím."
                    fifi "je fakt neuvěřitelné že tu nejsem jediná veganka"
                    fifi "tyjo, dneska jsem se vůbec nevyspala, věděl jsi o tom že nadesignovat funkční bombu je fakt těžký?"
                    menu:
                        "jo, určitě ti budu věřit že po nocích designuješ bomby":
                            $ FifiLove = FifiLove - 1
                            fifi "ale mě je přece uplně jedno jestli mě to věříš!"
                            fifi "přecejen, nepamatuju si že bych se tě někdy na něco ptala…"
                        "ne?":
                            $ FifiLove = FifiLove + 1
                            fifi "je to fakt dost komplikovaný, hlavně ta chemie kolem toho, ale to není problém, na to mám jiný lidi"
                if Lunch == 1:
                    fifi "*mumlá* ti debilní masožrouti"
                    fifi "včera jsem hodně přemýšlela nad tím jestli je ok když zabiješ jiný tvory za účelem toho aby jsi zachránila jiný ale víc, je to velice komplikovaná otázka!"
                    fifi "CO si o tom myslíš ty?"
                    menu: 
                        "asi záleži na tom o kolik víc těch tvorů zachráníš, pokud to bude jeden tak to za tu vraždu nestojí, pokud 1000 tak určitě":
                            $ FifiLove = FifiLove + 1
                        "ani náhodou, vraždění je vyloučené! co si za osobu že nad tím vůbec přemýšlíš???":
                            $ FifiLove = FifiLove - 1
                        "jo určitě!":
                            $ FifiLove = FifiLove + 2
                        "4.	já bych zabíjel i kdybych tím nikoho nezachránil":
                            $ FifiLove = FifiLove + 1
                    fifi "zajímavý názor"

                
        "Zlev":
            scene background15
            show lev:
                zoom 2
                ypos 300
            if LevLove < 6:
                lev "Ahoj uwu!"
            if LevLove >= 6:
                lev "nazdárek"
            lev "Kvízová otázka"
            me "cože?"
            lev "no tak přece potřebuju vědět jak jsi na tom s dějepisem ne?!"
            me "uhh no tak dobře..."
            lev "kdy byla podepsaná zlatá bula sicilská?"
            menu:
                "1916":
                    lev "to si děláš prdel ne? dám ti ještě jednu šanci!"
                    $ LevLove = LevLove -1
                "1334":
                    lev "to si děláš prdel ne? dám ti ještě jednu šanci!"
                    $ LevLove = LevLove -1
                "1212":
                    lev "no je vidět že základy asi umíš, ale co tohle?"
                    $ LevLove = LevLove +1
                "co je sakra zlata bula sicilská?":
                    lev "to si děláš prdel ne? dám ti ještě jednu šanci!"
                    $ LevLove = LevLove -1
            lev "jak se jmenoval ten giga chad kterej nás chtěl zbavit špinavé rasy?"
            menu:
                "Martin Roh":
                    lev "ten byl taky založený ale toho jsem nemyslel, toto je docela propadák… "
                    $ LevLove = LevLove + 1
                "Arved  Majvés":
                    lev "ten byl taky založený ale toho jsem nemyslel, toto je docela propadák… "
                    $ LevLove = LevLove + 1
                "radovan karadzic":
                    lev "ten byl taky založený ale toho jsem nemyslel, toto je docela propadák… "
                    $ LevLove = LevLove + 1
                "olga hepnarová":
                    lev "ten byl taky založený ale toho jsem nemyslel, toto je docela propadák… "
                    $ LevLove = LevLove + 1
                "adolf hitler":
                    lev "ano! snažil se tomuto světu pomoct ale lidé v něm neshledali pochopení"
                    $ LevLove = LevLove + 2


        "Myška":
            show myskus
            scene background16
            me "Ahoj, je tu volno?"
            mis "Jasně, posaď se!"
            if Event2 == 1:
                mis "Víš jak si mi říkal že máš rád ženské oblečení?"
                menu:
                    "N-no?":
                        $ MisLove = MisLove + 0
                    "Já ho přímo miluju!":
                        $ MisLove = MisLove + 1
            else:
                mis "Neuvěříš mi, co se mi stalo"
                menu:
                    "Povídej!":
                        $ MisLove = MisLove + 1
                    "Že by mě to zajímalo… ale když už jsi to nakousla tak pokračuj":
                        $ MisLove = MisLove - 1
            mis "Tak představ si, že když jsem si nedávno zapomněla ve škole tělocvik a musela se pro něj vrátit, tak jsem viděla učitele Chaliho (učitel češtiny), jak se po tělocvičně procházel v catmaid outfitu! "
            menu:
                "Možná je Pan učitel Chali založenější, než jsem si myslel.":
                    $ MisLove = MisLove + 0
                "To bych do něj opravdu neřekl.":
                    $ MisLove = MisLove + 0
            mis "Mám podezření, že má Pan učitel Chali v kabinetu pořádný šatník s ženským oblečením."
            menu:
                "To mi nepřijde moc pravděpodobné.":
                    mis "Mysli si co chceš, já si myslím své."
                    $ MisLove = MisLove - 1
                "Co kdybychom se mu trošku prohrábli v šatníku :trolak:?":
                    mis "Je vidět, že přemýšlíš stejně jako já… Ale teď už musím běžet, jede mi šalina a musim ji stihnout, měj se!"
                    $ MisLove = MisLove + 1
    scene background3
    show sutrak_1
    with dissolve
    if SutrakActive == 0:
        rock "máš jediný štěstí že tě krtkus chrání jinak bych z tebe vymlátil všechny prachy který máš!"
        menu:
            "1.	stejně jako tvoje máma vymlátila  všechno z mýho penisu včera?":
                rock "TY HAJZLE TO JSI UŽ PŘEHNAL!"
                show krtek at left with dissolve
                krtkus "ať tě to ani nenapadne…"
                rock "no jo no"
            "2.	no, to asi mám docela štěstí no":
                rock "no to si piš, jestli tě někdy přestane chránit tak dostaneš!"
    else:
        rock "teď už neutečeš!"
        rock "dej mi všechny tvoje prachy nebo dostaneš na prdel"
        menu:
            "nic ti nedám hajzle":
                rock "CO SI TO DOVOLUJEŠ, TEĎ DOSTANEŠ!"
                info "šutrák ti vzal všechno co u sebe máš"
            "no dobře no":
                rock "no to si myslím, teď mě to dej!"
                info "šutrák ti vzal část pěněz které u sebe právě máš"
    scene background1 with dissolve
    menu:
        "s kým si půjdu udělat úkol?"
        "Krtkus":
            $ KrtkusLove = KrtkusLove + 2
        "Fifi":
            $ FifiLove = FifiLove + 2
        "Miška":
            $ MisLove = MisLove + 2
        "Zlev":
            $ LevLove = LevLove + 2

    me "ukol byl složitej ale aspoň to mám už hotový..."
    me "tak teď už jenom jit domů a jít spát"
    jump den3

label den3:
    scene black 
    play sound "<from 0 to 2>audio/Alarm-ringtone.mp3" volume 0.4
    me "už do tehle školy chodím 3 dny? no super..."
    scene background1
    show fifi
    with dissolve
    fifi "Nazdar, prosimtě, sháním podpisy na petici našeho spolku proti rasismu."
    menu:
        "Jakou petici?":
            $FifiLove +=2
            fifi "Jsem ráda, že tě to zajímá, sháníme podpisy na petici za zavedení zákona, který potrestá vězením každého, kdo řekne slovo na N."
            menu:
                "Co kdyby sis radši sehnala nějaké feny?":
                    fifi "Trhni si nohou debile"
                    $FifiLove -=5
                    $LevLove +=1
                "Promiň, nemám zájem.":
                    fifi "Dobře, ale jedině tak zastavíme bezpráví a nastolíme rovnoprávnost!"
                    $FifiLove -=2
                "Ano, musíme potrestat každého rasistu, jedině tak dosáhneme na světě svobody a rovnosti! Kde to můžu podepsat?":
                    fifi "Jako bys mi mluvil z duše, máš čest být první ze školy kdo to podepíše!"
                    $FifiLove +=4
        "Promiň, musim si ještě udělat úkol před hodinou":
            fifi "To bude jen na minutku, s tím úkolem ti kldině pomůžu."
            menu:
                "No dobře, o čem je tedy ta petice?":
                    $FifiLove +=1
                    fifi "Jsem ráda, že tě to zajímá, sháníme podpisy na petici za zavedení zákona, který potrestá vězením každého, kdo řekne slovo na N."
                    menu:
                        "Co kdyby sis radši sehnala nějaké feny? ty negře":
                            fifi "Trhni si nohou debile"
                            $FifiLove -=5
                            $LevLove +=1
                        "Promiň, nemám zájem.":
                            fifi "Dobře, ale jedině tak zastavíme bezpráví a nastolíme rovnoprávnost!"
                            $FifiLove -=2
                        "Ano, musíme potrestat každého rasistu, jedině tak dosáhneme na světě svobody a rovnosti! Kde to můžu podepsat?":
                            fifi "Jako bys mi mluvil z duše, máš čest být první ze školy kdo to podepíše!"
                            $FifiLove +=4
                "Opravdu pospíchám, promiň.":
                    $FifiLove -=2
                    fifi "no dobře no..."
    scene background2
    me "Sakra, já si zapoměnř propisku."
    menu:
        "od koho si pujčim propisku??"
        "od Zagura":
            show zagur_2
            with dissolve
            zagur "Tak ty si chceš vypůjčit propisku?"
            show zagur_3
            hide zagur_2
            with dissolve
            zagur "Co kdyby sis radši vypůjčil nějaké feny!"
            menu:
                "Proč myslíš, že hraju tuhle hru?":
                    hide zagur_3
                    with dissolve
                "Debile.":
                    hide zagur_3
                    with dissolve
        "od Pavouka":
            scene background2
    show pavouk_2
    with dissolve
    pavouk "takže propisku jo?"
    show pavouk_3
    hide pavouk_2
    with dissolve
    pavouk "a nevadí že je ožužlaná?"
    menu:
        "já si ji očistím":
            $ PeroCisty = True
            scene background2
        "Tím líp >:)":
            $ PeroCisty = False
            scene background2

    if SittingWith == 1:
        show krtek
        hide pavouk_3
        with dissolve
        krtkus "Tak ty sis půjčil péro od pavouka?"
        krtkus "Pavouk je frajer, díky němu vznikl ten vtipobraz co jsem ti ukazoval první den, pamatuješ?"
        menu:
            "No jistě, Vel-ký Krtkus, velký Krtkus velký Krtkus!":
                krtkus "Ano, je to tak humorné!"
            "Já to zapomněr :lebka: ":
                krtkus "Jsi asi jediný člověk na planetě, kdo si ten chytlavý, skvělý text nezapamatoval, vem si svoje alzheimer prášky."
            "Ty myslíš tu nevtipnou píseň? I já bych napsal lepší":
                krtkus "Ty jsi horší než ta Fifina, fakt."
                $KrtkusLove = KrtkusLove - 5
        krtkus "Mimochodem, zapomněl jsem si dneska taky propisku, takže doufám, že mi ji budeš půjčovat."
        menu:
            "Tobě vždycky kamaráde retarde":
                krtkus "Díky Brácho"
                $KrtkusLove = KrtkusLove + 1
            "Vždyť ty zápisky stejně nepotřebuješ, naučíš se z učebnice.":
                krtkus "dobře, ale pokud se něco stane, jde to na tebe."
    elif SittingWith == 2:
        show myskus
        hide pavouk_3
        with dissolve
        if PeroCisty == True:
            mis "Jé, ty máš růžové pero, to je hezké"
            menu:
                "Musel jsem si ho půjčit":
                    mis "Aha, tak to nic"
                    $MisLove = MisLove - 2
                "Ano, moje oblíbená barva je růžová":
                    mis "Neobvyklé, ale líbivé"
                    $MisLove = MisLove + 2
        else:
            mis "Hezké pero, nějaké vlhké"
            menu:
                "No jo, teďka je období monzunů":
                    mis "když to říkáš"
                "Půjčil jsem si ho od Pavouka":
                    mis "On je takový hodný, že?"
                    $MisLove = MisLove + 2
                "Máš pravdu, mé pero je skutečně vlhké":
                    mis "Hihi, ty jsi tak vtipný"
                    $MisLove = MisLove + 6
    elif SittingWith == 3:
        show fifi
        hide pavouk_3
        with dissolve
        if PeroCisty == True:
            fifi "Jé ty sis pořídil růžové pero co se hodí k mému oblečení?"
            menu:
                "Ano je to dárek pro tebe":
                    fifi "Nejspíš s ním psát nebudu ale dík"
                    $ FifiLove = FifiLove + 2
                    $ PavoukRespekt = PavoukRespekt - 1
                "Ano abychom měli víc shodných barev":
                    if Event2 == 1:
                        fifi "No aspoň nebudeme spolu vypadat špatně"
                        $ FifiLove = FifiLove + 2
                    elif Event2 == 0:
                        fifi "....No zatím se barevně shoduje jen to pero ale ok..."
                "Ne jenom jsem si ho půjčil od Pavouka":
                    fifi "FUJ TY S TÍM STVOŘENÍM KAMARÁDÍŠ?"
                    menu:
                        "No ani ne...":
                             me "No ani n..."
                             fifi "Fuj a to jsem si myslela že seš docela fajn"
                             $ FifiLove = FifiLove - 2
                        "No docela jo...":
                            me "No docela j..."
                            fifi "Fuj a to jsem si myslela že seš docela fajn"
                            $ FifiLove = FifiLove - 4
                        "No moment, není tohleto rasismus proti arachnickému etniku?":
                            fifi "NO TOHLE! JÁ NEMÁM SLOV! MOJE KRYTÍ, tedy TAKOVÁ NEHORÁZNOST! Máš štěstí, že už začíná hodina."
        elif PeroCisty == False:
            info "Fifi se zhnuseně kouká na pero"
            fifi "FUJ PROČ JE TO OD SLIN!?"
            menu:
                "FUJ ani jsem si to neuvědomil. Hned si vezmu gumové rukavice a umyju ho.":
                    me "FUJ ani jsem si to neuvědomil. Hned si vezmu gumové rukavice a umyju ho."
                    fifi "Ah ty jsi jen mentálně nepozorný jako já už jsem se lekla že si to neočistil schválně"
                "Půjčil jsem si to od Pavouka a teď mám jeho sliny":
                    me "Půjčil jsem si to od Pavouka a teď mám jeho sliny, ježiš úplně z toho slintám taky *slint slint* kape to na to pero *slint*"
                    fifi "No Fuj Pavouk...asi budu zvracet..."
                    info "Fifi uteče na záchod a zbytek hodiny tam zůstane"
                    $ FifiLove = FifiLove - 8
label KrtkusOut1:
    $ KrtkusLove = KrtkusLove + 1
    show krtek at left
    if HasMoney == 0:
        krtkus "Hej viděl jsem jak tě Šutrák Otravoval před školou"
        me "Jo obral mě o peníze na oběd"
        krtkus "viděl jsem... Co kdybych ti od něj pomohl?"
        menu:
            "Fakt bys to pro mě udělal?":
                krtkus "Co bych byl za kamaráda kdybych ti od něj nepomohl"
                $ SutrakActive = 0
            "To bych po tobě nemohl chtít":
                krtkus "No jak myslíš..."
    if HasMoney == 1:
        krtkus "Slyšel jsem jak si před obědem urazil Šutráka"
        me "pořádně jsem mu to nandal co?"
        krtkus "Fakt si mu to nandal ale teď si na tebe dá extra pozor...Co kdybych ti od něj pomohl?"
        menu:
            "Fakt bys to pro mě udělal?":
                krtkus "Co bych byl za kamaráda kdybych ti od něj nepomohl"
                $ SutrakActive = 0
            "To bych po tobě nemohl chtít":
                krtkus "No jak myslíš..."
    krtkus "A teď je čas na pomstu!!"
    menu:
        "Neber to zas tak vážně, tolik se toho přece nestalo.":
            $KrtkusLove = KrtkusLove - 2
        "pomstu? To je něco podle mého gusta!":
            $KrtkusLove = KrtkusLove + 2
    krtkus "Jde o ředitele Vašuta, minulý rok dělal všechno proto abych neprošel. Takže mu to oplatíme na jeho fáru."
    scene background6
    show krtek at left:
        zoom 1.25
    menu:
        "To je zmetek, jdeme na to!":
            $Event1 = 1
            krtkus "Tady máš šroubovák, propícháme mu gumy."
            krtkus "teď rychle pryč"
            scene background7
            show krtek at left:
                zoom 1.25
            krtkus "Tady to je moje zašívárna, hele, někdo tady něco nechal… (drží dvě stříkačky)"
            krtkus "Zkusíme to??"
            menu:
                "No tak to je jasný he he he":
                    $KrtkusLove = KrtkusLove + 2
                    krtkus "tak jdeme na to"
                    play movie "background8.ogv"
                    krtkus "Tak to byla jízda"
                    me "to jo"
                    krtkus "musíme rychle domů aby nás tady někdo neviděl..."
                    stop movie
                    $ day = day + 1
                    $ KrtkusOut = KrtkusOut + 1
                    jump DenDecider
                "S drogama si radši začínat nebudu":
                    $KrtkusLove = KrtkusLove - 2
                    krtkus "no ok no, s tebou není žádná sranda..."
                    $ day = day + 1
                    $ KrtkusOut = KrtkusOut + 1
                    jump DenDecider
        "nemyslím že to je dobrý nápad...":
            $ KrtkusLove = KrtkusLove - 2
            krtkus "No jak chceš, klidně si jdi já tě k tomu nepotřebuju"
            $ day = day + 1
            $ KrtkusOut = KrtkusOut + 1
            jump DenDecider

label MyskusOut1:
    show myskus:
        zoom 1.25
        ypos 200

    me "chceš doprvodit domů?"
    mis "Ty mě chceš doprovodit? To je… milé."
    menu:
        "doufám že ti to nevadí":
            $ MisLove = MisLove + 1
            mis "Vůbec ne, hele, už mi jede šalina desítka."
        "Jeden den ve škole přece není dost na to, abych tě lépe poznal.":
            $ MisLove = MisLove - 1
            mis "Um… T-to zní… H-hele, už nám jede šalina desítka."
    scene background9
    show myskus:
        zoom 1.25
        ypos 200
    mis "Moc často nakupovat nechodím, ale teď nějaké nové oblečení potřebuji. Tady mají dámskou sekci. "
    menu:
        "Dobře.":
            mis "Co myslíš, slušelo by mi to?"
            menu:
                "Jo asi si vezmu to samé.":
                    $ MisLove = MisLove + 1
                    mis "A pro koho?"
                    menu:
                        "No, pro mojí mámu, to je snad jasné, ne? Vůbec si to neberu pro sebe nebo tak…":
                            mis "Aha, to mě mohlo napadnout."
                        "Pro sebe, rád si oblékám dámské oblečení, je pohodlné a pěkně přilnavé.":
                            mis "O-opravdu? T-to je fajn…"
                            $ Event2 = 1
                            $ MisLove = MisLove + 5
                "No, nevím jestli ti to úplně sedne.":
                    $ MisLove = MisLove - 1
                    mis "Jak to myslíš?"
                    menu:
                        "Vlastně nic, je to tvoje volba":
                            mis "N-no dobrá."
                        "No, možná v tom budeš vypadat trochu tlustě.":
                            $ MisLove = MisLove - 5
                            mis "Myškuska: C-COŽE?! T-ty sprosťáku! V-víš co? Radši už jdi."
                            $ day = day + 1
                            jump DenDecider
        "Já vím, taky tady nakupuju":
            mis "Jako tady v H&Mku?"
            me "No, přímo v dámské."
            $ MisLove = MisLove + 1
            mis "To kupuješ pro svou mamku? Nebo snad sestru?"
            menu:
                "A-ano, ano, jistě, vůbec to není pro mě, já totiž vůbec nikdy nenosím dámské oblečení, není to součástí mého módního stylu, to vůbec ne.":
                    mis "Když to říkáš… škoda."
                "No, kupuju to vlastně pro sebe, rád nosím dámské.":
                    $ Event2 = 1
                    $ MisLove = MisLove + 5
                    mis "No, hi hi, to máme něco společného. A musím říct, že ti to i sedne."
                    me "Ano, v H&M nakoupíte módu, domácí vybavení, dětské oblečení a dekorativní kosmetiku. Nabízí kvalitu za nejlepší cenu a udržitelným způsobem. Toto reklamní sdělení není sponzorováno."
                    mis "No, když to říkáš. Nicméně, jsem ráda, že je tu další H&M vychutnávač. Jsme lepší než ti sojový normiči C&A fanoušci."
    mis "Tak, já už mám tedy vybráno."
    menu:
        "Fajn, uvidíme se tedy zítra, ahoj.":
            mis "Bylo to fajn, tak ahoj zítra."
            $ day = day + 1
            jump DenDecider
        "Můžu to za tebe zaplatit, jestli chceš.":
            $ MisLove = MisLove + 2
            mis "T-to bys udělal? M-moc díky, tohle ti nezapomenu."
            $ day = day + 1
            jump DenDecider

label FifiOut1:
    show fifi:
        zoom 1.25
        ypos 300
    fifi "co zas chceš? jít semnou ven? no dobře..."
    fifi "co chceš dělat?"
    menu:
        "Je mi ctí pozvat někoho jako jsi ty na zmrzlinu, včera jsem byl u epického zmrzlináře který dělal fakt dobrou zmrzlinu, myslím že byla veganská…":
            fifi "veganská zmrzlina? to je moje oblíbená! nedopustila bych kvůli mě nějaká kráva takhle trpěla "
        "No, lidi tvýho typu obvykle stejně nic nedělaj, takže… hele co to tam parkuje za dodávku?":
            fifi "Nevím, můžem se jít podívat."
    scene background10
    show fifi:
        zoom 1.25
        ypos 300
    with dissolve
    olda "Tak co to bude?"
    fifi "dali bychom si 2 veganské zmrzliny"
    olda "kdo za debila by si kupoval veganský zmrzliny však to je totální sračka…"
    fifi "COŽE?"
    menu:
        "tak hele, když se budete chovat takhle, moc toho neprodáte.":
            olda " ano slyšeli jste mě, veganskou zmrzlinu vám dávat nebudu, chutná jako zmražená mrdka"
        "No… má trochu recht.":
            olda " ano slyšeli jste mě, veganskou zmrzlinu vám dávat nebudu, chutná jako zmražená mrdka"
    menu:
        "OK, myslím, že bychom měli radši jít…":
            olda "Přesně, táhněte si po svým, vy odporní vegani! Tfuj"
            fifi "toto je nechutné, canclnu vás na hvízdu!"
            menu:
                "Já taky!":
                    scene background10
                    show fifi:
                        zoom 1.25
                        ypos 300
                "Co je sakra hvízd?":
                    scene background10
                    show fifi:
                        zoom 1.25
                        ypos 300
                    fifi "hned teď jdu napsat hvízd, vy se tady dlouho neudržíte, je mě z vás blbě"
                    olda "lmao drž hubu, mě je jedno nějakej hvízďák"
            menu:
                "Velká Fifinko, nech toho, jenom nás ztrapňuješ":
                    fifi "A ty? Ty odpreskni, takhle se zastávat toho vraha zvířat, co nemá veganskou zmrzlinu."
                "Doufám, že té tvojí kraksně někdo přestřihne brzdové hadičky!":
                    fifi "Přesně tak!"
                    scene background11
                    show fifi:
                        zoom 1.25
                        ypos 300
                    with dissolve
                    fifi "Tys mu to nandal!"
                    menu:
                        "Vždycky využiju šanci vyhrožovat kočkoholce. Nesnáším jejich druh, hnusí se mi.":
                            fifi "A já si myslela, že to děláš ve jménu veganství, a on je to zločin z nenávisti."
                            $ day = day + 1
                            jump DenDecider
                        "Nesnáším tyto neuznavače veganství.":
                            fifi "Cítím to stejně"
                            $ day = day + 1
                            jump DenDecider
        "Toto je absurdní, máme právo na tu zmrzlinu, toto je rasistické, vy urážíte menšiny!!!":
            olda "neptal jsem se + drž hubu retarde"
            menu:
                "To si odskáčeš! Kdyby tady nebyli lidi, tak už máš koule ve stroji na ledovou tříšť.":
                    olda "Ty šašku, nic na mě nezkoušej, ať už tě tu nevidím!"
                    scene background11
                    show fifi:
                        zoom 1.25
                        ypos 300
                    with dissolve
                    fifi "Páni, ty jsi mu to natřel!"
                    menu:
                        "Nenávidím kočkoholky, tfuj, takovej póvl.":
                            fifi "A já si myslela, že to děláš ve jménu veganství, a on je to zločin z nenávisti."
                            $ day = day + 1
                            jump DenDecider
                        "Nesnáším tyto neuznavače veganství.":
                            fifi "cítím to stejně"
                            $ day = day + 1
                            jump DenDecider
                "Bohužel, na to se nedá fakt nic smysluplného namítnout.":
                    olda "Byl jsi poroštěn, a teď, padejte."
                    scene background11
                    show fifi:
                        zoom 1.25
                        ypos 300
                    with dissolve
                    fifi "no mohl ses tam snažit víc."
                    menu:
                        "Příště si ho podám.":
                            scene background11
                            show fifi:
                                zoom 1.25
                                ypos 300
                            $ day = day + 1
                            jump DenDecider
                        "Je mi to líto, ale já prostě nedokážu být hnusnej na kočkoholky.":
                            scene background11
                            show fifi:
                                zoom 1.25
                                ypos 300
                            $ day = day + 1
                            jump DenDecider
label ZlevOut1:
    show lev:
        zoom 2
        ypos 300
    lev "Hele chlapáku, moje spižírna je tak nějak prázdná. Jestli v ní nechceš skončit svázanej tak ti doporučuju jít se mnou do alboše doplnit zásoby."
    menu:
        "Jako kdyby jsem měl na výběr…":
            lev "Tak trošku hejbni řití. Nechceš mě poznat hladového."
        "Taky si tam něco čapnu. Doplnit zásoby se vždycky hodí.":
            lev "Za svoje, {b}%(player_name)s {/b}. Já tam za tebe nebudu platit ani halíř."
            if HasMoney == 1:
                me "Jasňačka že mam peníze. Nečekám, že mi tady někdo bude utírat řiť, to je jasný."
                lev "Výborně. Vidim že začínáš chápat jak to tady chodí. "
                $ LevLove = LevLove + 1
            else:
                me "No peníze už nemam…"
                lev "A za co si myslíš že tam prodávaj? Za přídělový lístky?"
                $ LevLove = LevLove - 1
            lev "Pojďme tedy. Albert je tudy o tři ulice dál."
            scene background12:
                zoom 4
            show lev:
                zoom 2
                ypos 300
            with dissolve
            lev "Ty dveře jim blbnou už nějakou dobu. Za poslední půlrok rozdrtily dva lidi. Máš štěstí že to povolilo."
            lev "No nic, teďka k věci. Já si du koupit nějaký uzeniny, jestli se chceš dneska večer vrátit domu tak mi skoč pro balík minerálek, měly by bejt ve třetím regálu od prava."
            lev "Vem mi ty saguaro lesní plody."
            menu:
                "Už tam jdu":
                    lev "Si blbej? V albertě přece saguaro neprodávaj! Vyber tam nějakou podle sebe. A hni sebou!"
                "Saguaro? Myslim že sme ve špatný prodejně…":
                    lev "Heheh… jenom sem tě zkoušel, jestli dáváš pozor. Dojdi tam vybrat nějakou podle sebe."
                    me "dobrá, za chvíli sem u pokladen."
            hide lev
            show zagur
            with dissolve
            menu:
                "Ahoj, my jsme spolu ještě ve třídě nemluvili, jsem {b}%(player_name)s {/b}.":
                    zagur "OK, já jsem Zagur. Hele, dávej bacha, mám podezření, že jsou ve zdech."
                    menu:
                        "Uuuuh, dobrá, ehm, můžu se zeptat, kde tu najdu minerálky?":
                            zagur "jasný, je to hned tady, není zač."
                        "Kdo je ve zdech?":
                            zagur "Ve škole, něco… něco žije ve zdech."
                            menu:
                                "proč myslíš?":
                                    zagur "Slyším to, jak to tam chodí, NĚCO JE VE ZDECH! Sleduje nás."
                                    menu:
                                        "OK, OK, dobře, věřím ti, hlavně klid.":
                                            zagur "Jo mimochodem, minerálky jsou tady za rohem, slyšel jsem, jak se o tom se Zlvem bavíte. Není zač."
                                        "Už bych radši šel, nevíš, kde jsou tu minerálky?":
                                            zagur "Jasný, hned tady za rohem."
                                        "Dobře, ehm, nevíš kde jsou tady minerálky? Já jsem tu prvně.":
                                            zagur "Hned tady za rohem, není zač."
                "Zdravím, kudy se prosím dostanu k minerálkám?":
                    zagur "Bacha! Ta věc, co je ve zdech… určitě ovládá ty dveře tady… Na co že jsi se ptal?"
                    menu:
                        "Jaká věc ve zdech?":
                            zagur "Žije ve zdech, ve škole ve zdech, a manipuluje těma nebezpečnýma dvěřima tady."
                            menu:
                                "Díky za radu. Ještě bych ale poTřeboval vědět, kde tu mají minerálky.":
                                    zagur "Jasně, hned tady za rohem."
                                "Ehm, radši půjdu.":
                                    zagur "Dobře, slyšel jsem jak se bavíte s zlvem, k minerálkám tudy. Ale měj oči na šťopkách."
                        "Na minerálky.":
                            zagur "Zagur: Jistě, jsou hned tady."
            scene background13:
                zoom 4
            menu:
                "vzít poděbradku":
                    $ Mineralka = 1
                "vzít gemerku":
                    $ Mineralka = 2
            scene background12:
                zoom 4
            show lev:
                zoom 2
                ypos 300
            with dissolve
            me "Vidim že jdu právě v čas."
            lev "Ano, jdeš. Jenom nemůžu najít svojí peněženku…"
            menu:
                "Klidně ti to zaplatím":
                    if HasMoney == 0:
                        lev "Však jsi mi říkal že nemáš žádný peníze..."
                    else:
                        lev "Fakt? Díky, ale s timhle přístupem moc dlouho nevydržíš. Budu to brát jako dar :trolak:"
                        $LevLove = LevLove + 1
                "*nic nedělat a čekat až ji najde*":
                    $LevLove = LevLove + 0
            lev "tak jakou jsi vybral?"
            if Mineralka == 1:
                lev "Hm, česká Poděbradka… dobrá volba."
                $LevLove = LevLove + 2
            if Mineralka == 2:
                lev "Slovenská gemerka? Má vtipnej název, ale je ze Slovenska. Myslíš si že mi říkaj “ČESKÝ zlev” jen tak pro prdel?"
                $LevLove = LevLove - 2
            lev " No, každopádně sme tady hotovi. Myslim že můžeš bejt rád že se vrátíš po svých domu- jinak by tě tlačil někdo jinej na vozíku."
            $LevLove = LevLove + 1
            $ day = day + 1
            jump DenDecider
label DenDecider:
    if day == 2:
        jump den2
    elif day == 3:
        jump den3
