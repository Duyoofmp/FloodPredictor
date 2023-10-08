from flask import Flask
import joblib, os, sklearn

app = Flask(__name__)

#  River_Basin, Station_Name, rainfall, Level, rainfall before 1 days, rainfall before 2, days river gauge 1 days

# river basin {'Chaliyar': 0, 'Korapuzha': 1, 'Kuttyadi': 2, 'Mahe': 3}
# station name {'F.C.S. Perambra': 0, 'Koodathai': 1, 'Kunnamangalam': 2, 'Thamarassery': 3, 'Vanimel': 4}



@app.route('/model')
def hello_world(rb=2,sn=0,rf=3.8,l=3.69,rf1=1.4,rf2=1.0,rg1=17.29):

	model = joblib.load(os.getcwd()+'/'+'waterlevel.pkl')
	level = model.predict([[rb,sn,rf,l,rf1,rf2,rg1]])
	# returns water level
	print(level[0])
	return str(level[0])

# main driver function
if __name__ == '__main__':

	app.run()
 
# api = http://127.0.0.1:5000/model?rb=2&sn=0&rf=3.8&l=3.69&rf1=1.4&rf2=1.0&rg1=17.29 
