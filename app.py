from flask import Flask, redirect, url_for, request, render_template
from db import Database
import config
import os

from coordi_conversion import draw_figure, draw_points

app = Flask(__name__)

app.config['DEBUG'] = True

db_obj = Database()
db_obj.connect()

@app.route('/')
def index():
	#return '''<html><body><h1>HEllllo eaarth</h1></body></html>'''
	return '''
	<html>
	<body>
	<a href="http://localhost:5000/display">Show Image!</a>
	<form action="http://localhost:5000/login" method="post">
		<p>Enter count number:</p>
		<p><input type = "text" name="nm"/></p>
		<p><input type="submit" value="submit"/></p>
	</form>
	</body>
	</html>
	'''


@app.route('/login',methods=['POST'])
def login():
	name = request.form['nm']
	result = db_obj.execute_query('SELECT * FROM team LIMIT '+name+';')
	output = 'Hello World!<br><br>'+name

	for row in result:
		output = output + '|' + str(row[0]) + '\t|\t' + str(row[1]) + '<br>'

	return output


@app.route('/display')
def display():
	delta = 8
	result = db_obj.execute_query(f'select {delta}*x as x, {delta}*y as y, count from (select x, y, count, rank() over(order by count desc) from (select att_pos_x / {delta} as x, att_pos_y / {delta} as y, count(*) from test_dmg group by x, y) as tmp) as tmp2 where rank <= 20;')

	draw_figure([row[0] for row in result], [row[1] for row in result], delta)

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


if __name__ == '__main__':
	app.run()