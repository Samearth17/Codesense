from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/movie/search', methods=['GET'])
def search_movie():
   query = request.args.get('query')
   api_key = '<YOUR_API_KEY>'
   url = 'http://www.omdbapi.com/?apikey={}&s={}'.format(api_key, query)

response = requests.get(url).json()

movies = []
for movie in response['Search']:
   movies.append({
   'title': movie['Title'],
   'id': movie['imdbID'],
   'year': movie['Year'],
   'poster': movie['Poster'],
   })

return {
 'movies': movies
}

@app.route('/movie/<movie_id>/rating', methods=['GET'])
def get_movie_rating(movie_id):
    url = 'http://www.omdbapi.com/?apikey={}&i={}'.format(api_key, movie_id)
    response = requests.get(url).json()
    return {
        'rating': response['imdbRating']
    }

@app.route('/movie/<movie_id>/reviews', methods=['GET'])
def get_movie_reviews(movie_id):
    url = 'http://www.omdbapi.com/?apikey={}&i={}'.format(api_key, movie_id)
    response = requests.get(url).json() 
    reviews = []
    for review in response['Ratings']:
        reviews.append({ 
            'source': review['Source'],
            'score': review['Value'],
        })
    return {
        'reviews': reviews
    }

if __name__ == '__main__':
	app.run(debug=True)