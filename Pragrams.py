# Reverse a String
"""1)"""

# s = "python"
# k=s[::-1]
# print(k)

"""2)"""
# s="python"
# rev=""
# for i in s:
#     rev=i+rev 
# print(rev)    

"""3)"""

# s="python"
# rev ="".join(reversed(s))
# print(rev)


"""4)"""   
# s="python"
# rev=""
# i=len(s)-1
# while i>=0:
#     rev += s[i]
#     i-=1
# print(rev)    


"""Check Palindrome"""

# s = "madam"
# l=s[::-1]
# if s==l:
#     print("polindram")
# else:
#     print(" not polindram")   

"""2)"""

# s = "madam"
# l=s==s[::-1] 
# print(l)

"""3)"""

# s="madam"
# rev =""
# for i in s:
#     rev =i +rev

# if s==rev:
#     print("p")  

# else:
#     print("not p")      


"""4)"""  

# s="madam"
# rev =""
# i=len(s)-1
# while i>=0:
#     rev +=s[i]
#     i-=1
# if s==rev:
#     print("p")
# else:
#     print("not p")        


"""Fibonacci Series (Simple Explanation)
Definition

The Fibonacci series is a sequence of numbers where each number is the sum of the previous two numbers.

"""

# n = 10
# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     temp = a
#     a = b
#     b = temp + b



"""Prime Number Check (Logic)

A number which is divisible by 1 or itself called as prime number

"""

# n=2
# for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
# else:
#         print("Prime")


"""Find Largest in List"""

# arr=[20,10,15,20]
# result=arr[0]
# for i in arr:
#     if i > result:
#         result=i
# print(result) 


"""Find smallest in List"""  

# arr=[20,10,15,20]
# result=arr[0]
# for i in arr:
#     if i < result:
#         result=i
# print(result) 

"""Remove Duplicates"""

# nums = [1,2,2,3,3]
# duplicate=[]
# non_d=[]
# for i in nums:
#     if i not in duplicate:
#         duplicate.append(i)
#     else:
#         non_d.append(i)   

# print(f"removed duplicate element{non_d}")  

# print(f"without duplicate {duplicate}")

# or 

# def remove_duplicates(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))  

# or 

# [1, 2, 3, 4]
# Method 2: Using dict.fromkeys() (Python 3.7+, concise) python

# def remove_duplicate(lst):
#   result = list(dict.fromkeys(lst))
#   return result
# print(*remove_duplicate(lst = [1, 2, 2, 3, 1, 4, 3,4,4,4,4])) 

# or 

# s="banana"
# result=""

# for i in s:
#     if i not in result:
#         result+=i
# print(result)   
     
"""Two Sum Problem"""

# nums = [2,7,11,15]
# target = 9

# d = {}

# for i, num in enumerate(nums):
#     if target - num in d:
#         print(d[target-num], i)
#     d[num] = i


"""Count Frequency"""

# from collections import Counter
# s="sundarddd"
# print(Counter(s))

"""or"""

# s=[1,2,3,2,1,2,1,1,1,1,1]
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1

# print(freq)  

# or 

# lst = ['a', 'b', 'a', 'c', 'b', 'a']

# freq = {}
# for item in lst:
#     freq[item] = freq.get(item, 0) + 1

# print(freq)  # {'a': 3, 'b': 2, 'c': 1}
      

"""anagram"""
# def ana(a,b):
#     if (sorted(a)==sorted(b)):
#         return " anagram"
#     else:
#         return " not anagram"
# print(ana("silent","listen") )   


# a="silent"
# b="listen"
# if sorted(a)==sorted(b):
#     print("anagram")
# else:
#     print("not angram")    


"""Binary Search"""

# def binary(arr, x):
#     low, high = 0, len(arr)-1
    
#     while low <= high:
#         mid = (low+high)//2
        
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             low = mid+1
#         else:
#             high = mid-1

# print(binary([1,2,3,4,5], 4))

