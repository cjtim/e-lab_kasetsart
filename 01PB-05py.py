length = int(input("Enter block length: "))
width = int(input("Enter block width: "))
houselength = int(input("Enter house length: "))
housewidth = int(input("Enter house width: "))
grass = (length*width)-(houselength*housewidth)
mowing_cost = grass*35
print("Mowing cost is",mowing_cost,"baht.")