# Tweets are stored in "tweets.json"
import json 

tweets_filename='tweets.json'
with open(tweets_filename) as data_file:
    alldata = json.loads (data_file.read())
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for tweet in alldata:
       
        if tweet['coordinates']:
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)
 
# Save geo data
with open('geo_data.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))
