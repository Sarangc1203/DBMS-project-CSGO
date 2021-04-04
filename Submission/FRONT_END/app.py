from flask import Flask, redirect, url_for, request, render_template
from db import Database
import config
import os

from map_data import draw_figure, draw_points

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
	# <a href="http://localhost:5026/display">Show Image!</a>
	# <form action="http://localhost:5026/login" method="post">
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

@app.route('/show_q1', methods=['POST'])
def show_q1():

	map = request.form['map']
	round_type = request.form['round_type']

	query = '''
	with valid_rounds as /*aayush*/
	(
		select file,round,winner_side
		from test_rounds where round_type = \''''+round_type+'''\' and map=\''''+map+'''\'
	),
	bombed_rounds as /*aayush*/
	(
		select distinct file,round,bomb_site
		from test_dmg
		where is_bomb_planted = true
	)
	select * from
	(
		with valid_bombed_rounds as
		(
			select valid_rounds.file,valid_rounds.round,winner_side,bomb_site
			from valid_rounds,bombed_rounds
			where valid_rounds.file = bombed_rounds.file and valid_rounds.round = bombed_rounds.round
		)
		select winner_side,bomb_site,count(*)
		from valid_bombed_rounds
		group by winner_side,bomb_site
	) as foo;
	'''

	result = db_obj.execute_query(query)
	print(result)

	return render_template('show_q1.html', output_table=result)

@app.route('/query2')
def query2():
	return render_template('query2.html')

@app.route('/query2a')
def query2a():
	return render_template('query2a.html')

@app.route('/show_q2a', methods=['POST'])
def show_q2a():

	map = request.form['map']
	player_id = request.form['player_id']
	disp_hl = True if 'disp_hl' in request.form.keys() else False
	per_match = True if 'per_match' in request.form.keys() else False

	query1 = '''
	with kill_data2 as (select att_id,SUM(count) as kills from kill_data WHERE att_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' group by att_id),
	assist_data2 as (select att_id,SUM(count) as assists from assist_data WHERE att_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' group by att_id),
	death_data2 as (select vic_id as att_id,SUM(count) as deaths from death_data WHERE vic_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' group by vic_id),
	mvp2 as (select att_id,COUNT(*) as num_mvp from mvp WHERE att_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' group by att_id) 

	select a3.att_id,kills,assists,deaths,ROUND( cast(kills as decimal)/deaths,2) as kd_ratio,coalesce(num_mvp,0) from ((kill_data2 natural join assist_data2) as a2 natural join death_data2) as a3 left outer join mvp2 on a3.att_id = mvp2.att_id
	;

	'''

	# select att_id,kills,assists,deaths,ROUND( cast(kills as decimal)/deaths,2) as kd_ratio,num_mvp from kill_data2 natural join assist_data2 natural join death_data2 left outer join mvp2

	result1 = db_obj.execute_query(query1)

	result2 = []
	

	query3 = '''
	with kill_data2 as (select file,att_team,att_side,att_id, map, SUM(count) as count from kill_data group by file,att_team,att_side,att_id, map)
	select file,att_team,att_side,att_id,count
	from(select  file,att_team,att_side,att_id,map,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_id) as rank
		from kill_data2
		) as a4
	where rank <=1 AND att_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' 
	;
	'''

	result3 = db_obj.execute_query(query3)
	
	query4 = '''
	with kill_data2 as (select file,att_team,att_side,att_id, map, SUM(count) as count from kill_data group by file,att_team,att_side,att_id, map)
	select file,att_team,att_side,att_id,count
	from(select  file,att_team,att_side,att_id,map,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_id) as rank
		from kill_data2
		) as a4
	where rank <=1 AND att_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' 
	;
	'''

	result4 = db_obj.execute_query(query4)

	query5 = '''
	with assist_data2 as (select file,att_team,att_side,att_id, map, SUM(count) as count from assist_data group by file,att_team,att_side,att_id, map)
	select file,att_team,att_side,att_id,count
	from(select  file,att_team,att_side,att_id,map,count,rank() OVER (PARTITION BY file ORDER BY file,count desc,att_id) as rank
		from assist_data2
		) as a4
	where rank <=1 AND att_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' 
	;
	'''

	result5 = db_obj.execute_query(query5)

	query6 = '''
	with assist_data2 as (select file,att_team,att_side,att_id, map, SUM(count) as count from assist_data group by file,att_team,att_side,att_id, map)
	select file,att_team,att_side,att_id,count
	from(select  file,att_team,att_side,att_id,map,count,rank() OVER (PARTITION BY file ORDER BY file,count,att_id) as rank
		from assist_data2
		) as a4
	where rank <=1 AND att_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' 
	;
	'''

	result6 = db_obj.execute_query(query6)

	query7 = '''
	with death_data2 as (select file,vic_team,vic_side,vic_id, map, SUM(count) as count from death_data group by file,vic_team,vic_side,vic_id, map)
	select file, vic_team, vic_side, vic_id,count
	from(select  file,vic_team, vic_side, vic_id, map, count,rank() OVER (PARTITION BY file ORDER BY file,count desc,vic_id) as rank
		from death_data2
		) as a4
	where rank <=1 AND vic_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' 
	;
	'''

	result7 = db_obj.execute_query(query7)


	query8 = '''
	with death_data2 as (select file,vic_team,vic_side,vic_id, map, SUM(count) as count from death_data group by file,vic_team,vic_side,vic_id, map)
	select file, vic_team, vic_side, vic_id,count
	from(select  file,vic_team, vic_side, vic_id, map, count,rank() OVER (PARTITION BY file ORDER BY file,count,vic_id) as rank
		from death_data2
		) as a4
	where rank <=1 AND vic_id=''' +player_id+ ('' if map=='all' else ''' AND map=\'''' + map+'\'') + ''' 
	;
	'''

	result8 = db_obj.execute_query(query8)

	print(result1)
	print(result2)
	print(result3)
	print(result4)
	print(result5)
	print(result6)
	print(result7)
	print(result8)

	return render_template('show_q2a.html', condition=disp_hl, result1=result1, result2=result2, result3=result3, result4=result4, result5=result5, result6=result6, result7=result7, result8=result8)

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

