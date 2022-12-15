
class Sensor:
    def __init__(self, pos, beacon):
        self.pos = pos
        self.beacon = beacon
        self.cov = self.get_dist(beacon)

    def get_dist(self, z):
        return abs(self.pos[0] - z[0]) + abs(self.pos[1] - z[1])

    def cover(self, z):
        return self.get_dist(z) <= self.cov

with open("input", "r") as f:
    
    sensors = []
    for line in f.readlines():
        a = line.strip().split("=") 
        sensor = (int(a[1].split(",")[0]), int(a[2].split(":")[0]))
        beacon = (int(a[3].split(",")[0]), int(a[4]))
        sensors.append(Sensor(sensor, beacon))

y = 2000000  #10
nob = 0
beacons = set([s.beacon for s in sensors])
beacons_at_y = [b for b in beacons if b[1] == y]
for i in range(-2*y, 4*y):
    if (i, y) in beacons_at_y:
        continue
    for s in sensors:
        if s.cover((i, y)):
            nob += 1
            break


