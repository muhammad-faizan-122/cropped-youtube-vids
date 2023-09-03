from helper.utils import *


def crop_youtube_videos(links, file_names, starts, ends):
    """
    Download and crop YouTube videos based on provided information.

    Args:
        links (list): List of YouTube video links.
        file_names (list): List of desired file names for the output videos.
        starts (list): List of start times for cropping each video.
        ends (list): List of end times for cropping each video.

    Returns:
        None
    """

    for link, file_name, start, end in zip(links, file_names, starts, ends):
        try:
            print(f"{file_name} is processing...")
            video = download_youtube_vid(link)
            cropped_youtube_vid(video, start, end, file_name)
            print(f"{file_name} video saved Sucessfully...")
        except Exception as e:
            print(f"Error processing video {link}: {e}")


if __name__ == "__main__":
    links, names, strts, ends = read_videos_info()
    crop_youtube_videos(links, names, strts, ends)
