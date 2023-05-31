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

		data = "hello Brother"
		return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@application.route('/home', methods = ['GET'])
def scrap_reels():
   #  http_1 = "185.199.228.220:7300:ewyhwkqa:989msyg77vq2"
   #  ht2 = "185.199.229.156:7492:ewyhwkqa:989msyg77vq2"
   # #  ht3 = "185.199.231.45:8382:ewyhwkqa:989msyg77vq2"
   # #  ht4 = "188.74.210.207:6286:ewyhwkqa:989msyg77vq2"
   # #  ht5 = "188.74.183.10:8279:ewyhwkqa:989msyg77vq2"
   # #  ht6 = "188.74.210.21:6100:ewyhwkqa:989msyg77vq2"
   # #  ht7 = "45.155.68.129:8133:ewyhwkqa:989msyg77vq2"
   # #  ht8 = "154.95.36.199:6893:ewyhwkqa:989msyg77vq2"
   # #  ht9 = "45.94.47.66:8110:ewyhwkqa:989msyg77vq2"
   #  inp = open("proxy_list.txt", "r")
   #  lines=inp.read().split("\n")
    
   #  http_proxy = random.choice(lines)
   # #  http_proxy = "154.95.36.199:6893:ewyhwkqa:989msyg77vq2"
    
   #  url = "https://ipv4.icanhazip.com"

   #  proxyDict = {
   #    "http": http_proxy,  
   #  }
    proxies = (  
    'http://ewyhwkqa:989msyg77vq2@185.199.229.156:7492',
    'http://ewyhwkqa:989msyg77vq2@185.199.228.220:7300',
    'http://ewyhwkqa:989msyg77vq2@185.199.231.45:8382',
    'http://ewyhwkqa:989msyg77vq2@188.74.210.207:6286',
    'http://ewyhwkqa:989msyg77vq2@188.74.183.10:8279',
    'http://ewyhwkqa:989msyg77vq2@188.74.210.21:6100',
    'http://ewyhwkqa:989msyg77vq2@45.155.68.129:8133',
    'http://ewyhwkqa:989msyg77vq2@154.95.36.199:6893',
    'http://ewyhwkqa:989msyg77vq2@45.94.47.66:8110'

    )
# length = len(proxies)
# n = length * 2 
# for i in range(n):
#     index = i % length
    pr_oxy = [0,1,2,3,4,5,6,7,8]
    index = random.choice(pr_oxy)
    print(index)
    proxyDict = {"http" : proxies[index], "https" : proxies[index]}
    a = {"csrftoken":"9zZx0NkkfikdC2VqOkXHR801Yl2U1Hkh","sessionid":"53168773914%3A1G2wzMulPT5S1n%3A5%3AAYchXc_6qOkoEkoO-aK7-1FCWh2VR7o6IcJHZ0Ld81c"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"dv7osDMXDhLX2lTOsbPPnQ4gBNDPsG3O","sessionid":"58499749216%3AnDhC7Z4zEP6AWi%3A17%3AAYeZCANvuq3KMl40YjQNMB_GLZS5VkIKpGmVO_BqtQ"} #amsterdam34158 Amaan@123
    e =  {"csrftoken":"3nKfn2qBQKRFHJNFw0AfG8Rfdb9o33jQ","sessionid":"53168773914%3AZiRqQaVRRDkGVm%3A14%3AAYe0yPbgq6hXRQEUZg0UFwp0QjS2OpOSCcrdLbRRGg"}   #rocky__8081  Ashar123
    f =  {"csrftoken":"BpYbMrkXYht3ECBFXkHOwtKmhFJglbKM","sessionid":"53168773914%3AdeYBC2nzIso7Ri%3A19%3AAYcrpsd6aywjewsCwazpEgfwL_W2w7yXfDbjRXf4PA"} #rocky__8081  Ashar123   
    g =  {"csrftoken":"Sl3Ibj3cTVK67mQW97gjaGEKhAAWFzJR","sessionid":"53168773914%3AYKdJ9vfDqszBpO%3A13%3AAYcj_vbdwZgbiNYlEY3DhEkm2oshzhDZ9jOXEKQbdw"} #rocky__8081  Ashar123   
