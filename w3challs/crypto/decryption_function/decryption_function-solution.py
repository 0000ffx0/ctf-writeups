from pycipher import Affine

'''
We have been given the function f(x)=21x+11 [26]
We have to encrypt GOOGLE with this function, after doing this we get = HTTHIR
Now we have to find a function in the same form as the given one`g(y)=ay+b[26]`, that will reverse HTTHIR to GOOGLE
Basically we have to find values of 'a' and 'b' that will give us GOOGLE when we give it HTTHIR
Then use that function to decrypt GELKT
'''

pt = "HTTHIR"
a = [1,3,5,7,9,11,15,17,19,21,23,25]
b = range(26)

find = "GOOGLE"

ct = "GELKT"

flag_format = "\nFLAG:  {}_{}y+{}[26]_{}\n"


def find_solution(str,a,b, find):

    found = ""
    found_a = 0
    found_b = 0

    for c in str:
        for i in a:
            for j in b:
                temp = Affine(a=i,b=j).encipher(str)
                curr_output = "(a={}, b={}) = {}".format(i,j,temp)
                if temp == find:
                    found = curr_output
                    found_a = i
                    found_b = j
                print(curr_output)

    return (found,found_a,found_b)

sol = find_solution(pt,a,b,find)

decrypted = Affine(a=sol[1],b=sol[2]).encipher(ct)

print(flag_format.format(pt.lower(),sol[1],sol[2],decrypted.lower()))

