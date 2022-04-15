#!/usr/bin/python3
# coding=utf-8

import unittest
from TestFeederInfo import FeederInfoTestCase

def main():

    suite = (unittest.TestLoader().loadTestsFromTestCase(FeederInfoTestCase))
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()