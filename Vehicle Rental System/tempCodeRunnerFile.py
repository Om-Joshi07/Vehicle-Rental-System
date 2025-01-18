def register(self):
        F_Name = input("Enter your Full Name:  ")
        Email = check_email()
        Phone = check_contact()
        Password = encryp()
        i=1
        while self.ws.cell(row= i+1, column= 1).value is not None:
            i+=1
        self.ws.cell(row= i+1, column= 1).value = F_Name
        self.ws.cell(row= i+1, column= 2).value = Email
        self.ws.cell(row= i+1, column = 3).value = Phone
        self.ws.cell(row= i+1, column= 4).value = Password
        print("Account created successfully!!")
        self.wb.save("VRS.xlsx")

        # self.account
        print(f"You have been registed as: {F_Name} ")

            
        # return F_Name, Email, Phone, Password
    


        # Loging in for a customer

    def login(self):
        Email = input("Enter your Email:    ")
        Password = decryp()
        for i in range(2, self.ws.max_row + 1):
            stored_email = self.ws.cell(row=i, column=2).value
            stored_password = self.ws.cell(row=i, column=4).value
            name = self.ws.cell(row=i, column=1).value
            if stored_email == Email and stored_password == Password:
                print("Login successful!!")
                print(f"You have been registed as: {name} ")
                break

                # return Email, Password
        else:
            print("Invalid Email or Password.")


