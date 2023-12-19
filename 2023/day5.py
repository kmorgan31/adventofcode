#!/usr/bin/python

from aocd import lines

import pdb

EXAMPLE = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4"
]


MAPS = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
}


def find_map_match(m, num):
    for destination, source, range_len in m:
        if source <= num < source + range_len:
            return destination + (num - source)
    return num


def find_seed_location(seed):
    soil = find_map_match(MAPS['seed-to-soil'], seed)
    fertilizer = find_map_match(MAPS['soil-to-fertilizer'], soil)
    water = find_map_match(MAPS['fertilizer-to-water'], fertilizer)
    light = find_map_match(MAPS['water-to-light'], water)
    temperature = find_map_match(MAPS['light-to-temperature'], light)
    humidity = find_map_match(MAPS['temperature-to-humidity'], temperature)
    return find_map_match(MAPS['humidity-to-location'], humidity)


def find_location_seed(location):
    humidity = find_map_match(MAPS['humidity-to-location'], location)
    temperature = find_map_match(MAPS['temperature-to-humidity'], humidity)
    light = find_map_match(MAPS['light-to-temperature'], temperature)
    water = find_map_match(MAPS['water-to-light'], light)
    fertilizer = find_map_match(MAPS['fertilizer-to-water'], water)
    soil = find_map_match(MAPS['soil-to-fertilizer'], fertilizer)
    return find_map_match(MAPS['seed-to-soil'], soil)


def is_seed(seed, seeds):
    return any(start <= seed < end for start, end in seeds)


def get_seeds(data, part=None):
    seeds = data[0].split(":")[1].split()
    if part == 1:
        return seeds
    elif part == 2:
        return [
            (int(seeds[i]), int(seeds[i]) + int(seeds[i+1]))
            for i in range(0, len(seeds), 2)
        ]


def prepare_maps(data, part=None):
    current_map = None
    for line in data[2:]:
        if not line:
            continue
        else:
            entry = line.split()
            if 'map' in entry[1]:
                current_map = MAPS[entry[0]]
            elif len(entry) == 3:
                # add entries to current_map
                if part == 1:
                    current_map.append(
                        (int(entry[0]), int(entry[1]), int(entry[2]))
                    )
                elif part == 2:
                    current_map.append(
                        (int(entry[1]), int(entry[0]), int(entry[2]))
                    )


def part_1(data):
    prepare_maps(data, part=1)

    min_location = float("inf")
    for seed in get_seeds(data, part=1):
        location = find_seed_location(int(seed))
        print(f"Seed {seed} -> Location {location}")
        min_location = min(location, min_location)
    return min_location


def part_2(data):
    prepare_maps(data, part=2)

    # start from least location to find corresponding seed
    for location in range(100_000_000, 150_000_000):
        seed = find_location_seed(location)
        if is_seed(seed, get_seeds(data, part=2)):
            return location

        if location % 1_000_000 == 0:
            print(location)


if __name__ == '__main__':
    # print(f'Day 5: Part 1 {part_1(lines)}')
    print(f'Day 5: Part 2 {part_2(lines)}')
