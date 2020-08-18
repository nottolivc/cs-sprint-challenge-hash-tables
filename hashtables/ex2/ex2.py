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
    # Loop through tickets setting ticket source to destination and next loc to none
    for ticket in tickets:
        trip[ticket.source] = ticket.destination
    
    next_trip = trip['NONE']

    while next_trip != 'NONE':
        route.append(next_trip)
        next_trip = trip[next_trip]

    route.append('NONE')
    print(trip)

    return route

    # cache = {}
    # route = [None] * length
    # for i in range(length):
    #     if tickets[i].source == "NONE":
    #         route[0] = tickets[i].destination
    #     if tickets[i].source not in cache:
    #         cache[tickets[i].source] = tickets[i].destination
    # for j in range(length):
    #     if route[j-1] is not None:
    #         route[j] = cache[route[j-1]]
    # return route
    # print(reconstruct_trip(tickets,length))