from tkinter import *
import random
import time
from faker import Factory

def regiun():
    '''生成身份证前六位'''
    #列表里面的都是一些地区的前六位号码
    first_list = ['362402','362421','362422','362423','362424','362425','362426','362427','362428','362429','362430','362432','110100','110101','110102','110103','110104','110105','110106','110107','110108','110109','110111']
    first = random.choice(first_list)
    return first

def year():
    '''生成年份'''
    now = time.strftime('%Y')
    #1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
    second = random.randint(1948,int(now)-18)
    age = int(now) - second
    # print('随机生成的身份证人员年龄为：'+str(age))
    return second


def month():
    '''生成月份'''
    three = random.randint(1,12)
    #月份小于10以下，前面加上0填充
    if three < 10:
        three = '0' + str(three)
        return three
    else:
        return three


def day():
    '''生成日期'''
    four = random.randint(1,31)
    #日期小于10以下，前面加上0填充
    if four < 10:
        four = '0' + str(four)
        return four
    else:
        return four


def randoms():
    '''生成身份证后四位'''
    #后面序号低于相应位数，前面加上0填充
    five = random.randint(1,9999)
    if five < 10:
        five = '000' + str(five)
        return five
    elif 10 < five < 100:
        five = '00' + str(five)
        return five
    elif 100 < five < 1000:
        five = '0' + str(five)
        return five
    else:
        return five


def random_IDcard():
    first = regiun()
    second = year()
    three = month()
    four = day()
    last = randoms()
    IDcard = str(first)+str(second)+str(three)+str(four)+str(last)
    e7.delete(0, END)
    e7.insert(0, IDcard)

fake = Factory().create('zh_CN')

root = Tk()
root.title("小工具")

def phone_number():
    x = fake.phone_number()
    e1.delete(0, END)
    e1.insert(0, x)

def random_name():
    """随机姓名"""
    x = fake.name()
    e2.delete(0, END)
    e2.insert(0, x)

def random_address():
    """随机地址"""
    x = fake.address()
    e3.delete(0, END)
    e3.insert(0, x)


def random_email():
    """随机email"""
    x = fake.email()
    e4.delete(0, END)
    e4.insert(0, x)


def random_ipv4():
    """随机IPV4地址"""
    x = fake.ipv4()
    e5.delete(0, END)
    e5.insert(0, x)


def random_str(min_chars=6, max_chars=16):
    """长度在最大值与最小值之间的随机字符串"""
    x = fake.pystr(min_chars=min_chars, max_chars=max_chars)
    e6.delete(0, END)
    e6.insert(0, x)

frame= Frame(root)
frame.pack(padx=50,pady=40) #set area
 
e1= Entry(frame,foreground = 'blue',font = ('Helvetica', '12'), width=30)
e2= Entry(frame,font = ('Helvetica', '12'), width=30)
e3= Entry(frame,foreground = 'blue',font = ('华康少女字体', '10'), width=40)
e4= Entry(frame,foreground = 'blue',font = ('华康少女字体', '12'), width=30)
e5= Entry(frame,foreground = 'blue',font = ('华康少女字体', '12'), width=30)
e6= Entry(frame,foreground = 'blue',font = ('华康少女字体', '12'), width=30)
e7= Entry(frame,foreground = 'blue',font = ('华康少女字体', '12'), width=30)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)


there_1 = Button(frame ,text=" 随机生成手机号码 ",font=("宋体",10),width=15,command= phone_number).grid(row=0,column=0,padx=10,pady=5)
there_2 = Button(frame ,text=" 随机姓名 ",font=("宋体",10),width=15,command= random_name).grid(row=1,column=0,padx=10,pady=5)
there_3 = Button(frame ,text=" 随机地址 ",font=("宋体",10),width=15,command= random_address).grid(row=2,column=0,padx=10,pady=5)
there_4 = Button(frame ,text=" 随机Email ",font=("宋体",10),width=15,command= random_email).grid(row=3,column=0,padx=10,pady=5)
there_5 = Button(frame ,text=" 随机网络IP ",font=("宋体",10),width=15,command= random_ipv4).grid(row=4,column=0,padx=10,pady=5)
there_6 = Button(frame ,text=" 随机密码 ",font=("宋体",10),width=15,command= random_str).grid(row=5,column=0,padx=10,pady=5)
there_7 = Button(frame ,text=" 随机身份证 ",font=("宋体",10),width=15,command= random_IDcard).grid(row=6,column=0,padx=10,pady=5)


there_quite = Button(frame ,text=" 退出 ",font=("宋体",10),width=10,command=root.quit).grid(row=7,column=1,padx=15,pady=5)
 
root.mainloop()