"""Find Missing Number"""

# arr=[1,2,3,4,5,6]
# n=len(arr)+1
# expected_sum=n*(n+1)//2
# actual_sum=sum(arr)
# print(expected_sum-actual_sum)

# def missing_number(arr, n):
#     return n*(n+1)//2 - sum(arr)
# print(missing_number(arr=[1,2,4,5,6,7],n= 7))



"""First Non-Repeating Character"""
# s = "aabbcde"
# for i in s:
#    if s.count(i)==1:
#       print(i)
#       break




""""count the vowel and consonent"""

# def vowel_c(s):
#     result_v=""
#     result_c=""
#     c=0
#     v=0
#     vo_co="aeiouAEIOU"
#     for i in s:
#         if i.isalpha():
#             if i in vo_co:
#                 v+=1
#                 result_v+=i
#             else:
#                 c+=1
#                 result_c+=i
#     print(f"vowels count is:{v},{result_v}")  
#     print(f"consonent count is:{c},{result_c}")   

# vowel_c("sundar")    
# 

"""Toggle function"""

# def u_l(s):
#  result=""
#  for i in s:
#     if i.isupper():
#        result +=i.lower()
#     else:
#      result +=i.upper()  
#  return result  
  
# print(u_l("sundar"))
      

"""reverse each word"""  

# def rev_word(s):
#     output=[]
#     result=s.split()
#     for i in result:
#         reverse_word=i[::-1]
#         output.append(reverse_word)
#         output_1=" ".join(output)
        
#     return output_1

   
# print(rev_word("sundar ranjan"))


"""write a program to reverse order of words"""
# input = hello sundar
# output = sundar hello

# def rev(s):
#     final=""
#     result =s.split()
#     n=len(result)-1
#     while n>=0:
#         final +=result[n]+ " "
#         n-=1
#     return final
# print(rev("hello sundar"))

# or

# def rev_w(s):
#     output=""
#     result=s.split()
#     final=result[::-1]
#     for i in final:
#        output+=i+" "
#     return output

# print(rev_w("sundar ranjan"))

""" only reverse  add postion characters """

# def add_po(s):
#   result=[]
#   word=s.split()
#   i=0
#   while i<len(word):
#     if i%2==0:
#       result.append(word[i])
#       i=i+1
#     else:
#       final=word[i][::-1]
#       result.append(final)
#       i+=1
    
#   return " ".join(result)

# print(add_po("hello sundar from python"))     


"print even and add position character"

# def even_add(s):
#     i=0
#     print("even posion characters")
#     while i< len(s):
#             print(s[i])
#             i+=2
#     i=1
#     print("add position characters:")
#     while i<len(s):
#           print(s[i])
#           i+=2
          
# even_add("sundar")


"""or """

# def add_even(s):
#     even=[]
#     add=[]
#     i=0
#     while i< len(s):
#         if i%2==0:
#             even.append(s[i])
#         else:
#             add.append(s[i])  
#         i+=1 
#     output=" ".join(even) 
#     output_1=" ".join(add) 
      

#     print("even number is :",output)  
#     print("add position :",output_1)

# add_even("sundar")            

"""or """
# def add_even(s):
#     result=s[::2]
#     print(result,"even position")

#     result_1=s[1::2]
#     print(result_1,"add position")

# add_even("sundar")    


"""find the second largest number in arry"""
# def sort_arry(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)) :
#             if arr[i]> arr[j] :
#                 temp=arr[i]
#                 arr[i]=arr[j]    
#                 arr[j]=temp
#     return arr            

# arr=sort_arry([10,1,2,3,100,99]) 
# unique_element=[]
# for i in arr:
#     if i not in unique_element:
#         unique_element.append(i)  
# print(" second largest number is:",unique_element[-2])   
# 



"or" 

# def sort_arry(arr):
#   result=list(set(arr))
#   result.sort()
#   return result[-2]
# print(sort_arry([10,1,2,3,100,99]))




