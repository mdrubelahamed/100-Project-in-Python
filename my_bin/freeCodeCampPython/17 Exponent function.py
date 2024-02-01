def raisePower(base,power):
    result=1
    for i in range(power):
        result = result*base
    return result

print(raisePower(2,10))