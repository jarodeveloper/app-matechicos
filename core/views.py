from django.shortcuts import render
from googleapiclient.discovery import build
from django.conf import settings

def home(request):
    return render(request, 'core/index.html')

def numeros(request):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

    search_response = youtube.search().list(
        q='numeros aprendiendo a contar',
        part='snippet',
        order='viewCount',
        type='video',
        maxResults=10,
        regionCode='ES'
    ).execute()

    videos = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_response = youtube.videos().list(
            part='snippet,status',
            id=video_id
        ).execute()

        # Verificar si el video es embeddable y se puede visualizar en una página externa
        status = video_response['items'][0]['status']
        if status['embeddable'] and status['privacyStatus'] == 'public':
            video = {
                'titulo': item['snippet']['title'],
                'id': video_id
            }
        videos.append(video)

    return render(request, 'core/numeros.html', {'videos': videos})

def aritmetica(request):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

    search_response = youtube.search().list(
        q='aritmetica para chiquitines',
        part='snippet',
        order='viewCount',
        type='video',
        maxResults=10,
        regionCode='ES'
    ).execute()

    videos = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_response = youtube.videos().list(
            part='snippet,status',
            id=video_id
        ).execute()

        # Verificar si el video es embeddable y se puede visualizar en una página externa
        status = video_response['items'][0]['status']
        if status['embeddable'] and status['privacyStatus'] == 'public':
            video = {
                'titulo': item['snippet']['title'],
                'id': video_id
            }
        videos.append(video)

    return render(request, 'core/aritmetica.html', {'videos': videos})


def geometria(request):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

    search_response = youtube.search().list(
        q='geometria para niños',
        part='snippet',
        order='viewCount',
        type='video',
        maxResults=10,
        regionCode='ES'
    ).execute()

    videos = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_response = youtube.videos().list(
            part='snippet,status',
            id=video_id
        ).execute()

        # Verificar si el video es embeddable y se puede visualizar en una página externa
        status = video_response['items'][0]['status']
        if status['embeddable'] and status['privacyStatus'] == 'public':
            video = {
                'titulo': item['snippet']['title'],
                'id': video_id
            }
        videos.append(video)

    return render(request, 'core/geometria.html', {'videos': videos})


def conjuntos(request):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

    search_response = youtube.search().list(
        q='conjuntos matematicos para pequeños',
        part='snippet',
        order='viewCount',
        type='video',
        maxResults=10,
        regionCode='ES'
    ).execute()

    videos = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_response = youtube.videos().list(
            part='snippet,status',
            id=video_id
        ).execute()

        # Verificar si el video es embeddable y se puede visualizar en una página externa
        status = video_response['items'][0]['status']
        if status['embeddable'] and status['privacyStatus'] == 'public':
            video = {
                'titulo': item['snippet']['title'],
                'id': video_id
            }
        videos.append(video)

    return render(request, 'core/conjuntos.html', {'videos': videos})
