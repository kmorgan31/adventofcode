#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data
from collections import defaultdict


EXAMPLE = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def parse_data(input_data):
    reports = []
    page_ordering_rules = defaultdict(list)

    for line in input_data.split('\n'):
        if "|" in line:
            page1, page2 = line.split("|")
            page_ordering_rules[page1].append(page2)
        elif "," in line:
            reports.append(line.split(","))

    return reports, page_ordering_rules


def total(reports):
    return sum([int(pages[int(len(pages)/2)]) for pages in reports])


def is_ordered(pages, page_ordering_rules):
    for i in range(len(pages)):
        if set(pages[i+1:]).difference(set(page_ordering_rules[pages[i]])) != set():
            return False
    return True

def reorder_pages(pages, page_ordering_rules):
    for i in range(len(pages)):
        for j in range(0, len(pages)-i-1):
            if not pages[j+1] in page_ordering_rules[pages[j]]:
                pages[j], pages[j+1] = pages[j+1], pages[j]
    return pages


def main(input_data, part=None):
    correct, incorrect = [], []

    reports, page_ordering_rules = parse_data(input_data)
    for pages in reports:
        if is_ordered(pages, page_ordering_rules):
            correct.append(pages)
        else:
            incorrect.append(pages)

    if part == 1:
        return total(correct)
    elif part == 2:
        reordered = [reorder_pages(pages, page_ordering_rules) for pages in incorrect]
        return total(reordered)



if __name__ == '__main__':
    print(f'Day 5: Part 1 {main(EXAMPLE, 1)}')
    print(f'Day 5: Part 1 {main(data, 1)}')
    print(f'Day 5: Part 2 {main(EXAMPLE, 2)}')
    print(f'Day 5: Part 2 {main(data, 2)}')
