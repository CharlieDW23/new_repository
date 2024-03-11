import tkinter as tk
import pandas as pd
from tkinter import *
import tkinter.messagebox
import webbrowser
root = tk.Tk()
root.title("My Organizer")
screen_width = 600
screen_height = 600
root.configure(bg='greenyellow')
root.minsize(screen_width, screen_height)


def clear_widgets(root):
    """This function will destroy any widgets you created"""
    for i in root.winfo_children():
        i.destroy()


# create the title page
def create_titlepage(root):
    clear_widgets(root)

    # place a citation on the first page
    inspiration_label = tk.Label(root, text='Have confidence \n that if you have \n done a little thing well, \n you can do a bigger thing \n well too.', font='System 26')
    inspiration_label.place(x=110, y=160)

    # place a label that greets the user
    greetings_label = tk.Label(root, text='Hi, welcome to your personal organizer!', font='Script 20', bg='white')
    greetings_label.place(x=160, y=32)

    # place a button that will end the application
    kill_button = tk.Button(root, text='EXIT', font='SansSerif 15', bg='red', command=quit)
    kill_button.place(x=60, y=540)

    # place a button that launches the second page
    second_page_button = tk.Button(root, text='Get started!', font='Script 15', bg='light green', command=lambda:create_second_page(root))
    second_page_button.place(x=500, y=540)

# create the homepage
def create_second_page(root):
    clear_widgets(root)

    # place a title label
    Title_label = tk.Label(root, text='My organizer', font='Script 20', bg='black', fg='white')
    Title_label.place(x=260, y=20)

    # place a button to return to the title page
    return_button = tk.Button(root, text='back', font='Script 16', bg='light blue', fg='black', command=lambda:create_titlepage(root))
    return_button.place(x=30, y=520)

    # place a button for the diary page
    diary_button = tk.Button(root, text='Diary', font='Script 16', bg='light green', fg='black', command=lambda:create_diary_page(root))
    diary_button.place(x=280, y=150)

    # place a button for the TO DO page
    to_do_button = tk.Button(root, text='TO DO', font='Script 16', bg='yellow', fg='black', command=lambda: create_todo_page(root))
    to_do_button.place(x=280, y=250)

    # place a button for the focus page
    music_button = tk.Button(root, text='Music', font='Script 16', bg='orange', fg='black', command=lambda: create_music_page(root))
    music_button.place(x=280, y=350)

    # place a button for the Study Page
    study_button = tk.Button(root, text='Study', font='Script 16', bg='pink', fg='black', command=lambda: create_study_page(root))
    study_button.place(x=280, y=450)


# create a dictionary which will store all the input from the user from the text fields
def store_user_data():
    # write a dictionary that will store the data to be accessed later
    user_data = {
        "date": date.get(),
        "diary_entry": diary_entry.get("1.0",'end-1c')
    }

    # convert the dictionary into a data frame
    user_data_df = pd.DataFrame([user_data])
    user_data_df.to_csv('Data/user_data_diary.csv', index=False, mode='a', header=False)

# write a definition that allows us to access the data and display the data in a text field
def show_user_data():
    user_data = pd.read_csv("Data/user_data_diary.csv") # read the csv file
    date = list(user_data.date)
# create text-box
    text_box = tk.Text(root,
                       bg='white',
                       fg='black',
                       font='Arial 10',
                       width=60)
    text_box.place(x=20, y=57, relwidth=0.7, relheight=0.7)

# re-structured code with ChatGPT https://chatx.de/
    for d in date:
        text_box.insert(tk.END, f"\nDate: {d}")
        entry = list(user_data[user_data.date == d].diary_entry)  # get the diary entry for the current date.
        # display the diary entry in the GUI window
        text_box.insert(tk.END, f"\n{entry[0]}")

# to delete information, mark it in the textbox and delete through the common keyboard button

