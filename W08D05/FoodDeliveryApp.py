import json
import datetime

def register_user(user_json, name, password, age, phn):
    user = {
        "id": 1,
        "name": name,
        "password": password,
        "age": age,
        "phone number": phn,
        "order history": {}
        # {"22-04-2022":["naan","chole"],"22-04-2022":["Bisleri"]}
    }
    try:
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                file.close()
                return "User already Exists"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

def user_order_history(user_json, user_id):
    file = open(user_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == user_id:
            print("Order History")
            print("Date | Order")
            for i,j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    file.close()
    return False

def user_place_order(user_json, food_json, user_id, food_name, quantity):
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    file = open(user_json, "r+")
    content = json.load(file)
    file1 = open(food_json, "r+")
    content1 = json.load(file1)
    for i in range(len(content1)):
        if content1[i]["name"] == food_name:
            if content1[i]["no of plates"] >= quantity:
                for j in range(len(content)):
                    if content[j]["id"] == user_id:
                        content1[i]["no of plates"]-=quantity
                        if date not in content[j]["order history"]:
                            content[j]["order history"][date] = [content1[i]["name"]]
                        else:
                            content[j]["order history"][date].append(content1[i]["name"])
            else:
                print("Pls Enter less quantity")
                break    
        else:
            print("Food Not Available")
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    
    file1.seek(0)
    file1.truncate()
    json.dump(content1, file1, indent=4)
    file1.close()

#CRUD operation for Food (create update read delete)
def add_food(food_json, food_name, no_plates=1):
    food = {
        "id":1,
        "name": food_name,
        "no of plates": no_plates
    }
    try:
        fp = open(food_json, "r+")
        content = json.load(fp)
        for i in range(len(content)):
            if content[i]["name"] == food_name:
                fp.close()
                return "Food Already Available"
        food["id"]=len(content)+1
        content.append(food)
    except JSONDecodeError:
        content = []
        content.append(food)
    fp.seek(0)
    fp.truncate()
    json.dump(content, fp, indent=4)
    fp.close()
    return "Success"

def update_food(food_json, food_id, no_plates=1):#no_plates=-1, price=-1):
    file = open(food_json, "r+")
    content = json.load(file)
#    if price > -1 and no_plates > -1: bla bla bla
#    elif price > -1: bla bla bla
#    else: bla bla bla
    for i in range(len(content)):
        if (content[i]["id"] == food_id):
            content[i]["no of plates"] += no_plates
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

def remove_food(food_json, food_id):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return "success"
    return "Pls Enter Valid ID"

def read_food(food_json):
    file = open(food_json)
    content = json.load(file)
    print("Menu:")
    for i in range(len(content)):
        print("Id: ", content[i]["id"])
        print(f"---> Name: {content[i]['name']}")
        print(f"---> Number of Plates: {content[i]['no of plates']}")
    file.close()
    return True
    
val = input("Do you Want to order Food Y/n: ")
while val.lower() == "y":
    print("Menu: ")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    val1 = input("Choose one value from the above: ")
    if val1 == "1":
#--------------Register----------------#
        print()
        name = input("Enter the name: ")
        password = input("Enter the password: ")
        age = int(input("Enter your Age"))
        phn = input("Enter the Phn number")
        register_user("user.json", name, password, age, phn)
        
    elif val1 == "2":
#--------------Login-------------------#
        print()
        while True:
            print("1) User")
            print("2) Admin")
            print("3) Exit")
            val2 = input("Choose on value from above: ")
            if val2 == "1":
                print("---------USER--------")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("user.json", "r+")
                content = json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == user:
                        if content[i]["password"] == password:
                            while True:
                                print()
                                print("1) View Menu")
                                print("2) Place New Order")
                                print("3) Show History of order")
                                print("4) Update Profile")
                                print("5) Exit")
                                val3 = input("Enter your Choice User!! ")
                                if val3 == "1":
                                    read_food("food.json")
                                elif val == "2":
                                    user_id = input("Enter User Id:")
                                    food_name = input("Enter the Food You want to Eat")
                                    quantity = int(input("Enter the quantity of food"))
                                    user_place_order("user.json", "food.json", user_id, food_name, quantity)
                                # Have implemented show order historyand update profile
                                else:
                                    print("Thanks FOr Your Visit (Because it was free and you don't have money)")
                                    break
                        else:
                            print("Wrong Password!!")
                    else:
                        print("Wrong Username!!")                            
                
            elif val2 == "2":
                print("$--------Admin------$")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("admin.json", "r+")
                content = json.load(file)
                if content["name"] == user:
                    if content["password"] == password:
                        while True:
                            print()
                            print("1) Add New Food")
                            print("2) Edit Food")
                            print("3) View Food")
                            print("4) Remove Food") 
                            print("5) Exit")
                            val3 = input("Enter Your Choice Admin!!")
                            if val3 == "1":
                                food_name = input("Enter Food Name: ")
                                no_plates = int(input("Enter the Stock Value: "))
                                add_food("food.json", food_name, no_plates)
                            elif val3 == "2":
                                food_id = input("Enter Food ID: ")
                                no_plates = int(input("Enter the Stock Value: "))
                                update_food("food.json", food_id, no_plates)
                            # Implement ViewFood and Remove Food
                            else:
                                file.close()
                                print("%%%%Bye Bye%%%%%")
                                break
                    else:
                        print("Wrong Password!!")
                else:
                    print("Wrong Username!!")
            else:
                break
    else:
#--------------Exit--------------------#
        print("Siyonara!!")
        break