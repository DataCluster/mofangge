import DGStorage as DGS
a=DGS.DGStorage();
a.select('knowledgebase');
ok=False;
i=0
while ok==False:
	res=a.fetch(20,(i-1)*20);
	i+=1;
	if len(res)==0:
		ok=True;
	for item in res:
		#a.setprop(item["uid"],"note","");
		a.setprop(item["uid"],"ex","");
		print('set '+item["uid"]);
