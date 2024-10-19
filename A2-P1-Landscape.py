#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     w0402993
#Student Name:  Andrew

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Establish a variable for over sized properties
    overSizeCharge = 0

    #Display Welcome message
    print("Landscape Caclulator")

    #prompt user for address
    address = input("\nEnter House Number: ")

    #Promtuser for property width and depth, then calculate square footage
    depth = float(input("Enter property depth (feet): "))
    width = float(input("Enter property width (feet): "))

    squareFeet = depth * width

    #add an oversize charge if the lanscape is over 5000 square feet
    if squareFeet > 5000:
        overSizeCharge = 500
    
    #prompt user for grass type
    grassType = input("Enter the type of grass (fescue, bentgrass, campus): ").lower()

    #establish the charge for each grass type
    if grassType == "fescue":
        grassCharge =  squareFeet * 0.05
    elif grassType == "bentgrass":
        grassCharge = squareFeet * 0.02
    elif grassType == "campus":
        grassCharge = squareFeet * 0.01

    #prompt user for the amount of trees then calculate the total tree charge

    trees = int(input("Enter the number of trees: "))

    treeCharge = trees * 100

    #caluclate the final cost then display that to the user
    finalCost = overSizeCharge + grassCharge + treeCharge + 1000

    print("\nTotal cost for house {0} is: ${1:.2f}".format(address,finalCost))


main()