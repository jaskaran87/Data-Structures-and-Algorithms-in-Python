def generatePermutation(string,start,end):  
    current = 0;  
    #Prints the permutations  
    if(start == end-1):  
        print(string);  
    else:   
        for current in range(start,end):  
  
       #Swapping the string by fixing a character  
            x = list(string);  
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp;  
  
      #Recursively calling function generatePermutation() for rest of the characters  
  
            generatePermutation("".join(x),start+1,end);  
            #Swapping the string by fixing a character  
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp;  
  
str = "AABC"  
n = len(str);  
print("All the permutations of the string are: ");  
generatePermutation(str,0,n);  


AABC
AACB
ABAC
ABCA
ACBA
ACAB
AABC
AACB
ABAC
ABCA
ACBA
ACAB
BAAC
BACA
BAAC
BACA
BCAA
BCAA
CABA
CAAB
CBAA
CBAA
CABA
CAAB
