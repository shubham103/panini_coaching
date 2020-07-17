import flask
import json
import mariadb
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# configuration used to connect to MariaDB
config = {
            'host': 'root_db_1',
            'port': 3306,
            'user': 'root',
            'password': 'example',
            'database': 'demo'
        }
# route to return all people

@app.route('/', methods=['GET'])
def hello():
   return "hello shubahm search /api/people for names from database"

@app.route('/api/people', methods=['GET'])
def index():
   # connection for MariaDB
   conn = mariadb.connect(**config)
   # create a connection cursor
   cur = conn.cursor()
   # execute a SQL statement
   cur.execute("select * from people")

   # serialize results into JSON
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
      json_data.append(dict(zip(row_headers,result)))
   # return the results!
   return json.dumps(json_data)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
