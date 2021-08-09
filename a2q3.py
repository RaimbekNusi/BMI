"Raimbek Nussipkhozhin, NFU892, 11313819, Jeffrey Long"
"Question 4"
print("To calculate your body mass index please...")
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
def bmi(weight, height):
    """
    This function calculates the body mass index of the user
    weight: a float for the weight of the user
    height: a float for the height of the user
    x: a float that represents BMI
    returns: the value of the BMI
    """
    x = weight/(height*height)
    return x
print("Your body mass index is " + str(bmi(weight, height)))