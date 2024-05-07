def count_Substring_With_Equal_Ends(s): 
    result = 0; 
    n = len(s); 
    for i in range(n):
        for j in range(1,n-i+1): 
            if (ord(s[i]) == ord(s[i+j-1])): 
                result+=1; 
    return result;
