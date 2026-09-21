class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin[id]

        travelTime = t - startTime

        key = (startStation, stationName)

        if key not in self.routes:
            self.routes[key] = [0, 0]

        self.routes[key][0] += travelTime
        self.routes[key][1] += 1

        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)

        totalTime = self.routes[key][0]
        totalTrips = self.routes[key][1]

        return totalTime / totalTrips