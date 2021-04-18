import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        # assert len(self.title) != 0, "Title is empty!"
        # assert self.start < self.end, "Start date is later than end date!"
        if self.start > self.end:
            raise TripDateException("Start date is later than end date!")
        if len(self.title) == 0:
            raise TripNameException("Title is empty!")

    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = list()
        for obj in trips:
            try:
                obj.check_data()
            except TripNameException as e:
                list_of_errors.append(f"{obj.symbol}: {e}")
            except TripDateException as e:
                list_of_errors.append(f"{obj.symbol}: {e}")
            except Exception as e:
                list_of_errors.append(f"{obj.symbol}: {e}")

        if len(list_of_errors) > 0:
            raise TripException("The list of trips has errors", list_of_errors)
        else:
            print("The offer will be published...")
        # assert len(list_of_errors) == 0, "The list of trips has errors: {}".format(list_of_errors)


class TripException(Exception):
    def __init__(self, text, description):
        super().__init__(text)
        self.description = description

    def __str__(self):
        return f"{super().__str__()}: {self.description}"


class TripNameException(TripException):
    def __init__(self, text):
        super().__init__(text, 'Name of the trip is missing. You need to name the trip somehow...')


class TripDateException(TripException):
    def __init__(self, text):
        super().__init__(text, 'The dates are incorrect. The starting date should be earlier than the ending date...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('Starting checking trips...')
    Trip.publish_offer(trips)
except Exception as e:
    # TripException("The list of trips has errors", )
    print("Critical ERROR! \nDetails: {}".format(e))

