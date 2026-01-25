import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except (FileNotFoundError , json.JSONDecodeError):
    
        return []
   
def save_data_helper(videos):
    with open('youtube.txt','w') as file :
        json.dump(videos,file)


def list_all_videos(videos):
    for index ,video in enumerate(videos,start=1):
        print(f"{index } ")


def addvideo(videos):
    name=input("Enter  The Name of the video")
    time=input("Enter the duration of the video")
    videos.append({'name':name , 'time':time})
    save_data_helper(videos)

def updatevideo():
    pass


def deletevideo():
    pass




def main():
    print("fd")
    while True :
        print("Starting main loop")
        videos=load_data()
        print("\n Welcome To Youtube Manager , Choose The appropiate Option")
        print("1: List all youtube Videos")
        print("2: Add a  youtube Videos")
        print("3: Update  youtube Videos")
        print("4: Delete a  youtube Videos")
        print("5: Exit The App-")
        choice=input("Enter Your choice \n")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                save_data_helper(videos)
                addvideo(videos)
            case '3':
                updatevideo()
            
            case '4':
                deletevideo()
            
            case '5':
                exit()
            case _:
                print("You Opted wrong Options ")
            