def create_diary_page(root):
    global date, diary_entry
    clear_widgets(root)
    # place a title label
    title_label = tk.Label(root, text='My Diary', font='Script 20', bg='black', fg='light green')
    title_label.place(x=45, y=40)
    # place a box for the date
    date = tk.StringVar()
    date = tk.Entry(root, width=10,
                          textvar=date,
                          font='Script 18',
                          bg='white', fg='black')
    date.place(x=45, y=125)
    # place a label for the date
    date_label = tk.Label(root,
                          text='Date',
                          font='Script 18',
                          bg='black', fg='white')
    date_label.place(x=45, y=90)
    # place a label for the entry box
    entry_label = tk.Label(root,
                         text='Todays Entry:',
                         font='Script 18',
                         bg='black', fg='white')
    entry_label.place(x=45, y=160)
    # place the entry field for the diary entry
    diary_entry = tk.Text(root,
                        width=50,
                        height=20,
                        font='Arial 10',
                        bg='white', fg='black')
    diary_entry.place(x=47, y=200)


    # place a button that will save the entry
    save_button = tk.Button(root, text='SAVE', font='Arial 16', bg='black', fg='light green', command=store_user_data)
    save_button.place(x=120, y=540)

    # place a button that will show the previous entries
    previous_entries_button = tk.Button(root, text='Previous entries', font='Arial 16', bg='black', fg='orange', command=lambda:create_display_entry_page(root))
    previous_entries_button.place(x=200, y=540)

    # place a button to return to the second page
    return_button = tk.Button(root, text='back', font='script 16', bg='light green', fg='black', command=lambda:create_second_page(root))
    return_button.place(x=23, y=543)


# create the page where the diary entries can be displayed
def create_display_entry_page(root):
    clear_widgets(root)
    title_label = tk.Label(root, text='Previous entries', font='Script 16', fg='black', bg='orange')
    title_label.place(x=40, y=20)

# place a button to return to the diary page
    return_button = tk.Button(root, text='back', font='Script 16', bg='orange', fg='black', command=lambda:create_diary_page(root))
    return_button.place(x=23, y=543)

# create the field for the stored entries
    previous_entries_field = tk.Entry(root, width=50, font='Arial 10', bg='white', fg='black')
    previous_entries_field.pack()

# display the entries
    show_user_data()


def create_todo_page(root): # https://techvidvan.com/tutorials/python-to-do-list/
    clear_widgets(root)
    # place a title label
    Title_label = tk.Label(root, text='TO DO', font='Script 20', bg='black', fg='yellow')
    Title_label.place(x=50, y=20)
    # place a return button on that page
    return_button = tk.Button(root, text='back', font='Script 16', bg='yellow', fg='black', command=lambda:create_second_page(root))
    return_button.place(x=25, y=540)

    # create a listbox for the tasks with a scroll-bar
    listbox_task = Listbox(root, bg='black', fg='white', font='Helvetica 12', height=21, width=35)
    scrollbar = Scrollbar(root, orient=VERTICAL, command=listbox_task.yview)  # https://techvidvan.com/tutorials/python-to-do-list/
    scrollbar.place(x=394, y=70, height=385)
    listbox_task.configure(yscrollcommand=scrollbar.set) # https://techvidvan.com/tutorials/python-to-do-list/
    listbox_task.place(x=64, y=64)

    # definition to add a new task to the To Do list # https://data-flair.training/python-to-do-list/
    def entertask():
        # window to take input
        input_text=''
        def add():
            input_text = entry_task.get(1.0, 'end-1c')
            if input_text == '':
                tkinter.messagebox.showwarning(title='WARNING!', message='Please enter a task.')
            else:
                listbox_task.insert(END, input_text)
                # close the pop-up window
                root1.destroy()

        root1=Tk()
        root1.title('Add task')
        entry_task=Text(root1, width=40, height=4)
        entry_task.pack()
        button_temp=tk.Button(root1, text='Add text', command=add)
        button_temp.pack()
        root1.mainloop()

    # easier function to delete a task and to mark a task as completed
    def deletetask():
        # this definition allows the user to select a specific task and mark it as completed
        selected = listbox_task.curselection()
        listbox_task.delete(selected[0])

    def markcompleted(): #https://data-flair.training/blogs/python-to-do-list/
        marked=listbox_task.curselection()
        temp=marked[0]

        # store the entry of the selected item in a string
        temp_marked=listbox_task.get(marked)
        # update the checklist
        temp_marked = temp_marked+'☑'
        # delete it then insert it
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)

    # entry_button to add tasks
    entry_button = tk.Button(root, text='Add task', width=20, command=entertask)
    entry_button.place(x=415, y=190)

    # button to delete a task
    delete_button = tk.Button(root, text='Delete selected task', width=20, command=deletetask)
    delete_button.place(x=415, y=220)

    # button to mark the task as completed
    mark_button = tk.Button(root, text='Mark as completed', width=20, command=markcompleted)
    mark_button.place(x=415, y=250)



