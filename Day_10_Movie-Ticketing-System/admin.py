import csv

class Admin:
    def __init__(self):
        self.movies = []
        self.cinemas = {}

    def add_movie(self, name, duration, timings, cinema_number):
        movie = {'name': name, 'duration': duration, 'timings': timings, 'cinema_number': cinema_number}
        self.movies.append(movie)
        self._save_movies_to_csv()

    def add_cinema(self, rows, seats_per_row):
        cinema = {'rows': rows, 'seats_per_row': seats_per_row, 'seats': self._generate_seats(rows, seats_per_row)}
        cinema_number = len(self.cinemas) + 1
        self.cinemas[cinema_number] = cinema
        self._save_cinemas_to_csv()

    def _generate_seats(self, rows, seats_per_row):
        seats = {}
        for row in range(rows):
            row_name = chr(ord('A') + row)
            seats[row_name] = ['available'] * seats_per_row
        return seats

    def _save_movies_to_csv(self):
        with open('movies.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Duration', 'Timings', 'Cinema Number'])
            for movie in self.movies:
                writer.writerow([movie['name'], movie['duration'], ','.join(movie['timings']), movie['cinema_number']])

    def _save_cinemas_to_csv(self):
        with open('cinemas.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Cinema Number', 'Rows', 'Seats Per Row', 'Seats'])
            for cinema_number, cinema in self.cinemas.items():
                writer.writerow([cinema_number, cinema['rows'], cinema['seats_per_row'], str(cinema['seats'])])



def main():
    admin = Admin()
    while True:
        # Main menu for admin
        print("\nWelcome to the Admin Panel!")
        print("1. Add Movie")
        print("2. Add Cinema")
        print("3. Exit")
        choice = input("Choose an option: ")

        # Add movie option
        if choice == '1':
            name = input("Enter movie name: ")
            duration = input("Enter duration (e.g. 2h 30m): ")
            timings = ['10:00', '13:00', '16:00', '19:00', '22:00', '01:00']
            cinema_number = int(input("Enter cinema number: "))
            admin.add_movie(name, duration, timings, cinema_number)

        # Add cinema option
        elif choice == '2':
            rows = int(input("Enter number of rows: "))
            seats_per_row = int(input("Enter number of seats per row: "))
            admin.add_cinema(rows, seats_per_row)

        # Exit option
        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()