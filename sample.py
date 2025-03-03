cart = []
def add(c):
    user = input("enter item to add: ")
    c.append(user)

def delete(c):
    user = input("enter item to remove: ")
    if user in c:
        c.remove(user)

    else:
        print("item not found")

def view(c):
    print(c)

while True:
    print("Enter 1.Add  2.Remove  3.View  4.Quit")
    user_choice = int(input("enter your choice: "))
    if user_choice == 1:
        add(cart)

    elif user_choice == 2:
        delete(cart)

    elif user_choice == 3:
        view(cart)

    elif user_choice == 4:
        break

    else:
        print("Enter correct choice.")