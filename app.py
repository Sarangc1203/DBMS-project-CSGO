from flask import Flask
from db import Database
import config

app = Flask(__name__)

app.config['DEBUG'] = True

db_obj = Database()
db_obj.connect()

@app.route('/')
def main():
	result = db_obj.execute_query('SELECT * FROM team;')
	output = 'Hello World!<br><br>'

	for row in result:
		output = output + '|' + str(row[0]) + '\t|\t' + str(row[1]) + '<br>'

	return output

if __name__ == '__main__':

	app.run()