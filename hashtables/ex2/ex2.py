#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    trip = {}
    route = []

    for ticket in tickets:
        trip[ticket.source] = ticket.destination
    
    next_trip = trip['NONE']

    while next_trip != 'NONE':
        route.append(next_trip)
        next_trip = trip[next_trip]

    route.append('NONE')
    print(trip)

    return route
