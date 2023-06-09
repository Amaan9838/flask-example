# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, url_for
import os
import requests
import Updated_Api as up
import json
from datetime import datetime
import requests
import youtube_dl
import random 
from pytube import YouTube

# creating a Flask app
application= Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.


@application.route("/", methods = ["GET", "POST"])
def home():
	if(request.method == "GET"):

		data = "hello world"
		return jsonify({"data": data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@application.route("/home", methods = ["GET"])
def scrap_reels():
   #  http_1 = "185.199.228.220:7300:xlqlutuh:g64kgmh8afoh"
   #  ht2 = "185.199.229.156:7492:xlqlutuh:g64kgmh8afoh"
   # #  ht3 = "185.199.231.45:8382:xlqlutuh:g64kgmh8afoh"
   # #  ht4 = "188.74.210.207:6286:xlqlutuh:g64kgmh8afoh"
   # #  ht5 = "188.74.183.10:8279:xlqlutuh:g64kgmh8afoh"
   # #  ht6 = "188.74.210.21:6100:xlqlutuh:g64kgmh8afoh"
   # #  ht7 = "45.155.68.129:8133:xlqlutuh:g64kgmh8afoh"
   # #  ht8 = "154.95.36.199:6893:xlqlutuh:g64kgmh8afoh"
   # #  ht9 = "45.94.47.66:8110:xlqlutuh:g64kgmh8afoh"
   #  inp = open("proxy_list.txt", "r")
   #  lines=inp.read().split("\n")
    
   #  http_proxy = random.choice(lines)
   # #  http_proxy = "154.95.36.199:6893:xlqlutuh:g64kgmh8afoh"
    
   #  url = "https://ipv4.icanhazip.com"

   #  proxyDict = {
   #    "http": http_proxy,  
   #  }
    proxies = (  
    "http://xlqlutuh:g64kgmh8afoh@185.199.229.156:7492",
    "http://xlqlutuh:g64kgmh8afoh@185.199.228.220:7300",
    "http://xlqlutuh:g64kgmh8afoh@185.199.231.45:8382",
    "http://xlqlutuh:g64kgmh8afoh@188.74.210.207:6286",
    "http://xlqlutuh:g64kgmh8afoh@188.74.183.10:8279",
    "http://xlqlutuh:g64kgmh8afoh@188.74.210.21:6100",
    "http://xlqlutuh:g64kgmh8afoh@45.155.68.129:8133",
    "http://xlqlutuh:g64kgmh8afoh@154.95.36.199:6893",
    "http://xlqlutuh:g64kgmh8afoh@45.94.47.66:8110"

    )
# length = len(proxies)
# n = length * 2 
# for i in range(n):
#     index = i % length
    pr_oxy = [0,1,2,3,4,5,6,7,8]
    index = random.choice(pr_oxy)
   #  print(index)
    proxyDict = {"http" : proxies[index], "https" : proxies[index]}
    a = {"csrftoken":"JIzYAn9hVRjoDdNIQnLsqFCoVouO1WMC","sessionid":"53168773914%3AD0YRVq8KvrDZCf%3A15%3AAYeyRlmOZf2XHeCEuLrRfccq-JNAPqUO9PMiBSRIsA"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"dv7osDMXDhLX2lTOsbPPnQ4gBNDPsG3O","sessionid":"58499749216%3AnDhC7Z4zEP6AWi%3A17%3AAYeZCANvuq3KMl40YjQNMB_GLZS5VkIKpGmVO_BqtQ"} #amsterdam34158 Amaan@123
    e =  {"csrftoken":"A6ledrZ83DJGCvmDYfF3vTIHQG1LOaCJ","sessionid":"53168773914%3Aafljno0aL18bpZ%3A23%3AAYcQfhhvaU7HHcy3YwKtp0x5bUbznwbsyqeKNMtYvw"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"yG0qeT6AdwIO2gUFLGSjvtYFYxhwA8eO","sessionid":"53168773914%3AiTndpEqqT0utPz%3A26%3AAYfZvE4oVH6l2zLFObt5svVqXXKFFJoAVk0uZ0pFjg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"0KDtcmLuS6S5piO0dJkTLZd5J8SAb8o3","sessionid":"53168773914%3Ag8rfaOhrydC3XF%3A3%3AAYc2B6nN_8PwOUgla2ZxAwGyYhnLXypui8fyQtXpbQ"} #farzi_kalosxyz  246800   
#a d
    c= [a,e,f,g]
    cookie_jar = random.choice(c)
    headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)",

         }
    csrf_token = cookie_jar["csrftoken"]
    session_id = cookie_jar["sessionid"]
     
    source = request.args["source"] 
    target = format(source)
    if target[:31] == "https://www.instagram.com/reel/" :
     cut_reel = target[31:42]

     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_reel}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
     meta = {
              "posts": user_id_req,
              "cookie_jar":cookie_jar,
              "ip": proxyDict
           }      
    elif target[:28] == "https://www.instagram.com/p/":
     cut_post = target[28:39]

     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_post}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
     meta = {
        "posts": user_id_req,
        }
     
    elif target[:34] == "https://www.instagram.com/stories/" :
      cut_s = target[34:]
      separator = "/"

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      uniqid = user_id["graphql"]["user"]["id"] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       #user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      # uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = "/"

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      uniqid = user_id["graphql"]["user"]["id"] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
      # user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      # uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }            
    elif target[:34] == "https://www.instagram.com/stories/" and target[-20:] == "?igshid=MDJmNzVkMjY=":
      cut_story = target[34:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
       uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }       
    elif target[:34] == "https://www.instagram.com/stories/" and target[-19:] == "?igshid=MDJmNzVkMjY":
      cut_story = target[34:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
       uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }     
    elif target[:30] == "https://instagram.com/stories/" and target[-19:] == "?igshid=MDJmNzVkMjY":
      cut_story = target[30:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
       uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }          
    elif  target[:30] == "https://instagram.com/stories/" and target[-31:] == "?utm_source=ig_story_item_share":
      cut_story = target[30:-51:] 
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
         user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
         uniqid = user_id["user"]["id"]
         user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
         meta = {
         "story": user_id_req,
         "uniqid":uniqid,
         "account": is_priv,
         
         } 
    elif  target[:30] == "https://instagram.com/stories/" and target[-32:] == "/?utm_source=ig_story_item_share":
      cut_story = target[30:-52:]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
       uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }
    elif target[:34] == "https://www.instagram.com/stories/" and target[-32:] == "/?utm_source=ig_story_item_share"  :
      cut_story = target[34:-52:]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
       uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }                   
    elif target[:34] == "https://www.instagram.com/stories/":
      cut_story = target[34:-21]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
       uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
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
      #  url = up.youtube(target)

      #  response = {
      #    'data': url,
      # }
    if target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/":
       
       return (response)
        
    else:

       return jsonify(meta)
