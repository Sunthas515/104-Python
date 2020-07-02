
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10482652
#    Student name: Callum McNeilage
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  What's On?: Online Entertainment Planning Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for planning an entertainment schedule.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it as a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.


# Name of the planner file. To simplify marking, your program should
# generate its entertainment planner using this file name.
planner_file = 'planner.html'

import os

#Create a window
Window = Tk()
Window.configure(background = 'black')

#Give the window a title
Window.title("What's On")

#Define common font
sysfont = ('Helvetica, 20')
devfont = ('Helvetica, 12')

#Define variables for event counter
Event_Count = IntVar()

#Define Lists for event names
Movies_List = []
Events_List = []
Performance_List = []

#Define lists for names
Movies_Name = []
Events_Name = []
Performance_Name = []

#Define lists for event descriptions
Movies_Times = []
Events_Times = []
Performance_Times = []

#Define lists for event images
Movies_Image = []
Events_Image = []
Performance_Image = []

#Define list of all events
All_Array = []
#Define list of selected events
Events_Array = []

#Define html
movies_page = ""
ent_page = ""
qso_page = ""

#Define online/offline status
Status = 'Online'

#--------------------------------------------------------------------------------------------------------------------------
# Backend functions

#Load information event
def sys_load():
    global movies_page
    global ent_page
    global qso_page

    global Movies_List
    global Events_List
    global Performance_List

    #Reset Lists for event names
    Movies_List = []
    Events_List = []
    Performance_List = []

    #Open webpages
    movies_page = urlopen("https://www.blueroomcinebar.com/movies/now-showing/").read().decode('utf-8')
    ent_page = urlopen('https://www.brisent.com.au/Event-Calendar').read().decode('utf-8')
    qso_page = urlopen('https://www.qso.com.au/events/all-events').read().decode('utf-8')

    #Add to lists
    Populate()


#Create counter for checkboxes to keep track of number of events
def count():
    #Define event counter
    counter = 0
    global Events_Array
    global All_Array

    Events_Array = []

    #Check if event is selected
    for evt in All_Array:
        if evt.get() != "":
            Events_Array.append(evt.get()) #Add selected events to events array

    #Count number of selected events
    counter = len(Events_Array)

    Printer.config(text = 'Print planner (' + str(counter) + ' events selected)')

#Command for using archived html or live html
def offline_mode():
    #Add all variables used in function
    global movies_page
    global ent_page
    global qso_page
    global Movies_List
    global Events_List
    global Performance_List
    global Movies_Name
    global Movies_Times
    global Movies_Image
    global Events_Name
    global Events_Times
    global Events_Image
    global Performance_Name
    global Performance_Times
    global Performance_Image
    global movies_page
    global ent_page
    global qso_page
    global Status
        
    #Reset Lists for events
    Movies_List = []
    Events_List = []
    Performance_List = []

    #Reset webpages
    movies_page = ""
    ent_page = ""
    qso_page = ""

    #Reset everything
    Movies_Name = []
    Movies_Times = []
    Movies_Image = []

    Events_Name = []
    Events_Times = []
    Events_Image = []

    Performance_Name = []
    Performance_Times = []
    Performance_Image = []

    #If working offline, use archived webpages. Otherwise, use online pages
    if Status == 'Online':

        dirname = os.path.dirname(__file__)

        movies_page = open(os.path.join(dirname, 'Archive/BlueRoom.html')) \
            .read()#.decode('utf-8')
        ent_page = open(os.path.join(dirname, 'Archive/EntertainmentCentre.html')) \
            .read()#.decode('utf-8')
        qso_page = open(os.path.join(dirname, 'Archive/QSO.html')) \
            .read()#.decode('utf-8')

        Status = 'Offline'
        DevText.config(text = Status)
        CheckDev.config(text = 'Use online webpages')

        Populate()
    else:
        Status = 'Online'
        DevText.config(text = Status)
        CheckDev.config(text = 'Use offline webpages')

        sys_load()

#Save selected events to database
def save():
    #Connect to database
    connection = connect(database = 'entertainment_planner.db')
    events_db = connection.cursor()

    #Delete values in table
    events_db.execute('DELETE FROM events;')

    #Insert events
    for events in range(len(Events_Array)):
        saved = Events_Array[events].split(";")
        rows = (str(saved[0]), str(saved[1]))
        query = "INSERT INTO events (event_name, event_date) VALUES {};".format(rows)

    #Execute the query
        events_db.execute(query)

    #Commit the query
    connection.commit()

    #Unlock the database
    events_db.close()
    connection.close()

