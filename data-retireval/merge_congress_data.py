clean_csv = open("data_clean.csv")
congress_csv = open("congressData.csv")
final_csv = open("final_data.csv", "w")

congress_info = {}
first = True
for line in congress_csv.readlines():
	if first == True:
		first = False
		continue
	info = line.split(",")
	congress_info[info[0]] = ",".join(info[1:]).strip()

print congress_info

for line in clean_csv.readlines():
	line = line.strip()
	congress = line.split(",")[0]
	status = line.split(",")[-1]
	final_csv.write(",".join(line.split(",")[:-1]) + "," + congress_info[congress] + "," + status + "\n")

clean_csv.close()
congress_csv.close()
final_csv.close()
