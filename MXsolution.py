#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import flask
from flask_cors import CORS
from flask import jsonify
from itertools import combinations,permutations


#cards=input()

cards_13=[]     #放13张牌
cards_8=[]   #放8张牌
third_trick=[]#放第三墩
second_trick=[]#放中墩
firsr_trick=[]#放后墩
temp_third=[]
temp_second=[]
temp_first=[]
ans_third=[]
ans_second=[]
ans_first=[]
best_third_trick=[] #
best_second_trick=[]
best_first_trick=[]
number=[]   #桶排
flower=[]  #花色
check=[]
check_2=[]


class a_card:
	flo=0
	num=0
	def __init__(self,f,n):
		self.flo=f
		self.num=n

def init_start():
	global end_ans,score
	end_ans,score=0.0,0.0
	for i in range(0,13):
		cards_13.append(a_card(0,0))
		cards_8.append(a_card(0,0))
		check.append(0)
		check_2.append(0)
	for i in range(0,5):
		flower.append(0)
		third_trick.append(a_card(0,0))
		second_trick.append(a_card(0,0))
		best_second_trick.append(a_card(0,0))	
		best_third_trick.append(a_card(0,0))
		temp_third.append(a_card(0,0))
		temp_second.append(a_card(0,0))
		ans_second.append(a_card(0,0))
		ans_third.append(a_card(0,0))
	for i in range (0,3):
		firsr_trick.append(a_card(0,0))
		best_first_trick.append(a_card(0,0))
		temp_first.append(a_card(0,0))
		ans_first.append(a_card(0,0))
		firsr_trick.append(a_card(0,0))
		best_first_trick.append(a_card(0,0))
		
	for i in range(0,15):
		number.append(0)
		

def return_num(x):
	
	return x.num
	
	
def FlowerToNum(hua):
	
	if hua == "$":       #黑桃
		
		return 1
		
	if hua == "&":      #红桃
		
		return 2
		
	if hua == "*":        #梅花
		
		return 3
		
	if hua == "#":        #方块
		
		return 4


def init_flo_num():
	for i in range(0,5):
		flower[i] = 0
		
	for i in range(0,15):
		number[i] = 0
		

def shunzi_5(x):
	for i in range (x,x+5):
		if number[x] <1:
			return 0	
	return 1
	

def change(x):
	
	if x==10:
		return "10"
		
	if x==11:
		return "J"
		
	if x==12:
		return "Q"
		
	if x==13:
		return "K"
		
	if x==14:
		return "A"
		
	return str(x)

	
	
def weight_5():
	
	init_flo_num()
	for i in range(0,5):
		temp_third[i] = third_trick[i]       #third_trick的顺序千万不能变!!!
	
	temp_third.sort(key=return_num)
	#print(temp_third[0].num,temp_third[1].num,temp_third[2].num,temp_third[3].num,temp_third[4].num)
		
	for i in range(0,5):
		flower[temp_third[i].flo]+=1
		number[temp_third[i].num]+=1
	x=1
	
	for i in range (1,5):
		if flower[i] == 5:
			if shunzi_5(temp_third[0].num):
				k = (9.0 + 0.9/9 * (temp_third[0].num - 1)) * 1.0
				#print("同花顺")
				return k              #同花顺
	x=1
	
	for i in range(0,5):
		if number[temp_third[i].num] == 4:
			k = (8.0+ 0.9/(130+13)*((temp_third[i].num - 1)*10))*1.0
			#print("sidaiyi")
			return k                #四带一
			
	x=1
	
	for i in range(0,5):
		 if number[temp_third[i].num] == 3:
			 x = temp_third[i].num
			 for j in range(0,5):
				 if number[temp_third[4-j].num] == 2:
					 k=(7.0 + 0.9 / (130 + 13)*((x - 1) * 10 + temp_third[4-j].num - 1))*1.0
					 #print("hulu")
					 return k  #葫芦
	x=1
	
	for i in range(0,5):
		
		if flower[temp_third[i].flo] ==5:
			
			k=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((temp_third[4].num-1)*10000+(temp_third[3].num - 1)*1000 + (temp_third[2].num - 1) * 100 + (temp_third[1].num - 1) * 10 + (temp_third[0].num - 1)))*1.0
			#print("tonghua")
			return k     #同花
	
	if shunzi_5(temp_third[0].num)==1:
		 k = (5.0 + 0.9 / 9 * (temp_third[0].num - 1) * 1.0)
		 #print("shunzi")
		 return k #顺子	
		 
	x=1
		
	for i in range(0,5):
		if number[temp_third[i].num] == 3:
			x=temp_third[i].num
		
		for j in range(0,5):
			if number[temp_third[4-j].num] == 1:
				 k = (4.0 + 0.9 / (1300 + 130 + 13) * ((x - 1) * 100))
				 return k        #三条
	
	for i in range(0,5):
		if number[temp_third[i].num]==2:
			if number[temp_third[i].num+1] == 2:
				k = (3.0 + 0.9 / 10 * (temp_third[i].num-1)) * 1.0
				return k      #连续两对
	
	for i in range(2,15):
		if number[i]==2:
			for j in range(i,15):
				if number[j] == 2:
					k = (2.0 + 0.9 / (130 + 13) * ((j - 1) * 10 + i - 1)) * 1.0
					#print("putongliangdui")
					return k  #普通两对
	x=1
	
	for i in range(2,15):
		if number[16-i] == 1:
			x=16-i
			
		if number[16-i] == 2:
			k=(1.0 + 0.9 / (130 + 13) * ((16-i-1) * 10 + x - 1)) * 1.0
			return k #一对
		
	k = (0.9 / (130000 + 13000 + 1300 + 130 + 13) * ((temp_third[4].num - 1) * 10000 + (temp_third[3].num - 1) * 1000 + (temp_third[2].num - 1) * 100 + (temp_third[1].num - 1) * 10 + temp_third[0].num*1.0))

	return k

