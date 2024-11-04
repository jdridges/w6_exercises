def conv_c_to_f(current_temp_c):
    current_temp_f = round((current_temp_c * 9 / 5) + 32, 2)
    return f' {current_temp_c} degrees celsius converts to {current_temp_f} degrees fahrenheit'
print(conv_c_to_f(100))
print(conv_c_to_f(45))
print(conv_c_to_f(19))
print(conv_c_to_f(0))
print(conv_c_to_f(-7))
print(conv_c_to_f(-40))