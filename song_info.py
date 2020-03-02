#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
"""
Displays the song info using Last.fm API.
See: https://www.last.fm/api/intro
"""

API_KEY = ''
USER = ''


def initialize_data():
    """
    Initializes API key and username data.

    Returns
    -------
    None.

    """
    import data.io_helper as io_helper
    
    global API_KEY, USER
    API_KEY, USER = io_helper.get_data()
    

def make_request():
    """
    Makes a GET request for the most recent played tracks.

    Returns
    -------
    GET-request.

    """
    
    url = 'https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks'
    parameters = {
        'api_key':    API_KEY,
        'format':     'json',
        'limit':      '1',
        'nowplaying': 'true',
        'user':        USER
        }
    
    return requests.get(url, parameters)


def handle_response(request):
    """
    Takes the most recent played track out of the response to our GET request.

    Parameters
    ----------
    request : json
        Response to getRecentTracks-method call.

    Returns
    -------
    The most recent track info.

    """
    
    response = request.json()
    return response['recenttracks']['track'][0] # the most recent one


def is_playing(track):
    """
    Checks if the track is playing at the moment.

    Parameters
    ----------
    track : json
        track information.

    Returns
    -------
    None.

    """
    
    return track['@attr']['nowplaying'] == 'true'


def format_track_info(track):
    """
    Takes out the artist and name of the track and formats them for displaying.

    Parameters
    ----------
    track : json
        track information.

    Returns
    -------
    None.

    """
    
    artist = track['artist']['#text']
    title = track['name']
    return artist + " - " + title


if __name__ == '__main__':
    import time
    
    initialize_data()
    while True:
        try:
            request = make_request()
            if request.status_code == 200: # if successful GET-request
                
                song = handle_response(request) # get the most recent track
                
                if is_playing(song):
                    song_info = format_track_info(song)
                    print(song_info, flush=True)
        
        except:
            pass
        time.sleep(5) 