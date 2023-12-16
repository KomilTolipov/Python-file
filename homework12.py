#-----------------------

# a=25
# b=12
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# a=20
# b=30
# c=30
# d=50
 
# d=c
# b=d
# a=c
# c=a
# d=a
# print(a,b,c,d)

#--------------------------

# s=a*b
# s1=type(c)
# print(s1)

# f=a/b
# f1=type(f)
# print(f1)

#---------------------------

import random

# a=(2,3,4,5,6)
# natija=random.choice(a)
# print(natija)

# a=(102,22,343,4,5,6)
# natija=random.choice(a)
# print(natija)

#----------------------------

# a=random.uniform(0,10)
# print(a)

# a=random.uniform(0,5)
# print(a)

#---------------------------

# a=random.randrange['komil','oybek','habiulloh']
# print(a)

# a=random.randrange[-1,10,3]
# print(a)

#---------------------------

# ism='Komil'
# d=len(ism)
# print(d)

# ism='   1223'
# d=len(ism)
# print(d)

#----------------------------

# i='home    less'
# a=i.find(' ')
# print(a)

# f='python'
# a=f.find('h')
# print(a)

#----------------------------

# ism='komil'
# a=ism.index('i',3,5)
# print(a)

# w='telefon22  '
# a=w.index(" ",5,10)
# print(a)

#-----------------------------

# a='100000'
# d=a.isdigit()
# print(d)

# a='2222'
# d=a.isdigit()
# print(d)

#------------------------------
# ism='Komil'
# d=ism.isalpha()
# print(d)

# ism='2333'
# d=ism.isalpha()
# print(d)

# ism='Komil  '
# d=ism.isalpha()
# print(d)

#----------------------------

# ism='teacher'
# d=ism.isalnum()
# print(d)

# ism='Saallodjs2'
# d=ism.isalnum()
# print(d)

# ism='1223'
# d=ism.isalnum()
# print(d)

#-----------------------------

# ism='hbbbbblkjn'
# d=ism.islower()
# print(d)

# ism='Vali'
# d=ism.islower()
# print(d)

# ism='kOmil'
# d=ism.islower()
# print(d)

#------------------------------

# ism='    '
# d=ism.isspace()
# print(d)

# ism=' m  '
# d=ism.isspace()
# print(d)

# ism='                               '
# d=ism.isspace()
# print(d) 

#-------------------------------

# ism='Tolipov Komil'
# d=ism.istitle()
# print(d)

# ism='dilmurod'
# d=ism.istitle()
# print(d)


#----------------------------

# ism='komil tolipov'
# d=ism.title()
# print(d)
 
# ism='ajajhsa  ahjsja a hasjahd'
# a=ism.title()
# print(a) 


#-----------------------------

# ism='komil tolipov'
# d=ism.capitalize()
# print(d)

# ism='q22222aawwqad'
# d=ism.capitalize()
# print(d)

# ism='abdullayev fayzulloh'
# a=ism.capitalize()
# print(a)


#list
#-------------------------

# a=ism[1:3:2]
# print(a)

# ism=['komil','abdurahim','habibulloh','oybek']
# d=ism[1:2:2]
# print(d)

# sonlar=[1,6,86,3,1,4,35,2]
# a=sonlar[1:9:2]
# print(a)

#--------------------------

# ism=['komil','oybek','habibulloh','azizbek','abdurahim']
# ism.append('abdurahmon')
# print(ism)

# ism=[1,2,3,4,5,5,7]
# ism.append(6)
# print(ism)

# ism=[23,57,67,77]
# ism.append(47)
# print(ism)

#--------------------------



# ism=['sasj','sas','gfh','asda']
# ism1=['sjsij','hhf','fhf']
# ism1.extend(ism)
# print(ism1)

# sonlar=[1,2,3,4,4,5,5,6,]
# sonlar1=[-1,-2,-3]
# sonlar1.extend(sonlar)
# print(sonlar1)

#-------------------------------

# sonlar=[1,2,3,4,4,5,5,6,]
# sonlar.insert(3,'200')
# print(sonlar)

# ism=['komil','habibulloh','oybek']
# ism.insert(2,'azizbek')
# print(ism)


#---------------------------------

# a=[1,2,3,4,4,5,5,6,]
# a.remove(5)
# print(a)

