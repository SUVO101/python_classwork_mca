def get_max_min(tuple):
    return max(tuple),min(tuple)
    #return multiplr values in tuple format

tuple=(5,85,700,0,45,-56,-2,20)
max_value,min_value=get_max_min(tuple)
print(f" tuple {tuple} \n maximum value {max_value} \n minimum value {min_value}")
print(type(get_max_min(tuple))) #<class 'tuple'>