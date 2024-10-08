def UpCamelToLowUnder(upperCamelString):
    for char in upperCamelString:
        if(char.isupper()):
            upperCamelString = upperCamelString.replace(char, "_" + char.lower());
    return upperCamelString

print(UpCamelToLowUnder("upperCamelStringTest"))