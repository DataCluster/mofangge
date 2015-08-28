#__author__=DGideas

def fetch(website,outfile):
	import subprocess;
	subprocess.check_output('wget --output-document='+str(outfile)+' -q "'+str(website)+'"',shell=True);
	return;

def fetchA(website,outfile,user,password,useragent="Links (2.8; Linux 2.6.32-504.30.3.el6.x86_64 x86_64; GNU C 4.4.7; text)"):
	import subprocess;
	subprocess.check_output('wget --user='+str(user)+' --password='+str(password)+' --user-agent="'+str(useragent)+'" --output-document='+str(outfile)+' -q "'+str(website)+'"',shell=True);
	return;
	
def fetchU(website,outfile,useragent="Links (2.8; Linux 2.6.32-504.30.3.el6.x86_64 x86_64; GNU C 4.4.7; text)"):
	import subprocess;
	subprocess.check_output('wget --user-agent="'+str(useragent)+'" --output-document='+str(outfile)+' -q "'+str(website)+'"',shell=True);
	return;
	
def fetchAU(website,outfile,user,password,useragent="Links (2.8; Linux 2.6.32-504.30.3.el6.x86_64 x86_64; GNU C 4.4.7; text)"):
	import subprocess;
	subprocess.check_output('wget --user='+str(user)+' --password='+str(password)+' --user-agent="'+str(useragent)+'" --output-document='+str(outfile)+' -q "'+str(website)+'"',shell=True);
	return;
