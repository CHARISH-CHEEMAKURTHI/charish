phone_no={"ram":1234,"shyam":5678,"mohan":9012}
phone_no1=dict([("ram",1234),("shyam",5678),("mohan",9012)])
print(phone_no)
print(phone_no1)
phone_no1["ram"]=789456
print(phone_no1)
phone_no["ram"]={"ram_home":201975 ,"ram_work":357890}
print(phone_no)
phone_no["shyam"]={623578,487,243856}
print(phone_no)
phone_no["ghef"]={2934}
print(phone_no)
del phone_no["ghef"]
print(phone_no)
phone_no.pop("shyam")
print(phone_no)
print(phone_no.values())