# Music Page
def create_music_page(root):
    clear_widgets(root)
    # place a title label
    Title_label = tk.Label(root, text='Focus with music', font='Script 20', bg='black', fg='orange')
    Title_label.place(x=50, y=20)
    # place a return button on that page
    return_button = tk.Button(root, text='back', font='Script 16', bg='orange', fg='black', command=lambda:create_second_page(root))
    return_button.place(x=30, y=540)

    # place buttons to listen to music online
    online_button_1 = tk.Button(text='Sad/Emotional Playlist', font='Arial 12', bg='pink', fg='black', command=lambda:callback('https://www.youtube.com/watch?v=UAWcs5H-qgQ&list=PLzzwfO_D01M4nNqJKR828zz6r2wGikC5a'))
    online_button_1.place(x=30, y=100)

    online_button_2 = tk.Button(text='Happy/Uplifting Playlist', font='Arial 12', bg='yellow', fg='black', command=lambda:callback('https://www.youtube.com/watch?v=pIgZ7gMze7A&list=PLJNlve0_Ebae2aPbjfolLT-6LvZkP8UZA'))
    online_button_2.place(x=30, y=140)

    online_button_3 = tk.Button(text='Angry Breakdown Playlist', font='Arial 12', bg='red', fg='black', command=lambda:callback('https://www.youtube.com/watch?v=Vrr3lRLjZ1Y&list=PLknqyEOvGo1YgL11BN1m-YOxaFHl29elY'))
    online_button_3.place(x=30, y=180)

    online_button_4 = tk.Button(text='Lounge Music / Soft Mix', font='Arial 12', bg='cyan', fg='black', command=lambda:callback('https://www.youtube.com/playlist?list=PLYxyJ_3ZnBORblpaTqlLEn9ctqn-YlZSn'))
    online_button_4.place(x=30, y=220)

    online_button_5 = tk.Button(text='Soundtrack', font='Arial 12', bg='goldenrod1', fg='black', command=lambda:callback('https://www.youtube.com/watch?v=HhKjfnaDQBQ&list=PL5n4nHJVIy2aLKxhS62pDDeQqj87GBQwG'))
    online_button_5.place(x=30, y=260)

    online_button_6 = tk.Button(text='90s Punk', font='Arial 12', bg='black', fg='red', command=lambda:callback('https://www.youtube.com/watch?v=LH-i8IvYIcg&list=RDQMt6j7_DaTbPQ&start_radio=1'))
    online_button_6.place(x=30, y=300)

    online_button_7 = tk.Button(text='Hip Hop', font='Arial 12', bg='blue', fg='white', command=lambda:callback('https://www.youtube.com/watch?v=alApDi8De04'))
    online_button_7.place(x=30, y=340)

    online_button_8 = tk.Button(text='New Pop', font='Arial 12', bg='purple', fg='white', command=lambda:callback('https://www.youtube.com/watch?v=Oa_RSwwpPaA&list=PLDIoUOhQQPlUDNpjEYTTE9tb-QvUHUSMt'))
    online_button_8.place(x=30, y=380)

    def callback(url):
        webbrowser.open_new_tab(url)
        # create field for link 1
        link_1 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/watch?v=UAWcs5H-qgQ&list=PLzzwfO_D01M4nNqJKR828zz6r2wGikC5a')
        link_1.place(x=300, y=80)
        # call link 1
        link_1.bind('<Button-1>', lambda e: callback('https://www.youtube.com/watch?v=UAWcs5H-qgQ&list=PLzzwfO_D01M4nNqJKR828zz6r2wGikC5a'))
        callback('https://www.youtube.com/watch?v=UAWcs5H-qgQ&list=PLzzwfO_D01M4nNqJKR828zz6r2wGikC5a')
        # create field for link 2
        link_2 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/watch?v=pIgZ7gMze7A&list=PLJNlve0_Ebae2aPbjfolLT-6LvZkP8UZA')
        link_2.place(x=300, y=85)
        # call link 2
        link_2.bind('<Button-1>', lambda e: callback('https://www.youtube.com/watch?v=pIgZ7gMze7A&list=PLJNlve0_Ebae2aPbjfolLT-6LvZkP8UZA'))
        callback('https://www.youtube.com/watch?v=pIgZ7gMze7A&list=PLJNlve0_Ebae2aPbjfolLT-6LvZkP8UZA')
        # create field for link 3
        link_3 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/watch?v=Vrr3lRLjZ1Y&list=PLknqyEOvGo1YgL11BN1m-YOxaFHl29elY')
        link_3.place(x=300, y=90)
        # call link 3
        link_3.bind('<Button-1>', lambda e: callback('https://www.youtube.com/watch?v=Vrr3lRLjZ1Y&list=PLknqyEOvGo1YgL11BN1m-YOxaFHl29elY'))
        callback('https://www.youtube.com/watch?v=Vrr3lRLjZ1Y&list=PLknqyEOvGo1YgL11BN1m-YOxaFHl29elY')
        # create field for link 4
        link_4 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/playlist?list=PLYxyJ_3ZnBORblpaTqlLEn9ctqn-YlZSn')
        link_4.place(x=300, y=95)
        # call link 4
        link_4.bind('<Button-1>', lambda e: callback('https://www.youtube.com/playlist?list=PLYxyJ_3ZnBORblpaTqlLEn9ctqn-YlZSn'))
        callback('https://www.youtube.com/playlist?list=PLYxyJ_3ZnBORblpaTqlLEn9ctqn-YlZSn')
        # create field for link 5
        link_5 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/watch?v=HhKjfnaDQBQ&list=PL5n4nHJVIy2aLKxhS62pDDeQqj87GBQwG')
        link_5.place(x=300, y=100)
        # call link 5
        link_5.bind('<Button-1>', lambda e: callback('https://www.youtube.com/watch?v=HhKjfnaDQBQ&list=PL5n4nHJVIy2aLKxhS62pDDeQqj87GBQwG'))
        callback('https://www.youtube.com/watch?v=HhKjfnaDQBQ&list=PL5n4nHJVIy2aLKxhS62pDDeQqj87GBQwG')
        # create field for link 6
        link_6 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/watch?v=LH-i8IvYIcg&list=RDQMt6j7_DaTbPQ&start_radio=1')
        link_6.place(x=300, y=105)
        # call link 6
        link_6.bind('<Button-1>', lambda e: callback('https://www.youtube.com/watch?v=LH-i8IvYIcg&list=RDQMt6j7_DaTbPQ&start_radio=1'))
        callback('https://www.youtube.com/watch?v=LH-i8IvYIcg&list=RDQMt6j7_DaTbPQ&start_radio=1')
        # create field for link 7
        link_7 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/watch?v=alApDi8De04')
        link_7.place(x=300, y=110)
        # call link 7
        link_7.bind('<Button-1>', lambda e: callback('https://www.youtube.com/watch?v=alApDi8De04'))
        callback('https://www.youtube.com/watch?v=alApDi8De04')
        # create field for link 8
        link_8 = tk.Text(root, font='Arial 12', fg='white', text='https://www.youtube.com/watch?v=Oa_RSwwpPaA&list=PLDIoUOhQQPlUDNpjEYTTE9tb-QvUHUSMt')
        link_8.place(x=300, y=115)
        # call link 8
        link_8.bind('<Button-1>', lambda e: callback('https://www.youtube.com/watch?v=Oa_RSwwpPaA&list=PLDIoUOhQQPlUDNpjEYTTE9tb-QvUHUSMt'))
        callback('https://www.youtube.com/watch?v=Oa_RSwwpPaA&list=PLDIoUOhQQPlUDNpjEYTTE9tb-QvUHUSMt')


