from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from youtubesearchpython import VideosSearch
import pandas as pd
import time
import argparse
import yt_dlp

# Full path to the chromedriver executable
path = r"C:\Users\let's go\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object with the path to chromedriver
service = Service(executable_path=path)

# Pass the service object to the Chrome driver
driver = webdriver.Chrome(service=service)

def scraping(spotify_playlist_url, output_csv):
    driver.get(spotify_playlist_url)
    driver.implicitly_wait(10)  # because this is a dynamic website we need to use this implicitly_wait() function
    time.sleep(3)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    scroll_attempts = 0
    max_attempts = 3  # Try scrolling 3 more times after no height change

    while scroll_attempts < max_attempts:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(5)  # Adjust this value based on the speed of page loading
    
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            scroll_attempts += 1
        else:
            scroll_attempts = 0  # Reset attempt counter if the page height increased
        
        last_height = new_height

    # Now that all data is loaded, scrape it
    titles = driver.find_elements(By.XPATH, '//div[contains(@class, "encore-text-body-medium") and contains(@class, "standalone-ellipsis-one-line")]')
    artists = driver.find_elements(By.XPATH, '//span[contains(@class, "encore-text-body-small") and contains(@class, "standalone-ellipsis-one-line")]//a')
 
    all_data = []

    for index in range(len(titles)):
        all_data.append({
            "title": titles[index].text,
            "artist": artists[index].text,
        })
    
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(all_data)
    df.to_csv(output_csv, index=False)
    
    return all_data
#youtube seach of the video  in the spotify playlist
def search(data):
    urls = []
    for song in data:
        keywords = f"{song['title']} {song['artist']}"
        videos_search = VideosSearch(keywords, limit=1)
        results = videos_search.result()
        try:
            url = results['result'][0]['link']#extact the links
            urls.append(url)
            print(f"Found URL for {keywords}: {url}")
        except IndexError:
            print(f"No results found for {keywords}")
            urls.append(None)
    
    return urls


def download(urls):
    path = r"C:\Users\let's go\Desktop\python project\spotify track\music"#path of the result where it will be placed
    for url in urls:
        try:
            #customize the download behavior 
            ydl_opts = { 
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': f"{path}/%(title)s.%(ext)s",
            }
            #handle download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")


if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-u", "--url", help="Spotify playlist URL", required=True)
    parser.add_argument("-o", "--output", help="Output filepath for CSV", required=True)
    
    # Read arguments from command line
    args = parser.parse_args()

    # Call the scraping function
    data = scraping(args.url, args.output)
    
    # Search and print YouTube URLs
    youtube_urls = search(data)
    download(youtube_urls)
