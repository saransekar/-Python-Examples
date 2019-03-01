import argparse
def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", metavar = 'symbol', nargs = '?', help = "enter the symbol")
	parser.add_argument("-l", type = int, metavar='limit', nargs='?', help = "enter the number")
	parser.add_argument("-word", choices = ['left', 'right', 'downside', 'upside'], metavar ='word', nargs = '?', help = "enter the word")
	args = parser.parse_args()
	return args

def instruct_pyramid():	
	print("Please select any one below given input:\n1.left triangle pyramid\n2.right triangle pyramid ")
	print("3.downside up triangle pyramid\n4.upside down triangle\n5.Exit")

def get_input_user():
	user_input = int(input("Enter the number:"))
	return user_input	

"""def get_pyramid_values(symbol,i):		
	for j in range(0,i):
		print(symbol,end=" ")
				
def form_left_triangle_pyramid():	
	for i in range(0,limit):
		left = get_pyramid_values(symbol,i+1)
		print()

def form_right_triangle_pyramid():
	k = 2*limit - 2
	for i in range(0, limit): 
		left = get_pyramid_values("",k)     
		k = k - 2 
		left = get_pyramid_values(symbol,i+1)
		print()	

def form_downside_up_pyramid():
	for i in range(0,limit): 
		left = get_pyramid_values("",limit-i-1)
		left = get_pyramid_values(symbol,i+1)		
		print()	

def form_upside_down_pyramid():
	for i in range(limit,0,-1): 
		left = get_pyramid_values("",limit-i)	
		left = get_pyramid_values(i+0)	
		print()"""
def form_left_triangle_pyramid():
	for i in range(0,limit):
		print("a " * limit)
	

def main():
	global symbol,limit
	args_input = create_parser()
	symbol = args_input.s
	limit = args_input.l
	word = args_input.word
	user = 0
	if word is None:
		instruct_pyramid()
		user = get_input_user()
	if word == 'left' or user == 1:
		form_left_triangle_pyramid()
	elif word == 'right' or user == 2:
		form_right_triangle_pyramid()
	elif word == 'downside' or user == 3:
		form_downside_up_pyramid()
	elif word == 'upside' or user == 4:
		form_upside_down_pyramid()
	else:
		print("Inavalid")				
if __name__ == '__main__':
  main()





"""import argparse
def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", metavar = 'symbol', nargs = '?', help = "enter the symbol")
	parser.add_argument("-l", type = int, metavar='limit', nargs='?', help = "enter the number")
	parser.add_argument("-word", choices = ['left', 'right', 'downside', 'upside'], metavar ='word', nargs = '?', help = "enter the word")
	args = parser.parse_args()
	return args

def instruct_triangle():	
	print("Please select any one below given input:\n1.left triangle pyramid\n2.right triangle pyramid ")
	print("3.downside up triangle pyramid\n4.upside down triangle\n5.Exit")

def get_input_user():
	user_input = int(input("Enter the triangle input:"))
	return user_input	
			

def form_left_triangle_pyramid():
	
	for i in range(0,limit):
		left = demo(i,1)
		for j in range(0, i+1):
			print(symbol,end=" ")
		print()

def form_right_triangle_pyramid():
	k = 2*limit - 2
	for i in range(0, limit): 
		for j in range(0,k): 
			print(end=" ")       
		k = k - 2 

		for j in range(0, i+1):          
			print(symbol, end=" ") 
		print() 

def form_triangle_pyramid():
	for i in range(0,limit): 
		for j in range(0, limit-i-1): 
			print(end=" ") 
				
		for j in range(0, i+1):           
			print(symbol,end=" ")   
		print() 

def form_upside_down_triangle():
	for i in range(limit,0,-1): 
		for j in range(0, limit-i): 
			print(end=" ") 			
		for j in range(0, i):           
			print(symbol,end=" ")   
		print() 
			
def main():
	global symbol,limit
	args_input = create_parser()
	symbol = args_input.s
	limit = args_input.l
	word = args_input.word
	if word is None:
		instruct_triangle()
		user = get_input_user()
		if user == 1:		
			form_left_triangle_pyramid()
		elif user == 2:	
			form_right_triangle_pyramid()
		elif user == 3:	
			form_triangle_pyramid()
		elif user == 4:	
			form_upside_down_triangle()
		else:
			exit()
	else:
		if word == 'left':
			form_left_triangle_pyramid()
		elif word == 'right':
			form_right_triangle_pyramid()
		elif word == 'downside':
			form_triangle_pyramid()
		elif word == 'upside':
			form_upside_down_triangle()
				
if __name__ == '__main__':
  main() """











"""space = 2*limit - 2    
for i in range(0, limit): 
	for j in range(0, space): 
		print(end=" ") 
	space = space - 1
	for j in range(0, i+1):           
		print(symbol, end="")   
	print() 

n = 5

for i in range(0,n): 
	for j in range(0, n-i-1): 
		print(end=" ") 	
	for j in range(0, i+1):           
		print("* ",end="")   
	print() """



""" print("Welcome to" , end = '@')
print("GeeksforGeeks", end = ' ') """




"""def asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( i + 1 ) + '*' * ( t * 2 + 1 ))
        return asterix_triangle( i - 1, t + 1 )

asterix_triangle(5)

def upside_down_asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( t + 1 ) + '*' * ( i * 2 - 1 ))
        return upside_down_asterix_triangle( i - 1, t + 1 )

upside_down_asterix_triangle(5)"""
