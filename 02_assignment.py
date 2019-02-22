'''
Assignment #2

1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not 
    guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 07_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables unless stated to do so
7. Make sure your work is committed to your master branch in Github


Installation requirements:

1. Please install numpy: pip install numpy

'''
import math
import unittest
import numpy as np
import requests as r

def exercise01():
    # Create a list called animals containing the following animals: cat, dog, crouching tiger, hidden dragon, manta ray

    # ------ Place code below here \/ \/ \/ ------
animals = ['cat', 'dog', 'crouching tiger', 'hidden dragon', 'manta ray']

    # ------ Place code above here /\ /\ /\ ------

    return animals


def exercise02():
    # Repeat exercise 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set the variable len_animals to the length of the animal list.

    # ------ Place code below here \/ \/ \/ ------
len_animals = len(animals)
animals = ['cat', 'dog', 'crouching tiger', 'hidden dragon', 'manta ray']
for i in range(len_animals):
    print(animals[i]),len_animals
    
animals
len_animals

    # ------ Place code above here /\ /\ /\ ------

    return animals, len_animals


def exercise03():
    # Programmatically reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list.
    # The 5th element will be stored in the variable the_fifth_element, which currently below has a dummy value of -999.
    # Remember, the index number of the 5th element is not 5
    
    countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
    the_fifth_element = -999

    # ------ Place code below here \/ \/ \/ ------
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
countdown.sort(reverse = True)
#The list after the sort
print(countdown)
#The element is n - 1
the_fifth_element = countdown[4]
the_fifth_element

    # ------ Place code above here /\ /\ /\ ------

    return countdown, the_fifth_element


def exercise04(more_temperatures, iot_sensor_points, a, b, c, d, e):
    # This exercise function receives a list of temperatures and a dictionary of temperature data where the key is an arbitrary sequential number and the value is the temperature and a,b,c,d and e are each a single temperature reading
    # To Do:
    # 1. Add all of the items in more_temperatures to the temperatures list
    # 2. Add all of the temperature values in iot_sensor_points to the temperatures list
    # 3. Add a,b,c,d and e to the temperature list
    # 4. Organize the temperatures in descending order
    # 5. The samples list will contain every 5th reading from the final temperatures list i.e in list [1,2,3,4,5,6,7,8,9,10] samples would be [5,10]
    # 6. Do a shallow copy of samples into copy_of_samples
    # 7. Organize samples in ascending order

    temperatures = list(np.random.randint(-25, 25, size=10))
    samples = []
    copy_of_samples = []

    # ------ Place code below here \/ \/ \/ ------



    # ------ Place code above here /\ /\ /\ ------

    return samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples


def exercise05(n):
    # This function will find n factorial using recursion (calling itself) and return the solution. For example exercise05(5) will return 120. No Python functions are to be used.

    # ------ Place code below here \/ \/ \/ ------

# f(5) = 5 * f(4)
# f(4) = 5 * f(3)
# f(3) = 5 * f(2)
# f(2) = 5 * f(1)

#f(2) = 2 * 1 -> 2
#f(3) = 3 * 2 -> 6
#f(2) = 4 * 6 -> 24
#f(2) = 5 * 24 -> 120

    # ------ Place code above here /\ /\ /\ ------


def exercise06(n):
     # This function will receive an arbitrary list of numbers of arbitrary size and find the average of those numbers. The size of the list may vary. Find the method that requires the  least amount of code. Return back the length, sum of list and average of list

    # ------ Place code below here \/ \/ \/ ------


    # ------ Place code above here /\ /\ /\ ------
    return length_n, sum_n, average_n


def exercise07(n):
    # This function looks for duplicates in list n. If there is a duplicate False is returned. If there are no duplicates True is returned.

    # ------ Place code below here \/ \/ \/ ------

def has_duplicates(t):
    """Returns True if any element appears more than once in (t),
    False otherwise."""
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

    # ------ Place code above here /\ /\ /\ ------

# Exercise 8
# Create a function called display_menu that receives an argument called menu. The function should do the following:
# 1. Verify that menu is in fact a tuple. If it isnt, return back -1. Remember that a function can return more than one value and -1 is just one of those values. Not all return values need to be meaningful in all cases.
# 2. Determine the number of elements in the menu tuple
# 3. Loops through menu & enumerate through the a menu to the screen. The test case will describe what the menu items are. The enumeration should be generate by code and not hardcoded.
# 4. Using input(), asks the user to select a menu item by entering a number and hitting Enter 
# 5. Validates if the number entered is a valid menu option and asks user to retry if number is not valid or is not a number / int
# 6. An EXIT menu option should be added at the end of the displayed list of menu options allowing the user to exit selecting a menu causing the display_menu() function to return back the number of the last menu option chosen prior to exit and also return the length of menu (the display_menu() function returns two values)
# 7. The menu options should repeatedly display after each selection until user selects EXIT

# ------ Place code below here \/ \/ \/ ------

def display_menu():
    pass

# ------ Place code above here /\ /\ /\ ------

