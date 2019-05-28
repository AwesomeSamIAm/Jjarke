## working(if hard-coded) interface
import appJar
from  appJar import gui
app = gui()
def main() :
    #title declaration
    app.addLabel("title", "Welcome to our webscraper! Please enter the information below.", 0,0,2)
    app.setLabelBg("title", "red")

    #labels and entry declarations
    app.addLabel("url", "Website URL: ", 1, 0)
    app.addEntry("web_url", 1, 1)
    app.addLabel("int", "Time Interval:  ", 2, 0)
    app.addEntry("interv", 2, 1)
    app.addLabel("a_sid", "Account sid: ", 3, 0 )
    app.addEntry("sid",3,1 )
    app.addLabel("auth", "Authorization Token: ", 4, 0)
    app.addEntry("auth_tok", 4,1)
    app.addLabel("twi", "Twilio Number: ", 5,0)
    app.addEntry("twi_num", 5,1)
    app.addLabel("dest", "Destination Number: ", 6,0)
    app.addEntry("dest_num", 6,1)
    app.addLabel("char", "Minimum Character Change: ", 7, 0)
    app.addEntry("character_length", 7, 1)
    #submit buttton code(global variable calls, global variable assignments)
    def save() :
        variables = app.getAllEntries()
        app.stop()
    #button declaration and app initialization
    app.addButton("Submit", save)
    app.go()


    

    


if __name__ == "__main__":
    main()


   
