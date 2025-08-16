import json
from collections import Counter
import os

def load_streaming_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def format_ms(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours} hours {minutes % 60} minutes"


def analyze_streaming_data(data):
    song_counter = Counter()
    album_counter = Counter()
    artist_counter = Counter()
    total_ms_played = 0

    for entry in data:
        song = entry.get("master_metadata_track_name")
        album = entry.get("master_metadata_album_album_name")
        artist = entry.get("master_metadata_album_artist_name")
        ms_played = entry.get("ms_played", 0)

        if song:
            song_counter[song] += 1
        if album:
            album_counter[album] += 1
        if artist:
            artist_counter[artist] += 1

        total_ms_played += ms_played

    return {
        "top_10_songs": song_counter.most_common(10),
        "top_10_albums": album_counter.most_common(10),
        "top_10_artists": artist_counter.most_common(10),
        "total_ms_played": total_ms_played
    }

# rename file path to match your json file
def main():
    filepath = os.path.join("data", "Streaming_History_Audio_2025_16.json")
    data = load_streaming_data(filepath)
    results = analyze_streaming_data(data)

    print("\n🎵 Top 10 Songs:")
    for song, count in results["top_10_songs"]:
        print(f"{song}: {count} times")

    print("\n💿 Top 10 Albums:")
    for album, count in results["top_10_albums"]:
        print(f"{album}")

    print("\n👩‍🎤 Top 10 Artists:")
    for artist, count in results["top_10_artists"]:
        print(f"{artist}: {count} times")

    print(f"\n⏱️ Total Listening Time: {format_ms(results['total_ms_played'])}")

if __name__ == "__main__":
    main()
