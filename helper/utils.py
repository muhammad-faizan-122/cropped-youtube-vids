import pytube
import os
import moviepy.editor as mp
import pandas as pd
import yaml


youtube_config_path = "config/youtube_vid_config.yml"
with open(youtube_config_path, "r") as file:
    yt_vid_consts = yaml.safe_load(file)


def make_output_dir():
    """
    creating output directory which contains the output json file
    """
    folder_name = "./data/output"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder {folder_name} created")
    else:
        print(f"Folder {folder_name} already exist")


def read_videos_info():
    """
    Read video information from a CSV file.

    Returns:
        tuple: A tuple containing lists of video links, file names, start times, and end times.
    """
    inp_csv_path = yt_vid_consts["inp_csv_file"]
    fake_vids_df = pd.read_csv(inp_csv_path)
    links, file_names = fake_vids_df["video"].values, fake_vids_df["video_name"].values
    starts, ends = fake_vids_df["start"].values, fake_vids_df["end"].values
    return links, file_names, starts, ends


def download_youtube_vid(vid_link):
    """
    Download a YouTube video.

    Args:
        vid_link (str): The YouTube video link.

    Returns:
        pytube.Stream: The downloaded video stream.
    """
    youtube = pytube.YouTube(vid_link)
    video = youtube.streams.filter(res=yt_vid_consts["resolution"]).first()
    video.download()
    return video


def cropped_youtube_vid(video, start, end, file_name):
    """
    Crop a downloaded YouTube video and save it.

    Args:
        video (pytube.Stream): The downloaded video stream.
        start (str): The start time for cropping.
        end (str): The end time for cropping.
        file_name (str): The desired name for the cropped video file.

    Returns:
        None
    """
    filename = video.default_filename
    video_clip = mp.VideoFileClip(filename).subclip(start, end)
    output_path = os.path.join(yt_vid_consts["output_cropped_vids"], f"{file_name}.mp4")
    video_clip.write_videofile(output_path, bitrate=yt_vid_consts["bitrate"])
    video_clip.close()
    os.remove(filename)