def shunzi3(x):
	
	if x<=12:
		for i in range(x,x+3):
			if number[i] == 0:
				return False
	
	return True
	
					
def first():

	global score
	init_flo_num()
	x = 1
	for i in range(0,3):
		temp_first[i] = firsr_trick[i]
	
	temp_first.sort(key=return_num)
	for i in range(0,3):
		flower[temp_first[i].flo] +=1
		number[temp_first[i].num]+=1
		
	x = 1
	
	for i in range(1,4+1):
		if flower[i] == 3:
			if shunzi3(temp_first[0].num) == 1:
				
				k=(9.0+0.9 / 11.0 * (temp_first[0].num - 1))
				
				#score += k
				
				return k # 3张同花顺
				
	x = 1
	
	for i in range(1,4+1):
		
		if flower[i] == 3:
			
			k=(6.0 +0.9/(1300+130+13)*((temp_first[2].num-1)*100+(temp_first[1].num-1)*10+(temp_first[0].num-1))*1.0 )
			
			#score += k
			
			return k #3张同花
			
	x = 1
	
	if shunzi3(temp_first[0].num) == 1:
		
		k=(5.0  + 0.9/11.0*(temp_first[0].num-1)*1.0)
		
		#score += k
		
		return k #3张顺子
		
	x = 1
	
	for i in range(0,3):
		
		if number[temp_first[i].num] == 3:
			
			k=(4.0+0.9/13.0*(temp_first[0].num - 1)*1.0)
			
			#score += k
			
			return k#三条
			
	x = 1
	
	for i in range(0,3):
		
		if number[temp_first[2-i].num] == 1:
			
			x = temp_first[2-i].num
			
		if number[temp_first[2-i].num] == 2:
			
			k=(1.0 + 0.9/(130+13)*((temp_first[2-i].num - 1)*10+x-1)*1.0)
			
			#score += k
			
			return k#单对
	
	x = 1
	
	k=0.9 / (1300.0 + 130.0 + 13.0)*((temp_first[2].num - 1) * 100 + (temp_first[1].num - 1) * 10 + (temp_first[0].num - 1))
	
	#score += k
	
	return k #散牌