#a d
    c= [a,e]
   #  c= [a]

    cookie_jar = random.choice(c)
    headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)',

         }
    csrf_token = cookie_jar['csrftoken']
    session_id = cookie_jar['sessionid']
     
    source = request.args['source'] 
    target = format(source)
    if target[:31] == "https://www.instagram.com/reel/" :
     cut_reel = target[31:42]

     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_reel}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
     meta = {
              "posts": user_id_req,
              "cookie_jar":cookie_jar,
              "ip": proxyDict
           }      
    elif target[:28] == "https://www.instagram.com/p/":
     cut_post = target[28:39]

     user_id_req = requests.get(f"https://www.instagram.com/p/{cut_post}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
     meta = {
        "posts": user_id_req,
        }
     
    elif target[:34] == "https://www.instagram.com/stories/" :
      cut_s = target[34:]
      separator = '/'

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      uniqid = user_id['graphql']['user']['id'] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       #user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar,).json()
      # uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = '/'

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      uniqid = user_id['graphql']['user']['id'] 
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
      # user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar,).json()
      # uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }            
    elif target[:34] == "https://www.instagram.com/stories/" and target[-20:] == "?igshid=MDJmNzVkMjY=":
      cut_story = target[34:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }       
    elif target[:34] == "https://www.instagram.com/stories/" and target[-19:] == "?igshid=MDJmNzVkMjY":
      cut_story = target[34:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }     
    elif target[:30] == "https://instagram.com/stories/" and target[-19:] == "?igshid=MDJmNzVkMjY":
      cut_story = target[30:-40]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }          
    elif  target[:30] == "https://instagram.com/stories/" and target[-31:] == "?utm_source=ig_story_item_share":
      cut_story = target[30:-51:] 
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
         user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
         uniqid = user_id['user']['id']
         user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
         meta = {
         "story": user_id_req,
         "uniqid":uniqid,
         "account": is_priv,
         
         } 
    elif  target[:30] == "https://instagram.com/stories/" and target[-32:] == "/?utm_source=ig_story_item_share":
      cut_story = target[30:-52:]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }
    elif target[:34] == "https://www.instagram.com/stories/" and target[-32:] == "/?utm_source=ig_story_item_share"  :
      cut_story = target[34:-52:]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }                   
    elif target[:34] == "https://www.instagram.com/stories/":
      cut_story = target[34:-21]
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
       uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
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
    a = {"csrftoken":"WHeDVmiW1BUNfI3rnfcFNScaDYRhyIBx","sessionid":"53168773914%3AarQgFzkPj248d1%3A9%3AAYfnYiTXzLEkCcPNdZoosyvVms2DVY58DjcOaKDWXw"}#rocky__8081  Ashar123
    b =  {"csrftoken":"1jwyJ5QczmCIva5ROe2OOj8opDwazXL3","sessionid":"36744979802%3AmISFYgnEY22rzr%3A20%3AAYc4E5uksgDF77ikhfeHkkTbGplkf92-acsJYzzptQ"} #farzi_kalosxyz  246800
    d =  {"csrftoken":"dv7osDMXDhLX2lTOsbPPnQ4gBNDPsG3O","sessionid":"58499749216%3AnDhC7Z4zEP6AWi%3A17%3AAYeZCANvuq3KMl40YjQNMB_GLZS5VkIKpGmVO_BqtQ"} #amsterdam34158 Amaan@123
    e =  {"csrftoken":"3nKfn2qBQKRFHJNFw0AfG8Rfdb9o33jQ","sessionid":"53168773914%3AZiRqQaVRRDkGVm%3A14%3AAYe0yPbgq6hXRQEUZg0UFwp0QjS2OpOSCcrdLbRRGg"}   #rocky__8081  Ashar123
    f =  {"csrftoken":"BpYbMrkXYht3ECBFXkHOwtKmhFJglbKM","sessionid":"53168773914%3AdeYBC2nzIso7Ri%3A19%3AAYcrpsd6aywjewsCwazpEgfwL_W2w7yXfDbjRXf4PA"} #rocky__8081  Ashar123   
    g =  {"csrftoken":"Sl3Ibj3cTVK67mQW97gjaGEKhAAWFzJR","sessionid":"53168773914%3AYKdJ9vfDqszBpO%3A13%3AAYcj_vbdwZgbiNYlEY3DhEkm2oshzhDZ9jOXEKQbdw"} #rocky__8081  Ashar123   