#Populate checkboxes of events on GUI
def Populate():     
    #Add movies to Movies at Blue Room Screen
    find_movie_names = findall(r'<h4 class="movie-title">(.*?)</h4>', movies_page)
    find_movie_times = findall(r'<p>([0-9]{1,2}:[0-9]{2} AM|PM)</p>', movies_page)
    find_movie_image = findall(r'<div class="poster" style="background-image: url\((.*?)\)">', movies_page)

    #Add movies to lists
    for movie in find_movie_names:
        Movies_Name.append(movie)
    for movie in find_movie_times:
        Movies_Times.append(movie)
    for movie in find_movie_image:
        Movies_Image.append(movie)

    for movie in range(len(Movies_Name)):
        Movies_List.append("{};{};{}".format(Movies_Name[movie], Movies_Times[movie], Movies_Image[movie]))

#Add Events to Events at Entertainment Centre Screen
    find_ent_names = findall(r'<td width="42%" valign="top"><h1 class="event-title">(.*?)</h1>', ent_page)
    find_ent_times = findall(r'<h2 class="Event-Date">(.*?)</h2>', ent_page)
    find_ent_image = findall(r'<img src="/(.*?)" width="270" />', ent_page)

    #Add events to lists
    for event in find_ent_names:
        Events_Name.append(event)
    for event in find_ent_times:
        Events_Times.append(event)
    for event in find_ent_image:
        Events_Image.append(event)

    for event in range(len(Events_Image)):
        Events_Image[event] = str("https://www.brisent.com.au/")+ str(Events_Image[event])

    for event in range(len(Events_Name)):
        Events_List.append("{};{};{}".format(Events_Name[event], Events_Times[event], Events_Image[event]))

#Add performances to Performances of QSO screen
    find_performance_name = findall(r'<h2><a href="(?:.*?)" rel="bookmark">(.*?)</a></h2>', qso_page)
    find_performance_times = findall(r'<div class="date">(.*?)</div>', qso_page)
    find_performance_image = findall( \
        r'<a href="(?:.*?)"><img src="(.*?)" width="280" height="214" alt="" /></a>      </div>', qso_page)

    #Add performances to lists
    for performance in find_performance_name:
        Performance_Name.append(performance)
    for performance in find_performance_times:
        Performance_Times.append(performance)
    for performance in find_performance_image:
        Performance_Image.append(performance)

    for performance in range(len(Performance_Name)):
        Performance_List.append("{};{};{}".format(Performance_Name[performance], Performance_Times[performance], Performance_Image[performance]))
#

#Load data
sys_load()

#-----------------------------------------------------------------------------------------------------------------------------
#Loops for generating event checkboxes

#Create Movies at Blue Room Screen
def Movies():
    global All_Array
    #Create window
    Movie_window = Toplevel()
    Movie_window.configure(background = 'black')

    #Give window a title
    Movie_window.title('Movies at Reading')

    #Generate checkboxes
    for movies in range(len(Movies_List)):
        var = StringVar()
        #Define text for labels
        Movies_text = Movies_Name[movies] + " " + Movies_Times[movies]

        check_movie = Checkbutton(Movie_window, text = Movies_text, font = sysfont, fg = 'cyan', bg = 'black', \
            variable = var, onvalue = Movies_List[movies], offvalue = "", command = count)
        check_movie.pack()
        All_Array.append(var)
    
    #Generate disclaimer label
    Movie_lbl1 = Label(Movie_window, text = "**Disclaimer: The times for movies are for today only**", font = devfont, fg = 'cyan', bg = 'black')
    Movie_lbl1.pack()

#Create Events at Entertainment Centre Screen
def Entertainment():
    global All_Array
    #Create Window
    Ent_window = Toplevel()
    Ent_window.configure(background = 'black')

    #Give window a title
    Ent_window.title("Events at Entertainment Centre")

    #Generate checkboxes
    for entertainment in range(len(Events_List)):
        var = StringVar()
        Events_Text = Events_Name[entertainment] + " " + Events_Times[entertainment]

        check_ent = Checkbutton(Ent_window, text = Events_Text, font = sysfont, \
            fg = 'maroon1', bg = 'black', variable = var, onvalue = Events_List[entertainment], offvalue = "", command = count)
        check_ent.pack()
        All_Array.append(var)

