import sys
import csv

def usage():
	print "usage:", sys.argv[0], "--school", "SCHOOL_NAME", "INPUT_FILE_1", "[INPUT_FILE_i]*"

def percentile(p, scores):
	# p = 0 - 100; mapping to scores 0 - (len-1)
	if len(scores) <= 0:
		sys.stderr.write("ERROR: length of scores is 0")
		return
	if p <= 0:
		return 0
	if p >= 100:
		return scores[-1]
	return scores[p * len(scores) / 100]

# argument parsing: ecdf.py --school "name" input_file1 input_file2 ...
if (len(sys.argv) < 4 or sys.argv[1] != "--school"):
	usage()
	sys.exit(0)
school_name = sys.argv[2]

class mean_test_score:
	def __init__(self):
		self.sum = 0
		self.num = 0
	def get(self):
		if self.num == 0:
			# this should never happen since we don't create it without any sample input
			sys.stderr.write("error while getting mean_test_score: divide by 0")
			sys.exit(0)
		return self.sum / self.num
	def add(self, score):
		self.sum += score
		self.num += 1

students = dict()

# read from files
for input_file in sys.argv[3:]:
	with open(input_file, "r") as f:
		count = 0
		for columns in csv.reader(f):
			# student_id,course_name,school_name,test_date,test_score
			count += 1
			if len(columns) != 5:
				# just ignore it
				sys.stderr.write("warning: something's wrong at line " + str(count) + " in file " + input_file)
			if columns[2] == school_name:
				if not columns[0] in students:
					students[columns[0]] = mean_test_score()
				students[columns[0]].add(float(columns[4]))

# parse (sort score only)
scores = []
for score in students.itervalues():
	scores.append(score.get())
scores.sort()

# output to files
print school_name, "students"
print
print "percentile\tmean_test_score"
for i in range(1,101):
	print str(i) + "\t" + str(percentile(i, scores))
