import os
from flask import Flask, jsonify

import genius_artist


app = Flask(__name__)

GENIUS_ACCESS_TOKEN = os.getenv('GENIUS_ACCESS_TOKEN')


@app.route('/get_artist_top_songs/<artist_name>')
def get_artist_top_songs(artist_name):

    try:
        #import ipdb; ipdb.set_trace()
        artist_name = artist_name.strip()

        status, artist_data = genius_artist.artist_songs(artist_name, quantity=10, page=1) #cache

        if not status:
            raise Exception('Artista não encontrato')

        return jsonify(
                {
                    'status': 'success',
                    'search_term': artist_name,
                    'message': f'Top {len(artist_data["song_list"])} músicas',
                    'artist_name': artist_data['artist_name'],
                    'songs_list': artist_data['song_list']
                }
            )
    except Exception as err:
        return jsonify(
            {
                'status': 'error',
                'search_term': artist_name,
                'message': str(err),
                'artist_name': None,
                'songs_list': []
            }
        )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
