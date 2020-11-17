from mpyg321.mpyg321 import MPyg321Player

class Song:
    name = ""       #Properties
    album = ""
    writer = ""
    duration = 0
    def play(self):
        p = MPyg321Player()
        p.play_song(self.name)
        print("PLAYing ",self.name)
    def pause(self):
        print("PAUSEing ",self.name)
    def stop(self):
        print("STOPing ",self.name)


bt = Song()    #default constructors
bt.name = "./songs/beat_it.mp3"
e = Song()
e.name = "songs/earth.mp3"
bl = Song()
bl.name = "songs/believer.mp3"
bt.play()
bt.pause()
bt.stop()

































# class python_lesson:
#     #properties
#     into = ""
#     no_students = 0
#     no_of_classes_tn = 0
#     #functions  
#     def __init__(self,date):
#         print("Turning on the mobile, texting on telegram, Creating a meet link, Joining class",date)
#     def topics_taught(self):
#         print("write topics on board, start teaching")
#     def take_attandence(self):
#         print("take register, mark attancence")


# sixnov2020 = python_lesson("6/11/2020") # parameterised constructors
# # sixnov2020.no_students = 3

# fivenov2020 = python_lesson("hello")
# # fivenov2020.no_of_classes_tn = 2





