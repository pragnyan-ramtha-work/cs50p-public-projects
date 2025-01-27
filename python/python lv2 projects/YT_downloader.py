from pytube import YouTube

link = input("PASTE THE LINK HERE")
yt = YouTube(link)

downloader = yt.streams.get_highest_resolution()

print("downloading...")

name = input("what do you wanna save this file as? ")

downloader.download(filename = name + ".mp4" )

print(f"{name} has been downloaded")