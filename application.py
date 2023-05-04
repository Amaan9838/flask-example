# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, url_for
import os
import requests
import json
from datetime import datetime
import requests
import youtube_dl
import random 
# creating a Flask app
application= Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.


@application.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@application.route('/home', methods = ['GET'])
def scrap_reels():
    a = {"csrftoken":"9zZx0NkkfikdC2VqOkXHR801Yl2U1Hkh","sessionid":"53168773914%3A1G2wzMulPT5S1n%3A5%3AAYdyF1aoB_O1O4VLYdXE1QAjZzEBg3_iEBi20XWwZH8"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"dv7osDMXDhLX2lTOsbPPnQ4gBNDPsG3O","sessionid":"58499749216%3AnDhC7Z4zEP6AWi%3A17%3AAYeZCANvuq3KMl40YjQNMB_GLZS5VkIKpGmVO_BqtQ"} #amsterdam34158 Amaan@123
    e =  {"csrftoken":"2LZbDPVRw8CVmREBbrvrYVbUPz6fFMCo","sessionid":"58522898773%3Apew23CUAfsoZlD%3A23%3AAYcu1Osx684xAtbepUEh5NMohJc1QEnqN6WlxZww_Q"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"l0vLN7prPz5KPq7RwBTGy8vAIOQByMfb","sessionid":"58522898773%3AN5wL7m53WTTjUl%3A19%3AAYck-3vKUlLv4XdVQRxxcy7ZcsBlmrtSaQnPeGwAEg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"nucq7KZdCY84HsYwva7OrQtwWtLTkZY2","sessionid":"58522898773%3AWlQxnrvSjEPtXY%3A15%3AAYcncTeucKLPJRMOTvZW7CbRSFLsLr4Moj90WPfvNg"} #farzi_kalosxyz  246800   
#a d
    c= [a]
    cookie_jar = random.choice(c)
    headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)'
         }
    csrf_token = cookie_jar['csrftoken']
    session_id = cookie_jar['sessionid']
     
    source = request.args['source'] 
    target = format(source)
    if target[:31] == "https://www.instagram.com/reel/" :
     cut_reel = target[31:42]

     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_reel}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
     meta = {
              "posts": user_id_req
           }      
    elif target[:28] == "https://www.instagram.com/p/":
     cut_post = target[28:39]
     
    
     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_post}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
     meta = {
        "posts": user_id_req,
        }
     
    elif target[:34] == "https://www.instagram.com/stories/" :
      cut_s = target[34:]
      separator = '/'

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = '/'

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }            
    elif target[:34] == "https://www.instagram.com/stories/" and target[-20:] == "?igshid=MDJmNzVkMjY=":
      cut_story = target[34:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }       
    elif target[:34] == "https://www.instagram.com/stories/" and target[-19:] == "?igshid=MDJmNzVkMjY":
      cut_story = target[34:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }     
    elif target[:30] == "https://instagram.com/stories/" and target[-19:] == "?igshid=MDJmNzVkMjY":
      cut_story = target[30:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }          
    elif  target[:30] == "https://instagram.com/stories/" and target[-31:] == "?utm_source=ig_story_item_share":
      cut_story = target[30:-51:] 
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
         user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
         uniqid = user_id['user']['id']
         user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
         meta = {
         "story": user_id_req,
         "uniqid":uniqid,
         "account": is_priv,
         
         } 
    elif  target[:30] == "https://instagram.com/stories/" and target[-32:] == "/?utm_source=ig_story_item_share":
      cut_story = target[30:-52:]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }
    elif target[:34] == "https://www.instagram.com/stories/" and target[-32:] == "/?utm_source=ig_story_item_share"  :
      cut_story = target[34:-52:]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }                   
    elif target[:34] == "https://www.instagram.com/stories/":
      cut_story = target[34:-21]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }
    elif target[:33] == "https://www.facebook.com/watch?v=" or target[:17] == "https://fb.watch/" or target[:24] == "https://www.facebook.com":
        ydl_opts = {}
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          info = ydl.extract_info(target, download=False)
        
        meta = {
            "ytdll": info,
        }
    else:
        cut = target[-11:]
        url = "https://youtube-video-download-info.p.rapidapi.com/dl"

        querystring = {"id": cut}

        headers = {
	"X-RapidAPI-Key": "6e7e0e613dmsh7da1932734a8a9ap14bcb6jsn4c51c4a9f466",
	"X-RapidAPI-Host": "youtube-video-download-info.p.rapidapi.com"
      }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
    if target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/":
       
       return (response)
        
    else:

       return jsonify(meta)
#http://127.0.0.1:5000/home?source=https://www.facebook.com/watch?v=1245895546280667
@application.route('/story', methods = ['GET'])
def reels():
    a = {"csrftoken":"9zZx0NkkfikdC2VqOkXHR801Yl2U1Hkh","sessionid":"53168773914%3A1G2wzMulPT5S1n%3A5%3AAYdyF1aoB_O1O4VLYdXE1QAjZzEBg3_iEBi20XWwZH8"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"dv7osDMXDhLX2lTOsbPPnQ4gBNDPsG3O","sessionid":"58499749216%3AnDhC7Z4zEP6AWi%3A17%3AAYeZCANvuq3KMl40YjQNMB_GLZS5VkIKpGmVO_BqtQ"} #amsterdam34158 Amaan@123
    e =  {"csrftoken":"2LZbDPVRw8CVmREBbrvrYVbUPz6fFMCo","sessionid":"58522898773%3Apew23CUAfsoZlD%3A23%3AAYcu1Osx684xAtbepUEh5NMohJc1QEnqN6WlxZww_Q"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"l0vLN7prPz5KPq7RwBTGy8vAIOQByMfb","sessionid":"58522898773%3AN5wL7m53WTTjUl%3A19%3AAYck-3vKUlLv4XdVQRxxcy7ZcsBlmrtSaQnPeGwAEg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"nucq7KZdCY84HsYwva7OrQtwWtLTkZY2","sessionid":"58522898773%3AWlQxnrvSjEPtXY%3A15%3AAYcncTeucKLPJRMOTvZW7CbRSFLsLr4Moj90WPfvNg"} #farzi_kalosxyz  246800   
#a d
    c= [a]
    cookie_jar = random.choice(c)
    headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)'
         }
    csrf_token = cookie_jar['csrftoken']
    session_id = cookie_jar['sessionid']
     
    source = request.args['source'] 
    target = format(source)
    if target[:34] == "https://www.instagram.com/stories/" :
      cut_s = target[34:]
      separator = '/'

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = '/'

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }    
    else:   
      cut_story= target
      
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
      "account": is_priv,
      }
      elif is_priv == False:
         user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
         uniqid = user_id['user']['id']
         user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar).json()
         meta = {
         "story": user_id_req,
         "uniqid":uniqid,
         "account": is_priv,
         }
    return jsonify(meta)
# driver function
if __name__ == '__main__':

	application.run(debug = True)