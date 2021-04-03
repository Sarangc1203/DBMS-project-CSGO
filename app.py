from flask import Flask, redirect, url_for, request, render_template
from db import Database
import config
import os

from Database.map_data import draw_figure, draw_points

app = Flask(__name__)

app.config['DEBUG'] = True

db_obj = Database()
db_obj.connect()

CS_GO_CT_COLOR = (92, 159, 239)
CS_GO_T_COLOR = (222,155,53)

@app.route('/')
def index():

	# result = db_obj.execute_query('select distinct wp_type, wp from test_dmg order by wp_type, wp;')
	# s = ''
	# for row in result:
	# 	s = s + f'<option value="{row[1]}">{row[0]} - {row[1]}</option>\n'
	# print(s)
	return render_template('index.html')

	# return '''
	# <html>
	# <body>
	# <a href="http://localhost:5000/display">Show Image!</a>
	# <form action="http://localhost:5000/login" method="post">
	# 	<p>Enter count number:</p>
	# 	<p><input type = "text" name="nm"/></p>
	# 	<p><input type="submit" value="submit"/></p>
	# </form>
	# </body>
	# </html>
	# '''


@app.route('/login', methods=['POST'])
def login():
	name = request.form['nm']
	result = db_obj.execute_query('SELECT * FROM team LIMIT '+name+';')
	output = 'Hello World!<br><br>'+name

	for row in result:
		output = output + '|' + str(row[0]) + '\t|\t' + str(row[1]) + '<br>'

	return output


