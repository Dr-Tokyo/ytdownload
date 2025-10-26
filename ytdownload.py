import yt_dlp
import os
from pydub import AudioSegment

def download_and_convert_to_mp3(youtube_url, output_path="output.mp3"):
    # Define download options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Best quality audio
        'outtmpl': 'downloaded_audio.%(ext)s',  # Temporary file name
        'extractaudio': True,  # Only extract audio, not video
        'audioquality': 1,  # Best audio quality
    }

    # Download the audio using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([youtube_url])

    # Find the downloaded file (the exact extension may vary)
    temp_audio_file = "downloaded_audio.webm"  # or .m4a, .opus, etc., depending on the source

    # Ensure we have downloaded the audio file
    if os.path.exists(temp_audio_file):
        print(f"Downloaded the audio, now converting to MP3...")

        # Convert to MP3 using pydub (FFmpeg required)
        try:
            audio = AudioSegment.from_file(temp_audio_file)
            audio.export(output_path, format="mp3")
            print(f"Downloaded and converted to {output_path}")
        except Exception as e:
            print(f"Error during conversion: {e}")
        finally:
            os.remove(temp_audio_file)  # Clean up the temp file
    else:
        print("Failed to download the audio.")

if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    download_and_convert_to_mp3(youtube_url)

