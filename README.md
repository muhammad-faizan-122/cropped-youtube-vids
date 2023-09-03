# Description
If you want to download the cropped the youtube video, you can easily do.

# Usage
- If you have conda, just run following command to create conda virtual env as well install the requirements require to run the code.
    ```
    conda env export > environment.yml
    ```
- other-wise you can just run in following commands in your virtual env
    ```
    pip install -r requirements.txt
    ```
- You need to add all videos in **data/input/youtube_vids_data.csv** which you want to cropped.
    - video: Represents link of youtube video. e.g (https://www.youtube.com/watch?v=oxXpB9pSETo)
    - start: Represents start time of video.  e.g 0:00:00
    - end: Represents end time of video. e.g 0:00:44
    - video_name: Represents what name you want to set without extension. e.g Freeman
- To run 
    ```
    python3 main.py
    ```
- output cropped videos saved in **data/output**.