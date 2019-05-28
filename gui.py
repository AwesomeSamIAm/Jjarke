## working(if hard-coded) interface
import appJar
from  appJar import gui
app = gui()

#global variable initializations
weburl = 0
interv = 0
sid = 0
authtok = 0
twinum = 0
destnum = 0

#title declaration
app.addLabel("title", "Welcome to our webscraper! Please enter the information below.", 0,0,2)
app.setLabelBg("title", "red")

#labels and entry declarations
app.addLabel("url", "Website URL: ", 1, 0)
app.addEntry("weburl", 1, 1)
app.addLabel("int", "Time Interval:  ", 2, 0)
app.addEntry("interv", 2, 1)
app.addLabel("asid", "Account sid: ", 3, 0 )
app.addEntry("sid",3,1 )
app.addLabel("auth", "Authorization Token: ", 4, 0)
app.addEntry("authtok", 4,1)
app.addLabel("twi", "Twilio Number: ", 5,0)
app.addEntry("twinum", 5,1)
app.addLabel("dest", "Destination Number: ", 6,0)
app.addEntry("destnum", 6,1)
#submit buttton code(global variable calls, global variable assignments)
def save() :
    global weburl
    global interv
    global sid
    global authtok
    global twinum
    global destnum
    weburl = app.getEntry("weburl")
    interv = app.getEntry("interv")
    sid = app.getEntry("sid")
    authtok = app.getEntry("authtok")
    twinum = app.getEntry("twinum")
    destnum = app.getEntry("destnum")
   

   



   
#button declaration and app initialization
app.addButton("Submit", save)
app.go()




# import appJar
# from  appJar import gui
# app = gui()
# web_url = 0
# twi= 0
# variables = ["web_url", "twi"]
# # add & configure widgets - widgets get a name, to help referencing them later
# allentries = ["ent1", "ent2"]
# app.addLabel("title", "Welcome to appJar")
# app.setLabelBg("title", "red")
# app.addLabel("url", "Website URL: ", 0, 0)
# app.addEntry("weburl", 0, 1)
# app.addLabel("twi", "Twilio:  ", 1, 0)
# app.addEntry("2", 1, 1)


# def save() :
#     e = app.getAllEntries()
#     def death():
#         for i in e:
#             a = e[i]
#             print(i)

#     # e.keys = e.values
#     print(e)
#     # for i in range(len(e)):
        
  
       
        

        


   

# app.addButton("Submit", save)
# app.go()