def second():
	
	global score
	
	init_flo_num()
	
	for i in range(0,5):
		
		temp_second[i] = second_trick[i]
		
	temp_second.sort(key=return_num)  # 中墩牌组有序化
	
	for i in range(0,5):
		
		flower[temp_second[i].flo] +=1
		
		number[temp_second[i].num]+=1
		
	x = 1
	
	for i in range(1,5):
		
		if flower[i] == 5:
			
			if shunzi_5(temp_second[0].num) == 1:
				
				k= (9.0 + 0.9 / 9 * (temp_second[0].num - 1)) * 1.0
				
				#score += k# 14 13 12 11 10
				

				# 同花顺
				
	x = 1
	
	for i in range(0,5):
		
		if number[temp_second[4-i].num] == 1:
			
			x = temp_second[4-i].num
			
		if number[temp_second[4-i].num]== 4:
			
			k=(8.0+ 0.9/(130+13)*((temp_second[4-i].num - 1)*10))*1.0
			
			#score += k
			
			return k#炸弹
			
	x = 1
	
	for i in range(0,5):
		
		if number[temp_second[4-i].num] == 3:
			
			x = temp_second[4-i].num
			
			for j in range(0,5):
				
				if number[temp_second[4-j].num] == 2:
					
					k=(7.0 + 0.9 / (130 + 13)*((x - 1) * 10 + temp_second[4-j].num - 1))*1.0
					
					score += k
					
					return k#葫芦
					
	x = 1
	
	for i in range(1,4+1):
		
		if flower[i] == 5:
			
			k=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((temp_second[4].num-1)*10000+(temp_second[3].num - 1)*1000 + (temp_second[2].num - 1) * 100 + (temp_second[1].num - 1) * 10 + (temp_second[0].num - 1)))*1.0
			
			#score +=k
			
			return k#同花

	x = 1
	
	if shunzi_5(temp_second[0].num) == 1 :
		
		k=(5.0 + 0.9/9*(temp_second[0].num - 1)*1.0)
		
		#score += k
		
		return k#5张顺子
		
	x = 1
	
	for i in range(0,5):
		
		if number[temp_second[4-i].num] == 3:
			
			x = temp_second[4-i].num
			
			for j in range(0,5):
				
				if number[temp_second[4-j].num] == 1:
					
					k=(4.0 + 0.9 / (1300+130+13) * ((x-1) * 100))
					
					score += k
					
					return k# 三条

	x = 1
	
	for i in range(0,5):
		
		if number[temp_second[i].num]==2:
			
			if number[temp_second[i].num+1] == 2:
				
				k = (3.0 + 0.9 / 10 * (temp_second[i].num -1-1)) * 1.0
				
				return k      #连续两对
				
	x = 1
	for i in range(2,15):
		
		if number[i]==2:
			
			for j in range(i,15):
				
				if number[j] == 2:
					
					k = (2.0 + 0.9 / (130 + 13) * ((j - 1) * 10 + i - 1)) * 1.0
					
					return k  #普通两对
					
	for i in range(2,15):
		
		if number[16-i] == 1:
			
			x=16-i
			
		if number[16-i] == 2:
			
			k=(1.0 + 0.9 / (130 + 13) * ((16-i-1) * 10 + x - 1)) * 1.0
			
			return k #一对
			
	k= (0.9 / (130000 + 13000 + 1300 + 130 + 13)*((temp_second[4].num - 1) * 10000 + (temp_second[3].num - 1) * 1000 + (temp_second[2].num - 1) * 100 + (temp_second[1].num - 1) * 10 + temp_second[0].num - 1))*1.0
	
	score +=k
	
	return k

def contrast_ans():
	
	global score,end_ans
	score = 0.0
	k1 = first()
	#print(k1)
	k2 = second()
	k3 =weight_5()
	score=k1*0.8+k2+k3*1.2
	if k1 > k2 or k2 > k3 or k1 > k3 :
		score = 0.0
		
	if score>end_ans :
		end_ans = score
		for i in range(0,3):
			best_first_trick[i] = temp_first[i]
			
			#print(temp_first[i].num)
		   
		for i in range(0,5):
			best_second_trick[i]= temp_second[i]
			best_third_trick[i] = temp_third[i]


	
	
	
def find_second(d,index_second):
	
	for i in range(d,8):
		check_2[i] = 1
		second_trick[index_second]=cards_8[i]
		
		if index_second == 4:
			#print("second_trick=")
			#print(second_trick[0].num,second_trick[1].num,second_trick[2].num,second_trick[3].num,second_trick[4].num)
			index_3=0
			
			for i in range(0,8):
				if check_2[i] == 0:
					firsr_trick[index_3] = cards_8[i]
					index_3+=1
				
			contrast_ans()	
			
		else :
			
			find_second(i+1,index_second+1)
		
		check_2[i]=0
			
			
	
