shopping_list= []
def show_help():
	print("What should we pick up at the store?")
	print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list	  
""")

def show_list():
	print("Here's your list:")
	for item in shopping_list:
		print(item)
		
show_help()

while True:
	new_item= input("> ")
	
	if new_item == "DONE":
		break
	elif new_item == 'HELP':
		show_help()
		continue
	elif new_item == "SHOW":
		show_list()
		continue
	
	shopping_list.append(new_item)
	
show_list()	
	
	