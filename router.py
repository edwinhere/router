import sys
from collections import namedtuple, deque
from pprint import pprint as pp, pformat as pf
from datetime import datetime, timedelta


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {
            e.start for e in self.edges
        } | {
            e.end for e in self.edges
        }

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
        s, u = deque(), dest
        total_cost = dist[u]
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return (s, total_cost)


Station = namedtuple('Station', "line, index, name, opening")

ns = [
    Station(line='NS', index=1, name='Jurong East', opening='3/10/1990'),
    Station(line='NS', index=2, name='Bukit Batok', opening='3/10/1990'),
    Station(line='NS', index=3, name='Bukit Gombak', opening='3/10/1990'),
    Station(line='NS', index=4, name='Choa Chu Kang', opening='3/10/1990'),
    Station(line='NS', index=5, name='Yew Tee', opening='2/10/1996'),
    Station(line='NS', index=7, name='Kranji', opening='2/10/1996'),
    Station(line='NS', index=8, name='Marsiling', opening='2/10/1996'),
    Station(line='NS', index=9, name='Woodlands', opening='2/10/1996'),
    Station(line='NS', index=10, name='Admiralty', opening='2/10/1996'),
    Station(line='NS', index=11, name='Sembawang', opening='2/10/1996'),
    Station(line='NS', index=12, name='Canberra', opening='12/1/2019'),
    Station(line='NS', index=13, name='Yishun', opening='12/20/1988'),
    Station(line='NS', index=14, name='Khatib', opening='12/20/1988'),
    Station(line='NS', index=15, name='Yio Chu Kang', opening='11/7/1987'),
    Station(line='NS', index=16, name='Ang Mo Kio', opening='11/7/1987'),
    Station(line='NS', index=17, name='Bishan', opening='11/7/1987'),
    Station(line='NS', index=18, name='Braddell', opening='11/7/1987'),
    Station(line='NS', index=19, name='Toa Payoh', opening='11/7/1987'),
    Station(line='NS', index=20, name='Novena', opening='12/12/1987'),
    Station(line='NS', index=21, name='Newton', opening='12/12/1987'),
    Station(line='NS', index=22, name='Orchard', opening='12/12/1987'),
    Station(line='NS', index=23, name='Somerset', opening='12/12/1987'),
    Station(line='NS', index=24, name='Dhoby Ghaut', opening='12/12/1987'),
    Station(line='NS', index=25, name='City Hall', opening='12/12/1987'),
    Station(line='NS', index=26, name='Raffles Place', opening='12/12/1987'),
    Station(line='NS', index=27, name='Marina Bay', opening='11/4/1989'),
    Station(line='NS', index=28, name='Marina South Pier', opening='11/23/2014'),
]

ew = [
    Station(line='EW', index=1, name='Pasir Ris', opening='12/16/1989'),
    Station(line='EW', index=2, name='Tampines', opening='12/16/1989'),
    Station(line='EW', index=3, name='Simei', opening='12/16/1989'),
    Station(line='EW', index=4, name='Tanah Merah', opening='11/4/1989'),
    Station(line='EW', index=5, name='Bedok', opening='11/4/1989'),
    Station(line='EW', index=6, name='Kembangan', opening='11/4/1989'),
    Station(line='EW', index=7, name='Eunos', opening='11/4/1989'),
    Station(line='EW', index=8, name='Paya Lebar', opening='11/4/1989'),
    Station(line='EW', index=9, name='Aljunied', opening='11/4/1989'),
    Station(line='EW', index=10, name='Kallang', opening='11/4/1989'),
    Station(line='EW', index=11, name='Lavender', opening='11/4/1989'),
    Station(line='EW', index=12, name='Bugis', opening='11/4/1989'),
    Station(line='EW', index=13, name='City Hall', opening='12/12/1987'),
    Station(line='EW', index=14, name='Raffles Place', opening='12/12/1987'),
    Station(line='EW', index=15, name='Tanjong Pagar', opening='12/12/1987'),
    Station(line='EW', index=16, name='Outram Park', opening='12/12/1987'),
    Station(line='EW', index=17, name='Tiong Bahru', opening='3/12/1988'),
    Station(line='EW', index=18, name='Redhill', opening='3/12/1988'),
    Station(line='EW', index=19, name='Queenstown', opening='3/12/1988'),
    Station(line='EW', index=20, name='Commonwealth', opening='3/12/1988'),
    Station(line='EW', index=21, name='Buona Vista', opening='3/12/1988'),
    Station(line='EW', index=22, name='Dover', opening='10/18/2001'),
    Station(line='EW', index=23, name='Clementi', opening='3/12/1988'),
    Station(line='EW', index=24, name='Jurong East', opening='11/5/1988'),
    Station(line='EW', index=25, name='Chinese Garden', opening='11/5/1988'),
    Station(line='EW', index=26, name='Lakeside', opening='11/5/1988'),
    Station(line='EW', index=27, name='Boon Lay', opening='7/6/1990'),
    Station(line='EW', index=28, name='Pioneer', opening='2/28/2009'),
    Station(line='EW', index=29, name='Joo Koon', opening='2/28/2009'),
    Station(line='EW', index=30, name='Gul Circle', opening='6/18/2017'),
    Station(line='EW', index=31, name='Tuas Crescent', opening='6/18/2017'),
    Station(line='EW', index=32, name='Tuas West Road', opening='6/18/2017'),
    Station(line='EW', index=33, name='Tuas Link', opening='6/18/2017'),
]

