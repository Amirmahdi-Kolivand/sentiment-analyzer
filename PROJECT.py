from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import sqlite3
import tkinter.font as tkfont
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from deep_translator import GoogleTranslator
from twilio.rest import Client
import random
from random import randint, randrange
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkfont
from datetime import datetime, timedelta
     
code=randrange(1000, 10000)
print(code)


#main
main=Tk()
main.geometry('700x400')
main.config(bg='#F8F8FA')
main.title('login')
font1 = tkfont.Font(family="Helvetica",size=15)
name_l=Label(main,text='name:',font=font1,bg='#F8F8FA',foreground='#30D180')
name_l.place(x=20,y=20)
name_e=Entry(main,bg='#CDC8FD',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='light green')
name_e.place(x=80,y=20)


user_l=Label(main,text='username:',font=font1,bg='#F8F8FA',foreground='#30D180')
user_l.place(x=20,y=100)
user_e=Entry(main,bg='#CDC8FD',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='light green')
user_e.place(x=120,y=100)
pass_l=Label(main,text='password:',font=font1,bg='#F8F8FA',foreground='#30D180')
pass_l.place(x=20,y=180)
pass_e=Entry(main,bg='#CDC8FD',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='light green')
pass_e.place(x=120,y=180)

def sign_up():
    font1 = tkfont.Font(family="Helvetica",size=15)
    A=Toplevel(main)
    A.geometry('700x550')
    A.config(bg='#F8F8FA')
    name_l=Label(A,text='name:',font=font1,bg='#F8F8FA',foreground='#30D180')
    name_l.place(x=20,y=20)
    name_e=Entry(A,bg='#C5F6CA',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='#CDC8FD')
    name_e.place(x=80,y=20)
    user_l=Label(A,text='username:',font=font1,bg='#F8F8FA',foreground='#30D180')
    user_l.place(x=20,y=100)
    user_e=Entry(A,bg='#C5F6CA',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='#CDC8FD')
    user_e.place(x=120,y=100)
    pass_l=Label(A,text='password:',font=font1,bg='#F8F8FA',foreground='#30D180')
    pass_l.place(x=20,y=180)
    pass_e=Entry(A,bg='#C5F6CA',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='#CDC8FD')
    pass_e.place(x=120,y=180)
    age_l=Label(A,text='age:',font=font1,bg='#F8F8FA',foreground='#30D180')
    age_l.place(x=20,y=260)
    age_s=Spinbox(A,from_=5,to=120,bg='#C5F6CA',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='#CDC8FD')
    age_s.place(x=70,y=260)
    gender_v=StringVar()
    gender_v.set(None)
    gender_l=Label(A,text='gender:',font=font1,bg='#F8F8FA',foreground='#30D180')
    gender_l.place(x=20,y=320)
    male_r=Radiobutton(A,text='male',activebackground='blue',variable=gender_v,value='male',bg='#C5F6CA',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='#CDC8FD')
    male_r.place(x=120,y=320)
    female_r=Radiobutton(A,text='female',activebackground='blue',variable=gender_v,value='female',bg='#C5F6CA',font=font1,highlightbackground='white',highlightthickness=2,foreground='#003333',highlightcolor='#CDC8FD')
    female_r.place(x=200,y=320)
    def save_data():
        name=name_e.get()
        age=age_s.get()
        gender=gender_v.get()
        username=user_e.get()
        password=pass_e.get()
        x=sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
        c=x.cursor()
        


        # Establish a connection to the database
        x = sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
        c = x.cursor()

        try:
            data_list = [(name, username, password, age, gender)]
            c.executemany('INSERT INTO user (name, username, password, age, gender) VALUES (?,?,?,?,?)', data_list)
        except sqlite3.IntegrityError:
            print("Error: Username already exists")
            
            return


        x.commit()
        x.close()
        A.destroy()
    savedata_b=Button(A,bg='blue',font=50,text='sign up',width=30,activebackground='light green',command=lambda:save_data())
    savedata_b.place(x=180,y=440)
    A.mainloop()

    
