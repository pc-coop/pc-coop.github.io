import json

import utils


with open('pccouchcoop.json') as f:
    data = json.loads(f.read())
results = data['results']['collection1']
games = [
    {
        'title': g['name']['text'].encode('utf8'),
        'mc_score': g['score'],
        'release': g['release'],
        'mc_url': g['link']['href'],
        'steam_url': g['steam']['href'],
    }
    for g in results
]
sorted_keys = ['title', 'mc_score', 'release', 'mc_url', 'steam_url']
utils.to_csv(games, 'data.csv', sorted_keys)
