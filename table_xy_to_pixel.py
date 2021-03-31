import csv
from coordi_conversion import convert_x, convert_y

# def writer(header, data, filename, option):
#         with open (filename, "w", newline = "") as csvfile:
#             if option == "write":

#                 movies = csv.writer(csvfile)
#                 movies.writerow(header)
#                 for x in data:
#                     movies.writerow(x)
#             elif option == "update":
#                 writer = csv.DictWriter(csvfile, fieldnames = header)
#                 writer.writeheader()
#                 writer.writerows(data)
#             else:
#                 print("Option is not known")


# def updater(filename):
#     with open(filename, newline= "") as file:
#         readData = [row for row in csv.DictReader(file)]
#         # print(readData)
#         readData[0]['Rating'] = '9.4'
#         # print(readData)

#     readHeader = readData[0].keys()
#     writer(readHeader, readData, filename, "update")

def main():
	inp = open('./Database/Filtered_data/filtered_esea_master_dmg_demos.csv', mode ='r')
	csvFile = csv.DictReader(inp)
	csvFile = [row for row in csvFile]

	up_dt = []
	
	# displaying the contents of the CSV file 
	for i, lines in enumerate(csvFile): 
		row = lines

		row['att_pos_x'] = convert_x(float(lines['att_pos_x']))
		row['att_pos_y'] = convert_y(float(lines['att_pos_y']))
		row['vic_pos_x'] = convert_x(float(lines['vic_pos_x']))
		row['vic_pos_y'] = convert_y(float(lines['vic_pos_y']))

		up_dt.append(row)
	
	headers = csvFile[0].keys()

	out = open("./Database/Filtered_data/test_dmg.csv", "w", newline='')

	out_file = csv.DictWriter(out, delimiter=',', fieldnames=headers)
	out_file.writerow(dict((heads, heads) for heads in headers))
	out_file.writerows(up_dt)
	
	out.close()


if __name__ == "__main__":
    main()

