import json
import datetime

def register_user(user_json,name,password,age,phn):
	user={

	     "id":1,
	     "name":name,
	     "password":password,
	     "age":age,
	     "phone_number":phn,
	     "order_history":[]



	}
	try:
		file=open(user_json,'r+')
		content=json.load(file)
		for i in range(len(content)):
			if content[i]["phone_number"]==phn:
				file.close()
				return "user already exists"
		else:
			user["id"]=len(content)+1
			content.append(user)
	except JSONDecodeError:
		content=[]
		content.append(user)
	file.seek(0)
	file.truncate()
	json.dump(content,file,indent=4)
	file.close()
	return "Success"

def user_order_history(user_json,user_id):
	file=open(user_json,'r+')
	content=json.load(file)
	for i in range(len(content)):
		if content[i]["id"]==user_id:
			print("order history")
			print("Date | Order")
			for i,j in content[i]["order_history"].items():
				print(f"{i} | {j}")
			file.close()
			return True
	file.close()
	return False

def add_food(user_json,food_name,no_of_plates=1):
	food={

	      "id":1,
	      "name":food_name,
	      "no_of_plates":no_of_plates



	}
	try:
		file=open(user_json,'r+')
		content=json.load(file)
		for i in range(len(content)):
			if content[i]["name"]==food_name:
				file.close
				return "Food already Present in Menu"
		food["id"]=len(content)+1
		content.append(food)
	except JSONDecodeError:
		content=[]
		content.append(food)

	file.seek(0)
	file.truncate()
	json.dump(content,file,indent=4)
	file.close()
	return "Success"

def update_food(food_json,food_id,no_of_plates=1):
	file=open(food_json,'r+')
	content=json.load(file)
	for i in range(len(content)):
		if content[i]["id"]==food_id:
			content[i]["no_of_plates"]+=no_of_plates
			break
	file.seek(0)
	file.truncate()
	json.dump(content,file,indent=4)
	file.close()
	return "Success"

def remove_food(file_json,food_id):
    file=open(food_json,'r+')
    content=json.load(file)
    for i in range(len(content)):
        if content[i]["id"]==food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return "Success"
    return "please enter valid food id"

def read_food(file_json):
	file=open(food_json,'r+')
	content=json.load(file)
	print("Menu")
	for i in range(len(content)):
		print(f"{content[i]['id']}-{content[i]['name']}-plates{content[i][no_of_plates]}")

	file.close()
	return "Success"
		