⚠️ NOTE 1: I am junior python programmer still learning and The project was done within one week so it is highly likely it might have a lot of bugs, some functions also may not work as supposed to. Therefore any contribution is welcomed!

FEATURES:

        User Authentication:

            A user can register by providing his/her name, username, password, age, and gender.
            User's credentials are securely stored in SQLite Database.
            It allows only authenticated users to log in.

        Sentiment Analysis:

            Users will input text for which VADER's SentimentIntensityAnalyzer analyzes the sentiment.
            Sentiments are stored in SQLite Database and visualized with Matplotlib.
            A pie chart shows the sentiments categorized as very good, good, neutral, bad, and very bad.
            Time-series analysis of sentiment is tracked over time.

        Task & Priority Management:

            Todo list: allow adding, deleting, and marking tasks as completed
            Three levels of priorities: high, medium, low, with countdown timers.
            Challenge System: A structured 30-day challenge to build positive habits.
            Track daily progress using an interactive button grid.
    
        Tech Stack:

            Python: GUI-based application, Tkinter
            Database: SQLite
            Data Visualization: Matplotlib
            Sentiment Analysis: VADER SentimentIntensityAnalyzer
    
        Libraries Used:

            tkinter - To display the GUI components
            sqlite3- Database management
            matplotlib - Graph and sentiment visualization
            numpy - For numerical computations
            vaderSentiment - Sentiment analysis
            random - Random code generation
            datetime - Handling time function
⚠️ NOTE 2:  This project was developed with the assistance of ChatGPT and Google (as all programmers do). However, the core idea and the main implementation are my own. Feel free to use my code or build upon the idea!
