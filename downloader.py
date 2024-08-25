import requests
import urllib3
import re


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_youtube_id(url):
    # Définir les différents motifs d'URL possibles
    patterns = [
        r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([\w-]{11})',
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?.*v=([\w-]{11})',
        r'(?:https?://)?(?:www\.)?youtu\.be/([\w-]{11})',
        r'(?:https?://)?(?:www\.)?youtube\.com/shorts/([\w-]{11})'
    ]
    
    # Parcourir les motifs et essayer de trouver une correspondance
    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            return match.group(1)
    
    return None  # Retourne None si aucun motif ne correspond


def fetch_video_links(url):
    video_id = extract_youtube_id(url)
    if video_id is not None:
        api_url = f"https://yt-api.p.rapidapi.com/dl?id={video_id}"
        headers = {
            'x-rapidapi-host': 'yt-api.p.rapidapi.com',
            'x-rapidapi-key': '2e23d87466msh02392d4212b6f4ap1c7aaajsn44897a354b8a'
        }

        response = requests.get(api_url, headers=headers, verify=False)
    
        if response.status_code == 200:
            data = response.json()
            if data['status']=="OK":
                video_info = {
                    'title': data['title'],
                    'thumbnail': data['thumbnail'][3].get('url'),
                    'mp4': data['formats'][0].get('url'),
                    'description': data['description'],
                    'audio_low_quality': data['adaptiveFormats'][len(data['adaptiveFormats']) - 2].get('url'),
                    'audio_high_quality': data['adaptiveFormats'][len(data['adaptiveFormats']) - 1].get('url'),
                    'video_mp4_high_quality': data['adaptiveFormats'][0].get('url'),
                    'video_mp4_low_quality': data['adaptiveFormats'][4].get('url')
                }
                return video_info
        return None
    else:
        print("Impossible d'extraire l'ID de la video.")


    
