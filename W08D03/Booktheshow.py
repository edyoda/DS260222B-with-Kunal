import json
class BookTheShow:
    seats = [["E","E","E","E"],["E","E","E","E"],["E","E","E","E"],["E","E","E","E"]]
    user = {}
    def __init__(self):
        self.name = ""
        self.phn = ""
        self.no_of_seat_booked = 0
        self.booking_list = []
    def booking(self):
        for i,row in enumerate(BookTheShow.seats):
            if "E" in row:
                self.booking_list.append(f"{BookTheShow.conv(i)}{row.index('E')}")
                BookTheShow.seats[i][row.index("E")] = "BS"
                self.no_of_seat_booked+=1
                return row,BookTheShow.conv(i)
        else:
            return None
    @staticmethod
    def conv(num):
        d = {i-ord("A"): chr(i) for i in range(ord("A"),ord("D")+1)}
        return d[num]
    
    def register(self, name, phn):
        if phn in BookTheShow.user.keys():
            return False
        self.name = name
        self.phn = phn
        BookTheShow.user[phn] = {"name":name, "phn": phn, "no_of_seat_booked": 0, "booking_list": []}
        return {"message": "success"}
    
def register_user(file_name, name, phn):
    b1 = BookTheShow()
    try:
        file = open(file_name,"r+")
        content = json.load(file)   #when smthng is there
    except FileNotFoundError:
        file = open(file_name,"w+")
        content = {}
    except JSONDecodeError:
        content = {}  
        
    result = b1.register(name, phn)
    print(result)        
    if result:
        result[phn] = b1.__dict__
        file.seek(0)
        file.truncate()
        json.dump(b1.user, file, indent=4)
        file.close()
        return "success"
    file.close()
    return "User is already available!!"

def booking_for_movie(file_name, phn):
    file = open(file_name, "r+")
    content = json.load(file)
    b1 = BookTheShow()
    for i,row in enumerate(b1.seats):
        if "E" in row:
            content[phn]["booking_list"].append(f"{BookTheShow.conv(i)}{row.index('E')}")
            BookTheShow.seats[i][row.index("E")] = "BS"
            content[phn]["no_of_seat_booked"]+=1
            print(content[phn]["no_of_seat_booked"])
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return row,BookTheShow.conv(i)  
        
def check_ticket_history(file_name, phn):
    with open(file_name, "r+") as file:
        content = json.load(file)
        print()
        if content[phn]["booking_list"]:
            for i in content[phn]["booking_list"]:
                print(i)
        else:
            print("Pls Book the tickets quickly")
            
book = input("Do you want to watch movie?Y/n")

while book.lower() == "y":
    print("Select one of the following option")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    option = input("Enter here: ")
    if option == "1":
        print("opt1")
        print(register_user("booktheshow.json", input("Enter name"), input("phn number:")))
        #do smthng
    elif option == "2":
        #do smthng
        file = open("booktheshow.json", "r+")
        content = json.load(file)
        phn  = input("phn number")
        if phn in content:
            while True:
                print("Select the options below:")
                print("1) Book the ticket")
                print("2) Booking History")
                print("3) Exit!!")
                option = input("Enter your option")
                if option == "1":
                    booking_for_movie("booktheshow.json",phn)
                    print("book ticket")
                elif option == "2":
                    print("Ticket History")
                    check_ticket_history("booktheshow.json", phn)
                else:
                    break
                    print("Logging off")
        else:
            print("Pls Register!")
            
    elif option == "3":
        print("Pls consider Us in your Free time!!")
        break
    else:
        print("Hey Select correct option!!")