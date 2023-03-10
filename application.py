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
    a = {"csrftoken":"ZAyaenm8ZGR4BNKeiNfosZlnsyheSBrA","sessionid":"58589135759%3AqHibKdAiXk37I7%3A12%3AAYffm45O5HuhedO9NYvDuBNCqh1731OsNwo7W0hMaQ"}
    b = {"csrftoken":"pvjN4tqBR76yNCFrpoud0pwoSltuQHXZ","sessionid":"58453106739%3Amyt8OfUzD6GfAY%3A8%3AAYeZ3ahhLJY3qmcD6ycFZiSUtfKg5HFQYimhD-waXg"} 
    c= [a,b]
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
    elif target[:30] == "https://instagram.com/stories/" or target[-20:] == "?igshid=MDJmNzVkMjY=":
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
    elif target[:33] == "https://www.facebook.com/watch?v=" or target[:17] == "https://fb.watch/":
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

# driver function
if __name__ == '__main__':

	application.run(debug = True)
