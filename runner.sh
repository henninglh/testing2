#!/usr/bin/env sh
./generator.py
./random_connected_graph.py -p -g graph.gml rankings.txt
./gml_to_input.py
./solution.py
