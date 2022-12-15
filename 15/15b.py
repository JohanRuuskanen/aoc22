
class Sensor:
    def __init__(self, pos, beacon):
        self.pos = pos
        self.beacon = beacon
        self.cov = self.get_dist(beacon)

    def get_dist(self, z):
        return abs(self.pos[0] - z[0]) + abs(self.pos[1] - z[1])

    def cover(self, z):
        return self.get_dist(z) <= self.cov

    def covery(self, y):
        return self.get_dist((self.pos[0], y)) <= self.cov

with open("input", "r") as f:
    
    sensors = []
    for line in f.readlines():
        a = line.strip().split("=") 
        sensor = (int(a[1].split(",")[0]), int(a[2].split(":")[0]))
        beacon = (int(a[3].split(",")[0]), int(a[4]))
        sensors.append(Sensor(sensor, beacon))

def merge_intervals(intvs):
    intvs.sort(key=lambda x: x[0])
    new_intvs = []
    i = 0
    j = 1
    
    while i < len(intvs):
        v = intvs[i]
        while j < len(intvs):
            if v[1] >= intvs[j][0] - 1:
                v[1] = max(v[1], intvs[j][1])
                j += 1
            else:
                break
        i = j
        j += 1
        new_intvs.append(v)

    return new_intvs

xlim = [0, 4000000]
ylim = [0, 4000000]

pos = [0, 0]
point = []
for y in range(ylim[1]):
    intervals = []
    for i, s in enumerate(sensors):
        if s.covery(y):
            d = s.cov - abs(y - s.pos[1])
            intervals.append([s.pos[0] - d, s.pos[0] + d]) 
    v = merge_intervals(intervals)
    
    if len(v) > 1:
        for i in range(len(v)-1):
            if v[i][1] < xlim[0] or v[i+1][0] > xlim[1]-1:
                continue 
            elif v[i+1][0] - v[i][1] == 2:
                point = [v[i][1]+1, y] 
                break
            else:
                raise Exception("More than 1 possible points")

    if point:
        break

print("15b tuning frequency {}".format(point[0]*4000000+point[1]))
