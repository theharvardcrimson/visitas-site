#!/Users/sfishman/.venvs/general/bin/python
from jinja2 import FileSystemLoader, Template
from jinja2.environment import Environment
import re
import subprocess
import os

env = Environment()
env.loader = FileSystemLoader('.')
cwd = os.getcwd()

if not os.path.exists('rendered/'):
	os.mkdir('rendered/')

for root, dirs, files in os.walk(cwd):
	if 'rendered' in dirs:
		dirs.remove('rendered')
	if '.git' in dirs:
		dirs.remove('.git')

	for f in files:
		if root.replace(cwd, '') != '':
			fname = root.replace(cwd, '')[1:] + '/' + f
		else:
			fname = f

		if not (f == "base.html.tmp" or f == __file__[2:]):
			if fname.find('.html.tmp') != -1:
				if fname != "index.html.tmp":
					path_start = 'rendered/' + fname[:-9]
					out_name = path_start + '/index.html'
					if not os.path.exists(path_start):
						os.makedirs(path_start)
				else:
					out_name = 'rendered/' + fname[:-4]
				url_path = out_name[out_name.find('/'):out_name.rfind('/') + 1]
				contents = env.get_template('/' + fname).render(__path__=url_path)
			else:
				out_name = 'rendered/' + fname
				with open(fname) as orig:
					contents = orig.read()
				if not os.path.exists(out_name[:out_name.rfind('/')]):
					os.makedirs(out_name[:out_name.rfind('/')])
			with open(out_name, 'w+') as out_file:
				out_file.write(contents)
