l1 = [{"name" : ["ram","ari","karan"]},{"sub" : ["Tamil","Eng","comp"]},{}]


name = l1[0]["name"]

sub = l1[1]["sub"]
l2 = l1[2]

l2 = l2.fromkeys(name,sub)

print(list(l2))








