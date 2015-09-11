import csv
afile = open('Workbook1.csv','r+')
csvReader1 = csv.reader(afile)
for row in csvReader1:
	print("    \u0027", row[0],"\u0027 \u003A \u0027", row[1],"\u0027,")