cg = [
    Station(line='CG', index=0, name='Tanah Merah', opening='11/4/1989'),
    Station(line='CG', index=1, name='Expo', opening='1/10/2001'),
    Station(line='CG', index=2, name='Changi Airport', opening='2/8/2002'),
]

ne = [
    Station(line='NE', index=1, name='HarbourFront', opening='6/20/2003'),
    Station(line='NE', index=3, name='Outram Park', opening='6/20/2003'),
    Station(line='NE', index=4, name='Chinatown', opening='6/20/2003'),
    Station(line='NE', index=5, name='Clarke Quay', opening='6/20/2003'),
    Station(line='NE', index=6, name='Dhoby Ghaut', opening='6/20/2003'),
    Station(line='NE', index=7, name='Little India', opening='6/20/2003'),
    Station(line='NE', index=8, name='Farrer Park', opening='6/20/2003'),
    Station(line='NE', index=9, name='Boon Keng', opening='6/20/2003'),
    Station(line='NE', index=10, name='Potong Pasir', opening='6/20/2003'),
    Station(line='NE', index=11, name='Woodleigh', opening='6/20/2011'),
    Station(line='NE', index=12, name='Serangoon', opening='6/20/2003'),
    Station(line='NE', index=13, name='Kovan', opening='6/20/2003'),
    Station(line='NE', index=14, name='Hougang', opening='6/20/2003'),
    Station(line='NE', index=15, name='Buangkok', opening='1/15/2006'),
    Station(line='NE', index=16, name='Sengkang', opening='6/20/2003'),
    Station(line='NE', index=17, name='Punggol', opening='6/20/2003'),
]

cc = [
    Station(line='CC', index=1, name='Dhoby Ghaut', opening='4/17/2010'),
    Station(line='CC', index=2, name='Bras Basah', opening='4/17/2010'),
    Station(line='CC', index=3, name='Esplanade', opening='4/17/2010'),
    Station(line='CC', index=4, name='Promenade', opening='4/17/2010'),
    Station(line='CC', index=5, name='Nicoll Highway', opening='4/17/2010'),
    Station(line='CC', index=6, name='Stadium', opening='4/17/2010'),
    Station(line='CC', index=7, name='Mountbatten', opening='4/17/2010'),
    Station(line='CC', index=8, name='Dakota', opening='4/17/2010'),
    Station(line='CC', index=9, name='Paya Lebar', opening='4/17/2010'),
    Station(line='CC', index=10, name='MacPherson', opening='4/17/2010'),
    Station(line='CC', index=11, name='Tai Seng', opening='4/17/2010'),
    Station(line='CC', index=12, name='Bartley', opening='5/28/2009'),
    Station(line='CC', index=13, name='Serangoon', opening='5/28/2009'),
    Station(line='CC', index=14, name='Lorong Chuan', opening='5/28/2009'),
    Station(line='CC', index=15, name='Bishan', opening='5/28/2009'),
    Station(line='CC', index=16, name='Marymount', opening='5/28/2009'),
    Station(line='CC', index=17, name='Caldecott', opening='10/8/2011'),
    Station(line='CC', index=19, name='Botanic Gardens', opening='10/8/2011'),
    Station(line='CC', index=20, name='Farrer Road', opening='10/8/2011'),
    Station(line='CC', index=21, name='Holland Village', opening='10/8/2011'),
    Station(line='CC', index=22, name='Buona Vista', opening='10/8/2011'),
    Station(line='CC', index=23, name='one-north', opening='10/8/2011'),
    Station(line='CC', index=24, name='Kent Ridge', opening='10/8/2011'),
    Station(line='CC', index=25, name='Haw Par Villa', opening='10/8/2011'),
    Station(line='CC', index=26, name='Pasir Panjang', opening='10/8/2011'),
    Station(line='CC', index=27, name='Labrador Park', opening='10/8/2011'),
    Station(line='CC', index=28, name='Telok Blangah', opening='10/8/2011'),
    Station(line='CC', index=29, name='HarbourFront', opening='10/8/2011'),
]

