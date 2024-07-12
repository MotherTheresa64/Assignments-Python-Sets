# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to.
print(our_routes.intersection(competitor_routes))
# 2. Destinations unique to your airline.
print(our_routes.difference(competitor_routes))
# 3. Whether there are any destinations that neither airline shares.
print(our_routes.symmetric_difference(competitor_routes))
# Above instruction was a bit vague so hopefully that's correct :/