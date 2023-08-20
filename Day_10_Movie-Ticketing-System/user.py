import csv

class User:
    def __init__(self):
        self.movies = self._load_movies_from_csv()
        self.cinemas = self._load_cinemas_from_csv()

    # Method to search for a movie
    def search_movie(self, name):
        return [movie for movie in self.movies if name.lower() in movie['name'].lower()]

    # Method to view movie details
    def view_movie_details(self, movie_name):
        for movie in self.movies:
            if movie_name == movie['name']:
                print("Name:", movie['name'])
                print("Duration:", movie['duration'])
                print("Timings:", movie['timings'])
                print("Cinema Number:", movie['cinema_number'])
                return

    # Method to book a seat
    def book_seat(self, movie_name, timing, seat):
        for movie in self.movies:
            if movie_name == movie['name']:
                cinema_number = movie['cinema_number']
                cinema = self.cinemas[cinema_number]
                row, seat_number = seat[0], int(seat[1:]) - 1
                if cinema['seats'][row][seat_number] == 'available':
                    cinema['seats'][row][seat_number] = 'booked'
                    print("Seat booked successfully!")
                    self._save_cinemas_to_csv()
                else:
                    print("Seat already booked!")
                return

    # Updated method to load movies from CSV
    def _load_movies_from_csv(self):
        movies = []
        with open('movies.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies.append({'name': row['Name'], 'duration': row['Duration'], 'timings': row['Timings'].split(','), 'cinema_number': int(row['Cinema Number'])})
        return movies

    # Helper method to load cinemas from CSV
    def _load_cinemas_from_csv(self):
        cinemas = {}
        with open('cinemas.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                seats = eval(row['Seats'])
                cinema_number = int(row['Cinema Number']) # Use cinema number as key
                cinemas[cinema_number] = {'rows': int(row['Rows']), 'seats_per_row': int(row['Seats Per Row']), 'seats': seats}
        return cinemas

    # Helper method to save cinemas to CSV
    def _save_cinemas_to_csv(self):
        with open('cinemas.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Rows', 'Seats Per Row', 'Seats'])
            for cinema_number, cinema in self.cinemas.items():
                writer.writerow([cinema['rows'], cinema['seats_per_row'], str(cinema['seats'])])

def main():
    user = User()
    while True:
        # Main menu for users
        print("\nWelcome to the Movie Ticketing System!")
        print("1. Search Movie")
        print("2. View Movie Details")
        print("3. Book Seat")
        print("4. Exit")
        choice = input("Choose an option: ")

        # Search movie option
        if choice == '1':
            name = input("Enter movie name to search: ")
            movies = user.search_movie(name)
            print("Found Movies:")
            for movie in movies:
                print(movie['name'])

        # View movie details option
        elif choice == '2':
            movie_name = input("Enter movie name to view details: ")
            user.view_movie_details(movie_name)

        # Book seat option
        elif choice == '3':
            movie_name = input("Enter movie name: ")
            timing = input("Enter timing (e.g. 10:00): ")
            seat = input("Enter seat (e.g. A2): ")
            user.book_seat(movie_name, timing, seat)

        # Exit option
        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()