# Study Page
def create_study_page(root):
    clear_widgets(root)
    # place a title label
    Title_label = tk.Label(root, text='Study Buddy', font='Script 20', bg='black', fg='pink')
    Title_label.place(x=50, y=20)
    # place a return button on that page
    return_button = tk.Button(root, text='back', font='Script 16', bg='pink', fg='black', command=lambda:create_second_page(root))
    return_button.place(x=30, y=540)
    # create a button that leads to the first study-tip website
    study_tip1_button = tk.Button(root, text='Source 1', font='Arial 12', bg='pink', fg='black', command=lambda:callback('https://summer.harvard.edu/blog/top-10-study-tips-to-study-like-a-harvard-student/'))
    study_tip1_button.place(x=30, y=200)
    # create a button that will lead to the second study-tip website
    study_tip2_button = tk.Button(root, text='Source 2', font='Arial 12', bg='pink', fg='black', command=lambda: callback('https://www.futurelearn.com/courses/improving-study-techniques'))
    study_tip2_button.place(x=30, y=240)
    # create a button that will lead to the third study website
    study_tip3_button = tk.Button(root, text='Source 3', font='Arial 12', bg='pink', fg='black', command=lambda: callback('https://www.ox.ac.uk/students/news/2018-10-25-six-tips-studying-effectively'))
    study_tip3_button.place(x=30, y=280)
    # create the button for the fourth study website
    study_tip4_button = tk.Button(root, text='Source 4', font='Arial 12', bg='pink', fg='black', command=lambda: callback('https://www.math.ucdavis.edu/resources/learning/math-study-tips'))
    study_tip4_button.place(x=30, y=320)

    # create a title label
    website_field_label = tk.Label(root, text='Websites with study tips', font='Arial 12', bg='black', fg='white') # create the label for it
    website_field_label.place(x=30, y=130)

    # create a label for mental health websites
    mental_health_website_label = tk.Label(root, text='Websites for mental health', font='Arial 12', bg='black', fg='white')
    mental_health_website_label.place(x=220, y=130)
    # create a button for the first mental-health website
    mental_health_button_1 = tk.Button(root, text='Source 1', font='Arial 12', bg='Green', fg='black', command=lambda: callback('https://www.deutsche-depressionshilfe.de/krisentelefone'))
    mental_health_button_1.place(x=270, y=200)
    # create a button for the second mental health website
    mental_health_button_2 = tk.Button(root, text='Source 2', font='Arial 12', bg='Green', fg='black', command=lambda: callback('https://www.barmer.de/gesundheit-verstehen/psyche/psychische-gesundheit'))
    mental_health_button_2.place(x=270, y=240)
    # create a button for the third mental health website
    mental_health_button_3 = tk.Button(root, text='Mental Health Hotlines', font='Arial 12', bg='Green', fg='black', command=lambda: callback('https://www.therapyroute.com/article/suicide-hotlines-and-crisis-lines-in-germany'))
    mental_health_button_3.place(x=270, y=280)
    # create a button for the fourth mental health website
    mental_health_button_4 = tk.Button(root, text='Immediate Help in Crisis', font='Arial 12', bg='Green', fg='black', command=lambda: callback('https://psychenet.de/de/hilfe-finden/schnelle-hilfe/soforthilfe.html'))
    mental_health_button_4.place(x=270, y=320)

    # create a button for a website for finding reliable literature online
    study_button = tk.Button(root, text='Literature online', font='Arial 12', bg='gold', fg='black', command=lambda: callback('https://www.sweetsearch.com/'))
    study_button.place(x=300, y=460)

    # define a callback function to open hyperlinks
    # https://www.tutorialspoint.com/how-to-create-a-hyperlink-with-a-label-in-tkinter
    def callback(url):
            webbrowser.open_new_tab(url)
        # create the field for link 1
            link_1 = tk.Text(root, font='Arial 12', fg='white', text='https://summer.harvard.edu/blog/top-10-study-tips-to-study-like-a-harvard-student/')
            link_1.place(x=350, y=90)
        # call link_1
            link_1.bind('<Button-1>', lambda e: callback('https://summer.harvard.edu/blog/top-10-study-tips-to-study-like-a-harvard-student/'))
            callback('https://summer.harvard.edu/blog/top-10-study-tips-to-study-like-a-harvard-student/')
        # create the field for link 2
            link_2 = tk.Text(root, font='Arial 12', fg='white', text='https://www.futurelearn.com/courses/improving-study-techniques')
            link_2.place(x=390, y=90)
        # call link 2
            link_2.bind('<Button-1>', lambda e: callback('https://www.futurelearn.com/courses/improving-study-techmniques'))
            callback('https://www.futurelearn.com/courses/improving-study-techniques')
        # create the field for link 3
            link_3 = tk.Text(root, font='Arial 12', fg='white', text='https://www.ox.ac.uk/students/news/2018-10-25-six-tips-studying-effectively')
            link_3.place(x=400, y=90)
        # call link 3
            link_3.bind('<Button-1>', lambda e: callback('https://www.ox.ac.uk/students/news/2018-10-25-six-tips-studying-effectively'))
            callback('https://www.ox.ac.uk/students/news/2018-10-25-sic-tips-studying-effectively')
        # create the field for link 4
            link_4 = tk.Text(root, font='Arial 12', fg='white', text='https://www.math.ucdavis.edu/resources/learning/math-study-tips')
            link_4.place(x=410, y=90)
        # call link 4
            link_4.bind('<Button-1>', lambda e: callback('https://www.math.ucdavis-edu/resources/learning/math-study-tips'))
            callback('https://www.math.ucdavis-edu/resources/learning/math-study-tips')


show_user_data()
create_titlepage(root)
root.mainloop()
