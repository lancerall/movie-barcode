# Movie Barcode Python Script

This Python script takes a video file in .mkv or .mp4 format as input and generates a single JPEG image containing all of the frames of the video, scaled down to 1 pixel wide. The end result resembles a colorful "barcode" which is unique to the video file provided as input.

## Requirements

To run this script, you will need to have Python 3 and the `cv2` library installed. You can install `cv2` using the following command:

```pip install cv2```

Copy code

## Usage

To use this script, run the following command, replacing `video_file.mkv` with the path to your video file:

```python movie-barcode.py video_file.mkv```

This will generate an output file with a name based on the input video file's name and a .jpg extension. For example, if the input file is called `Aladdin.mkv`, the output file will be called `Aladdin.jpg`.

## Example Output

An example output file for this script is shown below:

![Aladdin](Aladdin.jpg)

Readme authored by ChatGPT.