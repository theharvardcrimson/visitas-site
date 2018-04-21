#!/usr/bin/env python
from jinja2 import FileSystemLoader, Template
from jinja2.environment import Environment
from datetime import date
import re
import subprocess
import os
import comp_info

env = Environment()
env.loader = FileSystemLoader('.')
cwd = os.getcwd()

def comp_director(director):
	return '{name} (<a href="mailto:{email}">{email}</a>)'.format(**director)

env.filters['comp_director'] = comp_director

if not os.path.exists('rendered/'):
	os.mkdir('rendered/')

cur_year = date.today().year
cur_month = date.today().month
if cur_month <= 6:
    cur_season = "Spring"
else:
    cur_season = "Fall"
subtitle = "Fall Comp %d" % (cur_year)





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
				template = env.get_template('/' + fname)
				contents = template.render(
					__path__=url_path,
					subtitle=subtitle,
					comp=comp_info,
					comp_director=comp_director
				).encode()
			else:
				out_name = 'rendered/' + fname
				with open(fname, 'rb') as orig:
					contents = orig.read()
				if not os.path.exists(out_name[:out_name.rfind('/')]):
					os.makedirs(out_name[:out_name.rfind('/')])
			with open(out_name, 'wb+') as out_file:
				out_file.write(contents)
