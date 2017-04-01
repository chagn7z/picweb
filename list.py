# -*- conding:utf-8 -*-


import os
from flask import Flask
from flask import render_template, url_for

# tools function
def conv_path(path, code):
	sd = code.split('/')
	sd.remove('')
	dest_path = ''
	for i,c in enumerate(sd):
		cur_list = get_dir(path+dest_path)
		if len(cur_list) > int(c):
			dest_path = dest_path + '/' + cur_list[int(c)]
		else:
			break;
	return dest_path

def get_dir(path):
	print path
	dir_list = []
	if os.path.isdir(path):
		cur_list = os.listdir(path)
		for i,name in enumerate(cur_list):
			if os.path.isdir(path+'/'+name):
				dir_list.append(name)
	return dir_list

def gen_dir_list(code):
	dir_root = '/home/cc/downloads'
	real_path = conv_path(dir_root, code)
	dir_list = get_dir(dir_root+real_path)
	re_data = {'real_path':real_path,
				'code_path':code,
				'dir_list':dir_list}
	return re_data

# flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/list')
def list_page():
	return render_template('list.html')

@app.route('/temp')
def temp_page():
	navigation = [{"href":'www.bing.com', "caption":'Bing'},]
	list_data = gen_dir_list('/0')
	print list_data
	return render_template('temp.html', list_data=list_data, navigation=navigation)
	# return url_for('static', filename='temp.html')

if __name__ == '__main__':
	app.debug = True
	app.run()

