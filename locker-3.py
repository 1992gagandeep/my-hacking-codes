master_pin = input("Master Security Pin enter akro:")

if master_pin == "88921625":
    print("Pin Sahi Hai ! Safe Portal Unlocked.")

    while True:
        print("\n[Commands: 'list' se names dekhein | 'exit' se bahar niklein]")
        service = input(" Kaun si service ka password dekhna hai?: ")

        if service == "exit":
            print("Locker se bahar nikal rahe hain. Bye!")
            break
        elif service == "list":
            print("Saved Service: github, netflix")
        elif service == "github":
            print("Github -> Username: 1992gagandeep | Password: Divyansh$2016")
        elif service == "netflix":
            print("Netflix -> Username: 7589413197 | Password: Divyansh$1992")
        else:
            print("Is name se koi service saved nahi hai!")
else:
    print("Galat Pin! Access Denied.")
