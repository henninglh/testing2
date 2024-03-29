#!/usr/bin/env python
from toposort import toposort
from collections import defaultdict
network = defaultdict(set)
with open("input.txt", "r") as f:
    lines = [i for i in f.readlines()]
    for line in lines:
        source, target = [i.strip() for i in line.split(">")]
        network[source].add(target)
print list(toposort(network))
