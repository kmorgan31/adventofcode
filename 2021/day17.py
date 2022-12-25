#!/usr/bin/python

from aocd import lines

test_data = 'target area: x=20..30, y=-10..-5'


class OceanTrench():

    def __init__(self):
        pass

    def get_target_area(self, data):
        parts = data.split(': ')
        x_part, y_part = parts[1].split(', ')

        self.x_min = int(x_part.split('..')[0][2:])
        self.x_max = int(x_part.split('..')[1])
        self.y_min = int(y_part.split('..')[0][2:])
        self.y_max = int(y_part.split('..')[1])

    def check_in_target_area(self, probe):
        return (
            self.x_min <= probe.xp <= self.x_max and
            self.y_min <= probe.yp <= self.y_max
        )


class Probe():

    def __init__(self):
        self.xp = 0
        self.yp = 0

    def probe_step(self, vx, vy):
        # increase probe position by x, y
        self.xp += vx
        self.yp += vy

        # return updated velocity based on drag and gravity
        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1
        vy -= 1

        return vx, vy

    def launch(self, vx, vy, trench):
        peak_trajectory = 0
        while self.xp <= trench.x_max and self.yp >= trench.y_min:
            vx, vy = self.probe_step(vx, vy)

            peak_trajectory = max(peak_trajectory, self.yp)
            if trench.check_in_target_area(self):
                return peak_trajectory


def main(data, part):
    trench = OceanTrench()
    trench.get_target_area(data)

    highest_y_pos = 0
    num_in_target = 0
    for x in range(trench.x_max + 1):
        for y in range(-200, 200):
            peak_trajectory = Probe().launch(x, y, trench)
            if peak_trajectory is not None:
                num_in_target += 1
                highest_y_pos = max(highest_y_pos, peak_trajectory)

    if part == 1:
        return highest_y_pos
    elif part == 2:
        return num_in_target


if __name__ == '__main__':

    # tests
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    lines = lines[0]
    print(f'Day 17: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
