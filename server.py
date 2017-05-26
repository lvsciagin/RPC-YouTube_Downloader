#P15/36076/2015
#Lewis Munyi
#Assignment 1
from __future__ import unicode_literals
from xmlrpc.server import SimpleXMLRPCServer

import xmlrpc.client
import os
import re
import youtube_dl
import socket
serverName = 'RPC@127.0.0.1'
filename_concantenated = ""
meta_uploader = ""
meta_title=""
meta_id=""
meta_likes= ""
meta_dislikes=""
meta_duration=""
meta_description=""
meta_upload_date=""
meta_views=""
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        #Mako - Our Story [Exclusive Premiere]-awimSQD2Dyo.mp4
        #Mako - Our Story [Exclusive Premiere]-awimSQD2Dyo.mp4
        #Mako - Our Story [Exclusive Premiere]-awimSQD2Dyo
ydl_opts = {
		    'format': 'bestaudio/best',       
    		'outtmpl': '%(id)s',        
    		'noplaylist' : True,        
    		'progress_hooks': [my_hook],
    }

def processLink(ytlink):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		meta = ydl.extract_info(ytlink, download=False)
		global meta_upload_date
		global meta_uploader
		global meta_title
		global meta_id
		global meta_likes
		global meta_dislikes
		global meta_duration
		global meta_description
		global meta_upload_date
		global meta_views
		meta_upload_date=(meta['upload_date'])
		meta_uploader=(meta['uploader'])
		meta_views=(str(meta['view_count']))
		meta_likes=(str(meta['like_count']))
		meta_dislikes=(str(meta['dislike_count']))
		meta_id=(str(meta['id']))
		meta_format=(str(meta['format']))
		meta_duration=(str(meta['duration']))
		meta_title=(str(meta['title']))
		meta_description=(str(meta['description']))
		total = ('Title: ' + meta_title + '\n' + 'Uploader: ' + meta_uploader + '\n'+ 'Description: ' + meta_description
		 + '\n' + 'Duration ' + meta_duration + '\n' + 'Upload date: '
		  + meta_upload_date + '\n' + 'ID: ' + meta_id + '\n' + 'Format: ' + meta_format + '\n' 'Likes: '
		   + meta_likes + '\n' + 'Dislikes: ' + meta_dislikes + '\n')
		return total

def getServerName():
    return serverName

def download_video(video_link):
	try:
		ydl_opts = {}
		with youtube_dl.YoutubeDL(ydl_opts) as downloadVideo:
			filename = (meta_title + '-' + meta_id + '.mp4')
			print (filename)
			downloadVideo.download([video_link])
			global filename_concantenated
			filename_concantenated = filename.replace(" ", "")
			print (filename)
			os.rename(filename, filename_concantenated)
	except:
		error = ('Error experienced processing link. Make sure you:\n1. Have an active internet connection\n Enter a valid YouTube Link\n')
		return error
	else:
		return filename_concantenated

def download_audio(audio_link):
	ydl_opts = {
		    'format': 'bestaudio/best',       
    		'outtmpl': '%(id)s',        
    		'noplaylist' : True,        
    		'progress_hooks': [my_hook],
    }
	try:
		with youtube_dl.YoutubeDL(ydl_opts) as downloadaudio:
			downloadaudio.download([audio_link])
			filename = (meta_title + '-' + meta_id + '.m4a')
			filename_concantenated = filename.replace(" ", "")
			os.rename(meta_id, filename_concantenated)
	except:
		error = ('Error experienced processing link. Make sure you:\n1. Have an active internet connection\n Enter a valid YouTube Link\n')
		return error
	else:
		return filename_concantenated

def upload_audio():
	with youtube_dl.YoutubeDL(ydl_opts) as downloadVideo:
		filename_concantenated2 = (meta_title + '-' + meta_id + '.m4a')
		filename_concantenated2 = filename_concantenated2.replace(" ", "")
		with open(filename_concantenated2, "rb") as handle:
			return xmlrpc.client.Binary(handle.read())
		
def upload_video():
	with open(filename_concantenated, "rb") as handle:
		return xmlrpc.client.Binary(handle.read())

def clear_cache(filename_to_delete):
	os.remove(filename_to_delete)
	return "Cache cleared.\n"


def get_title(title_link):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl2:
		return meta_title

server = SimpleXMLRPCServer(("localhost", 8000), allow_none=False)
print("Listening on port 8000...lewis")
server.register_function(getServerName, "getServerName")
server.register_function(processLink, "processLink")
server.register_function(get_title, "get_title")
server.register_function(get_title, "get_title")
server.register_function(download_audio, "download_audio")
server.register_function(upload_video, "upload_video")
server.register_function(upload_audio, "upload_audio")
server.register_function(clear_cache, "clear_cache")
server.register_function(download_video, "download_video")
server.register_function(upload_video, "upload_video")
server.register_function(my_hook, 'my_hook')
server.serve_forever()
