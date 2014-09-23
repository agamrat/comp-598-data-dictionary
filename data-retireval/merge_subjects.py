data = open("final_data.csv")
subjects = open("subjects.csv")
final = open("data_with_subjects.csv", "w")

data_lines = data.readlines()
subjects_lines = subjects.readlines()

for i in xrange(0, len(data_lines)):
	final.write(data_lines[i].strip() + "," + subjects_lines[i].strip() + "\n")

data.close()
subjects.close()
final.close()
