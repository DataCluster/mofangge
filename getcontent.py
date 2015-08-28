from pyfetch import *
import DGStorage as DG
import time
import urllib.parse
import os
a=DG.DGStorage()
a.select('knowledgebase');
ok=False;
i=0;
while ok==False:
	res=a.fetch(20,(i-1)*20);
	i+=1;
	if len(res)==0:
		ok=True;
	for item in res:
		fetch(urllib.parse.unquote_plus(item["key"]),'tmp')
		with open('tmp') as cont:
			a.put(item["uid"],cont.read());
		os.remove('tmp');
		print('put cont '+item["uid"]);
		time.sleep(3);
