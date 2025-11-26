class Application:
    def __init__(self,application_name,catogary,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.catogary=catogary
        self.company=company
        self.app_size=app_size
        self.no_of_users=no_of_users
        self.ratings=ratings
    def sigup(self):
        print(f"sigup done ,{self.application_name}")

    def login(self):
        print(f"welcome to {self.application_name}")

    def logout(self):
        print("Thank You for using")

    def display_details(self):
        print("\n---- Application Details ----")
        print(f"Application Name : {self.application_name}")
        print(f"Category         : {self.catogary}")
        print(f"Company          : {self.company}")
        print(f"App Size (MB)    : {self.app_size}")
        print(f"No. of Users     : {self.no_of_users}")
        print(f"Ratings          : {self.ratings}")
        print("------------------------------")


app1=Application("Instagram","social media","meta",
                 44.47,1000,4.5)
app2=Application("Facebook","social media","meta",
                 50.45,950,3.5)
app3=Application("Whatsapp","social media","meta",
                 42.09,2000,4.5)
app1.sigup()
app1.login()
app1.display_details()
app1.logout()
print()

app2.sigup()
app2.login()
app2.display_details()
app2.logout()
print()

app3.sigup()
app3.login()
app3.display_details()
app3.logout()
print()

