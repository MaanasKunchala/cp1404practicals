from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and extra costs."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = (Taxi.price_per_km * fanciness)
        self.extra_fares = 0

    def start_fare(self):
        """Begins a new fare."""
        self.current_fare_distance = 0
        self.extra_fares += 1

    def get_fare(self):
        """Return the price for the taxi trip along with flagfall."""
        return (self.price_per_km * self.current_fare_distance) + (self.flagfall * self.extra_fares)
