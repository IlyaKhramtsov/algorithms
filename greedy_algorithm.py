def find_stations(stations: dict, states_needed: set) -> set:
    """Looking for stations to cover all states."""
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed.intersection(states)
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)
    return final_stations


states_needed = {'mt', 'wa', 'or', 'id', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {
    'one': {'id', 'nv', 'ut'},
    'two': {'wa', 'id', 'mt'},
    'three': {'or', 'nv', 'ca'},
    'four': {'nv', 'ut'},
    'five': {'ca', 'az'}
}

print(find_stations(stations, states_needed))

