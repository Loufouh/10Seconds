#!/usr/bin/env python3

class ClockDummy: # pylint: disable=R0903
    ''' Simplified Clock class for testing.'''
    def __init__(self, timeIncrement):
        self.timeIncrement = timeIncrement

    def get_time(self):
        return self.timeIncrement
