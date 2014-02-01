#!/Users/botros/.virtualenvs/templating/bin/python
from jinja2 import FileSystemLoader, Template
from jinja2.environment import Environment
import re
import subprocess

env = Environment()
env.loader = FileSystemLoader('.')

files = subprocess.Popen('ls', stdout=subprocess.PIPE).stdout.read().split("\n")[0:-1]
for fname in files:
	if not fname == "base.html.tmp":
		print fname
		if re.match(r'^.+\.tmp$', fname) is not None:
			open(fname[0:-4], 'w+').write(env.get_template(fname).render())