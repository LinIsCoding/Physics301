def flight_schedule():
    airports = {"DCA": "Washington, D.C.", "IAD": "Dulles",\
    "LHR": "London-Heathrow", "SVO": "Moscow",\
    "CDA": "Chicago-Midway", "SBA": "Santa Barbara",\
    "LAX": "Los Angeles","JFK": "New York City",\
    "MIA": "Miami", "AUM": "Austin, Minnesota"}

    flights = [("Southwest",145,"DCA",1,6.00),\
    ("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
    ("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60),\
    ("United",46,"LAX",5,6.5), ("Southwest",23,"SBA",6,12.5),\
    ("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
    ("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),\
    ("United",2032,"MIA",21,15.1),("SpamAir",1,"AUM",42,14.4)]

    sorted_by_airline = sorted(flights, key = lambda flight: flight[0])
    header = ["Flight","Destination","Gate", "Time"]
    print('{:s}\t\t   {:s}\t\t{:s}\t{:s}'.format(*header))
    print("---------------------------------------------------------")
    for f in sorted_by_airline:
        flight = "{:s} {:d}".format(f[0], f[1])
        des = airports[f[2]]
        gate = f[3]
        time = f[4]
        print('{:<20s}{:<20s}{:^5d}{:^15f}'.format(flight,des,gate,time))

    print
    sorted_by_time = sorted(flights, key = lambda flight: flight[4])
    print('{:s}\t\t   {:s}\t\t{:s}\t{:s}'.format(*header))
    print("---------------------------------------------------------")
    for f in sorted_by_time:
        flight = "{:s} {:d}".format(f[0], f[1])
        des = airports[f[2]]
        gate = f[3]
        time = f[4]
        print('{:<20s}{:<20s}{:^5d}{:^15f}'.format(flight,des,gate,time))


if __name__ == "__main__":
    flight_schedule()