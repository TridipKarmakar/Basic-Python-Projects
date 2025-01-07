import json 

def load_data() :
    try :
        with open("youtube.txt", "r") as file :
            return  json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos) :
    with open("youtube.txt", "w") as file :
        json.dump(videos, file)

def list_all_videos(videos) :
    for index , video in  enumerate(videos, start = 1) :
        print(f"{index}.")
     
def add_video(videos) :
    name = input("Enter the title of the video: ")
    time = input("Enter the duration of the video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos) :
    pass

def delete_video(videos) :
    pass

def list_all_videos(videos) :
    pass

def main() :
    videos = load_data()    
    while True :
        print("\n Youtube Manager | choose an option")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video details")
        print("4. Delete a video")
        print("5. Exit")
        print(videos)
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos) 
            case "2":
                add_video(videos)

            case "3":
                update_video(videos)

            case "4":
                delete_video(videos)

            case "5":
                break

if __name__ == "__main__" :
    main()
 