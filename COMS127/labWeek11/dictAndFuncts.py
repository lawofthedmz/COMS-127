# Murphy Glawe          10/29/2023
#
#   Lab Week 11   [COM S 127 Section 6]

# Ex: a + b + c + d, a - b + c + d, a + b - c + d, a + b + c - d, etc.
# 
# Description: program that has for input value (a, b, c, and d) and three operators (+, -, and *). a dictionary is stored with the 27 unique combinations of the values and operators with the combination name as the 'item' and return answer as the key 

def inputValidInt(input_prompt): # Function to check if the input is a valid integer
    while True:
        try:
            val = int(input(input_prompt))
            return val
        except ValueError:
            print("Enter valid integer.")
        

# Mathematical functions for different operator combinations
def calcAAA(a, b, c, d):
    return a + b + c + d
def calcAAS(a, b, c, d):
    return a + b + c - d
def calcASA(a, b, c, d):
    return a + b - c + d
def calcSAA(a, b, c, d):
    return a - b + c + d
def calcASS(a, b, c, d):
    return a + b - c - d
def calcSSA(a, b, c, d):
    return a - b - c + d
def calcSSS(a, b, c, d):
    return a - b - c - d
def calcSSM(a, b, c, d):
    return a - b - c * d
def calcSMS(a, b, c, d):
    return a - b * c - d
def calcMSS(a, b, c, d):
    return a * b - c - d
def calcSMM(a, b, c, d):
    return a - b * c * d
def calcMMS(a, b, c, d):
    return a * b * c - d
def calcMMM(a, b, c, d):
    return a * b * c * d
def calcMMA(a, b, c, d):
    return a * b * c + d
def calcMAM(a, b, c, d):
    return a * b + c * d
def calcAMM(a, b, c, d):
    return a + b * c * d
def calcMAA(a, b, c, d):
    return a * b + c + d
def calcAAM(a, b, c, d):
    return a + b + c * d
def calcAMS(a, b, c, d):
    return a + b * c - d
def calcASM(a, b, c, d):
    return a + b - c * d
def calcSAM(a, b, c, d):
    return a - b + c + d
def calcSMA(a, b, c, d):
    return a - b * c + d
def calcMSA(a, b, c, d):
    return a * b - c + d
def calcMAS(a, b, c, d):
    return a * b + c - d
def calcAMA(a, b, c, d):
    return a + b * c + d
def calcSAS(a, b, c, d):
    return a - b + c - d
def calcMSM(a, b, c, d):
    return a * b + c * d





def main(): # Main function

    a = inputValidInt("Enter an integer: ")
    b = inputValidInt("Enter an integer: ")
    c = inputValidInt("Enter an integer: ")
    d = inputValidInt("Enter an integer: ")


    calculations = { # or i could do calculations["AAA"] = calcAAA(a, b, c, d) for each item and key
        "AAA": calcAAA(a, b, c, d),
        "AAS": calcAAS(a, b, c, d),
        "ASA": calcASA(a, b, c, d),
        "SAA": calcSAA(a, b, c, d),
        "ASS": calcASS(a, b, c, d),
        "SSA": calcSSA(a, b, c, d),
        "SSS": calcSSS(a, b, c, d),
        "SSM": calcSSM(a, b, c, d),
        "SMS": calcSMS(a, b, c, d),
        "MSS": calcMSS(a, b, c, d),
        "SMM": calcSMM(a, b, c, d),
        "MMS": calcMMS(a, b, c, d),
        "MMM": calcMMM(a, b, c, d),
        "MMA": calcMMA(a, b, c, d),
        "MAM": calcMAM(a, b, c, d),
        "AMM": calcAMM(a, b, c, d),
        "MAA": calcMAA(a, b, c, d),
        "AAM": calcAAM(a, b, c, d),
        "AMS": calcAMS(a, b, c, d),
        "ASM": calcASM(a, b, c, d),
        "SAM": calcSAM(a, b, c, d),
        "SMA": calcSMA(a, b, c, d),
        "MSA": calcMSA(a, b, c, d),
        "MAS": calcMAS(a, b, c, d),
        "AMA": calcAMA(a, b, c, d),
        "SAS": calcSAS(a, b, c, d),
        "MSM": calcMSM(a, b, c, d)
      }
    
    print(f"""
input [a]: {a}
input [b]: {b}
input [c]: {c}
input [d]: {d}  """)
    
    for key, value in calculations.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    main()