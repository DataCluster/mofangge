import DGStorage as DGS
a=DGS.DGStorage()
a.select('knowledgebase');
ok=False;
i=0;
while ok==False:
	res=a.fetch(20,(i-1)*20);
	i+=1;
	if len(res)==0:
		ok=True;
	for item in res:
		item["content"]=item["content"].split('\n');
		exbody='';
		initstatus=False;
		for row in item["content"]:
			if row.find('题文</div>')!=-1:
				initstatus=True;
			if row.find('<span>题型：')!=-1:
				initstatus=False;
			if initstatus==True:
				exbody=exbody+'\n'+row;
		a.setprop(item["uid"],'body',exbody);
		print('get '+item["uid"]);
