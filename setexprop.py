import DGStorage as DGS
a=DGS.DGStorage()
a.select('knowledgebase');
ok=False;
i=0
total=0
avalible=0;
while ok==False:
	res=a.fetch(20,(i-1)*20);
	i+=1;
	if len(res)==0:
		ok=True;
	for item in res:
		total+=1;
		item["content"]=item["content"].split('\n');
		for row in item["content"]:
			if row.find('<span>题型')!=-1:
				avalible+=1;
				#print(row[row.find('难度'):row.find('</span><span>来源：')][3:]);
				#print(row[row.find('题型'):row.find('</span>')][3:]);
				print(row[row.find('来源'):row.find('</span></div>')][3:]);
				#a.setprop(item["uid"],"题型",row[row.find('题型'):row.find('</span>')][3:]);
				#a.setprop(item["uid"],"diff",row[row.find('难度'):row.find('</span><span>来源：')][3:]);
				a.setprop(item["uid"],"origin",row[row.find('来源'):row.find('</span></div>')][3:]);
				#print(item["prop"]);
			#else:
				#print(item["prop"]["type"]);
				#break;
print(avalible);
print(total);
