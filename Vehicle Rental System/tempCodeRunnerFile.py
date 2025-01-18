
Vehicle_list = {"Car": [{"ID": "C1", "Milage": "200", "Rent": " 300/hour", "Quantity Available": "7 units"},
                   {"ID": "C2", "Milage": "300", "Rent": " 500/hour", "Quantity Available": "9 units"}, 
                   {"ID": "C3", "Milage": "350", "Rent": " 600/hour", "Quantity Available": "11 units"},
                   {"ID": "C3", "Milage": "350", "Rent": " 600/hour", "Quantity Available": "17 units"}, 
                   {"ID": "C3", "Milage": "250", "Rent": " 400/hour", "Quantity Available": "28 units"}],

            "Cycle": [{"ID": "Cy1", "Milage": 'N/A', "Rent":"120/hour", "Quantity Available": "9 units"},
                      {"ID": "Cy1", "Milage": 'N/A', "Rent":"150/hour", "Quantity Available": "1 units"},
                      {"ID": "Cy1", "Milage": 'N/A', "Rent":"100/hour", "Quantity Available": "8 units"},
                      {"ID": "Cy1", "Milage": 'N/A', "Rent":"110/hour", "Quantity Available": "5 units"},
                      {"ID": "Cy1", "Milage": 'N/A', "Rent":"140/hour", "Quantity Available": "3 units"}],

            "Bike": [{"ID": "B1", "Milage": "120", "Rent": "240/hour", "Quantity Available": "6 units"},
                    {"ID": "B1", "Milage": "120", "Rent": "240/hour", "Quantity Available": "5 units"},
                    {"ID": "B1", "Milage": "120", "Rent": "240/hour", "Quantity Available": "4 units"},
                    {"ID": "B1", "Milage": "120", "Rent": "240/hour", "Quantity Available": "3 units"},
                    {"ID": "B1", "Milage": "120", "Rent": "240/hour", "Quantity Available": "2 units"}]
            }




class Vehicle:
    def __init__(self):
        pass

    def check_availability(self):
        if self.availabilty is True:
            return "Available"
        else:
            return "Not Available"
        
    def update_rate(self):
        new_rate = int(input("Enter the new rate"))
        self.rate = new_rate

    def list_vehicle(self):
        for i,j in Vehicle_list.items():
            print(f"{i}: ")
            for k in j:
                print(f"\nVehicle ID: {k['ID']}\nMilage of Vehicle: {k['Milage']}\nRent/hour: {k['Rent']}")

        

V = Vehicle()
V.list_vehicle()