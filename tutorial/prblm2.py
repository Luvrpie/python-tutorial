def age_classify():
    age=int(input("Enter Your Age:"))
    if age<18:
        print("minor")
    elif age>=18& age<=65:
        print("Adult")
age_classify()