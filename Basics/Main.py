#if __name__ == '__main__': (This script can be imported or run standalone)
#Functions and classes in this module can be reused without the main block block of code executing.


def fvrt_food(food):
    print(f"Your favorite food is {food}.")
    
def main():
    print("This is Main File.")
    fvrt_food("pizza")
    print("Goodbye!")
    
if __name__ == '__main__':
    main()