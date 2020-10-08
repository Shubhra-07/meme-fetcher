import praw
import random
import requests
import os

#fill these when you make your own instace

reddit = praw.Reddit(client_id="",
                    client_secret="",
                    user_agent="",
                    username="")



# you can add more sub-reddit just like below mentioned

cloud = {'animememes': [], 
         
         'memes': []
        
         }


n = random.randint(1,20)
star = []

#debug
def check(e, file):
  if e not in list(cloud[file]):
    print('adding:',e)
    cloud[file].append(e)
    return e
  
  
  else:
    print(f'---{e}---')
    e = random.randint(1,19)
    print('newpick:', e)
    return check(e, file)
  
  

   #adding download 





a = input('how many:')
for i in range (int(a)):
  n = random.randint(1,19 )#int(input('post:'))
  web = random.choice( list (cloud.keys() ) )#input('subreddit:')
  sub = reddit.subreddit( web )    
  meme = sub.hot(limit = 20)   
  
  post = list(meme) 
  # check the memes repitation in each subreddi dictionary.
  
  
  
  #change that to n
  test = check(4, web)
  print("updating cloud", cloud)
  print("title:", post[test].title)
  print('memeurl:',post[test].url)
  print("sub:",sub)
  print('obj:', (post[test]))
  
  #saving the image inside lol folder
  img_data = requests.get(post[test].url).content
  directory = f"{os.getcwd()}"+ "/here/"

  if not os.path.exists(directory):
   os.makedirs(directory)




  with open(os.getcwd()+'/here/'+ post[test].title, 'wb') as book:
  	book.write(img_data)

  print('------------------')