@app.route('/display')
def display():
	delta = 16
	topx1 = 20
	map = 'de_overpass' # 'de_dust2', 'de_overpass'
	
	# result = db_obj.execute_query(f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select vic_pos_x / {delta} as x, vic_pos_y / {delta} as y, count(*) from test_dmg where vic_side='CounterTerrorist' group by x, y) as tmp) as tmp2 where rank <= {topx};")
	# # print(result)

	# draw_figure([row[0] for row in result], [row[1] for row in result], delta, CS_GO_CT_COLOR, "out_1")

	# result = db_obj.execute_query(f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select vic_pos_x / {delta} as x, vic_pos_y / {delta} as y, count(*) from test_dmg where vic_side='Terrorist' group by x, y) as tmp) as tmp2 where rank <= {topx};")
	# # print(result)

	# draw_figure([row[0] for row in result], [row[1] for row in result], delta, CS_GO_T_COLOR, "out_2")
	
	query1 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select vic_pos_x / {delta} as x, vic_pos_y / {delta} as y, count(*) from test_dmg where vic_side='CounterTerrorist' and map=\'{map}\' group by x, y) as tmp) as tmp2 where rank <= {topx1};"
	result1 = db_obj.execute_query(query1)

	query2 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select vic_pos_x / {delta} as x, vic_pos_y / {delta} as y, count(*) from test_dmg where vic_side='Terrorist' and map=\'{map}\' group by x, y) as tmp) as tmp2 where rank <= {topx1};"
	result2 = db_obj.execute_query(query2)

	x_list_list = [[row[0] for row in result1], [row[0] for row in result2]]
	y_list_list = [[row[1] for row in result1], [row[1] for row in result2]]

	# print(result1)
	# print(result2)
	# print(x_list_list)
	draw_figure(x_list_list, y_list_list, delta, [CS_GO_CT_COLOR, CS_GO_T_COLOR], map, "out_1")

	topx2 = 10
	round_time = 30
	grenade_type = 'Flash' # 'Smoke', 'Incendiary', 'Flash', 'Molotov', 'Decoy', 'HE'

	query3 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select nade_land_x / {delta} as x, nade_land_y / {delta} as y, count(*) from (select tg.file, tg.round, tg.nade_land_x, tg.nade_land_y, tg.seconds-fr.start_seconds as seconds, tg.att_side, tg.map from (select * from test_grenade where nade=\'{grenade_type}\') as tg, test_rounds as fr where tg.file=fr.file and tg.round=fr.round) as tmp where att_side='CounterTerrorist' and map=\'{map}\' and seconds<={round_time} group by x, y) as tmp1) as tmp2 where rank <= {topx2};"

	result3 = db_obj.execute_query(query3)

	query4 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select nade_land_x / {delta} as x, nade_land_y / {delta} as y, count(*) from (select tg.file, tg.round, tg.nade_land_x, tg.nade_land_y, tg.seconds-fr.start_seconds as seconds, tg.att_side, tg.map from (select * from test_grenade where nade=\'{grenade_type}\') as tg, test_rounds as fr where tg.file=fr.file and tg.round=fr.round) as tmp where att_side='Terrorist' and map=\'{map}\' and seconds<={round_time} group by x, y) as tmp1) as tmp2 where rank <= {topx2};"
	result4 = db_obj.execute_query(query4)

	x_list_list = [[row[0] for row in result3], [row[0] for row in result4]]
	y_list_list = [[row[1] for row in result3], [row[1] for row in result4]]
	draw_figure(x_list_list, y_list_list, delta, [CS_GO_CT_COLOR, CS_GO_T_COLOR], map, "out_2")

	is_bomb_planted = 't'
	bomb_site = 'B'
	weapon_ct = 'AWP'
	topx3 = 10

	query5 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select att_pos_x / {delta} as x, att_pos_y / {delta} as y, count(*) from (select * from test_kills where wp=\'{weapon_ct}\' AND att_side='CounterTerrorist' and map=\'{map}\' AND is_bomb_planted=\'{is_bomb_planted}\' AND bomb_site=\'{bomb_site}\') as tmp group by x, y) as tmp1) as tmp2 where rank <= {topx3};"
	result5 = db_obj.execute_query(query5)

	weapon_t = 'AWP'
	query6 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select att_pos_x / {delta} as x, att_pos_y / {delta} as y, count(*) from (select * from test_kills where wp=\'{weapon_t}\' AND att_side='Terrorist' and map=\'{map}\' AND is_bomb_planted=\'{is_bomb_planted}\' AND bomb_site=\'{bomb_site}\') as tmp group by x, y) as tmp1) as tmp2 where rank <= {topx3};"
	result6 = db_obj.execute_query(query6)

	x_list_list = [[row[0] for row in result5], [row[0] for row in result6]]
	y_list_list = [[row[1] for row in result5], [row[1] for row in result6]]
	draw_figure(x_list_list, y_list_list, delta, [CS_GO_CT_COLOR, CS_GO_T_COLOR], map, "out_3")

	# full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
	# full_filename = '/home/sarang/Desktop/Codes/COL362/Project/' + 'out.png'

	# output = '''
	# <html>
	# <body>
	# Hello <br>
	# <img src="/home/sarang/Desktop/Codes/COL362/Project/out.png" alt="Top 20 dmg locations">
	# </body>
	# </html>
	# '''

	# draw_figure([result[0][0]], [result[0][1]], delta)

	# result = db_obj.execute_query(f'SELECT att_pos_x, att_pos_y FROM test_dmg LIMIT 20;')
	# print(result)

	# draw_points([row[0] for row in result], [row[1] for row in result], 5)

	# return output

	return render_template('display.html')


@app.route('/query1')
def query1():
	return render_template('query1.html')

@app.route('/query2')
def query2():
	return render_template('query2.html')

@app.route('/show_q2', methods=['POST'])
def show_q2():
	return render_template('show_q3.html')

@app.route('/query3')
def query3():
	return render_template('query3.html')

@app.route('/show_q3', methods=['POST'])
def show_q3():
	print([key for key in request.form.keys()])

	delta = int(request.form['delta'])

	map = request.form['map']
	topx = request.form['topx']
	is_bomb_planted = 't' if 'is_bomb_planted' in request.form.keys() else 'f'
	bomb_site = request.form['bomb_site']

	ct_bool = 't' if 'ct_bool' in request.form.keys() else 'f'
	ct_weapon = request.form['ct_weapon']

	t_bool = 't' if 't_bool' in request.form.keys() else 'f'
	t_weapon = request.form['t_weapon']

	print(map, topx, is_bomb_planted, bomb_site, ct_bool, ct_weapon, t_bool, t_weapon)

	x_list_list = []
	y_list_list = []
	color_list = []
	
	if ct_bool == 't':
		query5 = ""
		if is_bomb_planted == 't':
			query5 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select att_pos_x / {delta} as x, att_pos_y / {delta} as y, count(*) from (select * from test_kills where wp=\'{ct_weapon}\' AND att_side='CounterTerrorist' and map=\'{map}\' AND is_bomb_planted=\'{is_bomb_planted}\' AND bomb_site=\'{bomb_site}\') as tmp group by x, y) as tmp1) as tmp2 where rank <= {topx};"
		else:
			query5 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select att_pos_x / {delta} as x, att_pos_y / {delta} as y, count(*) from (select * from test_kills where wp=\'{ct_weapon}\' AND att_side='CounterTerrorist' and map=\'{map}\' AND is_bomb_planted=\'{is_bomb_planted}\') as tmp group by x, y) as tmp1) as tmp2 where rank <= {topx};"
		result5 = db_obj.execute_query(query5)
		x_list_list.append([row[0] for row in result5])
		y_list_list.append([row[1] for row in result5])
		color_list.append(CS_GO_CT_COLOR)
	
	if t_bool == 't':
		query5 = ""
		if is_bomb_planted == 't':
			query5 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select att_pos_x / {delta} as x, att_pos_y / {delta} as y, count(*) from (select * from test_kills where wp=\'{t_weapon}\' AND att_side='Terrorist' and map=\'{map}\' AND is_bomb_planted=\'{is_bomb_planted}\' AND bomb_site=\'{bomb_site}\') as tmp group by x, y) as tmp1) as tmp2 where rank <= {topx};"
		else:
			query5 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select att_pos_x / {delta} as x, att_pos_y / {delta} as y, count(*) from (select * from test_kills where wp=\'{t_weapon}\' AND att_side='Terrorist' and map=\'{map}\' AND is_bomb_planted=\'{is_bomb_planted}\') as tmp group by x, y) as tmp1) as tmp2 where rank <= {topx};"
		result5 = db_obj.execute_query(query5)
		x_list_list.append([row[0] for row in result5])
		y_list_list.append([row[1] for row in result5])
		color_list.append(CS_GO_T_COLOR)

	draw_figure(x_list_list, y_list_list, delta, color_list, map, "out")

	return render_template('show_q3.html')


@app.route('/query4')
def query4():
	return render_template('query4.html')

@app.route('/show_q4', methods=['POST'])
def show_q4():
	print([key for key in request.form.keys()])

	delta = int(request.form['delta'])

	map = request.form['map']
	topx = request.form['topx']

	ct_bool = 't' if 'ct_bool' in request.form.keys() else 'f'

	t_bool = 't' if 't_bool' in request.form.keys() else 'f'

	print(delta, map, topx, ct_bool, t_bool)

	x_list_list = []
	y_list_list = []
	color_list = []
	
	if ct_bool == 't':
		query1 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select vic_pos_x / {delta} as x, vic_pos_y / {delta} as y, count(*) from test_dmg where vic_side='CounterTerrorist' and map=\'{map}\' group by x, y) as tmp) as tmp2 where rank <= {topx};"
		result1 = db_obj.execute_query(query1)
		x_list_list.append([row[0] for row in result1])
		y_list_list.append([row[1] for row in result1])
		color_list.append(CS_GO_CT_COLOR)
	
	if t_bool == 't':
		query1 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select vic_pos_x / {delta} as x, vic_pos_y / {delta} as y, count(*) from test_dmg where vic_side='Terrorist' and map=\'{map}\' group by x, y) as tmp) as tmp2 where rank <= {topx};"
		result1 = db_obj.execute_query(query1)
		x_list_list.append([row[0] for row in result1])
		y_list_list.append([row[1] for row in result1])
		color_list.append(CS_GO_T_COLOR)

	draw_figure(x_list_list, y_list_list, delta, color_list, map, "out")

	return render_template('show_q3.html')

@app.route('/query6')
def query6():
	return render_template('query6.html')

@app.route('/show_q6', methods=['POST'])
def show_q6():
	print([key for key in request.form.keys()])

	budget = int(request.form['budget'])

	map = request.form['map']
	team_side = request.form['team_side']

	wp_type = request.form['wp_type']

	print("-------", map, team_side, budget, "-------")

	# query = "drop view budget_data_t; drop view budget_data_ct; drop view weapon_data_t; drop view weapon_data_ct; SELECT * from map_data;"
	# result = db_obj.execute_query(query)

	query = '''
	WITH weapon_data_team as (
		with weapon_data as
		(
			select wp_type,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
			from (select file,round,hp_dmg,arm_dmg,wp,wp_type,att_side from test_dmg where wp!='Unknown' AND map=\''''+map+'''\' ''' + ('' if wp_type=='All' else 'AND wp_type=\''+wp_type+'\'') + ''') as a1
			group by wp_type,wp,att_side
			order by wp_type,health_damage desc, armor_damage desc,wp
		)

		select wp_type,wp,att_side,price,health_damage,armor_damage
		from (select * from weapon_price where price is not NULL and weapon_price.''' + ('ct' if team_side=='CounterTerrorist' else 't') + ''' = 't') as a2 natural join weapon_data
		where att_side= \''''+team_side+'''\' AND price<='''+str(budget)+'''
	)

	select wp_type,wp,price
	from(select wp_type,wp,att_side,price,health_damage,armor_damage,rank() OVER (PARTITION BY wp_type ORDER BY health_damage desc,armor_damage desc,wp) as rank
		from weapon_data_team
		) as a4
	where rank <=1
	;
	'''

	print(query)
	result = db_obj.execute_query(query)
	# print(result)

	# print("query done!!")

	return render_template('show_q6.html', output_table=result)

@app.route('/query8')
def query8():
	return render_template('query8.html')

@app.route('/show_q8', methods=['POST'])
def show_q8():

	if os.path.isfile('static/out.png'):
		# print("File exists!")
		os.remove('static/out.png')
	# else:
	# 	print("File Error!")

	print([key for key in request.form.keys()])

	delta = int(request.form['delta'])

	map = request.form['map']
	topx = request.form['topx']
	grenade_type = request.form['grenade']
	round_time = request.form['round_time']

	ct_bool = 't' if 'ct_bool' in request.form.keys() else 'f'

	t_bool = 't' if 't_bool' in request.form.keys() else 'f'

	print(delta, map, topx, ct_bool, t_bool)

	x_list_list = []
	y_list_list = []
	color_list = []
	
	if ct_bool == 't':
		query3 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select nade_land_x / {delta} as x, nade_land_y / {delta} as y, count(*) from (select tg.file, tg.round, tg.nade_land_x, tg.nade_land_y, tg.seconds-fr.start_seconds as seconds, tg.att_side, tg.map from (select * from test_grenade where nade=\'{grenade_type}\') as tg, test_rounds as fr where tg.file=fr.file and tg.round=fr.round) as tmp where att_side='CounterTerrorist' and map=\'{map}\' and seconds<={round_time} group by x, y) as tmp1) as tmp2 where rank <= {topx};"
		result3 = db_obj.execute_query(query3)
		x_list_list.append([row[0] for row in result3])
		y_list_list.append([row[1] for row in result3])
		color_list.append(CS_GO_CT_COLOR)
	
	if t_bool == 't':
		query3 = f"select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select nade_land_x / {delta} as x, nade_land_y / {delta} as y, count(*) from (select tg.file, tg.round, tg.nade_land_x, tg.nade_land_y, tg.seconds-fr.start_seconds as seconds, tg.att_side, tg.map from (select * from test_grenade where nade=\'{grenade_type}\') as tg, test_rounds as fr where tg.file=fr.file and tg.round=fr.round) as tmp where att_side='Terrorist' and map=\'{map}\' and seconds<={round_time} group by x, y) as tmp1) as tmp2 where rank <= {topx};"
		result3 = db_obj.execute_query(query3)
		x_list_list.append([row[0] for row in result3])
		y_list_list.append([row[1] for row in result3])
		color_list.append(CS_GO_T_COLOR)

	draw_figure(x_list_list, y_list_list, delta, color_list, map, "out")
	# , opt=f'{delta}\t{map}\t{topx}\t{grenade_type}\t{round_time}\t{ct_bool}\t{t_bool}', output='out_3.png'

	return render_template('show_q3.html')

@app.route('/query9')
def query9():
	return render_template('query9.html')

@app.route('/show_q9', methods=['POST'])
def show_q9():

	print([key for key in request.form.keys()])

	budget = int(request.form['budget'])

	map = request.form['map']
	team_side = request.form['team_side']

	print("-------", map, team_side, budget, "-------")

	query = '''
	WITH weapon_data_team as (
		with weapon_data as
		(
			select wp_type,wp,att_side,AVG(hp_dmg) as health_damage,AVG(arm_dmg) as armor_damage
			from (select file,round,hp_dmg,arm_dmg,wp,wp_type,att_side from test_dmg where wp!='Unknown' AND map=\''''+map+'''\') as a1
			group by wp_type,wp,att_side
			order by wp_type,health_damage desc, armor_damage desc,wp
		)

		select wp_type,wp,att_side,price,health_damage,armor_damage
		from (select * from weapon_price where price is not NULL and weapon_price.''' + ('ct' if team_side=='CounterTerrorist' else 't') + ''' = 't') as a2 natural join weapon_data
		where att_side= \''''+team_side+'''\' 
	),
	budget_data_team as (
		with equipment_data as (select wp_type,wp,price,health_damage,armor_damage from weapon_data_team where wp_type = 'Equipment' ),
		grenade_data as (select wp_type,wp,price,health_damage,armor_damage from weapon_data_team where wp_type = 'Grenade' ),
		a1 as(select equipment_data.wp as Equipment_weapon,grenade_data.wp as Grenade_weapon, (equipment_data.price + grenade_data.price) as price, (equipment_data.health_damage + grenade_data.health_damage) as health_damage , (equipment_data.armor_damage + grenade_data.armor_damage) as armor_damage from equipment_data join grenade_data on grenade_data.wp_type!=equipment_data.wp_type),

		heavy_data as (select wp_type,wp,price,health_damage,armor_damage from weapon_data_team where wp_type = 'Heavy' ),
		pistol_data as (select wp_type,wp,price,health_damage,armor_damage from weapon_data_team where wp_type = 'Pistol' ),
		a2 as (select heavy_data.wp as Heavy_weapon,pistol_data.wp as Pistol_weapon, (heavy_data.price + pistol_data.price) as price, (heavy_data.health_damage + pistol_data.health_damage) as health_damage , (heavy_data.armor_damage + pistol_data.armor_damage) as armor_damage from heavy_data join pistol_data on heavy_data.wp_type!=pistol_data.wp_type),

		rifle_data as (select wp_type,wp,price,health_damage,armor_damage from weapon_data_team where wp_type = 'Rifle' ),
		smg_data as (select wp_type,wp,price,health_damage,armor_damage from weapon_data_team where wp_type = 'SMG' ),
		a3 as (select rifle_data.wp as Rifle_weapon,smg_data.wp as SMG_weapon, (rifle_data.price + smg_data.price) as price, (rifle_data.health_damage + smg_data.health_damage) as health_damage , (rifle_data.armor_damage + smg_data.armor_damage) as armor_damage from rifle_data join smg_data on rifle_data.wp_type!=smg_data.wp_type),

		a4 as (select  Equipment_weapon, Grenade_weapon, Heavy_weapon, Pistol_weapon, (a1.price + a2.price) as price, (a1.health_damage + a2.health_damage) as health_damage , (a1.armor_damage + a2.armor_damage) as armor_damage from a1 join a2 on a1.Equipment_weapon!=a2.Heavy_weapon),

		sniper_data as (select wp_type,wp,price,health_damage,armor_damage from weapon_data_team where wp_type = 'Sniper' ),
		a5 as (select  Rifle_weapon, SMG_weapon, sniper_data.wp as Sniper_weapon, (a3.price + sniper_data.price) as price, (a3.health_damage + sniper_data.health_damage) as health_damage , (a3.armor_damage + sniper_data.armor_damage) as armor_damage from a3 join sniper_data on a3.Rifle_weapon!=sniper_data.wp)

		select  Equipment_weapon, Grenade_weapon, Heavy_weapon, Pistol_weapon,  Rifle_weapon, SMG_weapon, Sniper_weapon,(a4.price + a5.price) as price, (a4.health_damage + a5.health_damage)/7 as health_damage , (a4.armor_damage + a5.armor_damage)/7 as armor_damage from a4 join a5 on a4.Equipment_weapon!=a5.Sniper_weapon
	)
	select * from budget_data_team where price <= ''' + str(budget) + ''' order by health_damage desc, armor_damage desc limit 1;
	;
	
	'''

	print(query)
	result = db_obj.execute_query(query)
	print(result)

	# print("query done!!")

	return render_template('show_q9.html', output_table=result)

if __name__ == '__main__':
	app.run()