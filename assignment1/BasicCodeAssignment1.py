Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> enrollment=[34,23,56,13]
>>> major=['kinese','compsci','business','chem']
>>> import numpy as ny
>>> en=ny.array(enrollment)
>>> ma=ny.array(major)
>>> ny.append(en,67)
array([34, 23, 56, 13, 67])
>>> ny.append(ma,'bio')
array(['kinese', 'compsci', 'business', 'chem', 'bio'], dtype='<U8')
>>> majoren={'kinese':34,'compsci':23,'business':56,'chem':13,'bio':67}
>>> print(majoren['compsci'])
23
>>> def ME(name,major):
	 print(name+ 'is in'+ major)

	 
>>> ME('Egi','kinese')
Egiis inkinese
>>> for x in majoren:
	print(x)

	
kinese
compsci
business
chem
bio
>>> 