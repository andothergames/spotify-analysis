This repo analyses spotify streaming history. (basic functionality atm)

To request streaming data history, log in to your spotify account, go to the privacy section, then in 'download your data' request a copy of your extended streaming history.

This will provide you with JSON files categorised by year containing a list of plays that provide the following information:
```
{
    "ts": "2011-04-22T22:55:30Z",
    "platform": "Windows Vista (Home Premium Ed) SP2 [x86 0]",
    "ms_played": 255609,
    "conn_country": "GB",
    "ip_addr": "00.000.00.000",
    "master_metadata_track_name": "Wraith Pinned To The Mist And Other Games",
    "master_metadata_album_artist_name": "of Montreal",
    "master_metadata_album_album_name": "The Sunlandic Twins",
    "spotify_track_uri": "spotify:track:5Q7vla0EpIHVcEL9SuE0Ka",
    "episode_name": null,
    "episode_show_name": null,
    "spotify_episode_uri": null,
    "audiobook_title": null,
    "audiobook_uri": null,
    "audiobook_chapter_uri": null,
    "audiobook_chapter_title": null,
    "reason_start": "trackdone",
    "reason_end": "trackdone",
    "shuffle": false,
    "skipped": false,
    "offline": false,
    "offline_timestamp": null,
    "incognito_mode": false
  }
  ```
  ---

  ### Play with the cloned repo

  Place the json file of a chosen year into the repo and then run:
  ```
  python main.py
  ```
  this will return your top 10 artists, top 10 songs, top 10 albums and total time spent listening to music from that year.