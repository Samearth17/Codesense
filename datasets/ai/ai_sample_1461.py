import json

tweets = [
 { 
 'user': 'John', 
 'tweet': 'This is a tweet in English', 
 'language': 'en' 
 }, 
 { 
 'user': 'Jane', 
 'tweet': 'Ceci est un tweet en français', 
 'language': 'fr' 
 }, 
 { 
 'user': 'Bob', 
 'tweet': 'Esta es una publicación en español', 
 'language': 'es' 
 }
 ]

language = 'en'

filtered = [tweet for tweet in tweets if tweet['language'] == language]

print(json.dumps(filtered, indent=2))