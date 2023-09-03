from helper.utils import *


def main():
    """
    Download and crop YouTube videos based on provided information.

    Returns:
        None
    """
    links, file_names, starts, ends = read_videos_info()
    make_output_dir()
    for link, file_name, start, end in zip(links, file_names, starts, ends):
        try:
            print(f"{file_name} is processing...")
            video = download_youtube_vid(link)
            cropped_youtube_vid(video, start, end, file_name)
            print(f"{file_name} video saved Sucessfully...")
        except Exception as e:
            print(f"Error processing video {link}: {e}")


if __name__ == "__main__":
    main()