ce = [
    Station(line='CE', index=0, name='Promenade', opening='4/17/2010'),
    Station(line='CE', index=1, name='Bayfront', opening='1/14/2012'),
    Station(line='CE', index=2, name='Marina Bay', opening='1/14/2012'),
]

dt = [
    Station(line='DT', index=1, name='Bukit Panjang', opening='12/27/2015'),
    Station(line='DT', index=2, name='Cashew', opening='12/27/2015'),
    Station(line='DT', index=3, name='Hillview', opening='12/27/2015'),
    Station(line='DT', index=5, name='Beauty World', opening='12/27/2015'),
    Station(line='DT', index=6, name='King Albert Park', opening='12/27/2015'),
    Station(line='DT', index=7, name='Sixth Avenue', opening='12/27/2015'),
    Station(line='DT', index=8, name='Tan Kah Kee', opening='12/27/2015'),
    Station(line='DT', index=9, name='Botanic Gardens', opening='12/27/2015'),
    Station(line='DT', index=10, name='Stevens', opening='12/27/2015'),
    Station(line='DT', index=11, name='Newton', opening='12/27/2015'),
    Station(line='DT', index=12, name='Little India', opening='12/27/2015'),
    Station(line='DT', index=13, name='Rochor', opening='12/27/2015'),
    Station(line='DT', index=14, name='Bugis', opening='12/22/2013'),
    Station(line='DT', index=15, name='Promenade', opening='12/22/2013'),
    Station(line='DT', index=16, name='Bayfront', opening='12/22/2013'),
    Station(line='DT', index=17, name='Downtown', opening='12/22/2013'),
    Station(line='DT', index=18, name='Telok Ayer', opening='12/22/2013'),
    Station(line='DT', index=19, name='Chinatown', opening='12/22/2013'),
    Station(line='DT', index=20, name='Fort Canning', opening='10/21/2017'),
    Station(line='DT', index=21, name='Bencoolen', opening='10/21/2017'),
    Station(line='DT', index=22, name='Jalan Besar', opening='10/21/2017'),
    Station(line='DT', index=23, name='Bendemeer', opening='10/21/2017'),
    Station(line='DT', index=24, name='Geylang Bahru', opening='10/21/2017'),
    Station(line='DT', index=25, name='Mattar', opening='10/21/2017'),
    Station(line='DT', index=26, name='MacPherson', opening='10/21/2017'),
    Station(line='DT', index=27, name='Ubi', opening='10/21/2017'),
    Station(line='DT', index=28, name='Kaki Bukit', opening='10/21/2017'),
    Station(line='DT', index=29, name='Bedok North', opening='10/21/2017'),
    Station(line='DT', index=30, name='Bedok Reservoir', opening='10/21/2017'),
    Station(line='DT', index=31, name='Tampines West', opening='10/21/2017'),
    Station(line='DT', index=32, name='Tampines', opening='10/21/2017'),
    Station(line='DT', index=33, name='Tampines East', opening='10/21/2017'),
    Station(line='DT', index=34, name='Upper Changi', opening='10/21/2017'),
    Station(line='DT', index=35, name='Expo', opening='10/21/2017'),
]

te = [
    Station(line='TE', index=1, name='Woodlands North', opening='12/31/2019'),
    Station(line='TE', index=2, name='Woodlands', opening='12/31/2019'),
    Station(line='TE', index=3, name='Woodlands South', opening='12/31/2019'),
    Station(line='TE', index=4, name='Springleaf', opening='12/31/2020'),
    Station(line='TE', index=5, name='Lentor', opening='12/31/2020'),
    Station(line='TE', index=6, name='Mayflower', opening='12/31/2020'),
    Station(line='TE', index=7, name='Bright Hill', opening='12/31/2020'),
    Station(line='TE', index=8, name='Upper Thomson', opening='12/31/2020'),
    Station(line='TE', index=9, name='Caldecott', opening='12/31/2020'),
    Station(line='TE', index=10, name='Mount Pleasant', opening='12/31/2021'),
    Station(line='TE', index=11, name='Stevens', opening='12/31/2021'),
    Station(line='TE', index=12, name='Napier', opening='12/31/2021'),
    Station(line='TE', index=13, name='Orchard Boulevard', opening='12/31/2021'),
    Station(line='TE', index=14, name='Orchard', opening='12/31/2021'),
    Station(line='TE', index=15, name='Great World', opening='12/31/2021'),
    Station(line='TE', index=16, name='Havelock', opening='12/31/2021'),
    Station(line='TE', index=17, name='Outram Park', opening='12/31/2021'),
    Station(line='TE', index=18, name='Maxwell', opening='12/31/2021'),
    Station(line='TE', index=19, name='Shenton Way', opening='12/31/2021'),
    Station(line='TE', index=20, name='Marina Bay', opening='12/31/2021'),
    Station(line='TE', index=21, name='Marina South', opening='12/31/2021'),
    Station(line='TE', index=22, name='Gardens by the Bay', opening='12/31/2021'),
]

