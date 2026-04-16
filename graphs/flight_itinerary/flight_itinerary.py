# Flight Itinerary (LeetCode #332 — Reconstruct Itinerary, tuple variant)
#
# Given a list of (origin, destination) flight tuples, reconstruct the full
# itinerary starting from "JFK". Use all tickets exactly once. If multiple
# valid itineraries exist, return the one with the smallest lexical order.
#
# Example:
#   Input:  tickets = [("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
#   Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#
#   Input:  tickets = [("JFK", "SFO"), ("JFK", "ATL"), ("SFO", "ATL"), ("ATL", "JFK"), ("ATL", "SFO")]
#   Output: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]


def find_itinerary(tickets: list[tuple[str, str]]) -> list[str]:
    pass


if __name__ == "__main__":
    tickets = [("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
    assert find_itinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    tickets = [("JFK", "SFO"), ("JFK", "ATL"), ("SFO", "ATL"), ("ATL", "JFK"), ("ATL", "SFO")]
    assert find_itinerary(tickets) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

    tickets = [("JFK", "KUL"), ("JFK", "NRT"), ("NRT", "JFK")]
    assert find_itinerary(tickets) == ["JFK", "NRT", "JFK", "KUL"]

    print("All tests passed!")