#http://127.0.0.1:5000/home?source=https://www.facebook.com/watch?v=1245895546280667
@application.route("/story", methods = ["GET"])
def reels():
    a = {"csrftoken":"JIzYAn9hVRjoDdNIQnLsqFCoVouO1WMC","sessionid":"53168773914%3AD0YRVq8KvrDZCf%3A15%3AAYeyRlmOZf2XHeCEuLrRfccq-JNAPqUO9PMiBSRIsA"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"dv7osDMXDhLX2lTOsbPPnQ4gBNDPsG3O","sessionid":"58499749216%3AnDhC7Z4zEP6AWi%3A17%3AAYeZCANvuq3KMl40YjQNMB_GLZS5VkIKpGmVO_BqtQ"} #amsterdam34158 Amaan@123
    e =  {"csrftoken":"A6ledrZ83DJGCvmDYfF3vTIHQG1LOaCJ","sessionid":"53168773914%3Aafljno0aL18bpZ%3A23%3AAYcQfhhvaU7HHcy3YwKtp0x5bUbznwbsyqeKNMtYvw"}   #farzi_kalosxyz 246800
    f =  {"csrftoken":"yG0qeT6AdwIO2gUFLGSjvtYFYxhwA8eO","sessionid":"53168773914%3AiTndpEqqT0utPz%3A26%3AAYfZvE4oVH6l2zLFObt5svVqXXKFFJoAVk0uZ0pFjg"} #farzi_kalosxyz  246800   
    g =  {"csrftoken":"0KDtcmLuS6S5piO0dJkTLZd5J8SAb8o3","sessionid":"53168773914%3Ag8rfaOhrydC3XF%3A3%3AAYc2B6nN_8PwOUgla2ZxAwGyYhnLXypui8fyQtXpbQ"} #farzi_kalosxyz  246800   
