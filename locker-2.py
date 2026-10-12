master_pin = input("Master Security PIN enter Karo: ")

if master_pin == "88921625":
    print("Pin Sahi Hai | Safe Portal Unlocked.")
    service = input("kaun si service ka password dekhna hai?: ")

    if service == "github":
      print("Github -> User name: 1992gagandeep | Password: Divyansh$2016")
    elif service == "netflix":
      print("Netflix -> username: 7589413197 | Password: Divyansh$1992")
    else:
      print("Ish Name se koi service saved nahi hai")
else:
    print("Galat Pin| Access Denied.")