stations = ns + ew + cg + ne + cc + ce + dt + te

def generate_edges(vertices):
    edges = [
        (start, end, abs(start.index - end.index))\
        for start in vertices\
        for end in vertices
    ]
    return edges

def generate_interchange_edges(vertices):
    edges = [
        (start, end, 0)\
        for start in vertices\
        for end in vertices\
        if start.name == end.name and start.line != end.line
    ]
    return edges

def time_calculator(line, start_time):
    hour = start_time.hour
    day = int(start_time.strftime("%w"))

    if hour >= 6 and hour < 9 and day >= 1 and day <= 5:
        if line == 'NS' or line == 'NE':
            return 12
        else:
            return 15
    elif hour >= 22 and hour < 6:
        if line == 'DT' or line == 'CG' or line == 'CE':
            return float('nan')
        elif line == 'TE':
            return 8
        else:
            return 10
    else:
        if line == 'DT' or line == 'TE':
            return 8
        else:
            return 10

def generate_edges_by_time(vertices, start_time):
    edges = [
        (
            start,
            end,
            abs(start.index - end.index) * time_calculator(
                start.line,
                start_time
            )
        )\
        for start in vertices\
        for end in vertices
    ]
    return edges

def generate_interchange_edges_by_time(vertices, start_time):
    hour = start_time.hour
    day = int(start_time.strftime("%w"))
    cost = float('nan')
    if hour >= 6 and hour < 9 and day >= 1 and day <= 5:
        cost = 15
    elif hour >= 22 and hour < 6:
        cost = 10
    else:
        cost = 10

    edges = [
        (start, end, cost)\
        for start in vertices\
        for end in vertices\
        if start.name == end.name and start.line != end.line
    ]
    return edges

def print_steps(plan, by_time=False):
    (route, cost) = plan
    route = list(route)

    route_codes = list(map(lambda x: x.line + str(x.index), route))
    print("Route: " + pf(route_codes))

    if by_time:
        print("Time: %s minutes" % cost)
    else:
        print("Stations Travelled: %s" % cost)

    for i in range(0, len(route) - 1):
        if(route[i].line == route[i + 1].line):
            print("Take %s from %s to %s" % (
                route[i].line,
                route[i].name,
                route[i + 1].name
            ))
        else:
            print("Change to line %s" % route[i + 1].line)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(
            "Usage: python " + sys.argv[0] + " <start-station-code> <end-station-code> [start-time]"
        )

    route_codes = list(map(lambda x: x.line + str(x.index), stations))
    if not sys.argv[1] in route_codes:
        sys.exit("Unknown station: %s" % sys.argv[1])
    if not sys.argv[2] in route_codes:
        sys.exit("Unknown station: %s" % sys.argv[2])

    start_station = list(filter(
        lambda x: x.line + str(x.index) == sys.argv[1],
        stations
    ))[0]

    end_station = list(filter(
        lambda x: x.line + str(x.index) == sys.argv[2],
        stations
    ))[0]

    by_time = False
    start_time = None
    if len(sys.argv) >= 4:
        start_time = datetime.strptime(sys.argv[3], '%Y-%m-%dT%H:%M')
        by_time = True

    if not by_time:
        singapore = (
            generate_edges(ns) +
            generate_edges(ew) +
            generate_edges(cg) +
            generate_edges(ne) +
            generate_edges(cc) +
            generate_edges(ce) +
            generate_edges(dt) +
            generate_edges(te) +
            generate_interchange_edges(stations)
        )
    else:
        singapore = (
            generate_edges_by_time(ns, start_time) +
            generate_edges_by_time(ew, start_time) +
            generate_edges_by_time(cg, start_time) +
            generate_edges_by_time(ne, start_time) +
            generate_edges_by_time(cc, start_time) +
            generate_edges_by_time(ce, start_time) +
            generate_edges_by_time(dt, start_time) +
            generate_edges_by_time(te, start_time) +
            generate_interchange_edges_by_time(stations, start_time)
        )
    graph = Graph(singapore)
    print("Travel from %s to %s" % (start_station.name, end_station.name))
    plan = graph.dijkstra(start_station, end_station)
    print_steps(plan, by_time=by_time)
