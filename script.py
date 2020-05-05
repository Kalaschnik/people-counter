import pandas as pd
from video_indexer import VideoIndexer

with open("subkey.txt") as f:
    subkey = f.readline()

with open("account.txt") as f:
    account = f.readline()

CONFIG = {
    "SUBSCRIPTION_KEY": subkey,
    "LOCATION": "Trial",
    "ACCOUNT_ID": account,
}

vi = VideoIndexer(
    vi_subscription_key=CONFIG["SUBSCRIPTION_KEY"],
    vi_location=CONFIG["LOCATION"],
    vi_account_id=CONFIG["ACCOUNT_ID"],
)

# uploaded videos (video1, video2, video3)
video_ids = ["2a8d248604", "ed2f2ff084", "613b1ba225"]

# Upload video for indexing
# video_id = vi.upload_to_video_indexer(
#    input_filename='some-video.mp4',
#    video_name='some-video-name',  # identifier for video in Video Indexer platform, must be unique during indexing time
#    video_language='English'
# )

face_array = []
# iterate over all videos
for video in video_ids:
    # store response
    response = vi.get_video_info(video, video_language="German")
    face_array.append(len(response["summarizedInsights"]["faces"]))


print(face_array)

video_df = pd.read_csv("data.csv", sep=";")
video_df["faces"] = pd.Series(face_array)
video_df.to_csv("data.tsv", sep="\t")

print(video_df)
