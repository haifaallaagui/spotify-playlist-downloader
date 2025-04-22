# Spotify Playlist Scraper and YouTube Music Downloader

This Python project automates the process of scraping songs from a Spotify playlist, searching for their corresponding videos on YouTube, and downloading them as MP3 files. It uses `Selenium` for web scraping, `youtubesearchpython` to search YouTube, and `yt-dlp` to download audio from the videos.

## Features
- **Spotify Web Scraping:** Scrapes song titles and artists from a Spotify playlist.
- **YouTube Search:** Finds YouTube videos for each song.
- **Audio Downloading:** Downloads audio from the YouTube videos in MP3 format.

## Prerequisites

1. **Python 3.8+** is required.
2. **Google Chrome** browser.
3. **ChromeDriver**: The ChromeDriver must be downloaded and its path specified in the script.
4. **Required Python Libraries**:
   - `selenium`
   - `pandas`
   - `youtubesearchpython`
   - `yt-dlp`
   - `argparse`
   - `time`

To install the necessary libraries, run:

```bash
pip install selenium pandas youtubesearchpython yt-dlp
```

## Setup Instructions

1. **ChromeDriver:**
   Download the correct version of ChromeDriver for your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a known directory.

## Usage

### Command-Line Arguments

- `-u`, `--url`: The URL of the Spotify playlist you want to scrape.
- `-o`, `--output`: The path where the scraped song data will be saved in CSV format.

### Example Usage

```bash
python script.py -u "https://open.spotify.com/playlist/your_playlist_url" -o "output.csv"
```

This will:
1. Scrape the song titles and artist names from the provided Spotify playlist URL.
2. Save the results into a CSV file (specified by the `-o` argument).
3. Search for corresponding YouTube videos.
4. Download the MP3 files to the specified directory in the script.

### Detailed Steps

1. **Scraping the Spotify Playlist:**
   The script uses Selenium to open the Spotify playlist URL and scrolls through the page to load all songs. It extracts the song titles and artist names, saving them to a CSV file.

2. **YouTube Search:**
   For each song in the playlist, the script searches for a matching video on YouTube using the `youtubesearchpython` library. It retrieves the first result and stores the video URLs.

3. **Downloading MP3 Files:**
   The script downloads the best available audio from YouTube videos using `yt-dlp` and saves them as MP3 files in the directory specified in the `download()` function.


## Notes

- Ensure that the ChromeDriver version matches your Chrome browser version.
- Make sure that the specified download path exists before running the script.
- Adjust the scrolling time in the script if the playlist is very large or slow to load.

This **README** provides instructions on setup, usage, and the overall workflow of your project.