"""
input
a=Ravi
b=teja

output
Rtaevjia
"""

# def merge_two_string(a,b):
#     i=0
#     j=0
#     output=""
#     while i<len(a) or j<len(b):
#         output=output + a[i]+ b[j]
#         i+=1
#         j+=1
#     return output
# print(merge_two_string("ravi","teja"))    

"""
input
a=Ravikumar
b=teja

output
Rtaevjiakumar
"""

# def merge_two_string(a,b):
#     i=0
#     j=0
#     output=""
#     while i<len(a) or j<len(b):
#         if i<len(a):
#             output=output + a[i]
#             i+=1 
#         if j<len(b):
#             output=output + b[j]   
#             j+=1
#     return output
# print(merge_two_string("Ravikumar","teja"))  



"""
input: B4A1D3
output ABD134
"""

# def str_order(s):
#     string=[]
#     number=[]
#     for i in s:
#         if i.isalpha():
#             string.append(i)
#         else:
#             number.append(i)    
#     output="".join(sorted(string)+ sorted(number))  
#     return output
# print(str_order("B4A1D3"))      


"""
input: a4b3c3d1
output aaaabbbcccd
"""
  
# def str_value(s):
#     result=""
#     for i in s:
#         if i.isalpha():
#             x=i
#         else:
#             output = int(i) 
#             result= result+ output*x
#     return result
# print(str_value("a4b3c3d1"))        


"""
input: 4a3b3c1d
output aaaabbbcccd
"""

# from collections import Counter
# input="aaaabbbcccd"
# la=Counter(input)
# print(la)


"""
input: a4k3b2
output aeknbd
"""


# def character(s):
#     output=""
#     for i in s:
#         if i.isalpha():
#             output=output + i
#             x=i
#         else:
#             d=int(i)   
#             result=chr(ord(x)+d)
#             output=output+result
#     return output
# print(character("a4k3b2"))        


"""
input: aaaabbbcccd
output: 4a3b3c1d
"""
# def char_num(s):
#     previos=s[0]
#     output=""
#     i=1
#     c=1
#     while i<len(s):
#         if s[i]==previos:
#             c+=1
#         else:
#             output=output+str(c)+previos  
#             previos=s[i]  
#             c=1

#         i+=1

#     return output
# print(char_num("aaaabbbccd"))    



""" find largest number and that index value"""

# arr=[3,1,9,2,7]
# ka=max(arr)
# la=arr.index(ka)
# print(ka)
# print(la)


"""Flatten Nested List. 
Method 3: Recursive function (handles arbitrary/deep nesting)
"""

# def flatten(lst):
#     result = []
#     for i in lst:
#         if isinstance(i, list):
#             result.extend(flatten(i))  
#         else:
#             result.append(i)
#     return result

# nested_list = [1, [2, 3], [4, [5, 6], 7], 8]

# flat_list = flatten(nested_list)

# print("Flattened list:", flat_list)


#or 
"""Method 1: Using list comprehension (for 2D lists only)"""
# nested = [[1, 2], [3, 4], [5, 6]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)  # [1, 2, 3, 4, 5, 6]

#or

""" sum() (trick for 2D lists only)"""

# nested = [[1, 2], [3, 4], [5, 6]]
# flat = sum(nested, [])
# print(flat)  # [1, 2, 3, 4, 5, 6]



"""FizzBuzz"""

# def fizz_buzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)


# # Call the function
# fizz_buzz(100)



"""
Dictionaries
"""

#. Merge two dictionaries

"""
Merge Two Dictionaries

Method 1: Using ** unpacking (Python 3.5+)python """

# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}
# merged = {**d1, **d2}
# print(merged)  # {'a': 1, 'b': 3, 'c': 4}




"""Note: If keys overlap, the value from the second/later dict wins (d2's 'b': 3 overwrites d1's 'b': 2).
Method 2: Using | operator (Python 3.9+)python"""



