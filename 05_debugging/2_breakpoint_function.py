#  breakpoint() is used to pause and inspect variables while the program is running.
#x = 5
#breakpoint() # Pause here to check x
#print(x / 2)

val_1 = int(input("Enter val_1      :"))
val_2 = int(input("Enter val_2      :"))

breakpoint()

result =  val_1 * val_2 # val_1 + val_2
print(f"Multiplication   :{result}")
