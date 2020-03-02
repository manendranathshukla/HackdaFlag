from flask import * #Flask ,render_template ,request,Response,send_file,redirect,url_for

import sqlite3
import datetime
app=Flask(__name__)



with sqlite3.connect("SubmissionData.db") as db:
        cursor=db.cursor()
#cursor.execute("delete from mydata1;")) 
cursor.execute('''create table if not exists Data(Time datetime,vtu varchar not null,flag1 varchar,flag2 varchar, flag3 varchar,flag4 varchar,flag5 varchar);''')


@app.route('/',methods=['POST','GET'])
def site():
	error = None
    	if request.method == 'POST':
        	if request.form['uname'] != 'hacktheflag' or request.form['psw'] != 'veltechhackers':
            		error = 'Invalid Username/Password.'
        	else:
            		return redirect(url_for('UmYpy5zaeo36dBl0MmBZAUJSZ9sPm4Ef2yVzTEoKjuE1'))
    	return render_template('site.html', error=error)




@app.route('/UmYpy5zaeo36dBl0MmBZAUJSZ9sPm4Ef2yVzTEoKjuE1')
def UmYpy5zaeo36dBl0MmBZAUJSZ9sPm4Ef2yVzTEoKjuE1():
	return render_template("UmYpy5zaeo36dBl0MmBZAUJSZ9sPm4Ef2yVzTEoKjuE1.html")


@app.route('/KFrGjs0B4SVlCQDauutLpLT13IxlnmKOABozTdLE0s2')
def KFrGjs0B4SVlCQDauutLpLT13IxlnmKOABozTdLE0s2():
	return render_template("KFrGjs0B4SVlCQDauutLpLT13IxlnmKOABozTdLE0s2.html")

@app.route('/site2',methods=['GET','POST'])
def site2():
	error = None
    	if request.method == 'POST':
        	if request.form['uname'] != 'admin' or request.form['psw'] != 'tantraz2020':
            		error = 'Invalid Username/Password.'
        	else:
            		return redirect(url_for('KFrGjs0B4SVlCQDauutLpLT13IxlnmKOABozTdLE0s2'))
    	return render_template('site2.html', error=error)


@app.route('/site3',methods=['GET','POST'])
def site3():
	 
	#cookies={'login':'false'}
	#requests.post("site3.html",cookies=cookies)
	#Response.set_cookie("login","false")
	
	r=request.cookies.get('login')
	if request.method == 'POST' and r=="true":
		#request.cookies.set("Login=false")
		return render_template('YtVkwxElXsbqM4WrARDLrXI0lolZGDWOTszIoBEb44.html')
	resp = make_response(render_template('site3.html'))  
        resp.set_cookie('login',"false") 
        return resp#render_template('site3.html')


@app.route('/YtVkwxElXsbqM4WrARDLrXI0lolZGDWOTszIoBEb44')
def YtVkwxElXsbqM4WrARDLrXI0lolZGDWOTszIoBEb44():
	return render_template("YtVkwxElXsbqM4WrARDLrXI0lolZGDWOTszIoBEb44.html")



@app.route('/site4',methods=['GET','POST'])
def site4():
        return render_template('site4.html')


@app.route('/site5',methods=['GET','POST'])
def site5():		
        return render_template('site5.html')


@app.route('/download_image',methods=['GET','POST'])
def download_image():
	
	if request.method == 'POST':
		return send_file('static/Flag5.jpg',
                     mimetype='image/png',
                     attachment_filename='Flag5.jpg',
                     as_attachment=True)
		
        return render_template('site5.html')




@app.route('/download_audio',methods=['GET','POST'])
def download_audio():
	
	if request.method == 'POST':
		return send_file('static/Flag_4.mp3',
                     mimetype='audio/mp3',
                     attachment_filename='Flag_4.mp3',
                     as_attachment=True)
		
        return render_template('site4.html')








@app.route('/submission',methods=['GET','POST'])
def submission():
	with sqlite3.connect("SubmissionData.db") as db:
        	con=db.cursor()
	if request.method=="POST":
		time=datetime.datetime.now()
		vt=request.form['vtu']
		f1=request.form['f1']
		f2=request.form['f2']
		f3=request.form['f3']
		f4=request.form['f4']
		f5=request.form['f5']

		
	
		con.execute("insert into Data (Time,Vtu,Flag1,Flag2,Flag3,Flag4,Flag5) values (?,?,?,?,?,?,?)",(time,vt,f1,f2,f3,f4,f5))
    		db.commit()
		con.execute("SELECT * FROM submissionData ;")
		mydata=con.fetchall()
		print(mydata)
	
	
		
	return render_template('submission.html')





if __name__=="__main__":
	app.run(debug=True)
