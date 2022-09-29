""" TEAM -2 STUDENT SYSTEM """
# module created by chandana and joseph
# whole code integration
# main module

from cont import continu
from linked_list import LinkedList

print('\n-------------------------** STUDENT SYSTEM **------------------------------')
while True:
    try:
        linkedlist = LinkedList()
        print("\n* Do want to Register a Student ?? (Press 1) \n* Do you want to see student details ?? (Press 2) ")
        opt_chose = input("--> ")
        info = []
        info_name = []
        result = []
        if opt_chose == '1':
            choice = int(input("how many students you want to register?: "))
            print("\nFill the below details")
            for i in range(choice):
                a = input("Enter student name: ").capitalize()
                b = input("Enter Roll no: ")
                c = input("Enter College name: ").capitalize()
                d = input("Email ID: ")
                e = input("Course name: ").capitalize()
                linkedlist.append(a)
                linkedlist.append(b)
                linkedlist.append(c)
                linkedlist.append(d)
                linkedlist.append(e)
                all = a,b,c,d,e
                t = list(all)
                print(t)
                info.append(t)
                info_name.append(a)
                result = {info_name[i]: info[i] for i in range(len(info_name))}
                print(f"""
                        -------------------------    
                        | Student name :   {a}  
                        | Roll number  :   {b}  
                        | College name :   {c}  
                        | Email ID :       {d}  
                        | Course :         {e}  
                        -------------------------
            Info is being recorded.......            
                                    """)
                with open(f"student_info.txt", mode="a") as file:
                    file.write(f"""
                        -------------------------    
                        | Student name :   {a}  
                        | Roll number  :   {b}  
                        | College name :   {c}  
                        | Email ID :       {d}  
                        | Course :         {e}  
                        -------------------------
                             """)
            while True:
                save = input("\nDo you want to save the info ? (y/n) - ").lower()
                if save in ['y', 'yes']:
                    print("Information has been saved....\n")
                    print(info_name)
                    v = input("enter student name to see the details: ")
                    print(result[v])
                    continu()
                    break
                elif save in ['n', 'no']:
                    print("\nDo you want to edit the info ?? (Press 1) \nDo you want to Quit ? (Press 2) ")
                    while True:
                        choice = input("--> ")
                        if choice == '1':
                            print('-------Student details-------')
                            # print('Information has been successfully changed...')
                            break
                        elif choice == '2':
                            exit()
                        else:
                            print("Press 1 or 2 ...")
                else:
                    input("Enter just y/n ...")
        elif opt_chose == '2':
            with open(f"student_info.txt") as file:
                contents = file.read()
                print(contents)
            continu()
        else:
            print('Choose your option in 1 or 2...')
    except KeyError:
        print("Enter the student name correctly as shown in the names list.....")

