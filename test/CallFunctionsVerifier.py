#!/usr/bin/env python3

import time

class CallFunctionsVerifier:
    def __init__(self):
        self.called1 = False
        self.executionTime1 = 0
        self.called2 = False
        self.executionTime2 = 0

    def function1(self):
        self.called1 = True
        self.executionTime1 = time.time()

    def function2(self):
        self.called2 = True
        self.executionTime2 = time.time()
