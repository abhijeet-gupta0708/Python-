# Using SqLlite3 as data base

import sqlite3

#making a connection or creating a database name video in form of db

conn = sqlite3.connect("video.db")

#making a cursor or say a remote to work under the table

cursor=conn.cursor()

#making a table that consist a list in tabular manner

cursor.execute(''' CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY , name TEXT NOT NULL ,time TEXT NOT NULL)''')



def list_videos() :
    cursor.execute("SELECT *FROM  videos")
    for row in cursor.fetchall():
        print((row))

def add_video():
    cursor.execute("INSERT INTO  videos (name,time) VALUES(?,?)" ("new_name","new_time"))
    cursor.commit()

def update_video():
    cursor.execute("UPDATE videos SET name =? , time =? ,WHERE id =? ",("new_name","new_time","video_id"))
    cursor.commit()

def delete_video():
    cursor.execute("DELETE video WHERE id =?",("video_id"))

#main block 

def main():
    while True :
        videos=[]
        print("\n \n Starting main loop " )
        print("\n Welcome To Youtube Manager , Choose The appropiate Option : ")
        print("1: List all youtube  Videos :  ")
        print("2: Add a  youtube  Video :  ")
        print("3: Update  youtube  Video :  ")
        print("4: Delete a  youtube  Video :  ")
        print("5: Exit The App : ")
        choice=input("Enter Your choice : ")
        if choice=='1':
            list_videos()
        elif choice=='2':
           new_name=input("Enter the name of video : ")
           new_time=input("Enter the name of video : ")
           add_video(new_name,new_time)
        elif choice=='3':
           video_id=int(input("Enter the Video Id to update : "))
           new_name =input("Enter the name of video : ")
           new_time =input("Enter the name of video : ")
           update_video(video_id,new_name,new_time)
        elif choice=='4':
           video_id=int(input("Enter the Video Id to delete : "))
           delete_video(video_id)
        elif choice=='5':
            break
        else :
            print("Invalid Option")
        



if __name__ == "__main__":
    main()