# ism=['komil','habibulloh','fayzulloh','oybek','abdurahmon']
# ism.remove('abdurahmon')
# print(ism) 

#---------------------------------

# ism="Traktor"
# a=ism.isalpha()
# print(a)

# b="hhhhhh"
# a=b.isalpha()
# print(a)

#------------------------------

# son='2009.5'
# d=son.isdigit()
# print(d)

# son='20'
# d=son.isdigit()
# print(d)


#------------------------------

# ism='   komil    '
# print(ism)
# d=ism.strip()
# print(d)

# ism='       '
# print(ism)
# d=ism.strip()
# print(d)


#------------------------

# ism='    f   '
# print(ism)
# d=ism.rstrip()
# print(d)

# ism='komil   '
# print(ism)
# d=ism.rstrip()
# print(d)

#-------------------------

# ism='   oybek   '
# print(ism)
# d=ism.lstrip()
# print(d)

# ism='   2323232   '
# print(ism)
# d=ism.lstrip()
# print(d)



#------------------------

# ism='komil'
# a=ism.upper()
# print(a)

# ism='oybek'
# a=ism.upper()
# print(a)

#-------------------------

# ism='oybek komil'
# d=ism.replace('oybek','habibulloh')
# print(d)

# ism='ali habibulloh  oybek'
# d=ism.replace('Ali','Madina')
# print(d)

#--------------------------

# e='komil@Tolipov'
# d=e.split('@')
# username=d[0]
# print(username)
# print(d)

# a='komil.tolipov'
# d=a.split('.')
# username=d[0]
# print(username)
# print(d)

#---------------------------

# X=list(range(1,15,2))
# print(X)

# a=list(range(1,1000001,2))
# print(a)

#---------------------------

# a=int(input("a="))
# b=int(input("b="))
# S=a*b
# print(S)

# a=int(input('a='))
# b=int(input('b='))
# l=(a+b)/2
# print(l)

#----------------------------

# a=tuple(range(10,101,2))
# print(a[2:10:2])

# a=tuple(range(9,1000,3))
# print(a[2:10:2])

#----------------------------

# a=tuple(range(10,100,2))
# b=list(a)
# b.append(1000)
# a=tuple(b)
# print(a)

# a=tuple(range(10,1000,10))
# b=list(a)
# b.insert(2,3000)
# a=tuple(b)
# print(a)

#-----------------------------

# a=(1,2,3,4,5,6,7,8,9)
# b=a.count(9)
# print(b)

# a=(1,1,1,2,3,4,5,6,7,8)
# b=a.count(1)
# print(b)

#----------------------------=

# sonlar=[200,100,10,['a','b','d','e',['komil','oybek'],-1],-1,-10]
# a=sonlar[3][4][0][4]
# print(a)

# sonlar=[1,100,['komil','d','e',-1],-1,-10]
# b=sonlar[2][0]
# print(b)

#-----------------------------


# a={1,2,3,4,5,6,7,8,9,10}
# a.add(10)
# print(a)


# a={1,2,3,4,5,}
# a.add(6)
# print(a)

#------------------------------

# a={1,2,3,4,5,6,7,8,9}
# b={10,11,12,13,14,15}
# b.update(a)
# print(b)

# a={1,2,3,4,5,6}
# b={7,8,9,10,11}
# b.update(a)
# print(b)

#------------------------------

# a={1,2,3,2,3,2,32,423,4,23,4}
# b=len(a)
# print(b)

# a={2342,423,4,23423,423}
# b=len(a)
# print(b)

#-------------------------------

# a={'oybek','komil','fayzulloh','habibulloh'}
# a.remove(1)
# print(a)


# a={'oybek','habibulloh','azizbek','komil'}
# a.remove(2)
# print(a)

#-------------------------------

# a={12,3,213,213,12,3}
# a.discard(2)
# print(a)

# s={'ajsdajs','duhsahduahdh','saduhdahduahd'}
# s.discard(-1)
# print(s)

#-------------------------------

# a={'komil','oybek','habibulloh'}
# a.pop()
# print(a)

# a={23,2,3,23,2,321,321,3,4}
# a.pop()
# print(a)


# union

# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5}
# d=a.union(b)
# print(d)


# a={'a','b','komil'}
# b={'habibulloh'}
# d=a.union(b)
# print(d)