import DGStorage as DGS
a=DGS.DGStorage()
a.select('english');
ok=False;
i=0;
while ok==False:
	res=a.fetch(20,(i-1)*20);
	if len(res)==0:
		ok=True;
	i+=1;
	for item in res:
		if item["prop"]["level"].find('高中')==-1:
			a.remove(item["uid"]);
			print('drop '+item["uid"]);
