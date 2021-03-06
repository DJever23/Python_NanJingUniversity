# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 10:18
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : local_date_acquisition.py
# @Software: PyCharm

#文件的打开
#file_obj = open(filename,mode='r',buffering=-1,...)
#filename可以包含文件路径
#mode为可选参数，默认值为r
#buffring也为可选参数，默认值为-1（0表示不缓冲，1或大于1的值表示缓冲一行或指定缓冲区大小）
#二进制文件（b）可以不选择缓冲，文本文件必须选择缓冲


#open()函数返回一个文件（file）对象
#文件对象可迭代，可以遍历文件中的每一个子项
#有关闭和读写文件相关的函数/方法
   #f.read(),f.write(),f.readline(),f.redlines(),f.writelines()
   #f.close()
   #f.seek()



# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w  	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。