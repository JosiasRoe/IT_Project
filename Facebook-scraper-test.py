#Imports för scrapern
from facebook_scraper import get_posts 
from facebook_scraper import * #För user agent

import pickle
from pathlib import Path #För att sätta filväg




def store_data_pickel(sida, post_nummer):
    postname_pickle = str(sida) + str(post_nummer) + '.pkl' #genererar unikt filnamn med facebooksida och post nummret
    print(f"Denna post sparas under namnet: {postname_pickle}") #Endast för oss att kunna checka att det blivit rätt enklare
    file = Path(".") / "Pickle" / postname_pickle #Gör att filen hamnar i mappen "Pickle" (Så vi får bättre organisation)
    with open(file,'wb') as sidorpickle: 
        pickle.dump(post, sidorpickle)

def pull_data_pickel(sida, post_nummer): # Hämtar datan för en post genom argumenten: facebooksidan och tiden den postades
    postname_pickle = str(sida) + str(post_nummer) + '.pkl' #genererar unikt filnamn med facebooksida och tiden den postades
    file = Path(".") / "Pickle" / postname_pickle #sätter rätt filväg
    with open(file,'rb') as sidorpickle:
        post = pickle.load(sidorpickle)
    return post

def print_data(post): #printar datan från en post
    print()
    print(post['text'])
    print(post['post_text'])
    print(post['post_url']) 
    print(post['time'])
    print(post['link'])
    print()
    print()
    print()


#Två olika user agent, båda funkar, vet inte om en är bättre än den andra
#set_user_agent("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0")



sidor =	{ #Här skriver vi alla sidor vi ska scrapea
    #"IT-Klubbverk": "itklubbv",
    "Norrlands nation": "norrlands.nation",
    #"Södermanlands-Nerikes Nation":"snerikes",
}


for x in sidor: #En sida i taget
    #Så att vi ser vilken sida (att saker stämmer)
    print(f"\nVilken sida som scrapeas denna loopning: {x}")
    print(f"Namnet på facebooksidan: {sidor[x]} \n\n\n")

    n=1 #Har n nu temporärt, gör att vi bara printar 3 posts (enklare att läsa) (scrapear dock lika mycket så sparar inte tid)
    
    post_nummer = 1

    #for post in get_posts(sidor[x], pages=3, credentials=("lukasspam10@gmail.com","d%6D9J^ZqTbG&1op"), options={"allow_extra_requests": False, "posts_per_page": 200}): #En loopning = en post
    for post in get_posts(sidor[x], pages=3, credentials=("itprojekt.test123@gmail.com","kiwzod-kymdyz-qaVzy1"), options={"allow_extra_requests": False, "posts_per_page": 3}): #En loopning = en post
        #while n <= 3:
            print(f"Post: {n}")


            store_data_pickel(x, post_nummer) #Sparar datan med pickle
            
            
            print("Print av post data: \n")
            print_data(post)
            print()
            #print("Print av pickle data: \n")
            #print_data(pull_data_pickel(x, post_nummer)) #printar datan den nyss spara genom att unpicklea den dirket
            print()
            
            post_nummer += 1
            n += 1

            