def exercise09():
    # Compile a list of 10 random URLs of dog pics. You will simply populate the dogs list with URLs of pics.

    dogs = []
    url = 'https://random.dog/woof.json'
    dog_media = r.get(url=url)
    print(str(dog_media.content))
    
    # ------ Place code below here \/ \/ \/ ------
    
    dogs = [url]
    url = 'https://random.dog/woof.json', 
    'https://www.dogster.com/wp-content/uploads/2018/06/Chinese-Shar-Pei-4-600x400.jpg',
    'https://www.hillspet.com/content/dam/cp-sites/hills/hills-pet/en_us/img/breeds/german-shepherd-tongue-out-outside.jpg',
    'https://www.thesprucepets.com/thmb/IQGCoLl7dB6RaigKHDZbw3myQvg=/450x0/filters:no_upscale():max_bytes(150000):strip_icc()/portrait-if-a-spitz-pomeranian_t20_v3o29E-5ae9bbdca18d9e0037d95983.jpg',
    'https://gfnc1kn6pi-flywheel.netdna-ssl.com/wp-content/uploads/2018/05/belgian-dog-breeds-header.jpg',
    'https://i.ytimg.com/vi/IHIbg3zHJ20/maxresdefault.jpg',
    'https://i.ytimg.com/vi/dw-olMXonus/maxresdefault.jpg',
    'http://www.directexpose.com/wp-content/uploads/2018/02/e57e24e7-23.-chow-chow-rare-dog-breeds-paws-playgrounds-dotcom.jpg',
    'https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/40/collie.jpg?crop=1.0xw:1xh;center,top&resize=480:*',
    'https://icdn3.themanual.com/image/themanual/best-dog-breeds-alaskan-malamute-800x1500.jpg'
    dog_media = r.get(url=url)
    print(str(dog_media.content))    

    # ------ Place code above here /\ /\ /\ ------

    return dogs

def exercise10(sentence):

    # Exercise10 receives an arbitrary string. Return the sentence backwards with the cases inverted and spaces an underscore _, i.e. HelLo returns OlLEh
    reversed = ''

    # ------ Place code below here \/ \/ \/ ------
    
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Robert"))
print(reverse(a))

    # ------ Place code above here /\ /\ /\ ------
    return reversed


class TestAssignment2(unittest.TestCase):
    def test_exercise01(self):
        print('Testing exercise 1')
        a = exercise01()
        self.assertEqual(len(a), 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)
    
    def test_exercise02(self):
        print('Testing exercise 2')
        a, l = exercise02()
        self.assertEqual(len(a), 5)
        self.assertEqual(l, 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)

    def test_exercise03(self):
        print('Testing exercise 3')
        c, tfe = exercise03()
        self.assertEqual(c[0], 10)
        self.assertEqual(c[11], -5)
        self.assertEqual(len(c), 12)
        self.assertEqual(tfe, 6)

    def test_exercise04(self):
        print('Testing exercise 4')
        more_temperatures = np.random.randint(300, 400, size=25)
        iot_sensor_points = {1: 801, 2: 644, 3: 991, 4: 721,
                             5: 752, 6: 871, 7: 991, 8: 1023, 9: 804, 10: 882}
        samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples = exercise04(more_temperatures, iot_sensor_points,
                                                                                                                 8000, 8500, 9000, 9500, 9999)

        self.assertEqual(len(temperatures), 50)
        self.assertEqual(len(samples), 10)
        self.assertEqual(temperatures[0], 9999)
        self.assertEqual(temperatures[11], 801)
        self.assertEqual(samples[9], 8000)
        self.assertEqual(copy_of_samples[0], 8000)
        self.assertEqual(a, 8000)
        self.assertEqual(b, 8500)
        self.assertEqual(c, 9000)
        self.assertEqual(d, 9500)
        self.assertEqual(e, 9999)

    def test_exercise05(self):
        print('Testing exercise 5')
        self.assertEqual(exercise05(5), 120)
        self.assertEqual(exercise05(10), 3628800)

    def test_exercise06(self):
        print('Testing exercise 6')
        length_n, sum_n, average_n = exercise06([1, 2, 3, 4, 5])
        self.assertEqual(average_n, 3)
        self.assertEqual(length_n, 5)
        length_n, sum_n, average_n = exercise06([1, 2, 120])
        self.assertEqual(average_n, 41)
        self.assertEqual(length_n, 3)

    def test_exercise07(self):
        print('Testing exercise 7')
        self.assertTrue(exercise07([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == False)
        self.assertTrue(exercise07([1, 2.00002, 2.00001, 4, 5, 6, 7, 8, 9, 10]) == True)

    def test_exercise08(self):
        print('Testing exercise 8')
        menu = ['Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum']
        r, l = display_menu(menu)
        self.assertEqual(r,-1)
        self.assertEqual(l,4)
        menu = ('Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum')
        r, l = display_menu(menu)
        self.assertTrue(r > 0)
        self.assertEqual(l,4)
    
    def test_exercise09(self):
        print('Testing exercise 9')
        dogs = exercise09()
        for d in dogs:
            print(d)
        self.assertTrue('https://random.dog/' in d)
            

    def test_exercise10(self):
        print('Testing exercise 10')
        self.assertEqual(exercise10('HellO'),'oLLEh')
        self.assertEqual(exercise10('ThIs Is MaD'),'dAm_Si_SiHt')




if __name__ == '__main__':
    unittest.main()