@app.route('/query7')
def query7():
	return render_template('query7.html')

@app.route('/show_q7', methods=['POST'])
def show_q7():
	print([key for key in request.form.keys()])

	map = request.form['map']
	round_type = request.form['round_type']
	ct_alive = request.form['ct_alive']
	t_alive = request.form['t_alive']

	is_bomb_planted = 't' if 'is_bomb_planted' in request.form.keys() else 'f'
	bomb_site = request.form['bomb_site']
	if bomb_site == 'None':
		bomb_site = 'A'

	# query = "drop view budget_data_t; drop view budget_data_ct; drop view weapon_data_t; drop view weapon_data_ct; SELECT * from map_data;"
	# result = db_obj.execute_query(query)
	query = ''
	if is_bomb_planted == 't':
		query = '''
		with filter_hp as /*aayush*/
		(
			select test_dmg.file,test_dmg.round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id 
			from test_dmg,test_rounds 
			where hp_dmg > 0 and test_dmg.file=test_rounds.file and test_dmg.round=test_rounds.round and test_rounds.round_type = \''''+round_type+'''\' and test_rounds.map=\''''+map+'''\'
		)
		,
		valid_rounds as /*aayush*/
		(
			select file,round,winner_side
			from test_rounds where round_type = \''''+round_type+'''\' and map=\''''+map+'''\'
		)
		,
		bombed_rounds as /*aayush*/
		(
			select distinct file,round,bomb_site
			from test_dmg
			where is_bomb_planted = true
		)
		select * from
		(
			with valid_bombed_rounds as /*aayush need to change to valid unbombed for other*/
			(
				select valid_rounds.file,valid_rounds.round,winner_side,bomb_site
				from valid_rounds,bombed_rounds
				where valid_rounds.file = bombed_rounds.file and valid_rounds.round = bombed_rounds.round and bomb_site=\''''+bomb_site+'''\'
			)
			,
			ranked_a_hp as
			(
				select file,round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,
				rank() over
				(
					partition by file,round,vic_id
					order by tick,att_side,vic_side,hp_dmg,is_bomb_planted
				)
				from filter_hp
			)
			select * from
			(
				with ranked_hp as /*aayush*/
				(
					select ranked_a_hp.file,ranked_a_hp.round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,rank
					from ranked_a_hp,valid_bombed_rounds /*aayush change to valid_unbombed*/
					where ranked_a_hp.file = valid_bombed_rounds.file and ranked_a_hp.round = valid_bombed_rounds.round
				)
				select * from
				(
				with recursive summed_hp(file,round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,rank,curr_health_loss) as
				(
					select *,hp_dmg as curr_health_loss
					from ranked_hp
					where rank=1
					union 
					select ranked_hp.file,ranked_hp.round,ranked_hp.tick,ranked_hp.att_side,ranked_hp.vic_side,ranked_hp.hp_dmg,ranked_hp.is_bomb_planted,ranked_hp.vic_id,ranked_hp.rank,(summed_hp.curr_health_loss+ranked_hp.hp_dmg) as curr_health_loss
					from ranked_hp,summed_hp
					where ranked_hp.file = summed_hp.file and ranked_hp.round = summed_hp.round and ranked_hp.vic_id = summed_hp.vic_id and ranked_hp.rank = summed_hp.rank+1 
				)
				select * from
				(
					with death_hp as
					(
						select file,round,tick,vic_side,is_bomb_planted
						from summed_hp where curr_health_loss = 100
					)
					select * from
					(
						with tick_death_ranked_hp as
						(
							select file,round,tick,vic_side,is_bomb_planted,
							rank() over
							(
								partition by file,round
								order by tick,vic_side,is_bomb_planted
							) rank2
							from death_hp
						)
						select * from
						(
							with recursive match_snapshot(file,round,is_bomb_planted,ct_alive,t_alive,rank2) as
							(
								select distinct file,round,false as is_bomb_planted,5 as ct_alive,5 as t_alive,0::bigint as rank2
								from summed_hp

								union

								select match_snapshot.file,match_snapshot.round,tick_death_ranked_hp.is_bomb_planted,
								(
									CASE
									WHEN vic_side = 'CounterTerrorist'
									THEN ct_alive-1
									ELSE ct_alive
									END
								) AS ct_alive,
								(
									CASE
									WHEN vic_side = 'Terrorist'
									THEN t_alive-1
									ELSE t_alive
									END
								) AS t_alive,
								tick_death_ranked_hp.rank2
								from
								match_snapshot,tick_death_ranked_hp
								where match_snapshot.file = tick_death_ranked_hp.file and match_snapshot.round = tick_death_ranked_hp.round and tick_death_ranked_hp.rank2 = match_snapshot.rank2+1                       
							)
							select * from
							(
								with full_match_snapshot as
								(
									select * from match_snapshot 
									union
									select match_snapshot1.file,match_snapshot1.round,true as is_bomb_planted,match_snapshot1.ct_alive,match_snapshot1.t_alive,match_snapshot1.rank2
									from match_snapshot as match_snapshot1,match_snapshot as match_snapshot2
									where match_snapshot1.file = match_snapshot2.file and match_snapshot1.round = match_snapshot2.round and match_snapshot1.is_bomb_planted = false and match_snapshot2.is_bomb_planted = true and match_snapshot2.rank2 = match_snapshot1.rank2+1
								)
								select * from
								(
									/*aayush*/
									with instance_occured as
									(
										select file,round
										from full_match_snapshot
										where ct_alive = '''+ct_alive+''' and t_alive = '''+t_alive+''' and is_bomb_planted = true
									)
									
									select winner_side,count(*)
									from instance_occured,valid_rounds
									where instance_occured.file = valid_rounds.file and instance_occured.round = valid_rounds.round
									group by winner_side
									
								) as foo
							) as foo                    
						) as foo
					) as foo
				) as foo
				) as foo
			) as foo
		) as foo
		;
		'''
	else:
		query = '''
		with filter_hp as /*aayush*/
		(
			select test_dmg.file,test_dmg.round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id 
			from test_dmg,test_rounds 
			where hp_dmg > 0 and test_dmg.file=test_rounds.file and test_dmg.round=test_rounds.round and test_rounds.round_type = \''''+round_type+'''\' and test_rounds.map=\''''+map+'''\'
		)
		,
		valid_rounds as /*aayush*/
		(
			select file,round,winner_side
			from test_rounds where round_type = \''''+round_type+'''\' and map=\''''+map+'''\'
		)
		select * from
		(
			with ranked_a_hp as
			(
				select file,round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,
				rank() over
				(
					partition by file,round,vic_id
					order by tick,att_side,vic_side,hp_dmg,is_bomb_planted
				)
				from filter_hp
			)
			select * from
			(
				with ranked_hp as /*aayush*/
				(
					select ranked_a_hp.file,ranked_a_hp.round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,rank
					from ranked_a_hp,valid_rounds /*aayush change to valid_unbombed*/
					where ranked_a_hp.file = valid_rounds.file and ranked_a_hp.round = valid_rounds.round
				)
				select * from
				(
				with recursive summed_hp(file,round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,rank,curr_health_loss) as
				(
					select *,hp_dmg as curr_health_loss
					from ranked_hp
					where rank=1
					union 
					select ranked_hp.file,ranked_hp.round,ranked_hp.tick,ranked_hp.att_side,ranked_hp.vic_side,ranked_hp.hp_dmg,ranked_hp.is_bomb_planted,ranked_hp.vic_id,ranked_hp.rank,(summed_hp.curr_health_loss+ranked_hp.hp_dmg) as curr_health_loss
					from ranked_hp,summed_hp
					where ranked_hp.file = summed_hp.file and ranked_hp.round = summed_hp.round and ranked_hp.vic_id = summed_hp.vic_id and ranked_hp.rank = summed_hp.rank+1 
				)
				select * from
				(
					with death_hp as
					(
						select file,round,tick,vic_side,is_bomb_planted
						from summed_hp where curr_health_loss = 100
					)
					select * from
					(
						with tick_death_ranked_hp as
						(
							select file,round,tick,vic_side,is_bomb_planted,
							rank() over
							(
								partition by file,round
								order by tick,vic_side,is_bomb_planted
							) rank2
							from death_hp
						)
						select * from
						(
							with recursive match_snapshot(file,round,is_bomb_planted,ct_alive,t_alive,rank2) as
							(
								select distinct file,round,false as is_bomb_planted,5 as ct_alive,5 as t_alive,0::bigint as rank2
								from summed_hp

								union

								select match_snapshot.file,match_snapshot.round,tick_death_ranked_hp.is_bomb_planted,
								(
									CASE
									WHEN vic_side = 'CounterTerrorist'
									THEN ct_alive-1
									ELSE ct_alive
									END
								) AS ct_alive,
								(
									CASE
									WHEN vic_side = 'Terrorist'
									THEN t_alive-1
									ELSE t_alive
									END
								) AS t_alive,
								tick_death_ranked_hp.rank2
								from
								match_snapshot,tick_death_ranked_hp
								where match_snapshot.file = tick_death_ranked_hp.file and match_snapshot.round = tick_death_ranked_hp.round and tick_death_ranked_hp.rank2 = match_snapshot.rank2+1                       
							)
							select * from
							(
								with full_match_snapshot as
								(
									select * from match_snapshot 
									union
									select match_snapshot1.file,match_snapshot1.round,true as is_bomb_planted,match_snapshot1.ct_alive,match_snapshot1.t_alive,match_snapshot1.rank2
									from match_snapshot as match_snapshot1,match_snapshot as match_snapshot2
									where match_snapshot1.file = match_snapshot2.file and match_snapshot1.round = match_snapshot2.round and match_snapshot1.is_bomb_planted = false and match_snapshot2.is_bomb_planted = true and match_snapshot2.rank2 = match_snapshot1.rank2+1
								)
								select * from
								(
									/*aayush*/
									with instance_occured as
									(
										select file,round
										from full_match_snapshot
										where ct_alive = '''+ct_alive+''' and t_alive = '''+t_alive+''' and is_bomb_planted = false
									)
									
									select winner_side,count(*)
									from instance_occured,valid_rounds
									where instance_occured.file = valid_rounds.file and instance_occured.round = valid_rounds.round
									group by winner_side
									
								) as foo
							) as foo                    
						) as foo
					) as foo
				) as foo
				) as foo
			) as foo
		) as foo
		;
		'''

	print(query)
	result = db_obj.execute_query(query)

	if len(result)==0:
		result = [('CounterTerrorist', 0), ('Terrorist', 0)]
	elif len(result)==1:
		if result[0][0]=='CounterTerrorist':
			result.append(('Terrorist', 0))
		else:
			result1 = result[0]
			result = [('CounterTerrorist', 0)]
			result.append(result1)

	print(result)
	# print("query done!!")

	return render_template('show_q7.html', output_table=result)

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

