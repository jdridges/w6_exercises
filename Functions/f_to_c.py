def conv_f_to_c(current_temp_f):
    current_temp_c = round(((current_temp_f -32)* 5)/ 9, 2 )
    return f' {current_temp_f} degrees fahrenheit converts to {current_temp_c} degrees celsius'


print(conv_f_to_c(int(input("How hot is it today?: "))))


#212 f = 100 c
#90 f = 32.22 C
#72 f = 22.22 C
#32 f = 0 c
# 0 f = -17.78 c
# -40 f = -40 c ... interesting