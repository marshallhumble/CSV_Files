#Get specific results from a csv

def getColumn(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    return [result[column] for result in results]
    
#We can use this like this:

x = getColumn(csv_file,0)
y = getColumn(csv_file,1)

#etc
