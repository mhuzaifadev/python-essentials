from flask import Flask, render_template, request, redirect, url_for
from admin import Admin
from user import User

app = Flask(__name__)
admin = Admin()
user = User()

@app.route('/')
def index():
    return render_template('admin_index.html')

@app.route('/add_movie', methods=['POST'])
def add_movie():
    name = request.form['name']
    duration = request.form['duration']
    cinema_number = request.form['cinema_number']
    added_movie = admin.add_movie(name, duration, cinema_number) # Change this line
    message = "Movie added successfully!"
    return render_template('admin_index.html', message=message, added_movie=added_movie)

@app.route('/add_cinema', methods=['POST'])
def add_cinema():
    rows = int(request.form['rows'])
    seats_per_row = int(request.form['seats_per_row'])
    added_cinema = admin.add_cinema(rows, seats_per_row) # Change this line
    message = "Cinema added successfully!"
    return render_template('admin_index.html', message=message, added_cinema=added_cinema)



@app.route('/view_ticket', methods=['GET'])
def view_ticket():
    ticket_id = request.args.get('ticket_id')
    ticket = admin.tickets[admin.tickets["ID"==ticket_id]]  # Assuming you have tickets attribute in Admin class
    return render_template('ticket_details.html', ticket=ticket)


if __name__ == "__main__":
    app.run(port=7000)
