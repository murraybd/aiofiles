#!/bin/sh

py.test-3 -k "not test_slow_file"
