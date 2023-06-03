from pytube import YouTube

def youtube(url):
    #   cut = target[-11:]
    #   url = "https://www.youtube.com/watch?v="+cut
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

                