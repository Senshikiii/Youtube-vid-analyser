# we need this line cuz python automatically won't pick up the env variable??
from dotenv import load_dotenv
import os

load_dotenv()

# load_dotenv() reads the .env file and loads gemini api into the env, letting us to what we need to do

from google import genai
from google.genai import types


def analyze(transcript_text): # wrapped the boilerplate code in the function
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"""You are analyzing a YouTube video transcript.
        here it is:
        Transcript:
        {transcript_text}

        Return only a JSON object with exactly these fields:
        - "summary": 3-5 sentence summary  
        - "sentiment": one of "positive", "neutral", or "negative"
        - "sentiment_reason": one sentence explaining why

        Return only valid JSON. No markdown, no explanation, nothing else.: {transcript_text}""",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low"),
        ),
    )
    return(response.text)


if __name__ == "__main__":
    sample_text = """P62sLqal7w4 English (auto-generated) True
Airlines have been serving food for 100 years, but most airplane food 
is considered terrible by the general public. In this video, I'm testi
ng every level of airplane food, from oatmeal on a budget airline to c
aviar in the most luxurious airplane seat. All to answer the age-old q
uestion, what's the deal with airplane food? Are we all getting scamme
d? I'm starting with Spirit Airlines. I'm going to try their most noto
rious food item. This is a 2 and 1/2 hour flight from Texas to Florida
. I am on Spirit Airlines, who is notorious for making you pay for add
-ons, luggage, Wi-Fi, extra leg room, bringing your dog, and of course
, the one I'm here for, food. There is a meal that you can buy on Spir
it Airlines, and it is a $15 bundle with ramen noodles. That does soun
d expensive, but the question is, is it worth it? People online love b
uying food from Spirit Airlines. Check out this review. Don't buy anyt
hing. Don't ever do inflight purchase on Spirit. Anyways, I located th
e ramen noodles on the menu. But while I was reaching for my wallet, I
 heard the flight attendant say something unimaginable. >> No. Say it 
with me. No. The entire motivation of buying this plane ticket was to 
try the $15 ramen noodle bundle. But don't worry, I have something els
e up my sleeve. With the same $15, I was not only able to purchase a k
ids snack box, but also oatmeal. It's hot. It's hot oatmeal. It's been
 a while since I've eaten applesauce. I kind of feel like a freak eati
ng this in front of other people. Look at these little snacks. Oh, whe
re' they go? Just kidding. I ate them up like a hound dog. There's a f
unsized bag of candy, but that's what Joy Ride is for. Goatmeal is hot
, but it's a little more on the liquidy side. It's honestly a good dea
l because you're also getting hydrated in the process. Eventually, I j
ust ditched the spoon and chugged it. Say it with me. >> Like a hound 
dog. >> Thanks. Airplane meal number one complete. We successfully lan
ded, which means I really need to open this envelope. For context, my 
friend's sister Carol is a flight attendant. She deals with hundreds, 
if not thousands of passengers every week. Inside this envelope is a l
ist of acts of kindness that she challenged me to do for my flight att
endants in this video. And the first act of kindness is smile. Being k
ind goes a long way. Here goes nothing. >> Smile. Cheese. >> Cheese. T
hank you, Ellie. >> You're welcome. >> Thank you so much. >> All right
, you guys are the best. Bye bye. >> Have a good one. >> Have a good o
ne. >> I did the first one. I checked into a hotel that has a view of 
the airport and open the envelope for my next act of kindness. Write a
 thank you note on a postcard. Aw, that's sweet. The next morning, I f
ound a store in the airport, picked out the coolest postcard I could p
ossibly find, and boarded our next flight. It's Delta Airlines. I love
 this song. This song makes me want to dance. I just I love this song.
 Out of every meal I'm going to try in this video, I think I'm most ex
cited for this one. I remember when I saw the articles saying Delta wa
s adding a Shake Shack burger to their in-flight menu. I immediately l
ooked up the next Delta flight I could get on so I could try it. But t
hen I had a dentist appointment and I forgot about it until now. The r
eviews for this Airplane burger almost sound fake because I've never s
een customers this satisfied. Got the Shake Shack burger. I love the m
icrowaved bun look. Does it feel microwaved? Yes, because it is. They'
re convection ovens. Not that that changes much. Ooh, that's cool. I h
ad it on Wednesday. Pretty good. I'm literally about to eat it again i
n 3 hours. I can eat cheese. Wow, the beach looks so pretty. Look at t
hat. Look at the beach. We're still in Florida. While we wait for the 
flight attendant, who we're surprising with a postcard. I'll show you 
what else comes with my seat. Look at that leg room. For reference, I'
m really tall. We've got outlets, a TV screen with YouTubers on it. I 
was super excited until I realized my channel wasn't included. But I d
id find myself in a Mr. Beast video. That's me. There's a foldout tabl
e for eating Shake Shack burgers. The airplane bathroom also so fun. B
ut now it's time to place my order. Shake. Thank you. Thank you. Shake
 Shack. >> Shake Shack burger acquired. This meal looks so fun. You ge
t a burger, dark chocolate brownie, Shack sauce, veggies. I ain't usin
g those. And Shake Shack crinkle cut potato chips. The burger is preci
sely how I like my burgers. Meat and cheese only. It looks just like a
 Shake Shack burger. I guess it is. That convection oven is doing work
 back there. This burger is insane. I can't believe it. Oh my gosh. Th
at is a banger. I'm not just saying this. This is one of the better Sh
ake Shack burgers I've ever had. That doesn't make any sense. That doe
sn't make any sense whatsoever. I'm I'm on a plane. It's juicy. It's h
ot. I have grease on my face. It's so delicious. I just had to eat it 
up. Why didn't you say it? You didn't say it at home, did you? Guys, I
'm going to introduce you to my airplane buddy, >> Rajie. >> Rajie, yo
u got a healthier meal than I did. >> Yeah, I did. >> How was it? >> I
 thought it was pretty good. >> I have two questions. >> Yeah. >> Woul
d you like my burger veggies? >> No, right. Thanks. >> Next, I explain
ed to Rajie the acts of kindness and how Carol gave me ideas for fligh
t attendants. I wondered if you wanted to try one and you can do it on
 your next flight or Sure. Yeah. >> A little souvenir from the airport
 makes our day. So, do you think you could get a souvenir for a flight
 attendant? Uh, sure. Yeah. >> I finished my postcard for Ash, my flig
ht attendant, and we landed in New York, where my next flight takes of
f from. >> Hey, Ash. Here you go. Got you a little postcard. >> Thank 
you. That's very nice. Take care. Have a good one. >> All right. Anoth
er one complete. I walked through the airport, stopped at a Hudson, an
d found Joyide. I still can't believe that my candy is in real life st
ores. I ate the watermelon wedges, and now it's time to draw another a
ssignment. My next flight is boarding pretty soon, so let's get anothe
r assignment from Carol's Airplane Guide. A free stay at an all-inclus
ive resort wouldn't hurt. Okay, she's joking. Okay, let's try this aga
in. If you really want to make our day, bring us a small gift card. No
w, this I can do. This is so sweet. I love it. I thought finding a gif
t card in the airport would be easy. No gift cards. I literally walked
 around for an hour. None of the stores had a single gift card. Shake 
Shack doesn't have gift cards. No one is selling gift cards. No one ha
s gift cards in this airport. >> Where are the gift cards? >> I got de
sperate and texted Carol pictures of items in this store and asked, "W
ould any of this stuff suffice if I can't find gift cards?" And she re
sponded with profound wisdom. Ooh, chocolate. I do think Starbucks sel
ls them. Coffee gift cards are my fave. With that information, I bough
t chocolate. I bought coffee gift cards. And now I'm at my gate just b
efore boarding. I'm warning you right now. This next flight is interna
tional. International. I'm flying from New York to London, England, an
d it is a red eye. That means it's overnight. That means people are go
ing to be sleeping and the lights are going to be off most likely. Tha
t means I'm going to be whispering into this microphone and filming as
 discreetly as possible so as to not disturb other passengers. But the
y are going to be serving a complete dinner and most likely snacks, so
 I will have to be awake the entire time. Sure, maybe I'm going to wan
t to go night night, but I can't. >> Perfect. Right. >> All right. Tha
nk you. We made it. Time for the title screen song. If I want to enjoy
 my complimentary meal on this flight, I cannot fall asleep. Guys, I'm
 so sleepy because I'm jet-lagged. That's a funny joke because it's on
ly a 1-hour difference from New York's time zone, so the jet lag would
 be pretty much non-existent in this context. I'm awake now, and this 
is an economy seat on an international flight. You get a fancy pillow 
and blanket, a big screen for watching movies, a remote that controls 
something. I'm not sure what this button does. H, who knows? Probably 
doesn't matter. And most importantly, an entire hot dinner. Look at th
is bounty. My fellow passenger saw me struggling to film myself, so sh
e helped me get this clip. I was offered chicken or pasta, and I opted
 for the chicken. It comes with salad, packaged bread, crackers. Sorry
 about the turbulence. It's kind of intense right now. Dessert, butter
, Swiss cheese, and iced water. How am I even going to eat all of this
? The food is actually all delicious. The chicken is yummy. This is my
 first time eating couscous, and surprisingly, as a picky eater, I lov
e it. The bread roll and crackers and brownie were scrumptious. And af
ter the flight attendant picked up my plate, I vowed to not fall aslee
p again. I fell asleep for like 4 hours. Oh my goodness, it's bright o
utside now. We are almost to London. My only fear is that I missed som
e complimentary food while I was sleeping. And by the looks of my neig
hbor's tray table, that's exactly what happened. I felt happy again wh
en the flight attendant offered me black coffee. Yeah, no sugar, just 
straight up black coffee. And finally, I built up the courage to go to
 the back of the plane and surprise the flight attendants with the gif
ts. Y'all, I found some flight attendants. Hey, I'm here with >> Micha
el and Kyle. Kyle served me and my middle name is Michael. >> Oh, ther
e we go. >> Yeah, we've got some connections. What is the nicest thing
 a passenger has ever done for you? >> Chocolates or like um actually 
like little baggies that have like chapstick and um like gift cards. Y
eah, like Starbucks gift cards. I'm not topping any of that. But I did
 bring you guys gifts. Okay. >> Chocolate. >> Thank you, >> Kyle. You 
get chocolate. >> Oh my goodness. >> And you read my mind. I got Starb
ucks gift card. >> Starbucks gift card. And for those off camera, too.
 I only have one more. You guys are amazing. Thank you for what you do
. I had a great time. >> Thank you. >> Thank you guys. That was so who
lesome. Back in my seat. I used the remote to land the plane. And now 
we are at London Heathrow Airport. I checked into Aotel. There are a f
ew things in this life that make me happier than a tiny hotel room ins
ide of an airport. I immediately went back to sleep, woke up, played s
ome Minecraft. Be sure to subscribe to my secret Minecraft channel, an
d I will turn you into a chicken in my world, and now I'm just here in
 my room. My next flight leaves in many hours from now. I'm having so 
much fun doing nice things for flight attendants. Carol, I hope you're
 proud of me. Let's see what we get next. One time, a lady gave me a $
20 tip, and it made me cry. Aw, I'm going to do that. I left my airpor
t hotel room on a mission. I immediately located an ATM where I withdr
ew 20 British pounds. Okay, honestly, I spent it on some British snack
s. Sorry. They were really good, though. I did go back to the ATM and 
withdraw another 20 British pounds. Now, we're boarding our next fligh
t. It's time to dance to the title screen song. You don't have to be d
ancing right now, but you could be. It's going to be a long flight. It
's about two and a half million light years going to the Andromeda gal
axy. On top of offering a full menu, this particular flight has three 
really cool features. Number one, the loft. That's what they call it. 
It's like a lounge where you can socialize and hang out. I will most d
efinitely be socializing if anyone is interested. Number two, tea time
. I have a theory that everything sounds more fun if you just put time
 after it. Snack time, jammy time, in this case, tea time. The list go
es on. If someone offers to serve me tea and calls it tea time, I'm gi
ving them the $20 tip. Shoot, they can take my whole wallet. Actually,
 no. I'm not comfortable with that. And lastly, the final feature of t
his flight experience, guy handing out candy. Who could that be? Who's
 who's doing that? I wanted to hear my flight attendant's perspective 
on the list that Carol made of the acts of kindness. >> Smile and bein
g kind goes a long way. Very true. Always very true. >> He seemed to h
ave a lot of fun reading through this list. Yeah, it is a good list. >
> Yeah, I think your friend Carol is 100% right. >> He is so fun. In o
ther news, this seat is awesome. The seat tour begins. This seat comes
 with all kinds of useful items, but I think I'm most excited for the 
socks. I put them on right away. It's actually really nice cuz my othe
r ones were pretty sweaty. I'm not putting that in. The TV screen does
 this. The foldout table does that. You get a comfy pillow and a night
n night sack. And now the food has begun arriving. We're starting off 
with coffee and barbecue chips, which may not seem that special, but w
hen you have a view like this, I didn't realize I was recording myself
. >> I can interest you in any bread. I'll do white. White. There you 
go. Thank you. You're welcome. >> Oh, we're already cooking. Your boy 
goes wild for a good bread stick. For the appetizer, we have spicy pra
wn. I'm a little bit worried about the spicy, but I will say that this
 year I've been eating more buffalo wings, chicken wings. That's a lit
tle spicy. That's a little spicy there. At least we got some watermelo
n to cool things off. Oh, no. That's spicy, too. That's also spicy. Da
ng, that was good. Come on, here's your chance. Okay, just when I had 
finished my spicy meal, I was brought more food. Salmon and vegetables
. It is so good. I even ate some veggies. I don't even know what veget
able this is. Does anyone know? Next was dessert, which brought out my
 inner food critic. It's cold. It's creamy. It's cinnamon. It's chocol
ate. I have only been on this plane for 1 hour, and there is so much m
ore to do. My game plan begins in the bathroom. I'm in the bathroom. T
his bathroom has a window. My intention is to freshen up a little bit 
before I go to the loft. If I'm going to be socializing, I'm going to 
need to be on my best behavior in terms of hygiene. And I should proba
bly put on some shoes. I'm going to wash my hands, put on some body lo
tion, and then we're lofting. We're We're going to the loft. At this p
oint, I'm feeling nervous about going to the loft because I'm not sure
 if I'll be able to make friends at the loft. I've never been to a lof
t. I don't know. But all of those nerves faded when I arrived. Y'all, 
the loft is incredible. This guy handed out a bunch of free candy. And
 these gentlemen, I probably talked to them for 2 hours straight. I th
ink they know more about my life than my own cousins. I don't really k
now my cousins that well. This man is so cool. He was showing us scuba
 diving videos. He does scuba diving. I did not want the loft experien
ce to end, but it did. I'm back in my seat now. But do you remember wh
en I showed you that video of the guy walking around handing out littl
e bags of candy? What if I told you it was me? That's right. If you lo
ok closely in the video, you will notice fun-sized bags of Joyide. You
 guys have been asking for it forever, and we finally have party packs
. We have many flavors of party packs. Actually, these are the ones I 
packed with me on the plane. But imagine having a fun-sized bag of Joy
ide in the spirit snack box or with the Shake Shack burger or instead 
of couscous. You get the point. Joyide party pack makes every occasion
 a party. If you bring this to school or work, you just became Mr. Pop
ular. My dream is to make Joyide the number one candy in America witho
ut fake colors, without junk ingredients, and up to 80% less sugar. If
 you want to join the mission, be sure to take a picture with your Joy
ide and tag your state just like this because we want to see which US 
state makes Joyide their number one candy first. I'm calling it the 50
 states challenge. It's got a ring to it. You can find Joyide in these
 stores. And on April 18th, party packs will be available at Target na
tionwide. Thank you guys so much for supporting my dream. I love seein
g Joyide runners on Instagram every day. I am now going to relax and e
at tiny bags of candy while I wait for tea time. I am waiting for tea 
time to begin. I'm so sleepy. I I can't even keep my eyes open. I'm so
 sleepy. I just I just can't wait to drink some tea. I'm trying my bes
t to stay awake. I don't want to miss another meal like I did on the l
ast flight. >> Okay, here we go. Your engines folks time. You chucked 
all your butts up in the river for one time many years ago. There you 
go. All right, >> afternoon tea has arrived. I do think this is one of
 the more British things I've participated in in my life. That's good.
 The food never ends on this plane. My goodness. Look at this angle. I
t was a cool angle while it lasted. I I knew it was risky going into i
t. And that's sometimes the price you pay for an angle like that. I me
an, look at that angle. This is the first flight I don't want to end. 
This is so fun. I'm going to enjoy the rest of my afternoon tea now wi
th a little bit less cool of an angle. What am I doing here? I'm going
 to get you a new one. I'm not going to do this again. That is so >> I
 was sort of just aggressively dipping the bread into the jam. And tha
t's not right. >> What you will do bottom and the top prize it open. S
o you got two halves. Cream on the bottom of both hearts. Doll pajam o
n both halves. >> All right, let's see if I can redeem tea time. >> I 
thought you would have gone top and bottom, but it's okay. Side by sid
e. I was supposed to slice it the other way. Tea time was everything I
 could have dreamed of and more. I still have these $20 in my pocket. 
And now that we've arrived, I think I know exactly who I'm giving it t
o. >> Thank you guys. I have a trip for you. Sweets and the 20s. Smile
. That was so fun. Emirates Lounge. That's right. Next, we're flying o
n arguably the best airline in the world, which means my final act of 
kindness needs to be spectacular. I don't want to show you the final c
ard I selected, so it's a surprise for you, too. Before boarding our p
lane, I have to take advantage of this delicious food from the Emirate
s Lounge. This is exquisite. But alas, it's time for our final flight 
and the final boss of airplane food. Guys, this seat is crazy. Right w
hen I got seated, I was immediately brought a cappuccino, some other b
everage, a selection of dates. I knew this was going to be awesome bec
ause I've had the privilege of flying Emirates one other time for a vi
deo and it was unreal. But this aircraft I'm on right now is actually 
different from that one. It's a completely different plane. This one h
as a spa on board with a shower in it. I reserved it for 3 hours from 
now. I don't even know what I'm going to do in there. There is also a 
lounge with a bar and flight attendants that serve you beverages. And 
the craziest part is that this first class flight menu is on demand. I
 guess you just order whatever you want. chicken, chocolate cake, popc
orn, caviar. You can just order that is. Anyways, before I experience 
all of that, seat tour. There are almost too many snacks being offered
 to me right now. And on the topic of leg room, this seat is really ju
st room. To my right is a mini fridge stocked with every beverage you 
can imagine. There's a blanket. There's a mattress. A big screen to co
ntrol your bigger screen. Headphones for listening to things. Cologne.
 I sprayed it in my face. Don't do that. I also nearly spilled sparkli
ng water everywhere. It's not going great. There's also a pullout tabl
e for what else but airplane food. Um, yeah. The first meal has arrive
d. I decided to order the seared beef fillet as well as the caviar. I 
also got some breads and I guess those are pickles. I don't know. We'v
e come a long way from the snack box. I don't even know. How do you ea
t this? Wow. Caviar on an airplane. Some consider caviar a delicacy. W
here I'm from, we consider it a gamble. Seafood is questionable where 
I'm from. This beef though, nothing questionable about this beef. It's
 good. This entire meal is great. I found myself going back to the cav
iar and going like this with my hands as if I have any capacity to app
reciate fine dining. Even the water tastes cleaner than normal. This d
ining experience built up my courage to actually try the cucumber thin
g. and it was surprisingly really good. But now it's time to explore t
he back of the plane where the social lounge is located. I found the s
ocial lounge. That's Margarita right there. Margarita, I have a questi
on. >> Yes. >> What are the odds you let me make a drink? >> Come agai
n. >> I was I was curious if I could make a drink behind the counter. 
>> Yes. Yes, of course you can. Okay. >> This is where Margarita stopp
ed recording the video. I handed her the phone while it was already re
cording, so she clicked the record button, which actually stopped the 
video. Here's some audio from the experience. What's up, guys? Margari
ta, let me get behind the bar. I'm making myself a Shirley Temple. You
're just going to want to grab a beverage such as Seven Up. Check this
 out. Cheers. Bless her heart. She has no idea. After the experience, 
she clicked the button, which actually made her start recording again,
 but that's okay. Now it's time to socialize in the social lounge. We 
love socializing. Emotionally, I feel like I just had a birthday party
. The flight is only halfway complete. I am simply going to order popc
orn and lay down flat on the mattress and watch a movie. Keep the food
 coming, Abra. That's the name of my flight attendant. I took the time
 to transform my seat into the ultimate movie experience so I can enjo
y a movie called Knives Out. I ordered popcorn and now I'm watching th
e movie. You probably wouldn't guess this about me, but I love a good 
mystery. The best part to me is you have no idea what's going to happe
n next. I'm in the spa. This is where the spa is. It's located right b
y my seat. My plan was just to brush my teeth, but look at this room. 
Is this all for me? Is this the toilet? Oh my gosh, it is. Look at the
 shower. I have to take a shower, right? Oh my goodness. Ow. I'm stand
ing in a shower on a plane. I don't know if there's like a time limit 
that I'm allowed to be in here. I'm just going to shower. Brush my tee
th. I don't know. Pushing random buttons. This one turns on the shower
. I took a hot shower 35,000 ft in the air. Brushed my teeth. And when
 I arrived back to my seat, there was more food. The party never ends.
 I told my flight attendant, Abra, that I wanted to order dessert by t
elling her a joke. Here it is. >> Uh, what do you call a dessert that 
no one can remember the name of a >> Oh, no. Like, I forgot. I actuall
y thought of it myself. Someone probably thought of it before me, but 
>> it's a good one. All right. I would love an avocado, actually. >> J
ust like that, I got an avocado. It's a sort of coffee ice cream. I me
an, it's delicious. Out of nowhere, Margarita offered to take a Polaro
id photo of me. Of course, I said yes. I think it turned out pretty go
od. When Carol challenged me to do all these, I honestly thought it wo
uld be really easy. One of the acts of kindness is to pay attention to
 announcements. I'm actually guilty of not doing that all the time, bu
t I do wipe the sink counter after using the bathroom. As a matter of 
fact, I did that off camera on Spirit. I didn't even get a clip of tha
t. Seemed weird to record. So, honestly, it has been easy, but only be
cause I'm consciously doing a challenge. The problem in real life is y
ou have to really fight to be considerate of others. And in such a str
essful environment like an airport, that almost feels impossible. Real
ly, I have never done most of these things. I've never even thought ab
out doing them. And because of that, I feel like I've learned a lot fr
om this trip. So, before I reveal what the final act of kindness is, t
he one I drew back in the lounge, I just got to say, whether you are a
t work or school or the grocery store or thousands of feet in the air 
in a metal tube, if we all truly try to consider others more important"""

print(analyze(sample_text))


