from models.Video import Video

class VideoRepository:
    
    def __init__(self):
        self.__videos = []

    def add_video(self, video):
        # first add to file then to private list
        with open("./data/videos.txt", "a+") as videos_file:
            title = video.get_title()
            genre = video.get_genre()
            length = video.get_length()
            videos_file.write("{},{},{}\n".format(title, genre, length))

    def get_videos(self):
        if self.__videos == []:
            with open("./data/videos.txt", "r") as video_file:
                for line in video_file.readlines():
                    title, genre, length = line.split(",")
                    new_video = Video(title, genre, length)
                    self.__videos.append(new_video)    
        
        return self.__videos