signup_b=Button(main,bg='sky blue',font=50,text='sign up',width=30,activebackground='light green',command=lambda:sign_up(),highlightbackground='white',highlightthickness=2,highlightcolor='light green')
signup_b.place(x=355,y=300)
def login():
    
    global username 
    global password
    username=user_e.get()
    password=pass_e.get()
    getty=name_e.get()
    

   
    x = sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
    c = x.cursor()
    c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
    rows = c.fetchall()
    if not rows:
        print("Invalid login details")
        messagebox.showerror("Login Error", "Invalid username or password")
    else:

        root=Toplevel(main)
        root.geometry('1000x1000')
        root.config(bg='#F8F8FA')
        font = tkfont.Font(family="Helvetica",size=15)

        analyze_t=Text(root,bg='#C5F6CA',font=8,highlightbackground='white',highlightthickness=3,foreground='#003333',highlightcolor='#CDC8FD',height=10)
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer







        
        
        




        def read():
            global username
            global password

            content = analyze_t.get("1.0", END)
            from matplotlib.figure import Figure
            from datetime import datetime

            def create_figure(timestamps, scores, username):
                # Convert timestamps to datetime objects for proper plotting
                formatted_timestamps = [datetime.strptime(ts, "%Y%m%d_%H%M%S") for ts in timestamps]

                # Create the figure
                fig = Figure(figsize=(5, 4), dpi=100)
                ax = fig.add_subplot(111)

                # Plot the data
                ax.plot(formatted_timestamps, scores, marker='o', linestyle='-', color='blue')
                ax.set_ylim(-10, 10)  # Set Y-axis range from -10 to 10
                ax.set_title(f"Sentiment Scores Over Time for {username}")
                ax.set_xlabel("Time")
                ax.set_ylabel("Sentiment Score")
                ax.grid()

                return fig

            

            # Initialize the sentiment analyzer
            analyzer = SentimentIntensityAnalyzer()

            # Example text
            

            # Analyze the text
            scores = analyzer.polarity_scores(content)

            # Map the compound score (-1 to 1) to the desired range (-10 to 10)
            scaled_score = scores['compound'] * 10

            # Print the result
            print(f"Sentiment score (scaled from -10 to 10): {scaled_score}")
                    
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            x = sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
            c = x.cursor()
            c.execute('''INSERT INTO sentiment_scores (username, timestamp, score) 
                        VALUES (?, ?, ?)''', (username, timestamp, scaled_score))
            x.commit()
            x.close()

            print("Sentiment score saved:", scaled_score)
                    

            x = sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
            c = x.cursor()
            c.execute("SELECT timestamp, score FROM sentiment_scores WHERE username=?", (username,))
            rows2 = c.fetchall()
            
            user_data = c.fetchone()
            print("User data fetched:", user_data)
            
            x = sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
            c = x.cursor()
            c.execute("SELECT score FROM sentiment_scores WHERE username=?", (username,))
            rows = c.fetchall()
            
            l=0
            s=0
            z=0
            p=0
            o=0

            # Convert the list of tuples to a list of floats
            i = [float(value[0]) for value in rows]
            c=len(i)
            for b in i:    
                if -2<=b<=2:
                    l=l+1
                    
                if 2<=b<=6:
                    s=s+1    
                if 6<=b<=10:
                    z=z+1
                if -6<=b<=-2:
                    p=p+1
                if -10<=b<=-6:
                    o=o+1
                print(b)
            print(o,p,z,s,l)
            mid=l/c*100
            
            good=s/c*100
            
            vgood=z/c*100
            
            bad=p/c*100
            
            vbad=o/c*100
            
            import numpy as np

            y = np.array([vgood,good,mid,bad,vbad])
            mylabels = ["very good sentiment", "good sentiment", "narutal senriment", "bad","very bad sentiment"]
            mycolors = ["green", "lightgreen", "grey", "lightcoral","red"]

            plt.pie(y, labels = mylabels, colors = mycolors)
            plt.show()  
                                    
            # Ensure timestamps and scores are fetched correctly
            timestamps = [row[0] for row in rows2]
            scores = [row[1] for row in rows2]

            # Convert timestamps to datetime
            formatted_timestamps = [datetime.strptime(ts, "%Y%m%d_%H%M%S") for ts in timestamps]

            fig = Figure(figsize=(10.3, 4), dpi=100)  # 5*2.5=12.5 (width), 4*1.5=6 (height)
            ax = fig.add_subplot(111)
            
            import numpy as np

        
            # Compute the average score and the standard deviation of the sentiment scores
            avg_score = np.mean(scores)
            std_dev = np.std(scores)
            
            # Define thresholds
            stable_threshold = 2.0  # Example threshold for determining stability
            negative_threshold = -0.5  # Threshold for considering negative sentiment
            positive_threshold = 0.5  # Threshold for considering positive sentiment
            if std_dev > stable_threshold:
                print("Unstable Sentiment")

                

          
            # Natural Sentiment
            
            
            # Unstable Sentiment

                
               

            # Convert the list of tuples to a list of floats
            i = [float(value[0]) for value in rows]
            # Plot segments with appropriate colorsfig = Figure(figsize=(10.3, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(formatted_timestamps, scores, marker='o', linestyle='-', color='blue')
            ax.set_title("Test Sentiment Scores")
            ax.set_xlabel("Time")
            ax.set_ylabel("Sentiment Score")
            ax.grid()

            # Embed the graph
            fig = create_figure(timestamps, scores, username)
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas_widget = canvas.get_tk_widget()

            # Use .place() to position the canvas
            canvas_widget.place(x=0, y=300, width=800, height=500)

            # Draw the canvas
            canvas.draw()
              # Stable Negative Sentiment
            if avg_score < negative_threshold and std_dev < stable_threshold:
                print("Stable Negative Sentiment")
            
            # Stable Positive Sentiment
            elif avg_score > positive_threshold and std_dev < stable_threshold:
                print("Stable Positive Sentiment")
            
            # Temporary Negative Sentiment
            elif scaled_score < 0 and std_dev > stable_threshold:
                print("Temporary Negative Sentiment")
            print(std_dev)
            print("Formatted Timestamps:", formatted_timestamps)
            import tkinter as tk
            from tkinter import ttk
            from datetime import datetime
            import random

            root1 = tk.Tk()
            root1.title("5x6 Button Grid with Challenges")
            root1.geometry("900x900")  # Adjust the window size to fit the grid
            
            # Function to handle button click and change the right side background color
            def on_button_click(button_number):
                day_index = button_number - 1  # Button number corresponds to day index (0-based)
                
                # Get the challenge set for the current day
                selected_challenges = challenges_sets[day_index]
                
                # Display the selected challenges in the label
                challenges_label.config(text="\n".join(selected_challenges))
                
                # Add the tasks with checkboxes
                update_task_list(selected_challenges)

                # Update button state to allow the next button to be clickable
                update_button_state()

                # Update the progress bar after button click
                update_progress()
            # Function to update task list with checkboxes
            def update_task_list(selected_challenges):
                # Clear the existing checkboxes
                for checkbox in task_checkboxes:
                    checkbox.destroy()
                
                # Create a list of checkboxes for each task
                for i, task in enumerate(selected_challenges):
                    var = tk.IntVar()
                    checkbox = tk.Checkbutton(right_frame, text=task, variable=var)
                    checkbox.place(x=10, y=100 + i * 30)
                    task_checkboxes.append(checkbox)
                    task_variables.append(var)
                    progressbar.step(0.8)

            progressbar = ttk.Progressbar(root1,orient=tk.VERTICAL, length=900)
            progressbar.place(x=0, y=800)


            # Function to update progress bar based on the number of buttons clicked
            def update_progress():
                # Count how many buttons have been clicked (i.e., enabled)
                completed_buttons = sum(1 for button in buttons if button.cget('state') == 'normal')
                
                # Update the progress bar
                

            # Create the main Tkinter window

            # Button dimensions
            button_width = 8
            button_height = 2
            button_spacing = 5  # Space between buttons

            # Create a frame for the right side of the window
            right_frame = tk.Frame(root1, width=400, height=900, bg="white")
            right_frame.place(x=500, y=0)

            # Create a label in the right frame to display the challenges
            challenges_label = tk.Label(right_frame, text="", font=("Helvetica", 12), justify="left")
            challenges_label.place(x=10, y=20)

            # Create a list to store task checkboxes and their variables
            task_checkboxes = []
            task_variables = []

            # 4 challenges for making unstable sentiment stable (Challenge sets for 2-day intervals)
            c# Define challenge sets for all 30 days
            challenges_sets = [
                # Day 1
                [
                    "1. Meditation for 5 minutes.",
                    "2. Write down your emotions.",
                    "3. Do 10 push-ups.",
                    "4. Read 10 pages of a book."
                ],
                # Day 2
                [
                    "1. Call a friend to talk.",
                    "2. Practice deep breathing for 5 minutes.",
                    "3. Write 3 things you're grateful for.",
                    "4. Do a 10-minute stretching session."
                ],
                # Day 3
                [
                    "1. Take a 15-minute walk outside.",
                    "2. Journal your thoughts.",
                    "3. Try yoga for 10 minutes.",
                    "4. Listen to calming music."
                ],
                # Day 4
                [
                    "1. Practice mindfulness for 10 minutes.",
                    "2. Read a motivational article.",
                    "3. Organize your workspace.",
                    "4. Drink 2 liters of water."
                ],
                # Day 5
                [
                    "1. Write down a positive affirmation.",
                    "2. Take a 30-minute break from screens.",
                    "3. Meditate for 10 minutes.",
                    "4. Try a new recipe."
                ],
                # Day 6
                [
                    "1. Call a family member.",
                    "2. Do 20 squats.",
                    "3. Write in your gratitude journal.",
                    "4. Reflect on your goals."
                ],
                # Day 7
                [
                    "1. Spend 15 minutes on a creative activity.",
                    "2. Practice deep breathing.",
                    "3. Do a random act of kindness.",
                    "4. Reflect on your week."
                ],
                # Day 8
                [
                    "1. Take a walk in nature.",
                    "2. Try journaling your emotions.",
                    "3. Stretch for 10 minutes.",
                    "4. Read a chapter of a book."
                ],
                # Day 9
                [
                    "1. Call a friend and check in.",
                    "2. Do a 10-minute workout.",
                    "3. Practice gratitude for 3 things.",
                    "4. Listen to an inspiring podcast."
                ],
                # Day 10
                [
                    "1. Meditate for 15 minutes.",
                    "2. Try a new hobby.",
                    "3. Do 15 minutes of yoga.",
                    "4. Reflect on your progress."
                ],
                # Day 11
                [
                    "1. Do 20 minutes of cardio.",
                    "2. Write a list of your strengths.",
                    "3. Spend time outdoors.",
                    "4. Eat a healthy meal."
                ],
                # Day 12
                [
                    "1. Do a creative activity.",
                    "2. Practice mindfulness for 10 minutes.",
                    "3. Drink 2 liters of water.",
                    "4. Take a 20-minute nap."
                ],
                # Day 13
                [
                    "1. Call someone you care about.",
                    "2. Do 10 push-ups.",
                    "3. Write down your goals for the month.",
                    "4. Read for 15 minutes."
                ],
                # Day 14
                [
                    "1. Reflect on your progress this week.",
                    "2. Take a break from social media.",
                    "3. Organize your living space.",
                    "4. Try deep breathing for 5 minutes."
                ],
                # Day 15
                [
                    "1. Meditate for 10 minutes.",
                    "2. Try a new workout.",
                    "3. Call a friend to catch up.",
                    "4. Practice gratitude."
                ],
                # Day 16
                [
                    "1. Read a book for 20 minutes.",
                    "2. Practice mindfulness.",
                    "3. Write a letter to yourself.",
                    "4. Take a walk in nature."
                ],
                # Day 17
                [
                    "1. Do a 10-minute stretch.",
                    "2. Drink a glass of water every hour.",
                    "3. Reflect on your achievements.",
                    "4. Listen to a calming podcast."
                ],
                # Day 18
                [
                    "1. Take a 30-minute walk outside.",
                    "2. Practice yoga for 15 minutes.",
                    "3. Do a random act of kindness.",
                    "4. Write a list of your goals."
                ],
                # Day 19
                [
                    "1. Write in your gratitude journal.",
                    "2. Call a loved one.",
                    "3. Do 30 minutes of cardio.",
                    "4. Read a motivational article."
                ],
                # Day 20
                [
                    "1. Reflect on your growth.",
                    "2. Do 10 minutes of deep breathing.",
                    "3. Organize your desk.",
                    "4. Meditate for 10 minutes."
                ],
                # Day 21
                [
                    "1. Try a new recipe.",
                    "2. Practice mindfulness for 15 minutes.",
                    "3. Spend time in nature.",
                    "4. Call a friend to talk."
                ],
                # Day 22
                [
                    "1. Do a 20-minute workout.",
                    "2. Write a positive affirmation.",
                    "3. Take a break from screens.",
                    "4. Listen to calming music."
                ],
                # Day 23
                [
                    "1. Do 10 push-ups.",
                    "2. Read for 20 minutes.",
                    "3. Reflect on your accomplishments.",
                    "4. Try yoga for 10 minutes."
                ],
                # Day 24
                [
                    "1. Meditate for 10 minutes.",
                    "2. Write a list of things you're grateful for.",
                    "3. Take a 15-minute walk.",
                    "4. Call someone you trust."
                ],
                # Day 25
                [
                    "1. Reflect on your goals.",
                    "2. Do 30 minutes of cardio.",
                    "3. Practice mindfulness for 10 minutes.",
                    "4. Read a chapter of a book."
                ],
                # Day 26
                [
                    "1. Call a family member.",
                    "2. Do a random act of kindness.",
                    "3. Try a new hobby.",
                    "4. Spend time outdoors."
                ],
                # Day 27
                [
                    "1. Practice deep breathing.",
                    "2. Reflect on your week.",
                    "3. Write a positive affirmation.",
                    "4. Try yoga for 15 minutes."
                ],
                # Day 28
                [
                    "1. Do a creative activity.",
                    "2. Spend time with loved ones.",
                    "3. Meditate for 10 minutes.",
                    "4. Write a letter to yourself."
                ],
                # Day 29
                [
                    "1. Take a walk in nature.",
                    "2. Reflect on your journey so far.",
                    "3. Call a friend to check in.",
                    "4. Try a new workout."
                ],
                # Day 30
                [
                    "1. Reflect on your month.",
                    "2. Set new goals for the next month.",
                    "3. Practice gratitude for 3 things.",
                    "4. Spend time doing something creative."
                ]
            ]


            # Create buttons in a 5x6 grid (5 rows and 6 columns)
            buttons = []  # To store button references
            for row in range(5):  # 5 rows
                for col in range(6):  # 6 columns
                    button_number = row * 6 + col + 1  # Calculate the button number (1 to 30)
                    
                    # Create a button
                    button = tk.Button(root1, text=str(button_number), width=button_width, height=button_height, bg="blue", fg="white", command=lambda button_number=button_number: on_button_click(button_number))
                    
                    # Initially disable all buttons
                    button.config(state=tk.DISABLED)

                    # Calculate the x and y positions based on the row and column
                    x_pos = col * (button_width * 10 + button_spacing)
                    y_pos = row * (button_height * 20 + button_spacing)
                    button.place(x=x_pos, y=y_pos)
                    
                    # Add button to the list
                    buttons.append(button)

            # Enable buttons in order (sequentially, one by one)
            for i, button in enumerate(buttons):
                button.config(state=tk.NORMAL if i == 0 else tk.DISABLED)  # Enable only the first button initially

            # Function to update button state after a click
            def update_button_state():
                for i, button in enumerate(buttons):
                    if button.cget('state') == 'normal' and i + 1 < len(buttons):
                        buttons[i + 1].config(state=tk.NORMAL)  # Enable the next button after the current one

            # Add a progress bar at the bottom of the right frame, with the same width as the right frame
            progress_bar = ttk.Progressbar(right_frame, length=400, maximum=100, mode='determinate')
            progress_bar.place(x=10, y=800)

            # Update button state after a click
            def on_button_click(button_number):
                # Change the background color of the right side frame to sky blue
                right_frame.config(bg="skyblue")
                
                # Determine the challenge set based on the button number clicked
                challenge_set_index = (button_number - 1) // 2  # Determine which challenge set to use (2-day intervals)
                
                # Get a random selection of 4 tasks from the selected challenge set (without repetition)
                selected_challenges = random.sample(challenges_sets[challenge_set_index], 4)
                
                # Display the selected challenges in the label
                challenges_label.config(text="\n".join(selected_challenges))
                
                # Add the tasks with checkboxes
                update_task_list(selected_challenges)

                # Update button state to allow the next button to be clickable
                update_button_state()

                # Update the progress bar after button click
                update_progress()
            a = Tk()
            a.geometry('1000x1000')
            a.config(bg='#F8F8FA')
            font1 = tkfont.Font(family="Helvetica", size=15)
            #Frame widget to hold the listbox and the scrollbar
            frame_task=Frame(a)
            frame_task.pack()
            #to hold items in a listbox
            listbox_task=Listbox(frame_task,bg="black",fg="white",height=15,width=50,font = "Helvetica")  
            listbox_task.pack(side=LEFT)
            #Scrolldown in case the total list exceeds the size of the given window 
            scrollbar_task=Scrollbar(frame_task)
            scrollbar_task.pack(side=RIGHT,fill=Y)
            listbox_task.config(yscrollcommand=scrollbar_task.set)
            scrollbar_task.config(command=listbox_task.yview)

            def entertask():
                input_text = ""

                def add():
                    input_text = entry_task.get(1.0, "end-1c")
                    if input_text == "":
                        messagebox.showwarning(title="Warning!", message="Please Enter some Text")
                    else:
                        listbox_task.insert(END, input_text)
                        root1.destroy()

                root1 = Tk()
                root1.title("Add task")
                entry_task = Text(root1, width=40, height=4)
                entry_task.place(x=20, y=20)
                button_temp = Button(root1, text="Add task", command=add)
                button_temp.place(x=20, y=100)
                root1.mainloop()

            def deletetask():
                selected = listbox_task.curselection()
                if selected:
                    listbox_task.delete(selected[0])
                else:
                    messagebox.showwarning("Warning", "No task selected to delete.")

            def markcompleted():
                marked = listbox_task.curselection()
                if marked:
                    temp = marked[0]
                    temp_marked = listbox_task.get(marked)
                    temp_marked = temp_marked + " ✔"
                    listbox_task.delete(temp)
                    listbox_task.insert(temp, temp_marked)
                else:
                    messagebox.showwarning("Warning", "No task selected to mark as completed.")

            b1=Button(a, text="Add Task", command=entertask, width=20).place(x=800, y=150)
            b2=Button(a, text="Delete Selected Task", command=lambda:deletetask(), width=20).place(x=800, y=200)
            b3=Button(a, text="Mark as Completed", command=lambda:markcompleted(), width=20).place(x=800, y=250)

            # Priority Sections (using .place() for positioning)
            def start_countdown(label, end_time):
                def update():
                    now = datetime.now()
                    remaining = end_time - now
                    if remaining.total_seconds() > 0:
                        label.config(text=str(remaining).split(".")[0])  # Show HH:MM:SS
                        label.after(1000, update)  # Update every second
                    else:
                        label.config(text="Time's up!")
                update()

            def set_priority_countdown(entry, label):
                try:
                    end_time_str = entry.get()
                    end_time = datetime.strptime(end_time_str, "%H:%M:%S").replace(
                        year=datetime.now().year,
                        month=datetime.now().month,
                        day=datetime.now().day
                    )
                    if end_time < datetime.now():
                        end_time += timedelta(days=1)  # Handle times past midnight
                    start_countdown(label, end_time)
                except ValueError:
                    messagebox.showerror("Error", "Please enter time in HH:MM:SS format")

            # Priority 1 Section
            firstp_l = Label(a, text='First priority:', font=font1, bg='#F8F8FA', foreground='#30D180')
            firstp_l.place(x=50, y=400)
            firstp_e = Entry(a, bg='#CDC8FD', font=font1, highlightbackground='white', highlightthickness=2,
                            foreground='#003333', highlightcolor='light green')
            firstp_e.place(x=150, y=400)
            firstp_timer_label = Label(a, text="Timer:", font=font1, bg='#F8F8FA', foreground='#30D180')
            firstp_timer_label.place(x=400, y=400)
            firstp_timer_entry = Entry(a, bg='#CDC8FD', font=font1, highlightbackground='white', highlightthickness=2,
                                    foreground='#003333', highlightcolor='light green')
            firstp_timer_entry.place(x=500, y=400)
            firstp_timer_display = Label(a, text="", font=font1, bg='#F8F8FA', foreground='red')
            firstp_timer_display.place(x=700, y=400)
            firstp_button = Button(a, text="Start First Priority Timer",
                                command=lambda: set_priority_countdown(firstp_timer_entry, firstp_timer_display))
            firstp_button.place(x=500, y=430)

            # Priority 2 Section
            secondp_l = Label(a, text='Second priority:', font=font1, bg='#F8F8FA', foreground='#30D180')
            secondp_l.place(x=50, y=475)
            secondp_e = Entry(a, bg='#CDC8FD', font=font1, highlightbackground='white', highlightthickness=2,
                            foreground='#003333', highlightcolor='light green')
            secondp_e.place(x=150, y=475)
            secondp_timer_label = Label(a, text="Timer:", font=font1, bg='#F8F8FA', foreground='#30D180')
            secondp_timer_label.place(x=400, y=475)
            secondp_timer_entry = Entry(a, bg='#CDC8FD', font=font1, highlightbackground='white', highlightthickness=2,
                                        foreground='#003333', highlightcolor='light green')
            secondp_timer_entry.place(x=500, y=475)
            secondp_timer_display = Label(a, text="", font=font1, bg='#F8F8FA', foreground='red')
            secondp_timer_display.place(x=700, y=475)
            secondp_button = Button(a, text="Start Second Priority Timer",
                                    command=lambda: set_priority_countdown(secondp_timer_entry, secondp_timer_display))
            secondp_button.place(x=500, y=505)

            # Priority 3 Section
            thirdp_l = Label(a, text='Third priority:', font=font1, bg='#F8F8FA', foreground='#30D180')
            thirdp_l.place(x=50, y=550)
            thirdp_e = Entry(a, bg='#CDC8FD', font=font1, highlightbackground='white', highlightthickness=2,
                            foreground='#003333', highlightcolor='light green')
            thirdp_e.place(x=150, y=550)
            thirdp_timer_label = Label(a, text="Timer:", font=font1, bg='#F8F8FA', foreground='#30D180')
            thirdp_timer_label.place(x=400, y=550)
            thirdp_timer_entry = Entry(a, bg='#CDC8FD', font=font1, highlightbackground='white', highlightthickness=2,
                                    foreground='#003333', highlightcolor='light green')
            thirdp_timer_entry.place(x=500, y=550)
            thirdp_timer_display = Label(a, text="", font=font1, bg='#F8F8FA', foreground='red')
            thirdp_timer_display.place(x=700, y=550)
            thirdp_button = Button(a, text="Start Third Priority Timer",
                                command=lambda: set_priority_countdown(thirdp_timer_entry, thirdp_timer_display))
            thirdp_button.place(x=500, y=580)
            a.mainloop()
            # Run the Tkinter event loop
            root.mainloop()
            # Main window setup



        savetext_b = Button(root, text='save and analyze', command=lambda:read(),bg='sky blue',font=50,width=30,activebackground='light green',highlightbackground='white',highlightthickness=2,highlightcolor='light green')
        savetext_b.place(x=0, y=225)

            
            
            




        analyze_t.place(x=0,y=0)











        root.mainloop()




login_b=Button(main,bg='sky blue',font=50,text='log in',width=30,activebackground='light green',command=lambda:login(),highlightbackground='white',highlightthickness=2,highlightcolor='light green',)
login_b.place(x=5,y=300)

main.mainloop()