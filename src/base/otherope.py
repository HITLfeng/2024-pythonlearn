lst1 = ["何炅", "杜海涛","周渝民"]
lst2 = lst1.copy()
lst1.append("李嘉诚")
print(lst1)
print(lst2)
print(id(lst1), id(lst2))



lst1 = ["何炅", "杜海涛","周渝民", ["麻花藤", "马芸", "周笔畅"]]
lst2 = lst1.copy()
lst1[3].append("无敌是多磨寂寞")
print(lst1)
print(lst2)
print(id(lst1[3]), id(lst2[3]))



