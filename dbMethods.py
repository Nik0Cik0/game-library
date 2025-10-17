import sqlite3

def createTables():
    conn = sqlite3.connect('database.sql', timeout=10)
    c = conn.cursor()
    
    # SQL statement to create the Users table
    SQL_statement1 = """
    CREATE TABLE IF NOT EXISTS Users(
        User_ID INTEGER PRIMARY KEY,
        Username VARCHAR(50) NOT NULL,
        Password VARCHAR(50) NOT NULL,
        Email VARCHAR(50),
        Class INT,
        SubClass VARCHAR(10),
        BirthDate DATE,
        Description VARCHAR(500),
        XP INTEGER DEFAULT 0,
        ProfilePicture BLOB
    );
    """
    
    # SQL statement to create the Courses table
    SQL_statement2 = """
    CREATE TABLE IF NOT EXISTS Courses (
        Course_ID INTEGER PRIMARY KEY,
        Course_Name VARCHAR(100) NOT NULL,
        Hours INT,
        Level VARCHAR(50),
        Description VARCHAR(500),
        Color VARCHAR(6),
        TColor VARCHAR(6),
        Icon BLOB
    );
    """

    # SQL statement to create the Lessons table
    SQL_statement3 = """
    CREATE TABLE IF NOT EXISTS Lessons (
        Lesson_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Course_ID INTEGER,
        Title TEXT NOT NULL,
        Description TEXT,
        Content TEXT,
        FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
    );
    """

    # SQL statement to create the Progress table
    SQL_statement4 = """
    CREATE TABLE IF NOT EXISTS Progress(
        Progress_ID INTEGER PRIMARY KEY,
        User_ID INTEGER,
        Lesson_ID INTEGER,
        Description VARCHAR(500),
        Status VARCHAR(50) DEFAULT 'not started',
        FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
        FOREIGN KEY (Lesson_ID) REFERENCES Lessons(Lesson_ID)
    );
    """

    # SQL statement to create the Games table
    SQL_statement5 = """
    CREATE TABLE IF NOT EXISTS Games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        icon_image VARCHAR(200) NOT NULL,
        html_file VARCHAR(200) NOT NULL
    );
    """

    # Execute all SQL statements
    c.execute(SQL_statement1)
    c.execute(SQL_statement2)
    c.execute(SQL_statement3)
    c.execute(SQL_statement4)
    c.execute(SQL_statement5)  # Create the Games table

    conn.commit()  # Commit the changes
    c.close()  # Close the cursor
    conn.close()  # Close the connection
