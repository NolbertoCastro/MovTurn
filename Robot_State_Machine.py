# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:31:03 2023

@author: jusus
"""

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def main():
    # Graphviz graph
    g = graphviz.Digraph('G', filename='state_machine.gv')
    
    # Start node
    g.edge("START", "Looking right")
    
    # Idle nodes and transitions to moving with MOV
    g.edge("Looking right", "Moving right", "MOV")
    g.edge("Looking left", "Moving left", "MOV")
    g.edge("Looking up", "Moving up", "MOV")
    g.edge("Looking down", "Moving down", "MOV")
    
    # Moving nodes and immediate transition back to idle
    g.edge("Moving right", "Looking right")
    g.edge("Moving left", "Looking left")
    g.edge("Moving up", "Looking up")
    g.edge("Moving down", "Looking down")

    # Idle transitions with TURN to different directions using angles
    g.edge("Looking right", "Looking left", "TURN 180")
    g.edge("Looking left", "Looking right", "TURN 180")
    g.edge("Looking up", "Looking down", "TURN 180")
    g.edge("Looking down", "Looking up", "TURN 180")
    
    g.edge("Looking right", "Looking up", "TURN 90")
    g.edge("Looking left", "Looking down", "TURN 90")
    g.edge("Looking up", "Looking left", "TURN 90")
    g.edge("Looking down", "Looking right", "TURN 90")
    
    g.edge("Looking right", "Looking down", "TURN 270")
    g.edge("Looking left", "Looking up", "TURN 270")
    g.edge("Looking up", "Looking right", "TURN 270")
    g.edge("Looking down", "Looking left", "TURN 270")
    
    g.edge("Looking right", "Looking right", "TURN 360")
    g.edge("Looking left", "Looking left", "TURN 360")
    g.edge("Looking up", "Looking up", "TURN 360")
    g.edge("Looking down", "Looking down", "TURN 360")
    

    # Creates graph and opens it
    g.view()

main()    