@app.route('/query10')
def query10():
	return render_template('query10.html')

@app.route('/show_q10', methods=['POST'])
def show_q10():

	print([key for key in request.form.keys()])

	match = request.form['match']
	round = request.form['round']

	query = '''
	with filter_hp as
	(
	select file,round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id from test_dmg where hp_dmg > 0 AND file=\''''+match+'''\' and round='''+round+'''
	)
	select * from
	(
		with ranked_hp as
		(
			select file,round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,
			rank() over
			(
				partition by file,round,vic_id
				order by tick,att_side,vic_side,hp_dmg,is_bomb_planted
			)
			from filter_hp
		)
		select * from
		(
			with recursive summed_hp(file,round,tick,att_side,vic_side,hp_dmg,is_bomb_planted,vic_id,rank,curr_health_loss) as
			(
				select *,hp_dmg as curr_health_loss
				from ranked_hp
				where rank=1
				union 
				select ranked_hp.file,ranked_hp.round,ranked_hp.tick,ranked_hp.att_side,ranked_hp.vic_side,ranked_hp.hp_dmg,ranked_hp.is_bomb_planted,ranked_hp.vic_id,ranked_hp.rank,(summed_hp.curr_health_loss+ranked_hp.hp_dmg) as curr_health_loss
				from ranked_hp,summed_hp
				where ranked_hp.file = summed_hp.file and ranked_hp.round = summed_hp.round and ranked_hp.vic_id = summed_hp.vic_id and ranked_hp.rank = summed_hp.rank+1 
			)
			select * from
			(
				with death_hp as
				(
					select file,round,tick,vic_side,is_bomb_planted
					from summed_hp where curr_health_loss = 100
				)
				select * from
				(
					with tick_death_ranked_hp as
					(
						select file,round,tick,vic_side,is_bomb_planted,
						rank() over
						(
							partition by file,round
							order by tick,vic_side,is_bomb_planted
						) rank2
						from death_hp
					)
					select * from
					(
						with recursive match_snapshot(file,round,is_bomb_planted,ct_alive,t_alive,rank2) as
						(
							select distinct file,round,false as is_bomb_planted,5 as ct_alive,5 as t_alive,0::bigint as rank2
							from summed_hp

							union

							select match_snapshot.file,match_snapshot.round,tick_death_ranked_hp.is_bomb_planted,
							(
								CASE
								WHEN vic_side = 'CounterTerrorist'
								THEN ct_alive-1
								ELSE ct_alive
								END
							) AS ct_alive,
							(
								CASE
								WHEN vic_side = 'Terrorist'
								THEN t_alive-1
								ELSE t_alive
								END
							) AS t_alive,
							tick_death_ranked_hp.rank2
							from
							match_snapshot,tick_death_ranked_hp
							where match_snapshot.file = tick_death_ranked_hp.file and match_snapshot.round = tick_death_ranked_hp.round and tick_death_ranked_hp.rank2 = match_snapshot.rank2+1                       
						)
						select * from
						(
							with full_match_snapshot as
							(
								select * from match_snapshot 
								union
								select match_snapshot1.file,match_snapshot1.round,true as is_bomb_planted,match_snapshot1.ct_alive,match_snapshot1.t_alive,match_snapshot1.rank2
								from match_snapshot as match_snapshot1,match_snapshot as match_snapshot2
								where match_snapshot1.file = match_snapshot2.file and match_snapshot1.round = match_snapshot2.round and match_snapshot1.is_bomb_planted = false and match_snapshot2.is_bomb_planted = true and match_snapshot2.rank2 = match_snapshot1.rank2+1
							)
							select * from full_match_snapshot
							
							order by rank2,is_bomb_planted
						) as foo                    
					) as foo
				) as foo
			) as foo
		) as foo
	) as foo
	;
	'''

	print(query)
	result = db_obj.execute_query(query)
	print(result)

	result1 = []
	restult2 = []
	ind = len(result)
	for i, row in enumerate(result):
		if row[2] == True:
			ind = i
			break
	
	print(f'i: {i}')
	result1 = result[:ind]
	result2 = result[ind+1:]
	print(f'Result1: {result1}')
	print(f'Result2: {result2}')

	condition = False
	bomb_site = 'None'
	if ind < len(result):
		condition = True
		query3 = '''
		select distinct bomb_site
		from test_dmg
		where file=\''''+match+'''\' and round='''+round+''' and is_bomb_planted = true
		'''
		result3 = db_obj.execute_query(query3)
		bomb_site = result3[0][0]

	# print("query done!!")
	query4 = '''
	select winner_side
	from test_rounds
	where file=\''''+match+'''\' and round='''+round+''';
	'''
	result4 = db_obj.execute_query(query4)
	round_winner = result4[0][0]

	return render_template('show_q10.html', output_table1=result1, output_table2=result2, condition=condition, bomb_site=bomb_site, round_winner=round_winner)

if __name__ == '__main__':
	app.run(host="localhost", port=5026, debug=True)