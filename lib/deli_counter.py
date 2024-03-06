
katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        new_list = [(str(index+1) + ". " + name) for index, name in enumerate(katz_deli)]
        print(new_list)
        result = " ".join(new_list)
        return "The line is currently: "+result

def take_a_number(katz_deli, name):
    katz_deli = katz_deli
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_customer = katz_deli.pop(0)
        print(current_customer)
        return f"Currently serving {current_customer}."

