# a=(1979,1982,2005,2009,2010)
# print(a[3])


# son=[1,2,323,13,5,3,6,('a','b','c',[2000,2001]),9,453]
# a=(son[7][3][1])
# print(a)

# son=[1,2,323,13,5,3,6,('a','b','c',[2000,2001,(200,3000,3,'ozoda')]),9,453]
# ismlar=('guli','ali','vali',son,'ishmat')
# a=(ismlar[3][9])
# b=(ismlar[3][7][3][2][0])
# print(a+b)



son=[1,2,323,13,5,3,6,('a','b','c',[2000,2001,(200,3000,3,'ozoda')]),9,453]
ismlar=('guli','ali','vali',son,'ishmat')
a=ismlar[4]
b=ismlar[3][7][3][2][1]
n=str(b)
print(a+n)
