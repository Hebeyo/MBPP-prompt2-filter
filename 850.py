def is_triangleexists(a,b,c):
    if(a == 0 or b == 0 or c == 0 or (a + b + c)!= 180):
        return False
    if((a + b)< c or (b + c)< a or (a + c)< b):
        return False
    return True
