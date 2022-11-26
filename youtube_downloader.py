import os
import yt_dlp
import moviepy.editor as moviepy

cur_dir = os.getcwd()
download_dir = os.path.join(cur_dir, "downloads")


def download_video(link,  video_id):
    youtube_dl_options = {
        'format_sort': ['res:1080', 'ext:mp4:m4a']
        #"outtmpl": video_path(video_id),
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        return ydl.download([link])


def mp4_to_mp3(mp4, mp3):
    try:
        mp4_without_frames = moviepy.AudioFileClip(mp4)
        mp4_without_frames.write_audiofile(mp3)
        mp4_without_frames.close()
        return 0
    except Exception as e:
        return 1


def get_title(link):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(link, download=False)
        return info_dict.get('title', None)


def video_path(video_id):
    return os.path.join(download_dir, f"{video_id}.mp4")


def audio_path(video_id):
    return os.path.join(download_dir, f"{video_id}.mp3")
