import module_with_main as mwm
#from module_with_main import area as area

def main():
    print(__name__)
    num = int(input("Enter a radius of a circle: "))
    print(f"The area of a circle with a radius of {num} is {mwm.area(num)}")
    # mwm.main()

if __name__ == "__main__":
    main()