#a d
    proxies = (  
    "http://xlqlutuh:g64kgmh8afoh@185.199.229.156:7492",
    "http://xlqlutuh:g64kgmh8afoh@185.199.228.220:7300",
    "http://xlqlutuh:g64kgmh8afoh@185.199.231.45:8382",
    "http://xlqlutuh:g64kgmh8afoh@188.74.210.207:6286",
    "http://xlqlutuh:g64kgmh8afoh@188.74.183.10:8279",
    "http://xlqlutuh:g64kgmh8afoh@188.74.210.21:6100",
    "http://xlqlutuh:g64kgmh8afoh@45.155.68.129:8133",
    "http://xlqlutuh:g64kgmh8afoh@154.95.36.199:6893",
    "http://xlqlutuh:g64kgmh8afoh@45.94.47.66:8110"

    )
    pr_oxy = [0,1,2,3,4,5,6,7,8]
    index = random.choice(pr_oxy)
    proxyDict = {"http" : proxies[index], "https" : proxies[index]}
    c= [a,e,f,g]
    cookie_jar = random.choice(c)
    headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)"
         }
    csrf_token = cookie_jar["csrftoken"]
    session_id = cookie_jar["sessionid"]
     
    source = request.args["source"] 
    target = format(source)
    if target[:34] == "https://www.instagram.com/stories/" :
      cut_s = target[34:]
      separator = "/"

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      uniqid = user_id["graphql"]["user"]["id"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       #user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
       
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = "/"

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      is_priv = user_id["graphql"]["user"]["is_private"]
      uniqid = user_id["graphql"]["user"]["id"]
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       #user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       #uniqid = user_id["user"]["id"]
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }    
    elif target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/":
         # url = "https://www.youtube.com/watch?v=11OWuPcElJw"   
         # age restricted
         # url = "https://www.youtube.com/watch?v=OQPYLFUKnVc"
         # video = YouTube(url,use_oauth=True, allow_oauth_cache=False)
      cut = target[-11:]
      url = "https://www.youtube.com/watch?v="+cut
      video = YouTube(url)


        # streams1 = video.streams.all()
        # duration = video.length
      title = video.title
            # print(streams1)

            # print(title)

      streams_720p = video.streams.filter(progressive=True,res="720p",audio_codec="mp4a.40.2").first().url
      streams_720p_download = video.streams.filter(progressive=True,res="720p",audio_codec="mp4a.40.2").first()

      streams_360p = video.streams.filter(progressive=True,res="360p",audio_codec="mp4a.40.2").first().url
      streams_144p = video.streams.filter(progressive=True,res="144p",audio_codec="mp4a.40.2").first().url

      streams_2160p_mp4 = video.streams.filter(progressive=False,res="2160p")
      streams_1440p_mp4 = video.streams.filter(progressive=False,res="1440p")
      streams_1080p_mp4 = video.streams.filter(progressive=False,res="1080p",mime_type="video/mp4")
      streams_720p_mp4 = video.streams.filter(adaptive=True,res="720p",mime_type="video/mp4")
      streams_480p_mp4 = video.streams.filter(progressive=False,res="480p",mime_type="video/mp4").first()
      streams_360p_mp4 = video.streams.filter(adaptive=True,res="360p",mime_type="video/mp4").first()
      streams_240p_mp4 = video.streams.filter(progressive=False,res="240p",mime_type="video/mp4").first()
      streams_144p_mp4 = video.streams.filter(progressive=False,res="144p",mime_type="video/mp4").first()
      streams_audio = video.streams.filter(progressive=False,mime_type="audio/mp4")


        # print(streams_audio.first().url)

        # print(streams_2160p_mp4.first())
      # streams_720p_download.download(filename="test_vid4.mp4")
        # print(streams_1440p_mp4)
        # print(streams_1080p_mp4)

        # preffered_resolution = ["144p", "240p", "360p", "480p", "720p", "1080p","1440p","2160p"]
        # for resolution in preffered_resolution: 
        #     video_adaptive_streams = video.streams.filter(progressive=False, res=resolution)
        #     print(video_adaptive_streams)
      if len(streams_2160p_mp4) > 0 :
            meta = {
                "adaptive_formats_mp4":{ 
                    "0":{
                        "quality": "2160p",
                        "mime_type": "video/mp4",
                        "url": streams_2160p_mp4.first().url,       
                  }, 
                    "1":{
                        "quality": "1440p",
                        "mime_type": "video/mp4",
                        "url": streams_1440p_mp4.first().url,       
                  },
                    "2":{
                        "quality": "1080p",
                        "mime_type": "video/mp4",
                        "url": streams_1080p_mp4.first().url,       
                  },
                     "3":{
                        "quality": "720p",
                        "mime_type": "video/mp4",
                        "url": streams_720p_mp4.first().url,  
                  },
                    "4":{
                        "quality": "480p",
                        "mime_type": "video/mp4",
                        "url": streams_480p_mp4.url,
                  },
                    "5":{
                        "quality": "360p",
                        "mime_type": "video/mp4",
                        "url": streams_360p_mp4.url,
                  },
                    "6":{
                        "quality": "240p",
                        "mime_type": "video/mp4",
                        "url": streams_240p_mp4.url,
                  },
                    "7":{
                        "quality": "144p",
                        "mime_type": "video/mp4",
                        "url": streams_144p_mp4.url,
                  },
                },
                  "formats":{
                     "22":{
                        "quality": "720p",
                        "mime_type": "video/mp4",
                        "url": streams_720p,     
                  },
                     "18":{
                        "quality": "360p",
                        "mime_type": "video/mp4",
                        "url": streams_360p,        
                  },
                     "17":{
                        "quality": "144p",
                        "mime_type": "video/mp4",
                        "url": streams_144p,     
                  },
            },
                     "title": title,
                }
            return (meta)
                

      elif len(streams_1080p_mp4) > 0 :
            meta = {
                "adaptive_formats_mp4":{  
                    "0":{
                        "quality": "1080p",
                        "mime_type": "video/mp4",
                        "url": streams_1080p_mp4.first().url,       
                  },
                     "1":{
                        "quality": "720p",
                        "mime_type": "video/mp4",
                        "url": streams_720p_mp4.first().url,  
                  },
                     "2":{
                        "quality": "480p",
                        "mime_type": "video/mp4",
                        "url": streams_480p_mp4.url,
                  },
                     "3":{
                        "quality": "360p",
                        "mime_type": "video/mp4",
                        "url": streams_360p_mp4.url,
                  },
                     "4":{
                        "quality": "240p",
                        "mime_type": "video/mp4",
                        "url": streams_240p_mp4.url,
                  },
                     "5":{
                        "quality": "144p",
                        "mime_type": "video/mp4",
                        "url": streams_144p_mp4.url,
                  },
                },
                  "formats":{
                     "22":{
                        "quality": "720p",
                        "mime_type": "video/mp4",
                        "url": streams_720p,     
                  },
                     "18":{
                        "quality": "360p",
                        "mime_type": "video/mp4",
                        "url": streams_360p,        
                  },
                     "17":{
                        "quality": "144p",
                        "mime_type": "video/mp4",
                        "url": streams_144p,     
                  },
               },
                     "title": title,
                }
            return (meta)
                

      elif  len(streams_720p_mp4) > 0:
            meta = {
            "adaptive_formats_mp4":{  
                  "0":{
                    "quality": "720p",
                    "mime_type": "video/mp4",
                    "url": streams_720p_mp4.first().url,  
               },
                  "1":{
                    "quality": "480p",
                    "mime_type": "video/mp4",
                    "url": streams_480p_mp4.url,
               },
                  "2":{
                    "quality": "360p",
                    "mime_type": "video/mp4",
                    "url": streams_360p_mp4.url,
               },
                  "3":{
                    "quality": "240p",
                    "mime_type": "video/mp4",
                    "url": streams_240p_mp4.url,
               },
                  "4":{
                    "quality": "144p",
                    "mime_type": "video/mp4",
                    "url": streams_144p_mp4.url,
               },
            },
               "formats":{
                  "22":{
                     "quality": "720p",
                     "mime_type": "video/mp4",
                     "url": streams_720p,
                     
               },
                  "18":{
                     "quality": "360p",
                     "mime_type": "video/mp4",
                     "url": streams_360p,        
               },
                  "17":{
                     "quality": "144p",
                     "mime_type": "video/mp4",
                     "url": streams_144p,   
               },
            },
                  "title": title,
            }
            return (meta)
                

      elif len(streams_480p_mp4) > 0:
            meta = {
            "adaptive_formats_mp4":{  
                  "0":{
                    "quality": "480p",
                    "mime_type": "video/mp4",
                    "url": streams_480p_mp4.url,
               },
                  "1":{
                    "quality": "360p",
                    "mime_type": "video/mp4",
                    "url": streams_360p_mp4.url,
               },
                  "2":{
                    "quality": "240p",
                    "mime_type": "video/mp4",
                    "url": streams_240p_mp4.url,
               },
                  "3":{
                    "quality": "144p",
                    "mime_type": "video/mp4",
                    "url": streams_144p_mp4.url,
               },
            },
               "formats":{
                  "22":{
                     "quality": "720p",
                     "mime_type": "video/mp4",
                     "url": streams_720p,       
               },
                  "18":{
                     "quality": "360p",
                     "mime_type": "video/mp4",
                     "url": streams_360p,      
               },
                  "17":{
                     "quality": "144p",
                     "mime_type": "video/mp4",
                     "url": streams_144p,   
               },
            },
                  "title": title,
            }    

            return (meta)
                

      elif len(streams_360p_mp4) > 0:
            meta = {
            "adaptive_formats_mp4":{  
                  "0":{
                     "quality": "360p",
                     "mime_type": "video/mp4",
                     "url": streams_360p_mp4.url,
               },
                  "1":{
                     "quality": "240p",
                     "mime_type": "video/mp4",
                     "url": streams_240p_mp4.url,
               },
                  "2":{
                     "quality": "144p",
                     "mime_type": "video/mp4",
                     "url": streams_144p_mp4.url,
               },
            },
               "formats":{
                  "22":{
                     "quality": "720p",
                     "mime_type": "video/mp4",
                     "url": streams_720p,       
               },
                  "18":{
                     "quality": "360p",
                     "mime_type": "video/mp4",
                     "url": streams_360p,      
               },
                  "17":{
                     "quality": "144p",
                     "mime_type": "video/mp4",
                     "url": streams_144p,   
               },
            },
               "title": title,
         }    
            return (meta) 

      # return jsonify(meta)
    else:   
      cut_story= target
      
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers, cookies=cookie_jar, ).json()
      uniqid = user_id["graphql"]["user"]["id"]
      is_priv = user_id["graphql"]["user"]["is_private"]
      
      if is_priv == True:
         meta = {
      "account": is_priv,
      }
      elif is_priv == False:
         user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers, cookies=cookie_jar, ).json()
         meta = {
         "story": user_id_req,
         "uniqid":uniqid,
         "account": is_priv,
         }
    # if target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/":
    
    #    return (response.json())
        
    # else:

    return jsonify(meta)
# driver function

if __name__ == "__main__":

	application.run(debug = True)
