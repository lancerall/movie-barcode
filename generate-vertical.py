import argparse
import cv2
import os
import time
import sys
import numpy as np

def format_duration(seconds: int) -> str:
    # Convert seconds to minutes
    minutes, seconds = divmod(seconds, 60)

    # Convert minutes to hours
    hours, minutes = divmod(minutes, 60)

    # Convert hours to days
    days, hours = divmod(hours, 24)

    # Initialize the duration string
    duration = ""

    # Add days to the duration string
    if days > 0:
        duration += f"{days} days "

    # Add hours to the duration string
    if hours > 0:
        duration += f"{hours} hours "

    # Add minutes to the duration string
    if minutes > 0:
        duration += f"{minutes:.0f} minutes "

    # Add seconds to the duration string
    if seconds > 0:
        duration += f"{seconds:.2f} seconds"

    # Return the duration string
    return duration


# parse the command line argument
parser = argparse.ArgumentParser()
parser.add_argument("video_file", help="name of the mkv video file")
args = parser.parse_args()

# Open the video file
video = cv2.VideoCapture(args.video_file)

# Check if the video file was opened successfully
if not video.isOpened():
    print("Error opening video file")
    sys.exit()

# Get the number of frames in the video
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"{num_frames} frames")

# get the width and height of the frames in the video
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# calculate the number of frames needed to reach the desired width
keyframes = int(num_frames / width)

print(f"Final image {width}px x {height}px, key every {keyframes}")

# create an empty image
result_image = np.zeros((height, 1, 3), dtype=np.uint8)

start_time = time.time()
# iterate through the frames in the video
frame_count = 0
while True:
    # read the next frame
    success, frame = video.read()

    # if we have reached the end of the video, break out of the loop
    if not success:
        break

    # increment the frame count
    frame_count += 1

    # if we have reached the desired number of frames, reset the frame count and
    # clear the result image
    if frame_count % keyframes == 0:
        # scale the frame to 1 pixel wide
        frame = cv2.resize(frame, (1, height))

        # add the frame to the result image
        result_image = cv2.hconcat([result_image, frame])

        end_time = time.time()
        elapsed_time = end_time - start_time
        time_per_frame = elapsed_time / frame_count
        # print(f"Time per row: {time_per_row:.3f}")
        remaining_frames = num_frames - frame_count
        # print(f"Remaining rows: {remaining_rows:.3f}")
        remaining_time = remaining_frames * time_per_frame
        print(f"{frame_count}/{num_frames} ({round(frame_count / num_frames * 100, 2):.2f}%): {elapsed_time:.1f}s elapsed, {format_duration(remaining_time)} remaining...")

# generate the output file name
output_file = os.path.splitext(args.video_file)[0] + ".jpg"

# save the result image to the output file
cv2.imwrite(output_file, result_image)
