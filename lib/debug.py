#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    # p1 = NationalPark("Yosemmette")
    # vis = Visitor('Tom')
    # vis2 = Visitor('Mark')
    # t_1 = Trip(vis, p1, "May 5th", "May 9th")
    # t_3 = Trip(vis, p1, "January 5th","January 20th")
    # t_3 = Trip(vis2, p1, "January 5th","January 20th")
    
    p1 = NationalPark("Yosemmette")
    vis = Visitor('Sheryl')
    t1 = Trip(vis, p1, "May 5th", "May 9th")
    t2 = Trip(vis, p1, "June 20th", "July 4th")
    t3 = Trip(vis, p1, "January 5th","January 20th")
    
    ipdb.set_trace()
