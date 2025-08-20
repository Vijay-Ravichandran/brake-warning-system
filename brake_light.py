def check_brake_fluid(fluid_percent):
    if fluid_percent <0 or fluid_percent >100:
        return "ERROR"
    if fluid_percent <20:
        return "ON"
    else: 
        return "OFF"
print(check_brake_fluid(15))
print(check_brake_fluid(-1))
print(check_brake_fluid(101))
print(check_brake_fluid(75))