#a d
    proxies = (  
    'http://ewyhwkqa:989msyg77vq2@185.199.229.156:7492',
    'http://ewyhwkqa:989msyg77vq2@185.199.228.220:7300',
    'http://ewyhwkqa:989msyg77vq2@185.199.231.45:8382',
    'http://ewyhwkqa:989msyg77vq2@188.74.210.207:6286',
    'http://ewyhwkqa:989msyg77vq2@188.74.183.10:8279',
    'http://ewyhwkqa:989msyg77vq2@188.74.210.21:6100',
    'http://ewyhwkqa:989msyg77vq2@45.155.68.129:8133',
    'http://ewyhwkqa:989msyg77vq2@154.95.36.199:6893',
    'http://ewyhwkqa:989msyg77vq2@45.94.47.66:8110'

    )
    pr_oxy = [0,1,2,3,4,5,6,7,8]
    index = random.choice(pr_oxy)
    proxyDict = {"http" : proxies[index], "https" : proxies[index]}
    c= [a,e,f,g]
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
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      uniqid = user_id['graphql']['user']['id']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       #user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar,).json()
       
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }   
    elif target[:30] == "https://instagram.com/stories/" :
      cut_s = target[30:]
      separator = '/'

      cut_story = cut_s.split(separator, 1)[0]  
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      is_priv = user_id['graphql']['user']['is_private']
      uniqid = user_id['graphql']['user']['id']
      if is_priv == True:
         meta = {
        "account": is_priv,
       }
      elif is_priv == False:
       #user_id = requests.get(f"https://www.instagram.com/stories/{cut_story}/?__a=1&__d=dis",headers=headers, cookies=cookie_jar).json()
       #uniqid = user_id['user']['id']
       user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
       meta = {
        "story": user_id_req,
        "uniqid":uniqid,
        "account": is_priv,
       }    
    elif target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/":
         url = "https://youtube-search-and-download.p.rapidapi.com/video"
         cut = target[-11:]
         querystring = {"id": cut}

         headers = {
         "X-RapidAPI-Key": "6e7e0e613dmsh7da1932734a8a9ap14bcb6jsn4c51c4a9f466",
         "X-RapidAPI-Host": "youtube-search-and-download.p.rapidapi.com"
      }

         response = requests.get(url, headers=headers, params=querystring)
         meta = {
            "youtube": response
         }
    else:   
      cut_story= target
      
      user_id = requests.get(f"https://www.instagram.com/{cut_story}?__a=1&__d=dis",headers=headers,  cookies=cookie_jar,).json()
      uniqid = user_id['graphql']['user']['id']
      is_priv = user_id['graphql']['user']['is_private']
      
      if is_priv == True:
         meta = {
      "account": is_priv,
      }
      elif is_priv == False:
         user_id_req = requests.get(f"https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={uniqid}",headers=headers,  cookies=cookie_jar,).json()
         meta = {
         "story": user_id_req,
         "uniqid":uniqid,
         "account": is_priv,
         }
    if target[:32] == "https://www.youtube.com/watch?v=" or target[:31] == "https://www.youtube.com/shorts/" or target[:27] == "https://youtube.com/shorts/" or target[:17] == "https://youtu.be/":
       
       return (response.json())
        
    else:

       return jsonify(meta)
# driver function
if __name__ == '__main__':

	application.run(debug = True)