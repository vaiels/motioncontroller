## MMS
class PathPlanner():
    def __init__(self, csv_reference):
        self._reference = self._load_reference_csv(csv_reference)

    def get_next_reference(self, car_state):
        # Should find the closest reference to the current position, and then return the next 10 refs
        return []

    def _load_reference_csv(self, csv_reference):
        # Should just hardcode the reference lines for each trackmap
        return []
