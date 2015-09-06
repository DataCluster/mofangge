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
			if row.find('答案</div>')!=-1:
				initstatus=True;
			if row.find('马上分享给同学</span>')!=-1:
				initstatus=False;
			if initstatus==True:
				exbody=exbody+'\n'+row;
		exbody=exbody.split('\n');
		if len(exbody)==6:
			exbody=exbody[4];
		else:
			exbody=exbody[4:-1];
		#print(exbody);
		a.setprop(item["uid"],'answer',exbody);
		print('set '+item["uid"]);