#Create qso at event dates
def qso():
    global All_Array
    #Create window
    qso_window = Toplevel()
    qso_window.configure(background = 'black')

    #Give window a title
    qso_window.title("QSO Performances")

    #Generate checkboxes
    for qso in range(len(Performance_List)):
        var = StringVar()
        QSO_Text = Performance_Name[qso] + " " + Performance_Times[qso]

        check_qso = Checkbutton(qso_window, text = QSO_Text, font = sysfont, \
            fg = 'green2', bg = 'black', variable = var, onvalue = Performance_List[qso], offvalue = "", command = count)
        check_qso.pack()
        All_Array.append(var)

#-----------------------------------------------------------------------------------------------------------------------------

#Print events html
def print_page(): 
    global planner_file 
    html =  "<html>\n<head></head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"
    
    #Create webpage title
    title = "What's On - Event Planner"
    html += '\n<h1>' + title + '</h1>\n'

    #Add events
    for event in range(len(Events_Array)):
        s = Events_Array[event].split(";")
        name = '<p>' + s[0] + '</p>\n'
        html += name
        time = '<p>' + s[1] + '</p>\n'
        html += time
        img = '<img src=' + s[2] + '>\n'
        html += img

    #Write to file
    with open(planner_file, 'w') as f:
        f.write(html + "\n</body>\n</html>")
    
    Printer.config(text = 'Printed Successfully')


#------------------------------------------------------------------------------------------------------------
#Front end functions for GUI

#Display logo
canvas = Canvas(Window, width = 800, height = 200, bg = 'black', borderwidth = 0, highlightthickness = 0)
canvas.grid(row = 0, column = 1, padx = 20, pady = 20, rowspan = 4, columnspan = 5)
img = PhotoImage(file = "whats_on.png")
canvas.create_image(2, 2, anchor = NW, image = img)

#Display developer settings status for online/offline data
DevSettings = Label(Window, text = "Developer Settings:", font = devfont, fg = 'white', bg = 'black')
DevSettings.grid(row = 1, column = 6, padx = 20)

CheckDev = Button(Window, text = "Use offline webpages", font = devfont, \
    command = offline_mode, bg = 'black', fg = 'white')
CheckDev.grid(row = 2, column = 6, padx = 20)

DevText = Label(Window, text = Status, font = devfont, fg = 'white', bg = 'black')
DevText.grid(row = 3, column = 6, padx = 20)

#GUI interface for saving events to database
SaveDev = Button(Window, text = "Save events to Database", font = devfont, \
    command = save, bg = 'black', fg = 'white')
SaveDev.grid(row = 4, column = 6, padx = 20)

SaveText = Label(Window, text = "", font = devfont, fg = 'white', bg = 'black')
SaveText.grid(row = 5, column = 6, padx = 20)

#Display frame for Event categories
frameTitle = Label(Window, text = "Event categories - Click to select", font = sysfont, fg = 'white', bg = 'black')
frameTitle.grid(row = 5, column = 4, sticky = W, padx = 20)
frame = Frame(Window, borderwidth = 5, relief = 'groove', bg = 'black')
frame.grid(row = 6, column = 2, columnspan = 6, sticky = W, pady = 20, padx = 20)

#Display buttons for events within frame
Movies = Button(frame, text = 'Movies at the Blue Room', font = sysfont, fg = 'cyan', bg = 'black', borderwidth = 2, \
    relief = 'raised', command = Movies)
Movies.grid(row = 0, column = 1, padx = 10, pady = 10)

Events = Button(frame, text = 'Events at Entertainment Centre', font = sysfont, fg = 'maroon1', bg = 'black', \
    borderwidth = 2, relief = 'raised', command = Entertainment)
Events.grid(row = 0, column = 2, padx = 10, pady = 10)

Performance = Button(frame, text = 'QSO Performances', font = sysfont, fg = 'green2', bg = 'black', borderwidth = 2, \
    relief = 'raised', command = qso)
Performance.grid(row = 0, column = 3, padx = 10, pady = 10)

#Display Print planner button
Printer = Button(Window, text = 'Print planner (0 events selected)', font = sysfont, \
     fg = 'white', bg = 'black', command = print_page)
Printer.grid(row = 7, column = 4, pady = 20, sticky = E)

#Start event loop
Window.mainloop()
