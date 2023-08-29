from flask import Flask, render_template, request, redirect, url_for
from user import User

app = Flask(__name__) #Establishing a Flask App
user = User()

@app.route('/')
def index():
    return render_template('user_index.html')

@app.route('/search_movie', methods=['POST'])
def search_movie():
    name = request.form['name']
    movies = user.search_movie(name)
    return render_template('user_index.html', movies=movies)

@app.route('/view_movie_details/<movie_name>')
def view_movie_details(movie_name):
    movie_details = user.view_movie_details(movie_name)
    return render_template('movie_details_partial.html', movie=movie_details)


@app.route('/book_seat', methods=['POST'])
def book_seat():
    movie_name = request.form['movie_name']
    timing = request.form['timing']
    seat = request.form['seat']
    ticket_id = user.book_ticket(movie_name, timing, seat)
    return render_template('user_index.html', ticket_id=ticket_id)

# 619da5cb-057c-439c-b77c-b1e82737ea00
if __name__ == "__main__":
    app.run(port=7500)
