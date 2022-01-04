class Workout:
    def __init__(self, name, capacity, prem_only, class_time, id = None):
        self.name = name
        self.capacity = capacity
        self.prem_only = prem_only
        self.class_time = class_time
        self.id = id