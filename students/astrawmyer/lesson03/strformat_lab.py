#!/usr/bin/env python3

input_tuple = (2, 123.4567, 10000, 12345.67)

#Task One

task_one = 'file_{0:0>3}: {1:.2f}, {2:.2e}, {3:.2e}'.format(2, 123.4567, 10000, 12345.67)
print(task_one)

#Made it generic for inputs.
asd = 'file_{0:0>3}: {1:.2f}, {2:.2e}, {3:.2e}'.format(*input_tuple)
print(asd)

#Task Two

