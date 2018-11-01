#列表list和元组tuple类似于数组
#列表里面的数据可以重新赋值
abc=["My","You"]
print(abc)
print(abc[0])
print(abc[1])
abc[1]="He"
print(abc[1])

#元组里面的元素不可以修改
cde=("one","two")
print(cde[1])

#集合
a="fajwfjgfajukfb"
b="vasjuafuksyfiaklqw"
sa=set(a)
sb=set(b)
print(sa)
print(sb)
print(sa&sb)
print(sa|sb)

#字典 键找值
#{k1:v1,k2:v2}
dic1={"name":"yduan","gender":"male"}
print(dic1["gender"])




