#!/usr/bin/env python

nodes = {}

with open("graph.gml", "r") as gml, open("input.txt", "w") as f:
    lines = gml.readlines();
    filtered_lines = []
    for line in lines:
        if "graph [" not in line \
            and "node [" not in line \
            and "]" not in line \
            and "edge [" not in line:
            filtered_lines.append(line)


    lines_iterator = iter(filtered_lines)
    edges = 0
    for x in lines_iterator:
        line1 = [i.strip().replace('"', '') for i in x.split()]
        line2 = [i.strip().replace('"', '') for i in next(lines_iterator).split()]

        if line1[0].startswith("id"):
            source_key = line1[1]
            target_key = ""
            if len(line2) > 2:
                target_key = ' '.join(line2[1:])
            else:
                target_key = line2[1]
            nodes[source_key] = target_key
        else:
            source = nodes[line1[1]]
            target = ""
            if len(line2) > 2:
                target = ' '.join(line2[1:])
            else:
                target = nodes[line2[1]]
            f.write("{} > {}\n".format(source, target))
            edges += 1
    print "edges: {}".format(edges)
