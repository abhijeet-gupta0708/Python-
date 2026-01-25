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
        print(f"{index }.{video['name']} , duration{video['time']} ")


def addvideo(videos):
    name=input("Enter  The Name of the video : ")
    time=input("Enter the duration of the video : ")
    videos.append({'name':name , 'time':time})
    save_data_helper(videos)

def updatevideo(videos):
    list_all_videos(videos)
    index=int(input("Enter the Video Number you want to update : "))
    if 1<=index<=len(videos):
        name=input("ENter the New name of Video : ")
        time=input("Enter the duration of the video : ")
        videos[index-1]={'name':name ,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index of video")

def deletevideo(videos):
    list_all_videos(videos)
    index=int(input("Enter the Video Number you want to delete : "))
    if 1<=index<=len(videos):
        del(videos[index-1])
    else:
        print("Invalid input")
    save_data_helper(videos)


def main():
    while True :
        print("\n \n Starting main loop")
        videos=load_data()
        # print(videos)
        print("\n Welcome To Youtube Manager , Choose The appropiate Option : ")
        print("1: List all youtube  Videos :  ")
        print("2: Add a  youtube  Video :  ")
        print("3: Update  youtube  Video :  ")
        print("4: Delete a  youtube  Video :  ")
        print("5: Exit The App : ")
        choice=input("Enter Your choice : ")
        match choice:
            case '1':
                list_all_videos(videos)
                print(videos)
            case '2':
                addvideo(videos)
                save_data_helper(videos)
            case '3':
                updatevideo(videos)
            
            case '4':
                deletevideo(videos)
            
            case '5':
                exit()
            case _:
                print("You Opted wrong Options ")
            
if __name__=="__main__":
    main()

