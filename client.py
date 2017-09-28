import xmlrpc.client
import socket

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
	#print('Hello '+ proxy.getServerName() + 'lewis')

	print("\n|-------------------------------------------|")
	print("\n| REGISTRATION NUMBER |        NAME         |")
	print("\n|-------------------------------------------|")
	print("\n| P15/1718/2016       |   Mercy Kwambai     |")
	print("\n| P15/36076/2015      |   Lewis Munyi       |")
	print("\n| P15/1726/2016       |   Elvis Agin        |")
	print("\n|-------------------------------------------|\n\n\n\n")
	print("\n|-------------------------------------------|")
	print("\n| DESCRIPTION                               |")
	print("\n|-------------------------------------------|")
	print("\n|This is a python program that asks for user|")
	print("\n| for a valid YouTube URL, processes it and |")
	print("\n|then returns a video or audio file over an |")
	print("\n|RPC connection.                            |")
	print("\n|-------------------------------------------|\n\n\n\n")
	#print("\n|-------------------------------------------|")
	print("\n|Try any one of these examples:             |")
	print("\n https://www.youtube.com/watch?v=JZncdTFNcg0 ")
	print("\n https://www.youtube.com/watch?v=awimSQD2Dyo ")
	print("\n|-------------------------------------------|")

	#Get user input
	url = input("\nEnter a valid youtube URL: \n")
	#url= "https://www.youtube.com/watch?v=JZncdTFNcg0"
	
	#Send url to server for processing and return the details of the URL
	print(proxy.processLink(url) + '\n')

	#Confirm video
	answer = input('Proceed to download video? \n 1. Yes (y) \n 2. Abort (Press any key) \n')

	if answer in ['y' or 'Y' or 'Yes' or 'YES' or 'yes' or "1"]:
		
		#Ask format which they want to download the file
		choice = input('What type of file format do you wish to download? \n 1. Video[mp4]\n 2. Audio[m4a]\n')

		#If video
		if choice in ['1' or 'v' or 'video' or 'Video' or 'VIDEO' or 'V']:
			print('Gathering information..\nExtracting video.. \nThis might take a while depending on:\n		The size of the video\n		The speed of your connection\n')
			
			#Command server to download video and return the file name if the file
			filenametoupload = proxy.download_video(url)
			print ("Extraction complete..\nUploading video.. \n")
			
			#Upload video frrom server to client
			with open(filenametoupload, "wb") as handle:
				handle.write(proxy.upload_video().data)

			#Delete file from server
			print ("Finalizing.. \n" + proxy.clear_cache(filenametoupload) + "Upload complete \n")

		#If audio
		elif choice in['2' or 'Audio' or 'audio' or 'a' or 'A' or 'AUDIO']:
			print('Gathering information..\nExtracting audio.. \nThis might take a while depending on the size of the video\n')

			#Call download function and return the downloaded file name
			filenametoupload = (proxy.download_audio(url))
			print ("Uploading..\n")

			#Copy file to root
			with open(filenametoupload, "wb") as handle:
				handle.write(proxy.upload_audio().data)
			
			#Delete file from server
			print ("Final steps.. \n" + proxy.clear_cache(filenametoupload) + "Upload complete \n")
		else: print("Incorrect choice. Exiting")
	else:
		print('incorrect choice. Exiting')



 
