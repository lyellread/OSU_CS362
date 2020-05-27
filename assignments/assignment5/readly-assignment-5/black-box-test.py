#!/usr/bin/env python3

import os
from subprocess import Popen, PIPE, STDOUT
import sys

def correct (matrix):

	# this would be the correct implementation of the function that derives W, T

	# alternatively, this program could be run and the output shown, and a dictionary of correct outputs produced manually, depending on the problem at hand.

	return [W, T]

def run_prog (progname, args):

	# This runs the program with name progname, and passes it each argument
	#provided in the list args. 

	cmd = progname + ' ' + ' '.join(args)
	p = Popen(cmd, 
			shell=True,
			stdin=PIPE,
			stdout=PIPE,
			stderr=STDOUT,
			close_fds=True)

	# parse stdout according to output pattern, to generate W and T
	return [W, T]

def test_ecp_class (n, side, x, y, progname):

	#This ECP Class test tests that numbers of length n are processed correctly.

	if side == top:
		min_random = 10**(abs(n)-1)
		max_random = int(min_random * 1.1)
	else:
		max_random = 10**abs(n) - 1
		min_random = int(max_random * 0.9)

	if n < 0:
		min_random *= -1
		max_random *= -1


	# Fill matrix semi-randomly with either 0 or a val in range
	matix = [[random.choice([0].append(random.randint(min_random, max_random))) for a in x] for b in y]

	assert correct(matrix) == run_prog(progname, str(matrix)), "ERROR: Caught failure case with matrix: " + matrix

	return


def test_ecp_zero_locatio():

	# this tests top three and bottom three locations of the first nonzero

	# positive
	matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
				[0, , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

	assert correct(matrix) == run_prog(progname, str(matrix)), "ERROR: Caught failure case with matrix: " + matrix

	# negative
	matrix = [[0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
				[0, , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0]]

	assert correct(matrix) == run_prog(progname, str(matrix)), "ERROR: Caught failure case with matrix: " + matrix

	return

def run_tests ():

	# test class boundaries.

	# Testing classes of number lengths (num digits) in array values
	for x in range (0, len(INT_MAX)):

		# positive
		test_ecp_class(x, bottom, 9, 9, progname)
		test_ecp_class(x, top, 9, 9, progname)

		# negative
		test_ecp_class(-1 * x, bottom, 9, 9, progname)
		test_ecp_class(-1 * x, top, 9, 9, progname)

	# Testing array length classes from 1 digit to ARRAY_SIZE bottom and top respectively
	for x in range (0, len(ARRAY_MAX)):

		min_random = 10**(x-1)
		max_random = int(min_random * 1.1)

		# positive
		test_ecp_class(5, 
						bottom, 
						random.randint(min_random, max_random), 
						random.randint(min_random, max_random), 
						progname)
		# negative
		test_ecp_class(-5, 
						bottom, 
						random.randint(min_random, max_random), 
						random.randint(min_random, max_random), 
						progname)

		max_random = 10**x - 1
		min_random = int(max_random * 0.9)
		
		# positive
		test_ecp_class(5, 
						bottom, 
						random.randint(min_random, max_random), 
						random.randint(min_random, max_random), 
						progname)
		# negative
		test_ecp_class(-5, 
						bottom, 
						random.randint(min_random, max_random), 
						random.randint(min_random, max_random), 
						progname)

	# Testing if X position of nonzero changes anything.
	# i.e. class is position of nonzero, boundaries are start and end of array.

	test_ecp_zero_location()

	return


if __name__ == "__main__":

	assert len(sys.argv) == 3, "Please provide an argument with the name of the executable to test. Quitting."
	assert os.path.exists(sys.argv[1]), "That executable file is not valid. Quitting."
	ARRAY_MAX = int(sys.argv[2])
	progname = sys.argv[1]





 