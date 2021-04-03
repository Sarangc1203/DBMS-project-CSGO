import csv
from map_data import convert_x, convert_y

def build_dmg():
	inp = open('./filtered_esea_master_dmg_demos.csv', mode ='r')
	csvFile = csv.DictReader(inp)
	csvFile = [row for row in csvFile]

	up_dt = []

	# map_info = db_obj.execute_query(f"SELECT * FROM map_data")
	# print(map_info)
	
	# displaying the contents of the CSV file 
	for i, lines in enumerate(csvFile): 
		row = lines

		# map_info = db_obj.execute_query(f"SELECT * FROM map_data WHERE mapname=\'{lines['map']}\'")
		# print(map_info)

		row['att_pos_x'] = convert_x(float(lines['att_pos_x']), lines['map'])
		row['att_pos_y'] = convert_y(float(lines['att_pos_y']), lines['map'])
		row['vic_pos_x'] = convert_x(float(lines['vic_pos_x']), lines['map'])
		row['vic_pos_y'] = convert_y(float(lines['vic_pos_y']), lines['map'])

		up_dt.append(row)
	
	headers = csvFile[0].keys()

	out = open("./test_dmg.csv", "w", newline='')

	out_file = csv.DictWriter(out, delimiter=',', fieldnames=headers)
	out_file.writerow(dict((heads, heads) for heads in headers))
	out_file.writerows(up_dt)
	
	out.close()


def build_grenade():
	inp = open('./filtered_esea_master_grenade_demos.csv', mode ='r')
	csvFile = csv.DictReader(inp)
	csvFile = [row for row in csvFile]

	up_dt = []
	
	# displaying the contents of the CSV file 
	for i, lines in enumerate(csvFile): 
		row = lines

		# map_info = db_obj.execute_query(f"SELECT * FROM map_data WHERE mapname=\'{lines['map']}\'")

		row['att_pos_x'] = convert_x(float(lines['att_pos_x']), lines['map'])
		row['att_pos_y'] = convert_y(float(lines['att_pos_y']), lines['map'])
		row['nade_land_x'] = convert_x(float(lines['nade_land_x']), lines['map'])
		row['nade_land_y'] = convert_y(float(lines['nade_land_y']), lines['map'])
		
		if row['vic_pos_x']:
			row['vic_pos_x'] = convert_x(float(lines['vic_pos_x']), lines['map'])
		if row['vic_pos_y']:
			row['vic_pos_y'] = convert_y(float(lines['vic_pos_y']), lines['map'])

		up_dt.append(row)
	
	headers = csvFile[0].keys()

	out = open("./test_grenade.csv", "w", newline='')

	out_file = csv.DictWriter(out, delimiter=',', fieldnames=headers)
	out_file.writerow(dict((heads, heads) for heads in headers))
	out_file.writerows(up_dt)
	
	out.close()


def main():
	build_dmg()
	build_grenade()
	print('---Conversion Done---')


if __name__ == "__main__":
    main()

