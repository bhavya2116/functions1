q_list = [
	"How many continents are there?",  			# pehla question
	"What is the capital of India?",			# doosra question
	"NG mei kaun se course padhaya jaata hai?"	# teesra question
]

o_list = [
	#pehle question ke liye options
	["Four", "Nine", "Seven", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
s_list = [3, 4, 1]
print('welcome to kbc')
i=0
while i<len(q_list):
	print('your question is',i+1)
	print(q_list[i])
	q=0
	while q<len(o_list[i]):
		print(q+1, o_list[i][q])
		q=q+1
	a=int(input('choose your answer: '))
	if s_list[i]==a:
		print('congrats your answer is right')
					
	else:
		print('wrong You loss the game')
		break	
	i+=1
print("game over")    