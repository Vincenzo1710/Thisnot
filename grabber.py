import requests
import re

url_sito = "https://thisnot.business/eventi.php"
file_m3u = "playlist.m3u"

def get_mpd():
    try:
        r = requests.get(url_sito, timeout=10)
        match = re.search(r'https?://[^\s"\'<>]+?\.mpd', r.text)
        if match:
            return match.group(0)
    except:
        return None
    return None

mpd_link = get_mpd()

if mpd_link:
    with open(file_m3u, "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTINF:-1, Evento Live\n")
        f.write(f"{mpd_link}\n")
    print("Playlist aggiornata!")
else:
    print("Link non trovato.")