def find_third(d,index_third):
	
	for i in range(d,13):
		check[i] = 1
		third_trick[index_third] = cards_13[i]
		
		#print(str(third_trick[index_third].flo)+" "+str(third_trick[index_third].num))
		
		if index_third == 4:
			k=weight_5()
			#print(number)
			#print("k3="+str(k))
			if k>=2.0 :      #后墩最差的情况也有两个对子
				index_8=0
				for j in range (0,13):
					if check[j] == 0:
						cards_8[index_8] = cards_13[j]
						index_8+=1
				find_second(0,0)
				
		else:
			find_third(i+1,index_third+1)
						
		check[i] = 0
		

def NumToFlower(n):
	
	if n == 1:
		return "$"
	
	if n ==2:
		return "&"
		
	if n==3:
		return "*"
		
	if n == 4:
		return "#"					

def print_ans():
	submit_ans=[]
	s=''
	for i in range(0,3):  #前墩
		s+=str(NumToFlower(best_first_trick[i].flo))+str(change(best_first_trick[i].num))
		if i!=2:
			s+=' '
			
	submit_ans.append(s)	
	s=''
	for i in range(0,5):  #中墩
		s+=str(NumToFlower(best_second_trick[i].flo))+str(change(best_second_trick[i].num))
		if i!=4:	
			s+=' '
	submit_ans.append(s)	
	s=''
	for i in range(0,5):
		s+=str(NumToFlower(best_third_trick[i].flo))+str(change(best_third_trick[i].num))
		if i!=4:
			s+=' '
	submit_ans.append(s)
	return submit_ans
	#print(submit_ans)
	
def end():
	
	ans_first.clear()
	
	ans_second.clear()
	
	ans_third.clear()
	
	best_first_trick.clear()
	
	best_second_trick.clear()
	
	best_third_trick.clear()
	
	cards_13.clear()
	
	cards_8.clear()
	
	check.clear()
	
	check_2.clear()
	
	firsr_trick.clear()
	
	flower.clear()
	
	number.clear()
	
	second_trick.clear()
	
	temp_first.clear()
	
	temp_second.clear()
	
	temp_third.clear()
	third_trick.clear()
		
	
	
def findbest(cards):
	
	newcards = cards.replace("10","T")
	#print(newcards)
	init_start()
	
	index=0
	
	for i in range(1,39,3):
		#print(newcards[i-1]+" "+str(FlowerToNum(newcards[i-1]))+str(newcards[i]))
		
		if newcards[i]=='T':
			x= a_card(FlowerToNum(newcards[i-1]),10)
			
		elif newcards[i] =='J':
			x= a_card(FlowerToNum(newcards[i-1]),11)
			
		elif newcards[i] == "Q":
			x = a_card(FlowerToNum(newcards[i-1]),12)
			
		elif newcards[i] == "K":
			x = a_card(FlowerToNum(newcards[i-1]),13)
			
		elif newcards[i] == "A":
			x = a_card(FlowerToNum(newcards[i-1]),14)
			
		else:
			x= a_card(FlowerToNum(newcards[i-1]),int(newcards[i]))
			
		cards_13[index]=x
		index=index+1
	
	cards_13.sort(key = return_num)
		
	find_third(0, 0)
	ans=print_ans()
	print(ans)
	end()
	return ans
	

#findbest()
server = flask.Flask(__name__)  # __name__代表当前的python文件。把当前的python文件当做一个服务启动

CORS(server, resources=r'/*')


@server.route('/getcards', methods=['post'])  # 第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
def getcards():
	card = flask.request.values.get('card')
	# 你的队友调用你的接口的时候会发给你13张牌，这一行代码可以获取那13张牌，
	# 并以字符串的形式存储在card中，比如card="*2 *3 *4 *5 *6 *7 *8 *9 *10 *J *Q *K *A"

	# 然后在这里你要用你的算法对这个字符串进行处理，分成三墩，然后存储在res中，比如res=["*2 *3 *4","*5 *6 *7 *8 *9","*10 *J *Q *K *A"]
	# 剩下的就不用改了
	# 最后的的接口的url是http://你的ip:port/getcards
	res=findbest(card)
	print(res)
	cardAns = {'card':res}
	print(cardAns)
	response = flask.make_response(jsonify(cardAns))
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
	response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
	return response


server.run(port=8090, debug=True, host='127.0.0.1')