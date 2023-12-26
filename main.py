class ParkingLot: 
	# Initializing the default Levels A & B with 20 parking spots each
	def __init__(self):
		self.level_A = {i: "" for i in range(1,21)}
		self.level_B = {i: "" for i in range(21,41)}

	# Function to park a car
	def parkVehicle(self, vehicle_number):

		# check to see if the vehicle is already parked 
		for spot, vehicle in self.level_A.items():
			if vehicle == vehicle_number:
				print(f"Sorry! The vehicle - {vehicle_number} has already been parked at spot {spot} in Level A.\n")
				return 

		for spot, vehicle in self.level_B.items():
			if vehicle == vehicle_number:
				print(f"Sorry! The vehicle - {vehicle_number} has already been parked at spot {spot} in Level B.\n")
				return 

		for spot, vehicle in self.level_A.items():
			if vehicle == "":
				self.level_A[spot] = vehicle_number
				print("\nVehicle successfully parked!\n")
				return 

		for spot, vehicle in self.level_B.items():
			if vehicle == "":
				self.level_B[spot] = vehicle_number
				print("\nVehicle successfully parked!\n")
				return  
			
		print("\nSorry! The parking space is full. Please come back after some time.\n")

	# Function to get details of a parked car
	def getParkingDetails(self, vehicle_number):
		for spot in self.level_A.keys():
			if self.level_A[spot] == vehicle_number:
				print(f"\nThe vehicle - {vehicle_number} has been parked at spot {spot} in Level A.\n")
				return 

		for spot in self.level_B.keys():
			if self.level_B[spot] == vehicle_number:
				print(f"\nThe vehicle - {vehicle_number} has been parked at spot {spot} in Level B.\n")
				return 

		print(f"\nSorry! We could not find the vehicle - {vehicle_number} in our parking lot. Please check if the vehicle number you entered is correct.\n")

	# Function to unpark a vehicle 
	def unparkVehicle(self, vehicle_number):
		for spot in self.level_A.keys():
			if self.level_A[spot] == vehicle_number:
				self.level_A[spot] = ""
				print("\nVehicle successfully unparked!\n")
				return 
	
		for spot in self.level_B.keys():
			if self.level_B[spot] == vehicle_number:
				self.level_B[spot] = ""
				print("\nVehicle successfully unparked!\n")
				return 
	
		print(f"\nSorry! We could not find the vehicle - {vehicle_number} in our parking lot. Please check if the vehicle number you entered is correct.\n")
	


# writing a class for our Parking Lot App named ParkSpace
class ParkSpace:
	def __init__(self):
		self.parking_lot = ParkingLot()

	def runApp(self):
		while True: 
			print("----------------- WELCOME TO ParkSpace ---------------------\n")

			print("1. Park a Vehicle")
			print("2. Unpark a Vehicle")
			print("3. Get Parking Spot Details")
			print("4. Exit")

			user_input = input("\nPlease select an option from above: ",)

			if user_input == "1":
				vehicle_number = input("\nPlease enter the vehicle number to park: ")
				self.parking_lot.parkVehicle(vehicle_number)
			elif user_input == "2":
				vehicle_number = input("\nPlease enter the vehicle number to unpark: ")
				self.parking_lot.unparkVehicle(vehicle_number)
			elif user_input == "3":
				vehicle_number = input("\nPlease enter the vehicle number to get parking details: ")
				self.parking_lot.getParkingDetails(vehicle_number)
			elif user_input == "4":
				print("\nThanks for using ParkSpace! Exiting the app...")
				break 
			else: 
				print("Invalid Option! Please try again.\n")

if __name__ == "__main__":
	parking_app = ParkSpace()
	parking_app.runApp()


'''
We can make this app even more comprehensive by - 
1. Adding QC checks for vehicle numbers entered to ensure they fit the standard RTO patterns.
2. We can create a user-friendly web app for this using a Python framework like Django or Flask. 
3. We can use a database like MySQL or MongoDB to store other details of the vehicles.
'''