# merged = d1 | d2
# print(merged)  # {'a': 1, 'b': 3, 'c': 4}



"""Method 3: Using update() (modifies in place)python"""

# d1.update(d2)
# print(d1)  # {'a': 1, 'b': 3, 'c': 4}


"""Note: This modifies d1 directly — use d1.copy() first if you want to preserve the original.
Method 4: Manual loop (for custom merge logic, e.g., summing values)python"""


# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}

# merged = d1.copy()
# for key, value in d2.items():
#     if key in merged:
#         merged[key] += value  # custom logic: sum instead of overwrite
#     else:
#         merged[key] = value

# print(merged)  # {'a': 1, 'b': 5, 'c': 4}


"""27. Find Keys with Maximum/Minimum Values"""

# Method 1: Using max()/min() with key parameter python


# d = {'a': 10, 'b': 25, 'c': 5, 'd': 25}

# max_key = max(d, key=d.get)
# min_key = min(d, key=d.get)

# print(max_key)  # 'b' (first key with max value)
# print(min_key)  # 'c'


# or 

# d = {'a': 10, 'b': 25, 'c': 5, 'd': 25}
# max_key = None
# max_val = float('-inf')

# for k, v in d.items():
#     if v > max_val:
#         max_val = v
#         max_key = k

# print(max_key, max_val)  # b 25



"""
28. Invert a Dictionary (Swap Keys and Values)
"""
# Method 1: Dictionary comprehension (most common) python

# d = {'a': 1, 'b': 2, 'c': 3}
# inverted = {v: k for k, v in d.items()}
# print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}



# Method 2: Using zip()python

# d = {'a': 1, 'b': 2, 'c': 3}
# inverted = dict(zip(d.values(), d.keys()))
# print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}



"""34. Sum of Digits of a Number"""

# def sum_of_digits(n):
#     n = abs(n)  # handle negative numbers
#     total = 0
#     while n > 0:
#         digit = n % 10      # get last digit
#         total += digit
#         n = n // 10         # remove last digit
#     return total

# print(sum_of_digits(12345))  # 1+2+3+4+5 = 15


#or


"""Method 2: Using string conversion python"""

# def sum_of_digits(n):
#     return sum(int(d) for d in str(abs(n)))

# print(sum_of_digits(12345))  # 15


"""35. Check if a Number is an Armstrong Number"""

# def is_armstrong(n):
#     temp = n
#     num_digits = len(str(n))  # still need this for digit count
#     total = 0
    
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** num_digits
#         temp //= 10
    
#     return total == n

# print(is_armstrong(153))  # True



# or


# def is_armstrong(n):
#     num_str = str(n)
#     num_digits = len(num_str)
    
#     total = sum(int(digit) ** num_digits for digit in num_str)
    
#     return total == n

# print(is_armstrong(153))  # True
# print(is_armstrong(123))  # False (1+8+27=36 ≠ 123)
# print(is_armstrong(9474)) # True (9^4+4^4+7^4+4^4 = 6561+256+2401+256=9474)


"""Armstrong Number Program (1 to 1000)"""

# def is_armstrong(n):
#     temp = n
#     num_digits = len(str(n))
#     total = 0

#     while temp > 0:
#         digit = temp % 10
#         total += digit ** num_digits
#         temp //= 10

#     return total == n


# for num in range(1, 1000):
#     if is_armstrong(num):
#         print(num)

# # 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407




"""GCD (Greatest Common Divisor)"""

# Euclidean algorithm — iterative

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(12, 18))  # 6

# or 

# def gcd(a, b):
#     while b:
#         temp_a = b           # save current b
#         temp_b = a % b        # compute a % b using OLD a and b
#         a = temp_a            # update a
#         b = temp_b            # update b
#     return a

# print(gcd(12, 18))  # 6




"""LCM (Least Common Multiple)"""

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return (a * b) // gcd(a, b)

# print(lcm(12, 18))  # 36