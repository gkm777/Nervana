import sys
import csv

def percentile(p, data):
	try:
		p = int(p)
		assert p >= 0
		assert p <= 100
		assert data
	except:
		return "Invalid"
	if p <= 0:
		return 0
	if p >= 100:
		return data[-1]
	# input:
	#  p: percentile rank
	#  data: sorted samples
	# algorithm 2:
	#  based on statsmodels.distributions.empirical_distribution.ECDF
	#  N = len(data); divide 100 percentile by (N+1) sections linearly so that
	#   the first section (0~100/(N+1)) = 0
	#   the second section (100/(N+1)~200/(N+1)) = lowest score
	#   ...
	#   the (N+1)-th section (100*N/(N+1)~100) = highest score
	index = p * (len(data)+1) / 100	# 0~N (total numbers = N+1)
	if index < 1:
		return 0
	return data[index - 1]
	
	# Note: Since I use statsmodels lib for Bonus Challange 2, I should follow
	# its implementation for consistency. 
	# Therefore, I apply algorithm 2 instead of algorithm 1.
	# algorithm 1:
	#  wiki page http://en.wikipedia.org/wiki/Percentile#Nearest_Rank_method
	#  (valid 4/1/2015)
	#  The Nearest Rank method: 
	#   p   => data[ ceil(p / 100 * N) - 1 ]
	#   eg.
	#   0   => 0
	#   100 => highest data
	# return data[p * len(data) / 100]

class mean_test_score:
	def __init__(self):
		self.sum = 0
		self.num = 0
	def get(self):
		if self.num == 0:
			# this should never happen
			sys.stderr.write("error in mean_test_score: divide by 0")
			sys.exit(0)
		return self.sum / self.num
	def add(self, score):
		self.sum += score
		self.num += 1

def loadScores(school_name, input_files):
	students = dict()

	# read from files
	for input_file in input_files:
		with open(input_file, "r") as f:
			count = 0
			for columns in csv.reader(f):
				# student_id,course_name,school_name,test_date,test_score
				count += 1
				if len(columns) != 5:
					# just ignore it
					sys.stderr.write("warning: something's wrong at line "
									+ str(count) + " in file " + input_file)
				if columns[2] == school_name:
					if not columns[0] in students:
						students[columns[0]] = mean_test_score()
					students[columns[0]].add(float(columns[4]))

	scores = []
	for score in students.itervalues():
		scores.append(score.get())
	scores.sort()
	return scores

def usage():
	print "usage:", sys.argv[0], \
		  "--school", "SCHOOL_NAME", "INPUT_FILE_1", "[INPUT_FILE_i]*"

def parseArguments():
	# argument parsing: ecdf.py --school "name" input_file1 input_file2 ...
	if (len(sys.argv) < 4 or sys.argv[1] != "--school"):
		usage()
		sys.exit(0)
	school_name = sys.argv[2]
	return (school_name, loadScores(school_name, sys.argv[3:]))
	
def main():
	(school_name, scores) = parseArguments()
	
	# output to files
	print school_name, "students"
	print
	print "percentile\tmean_test_score"
	for i in range(1,101):
		print str(i) + "\t" + str(percentile(i, scores))

if __name__ == "__main__":
	main()
