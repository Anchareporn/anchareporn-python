

def welcome_message(name, course):
    # Your Problem 1 solution
    return"Welcome" + name +"to" + Course +"Class!"
    return f"Welcome {name} to {course}class!"


def calculate_circle(radius):
    # Your Problem 2 solution
    pi =3.14159
    area = pi *radius * radius
    cicrcumference =2*pi * radius
    return{
        "area" : area,
        "cicrcumfence" ; cicrcumference
    }


def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    if premium:
        return f"{user name} (age:{age}) - Premium User"
    else:
        return f"[username] (age: {age}) - [Permium User/Stadard User]"



def analyze_scores(scores):
    # Your Problem 4 solution
   total= sum (numbers)
   count=len(numbers)
   average=total/count
   lowest=min(numbers)
   higthest=(numbers)
   return{
       'sum' : total,
       'count':count,
       'average': round(average,2),
    'Lowest: Lowest,
    'higthest':higthest,
    'passed': counter
   }

def count_vowels_consonants(text):
    # Your Problem 5 solution
    text="I'm Iron Man"
    text.lower()
    text.replace("","")
    text.replace("0","")
    text.replace("1","")
    text.replace("2","")
    text.replace("3","")
    text.replace("4","")
    text.replace("5","")
    text.replace("6","")
    text.replace("7","")
    text.replace("8","")
    text.replace("9","")
     
    vowels=text.count('a')+text.count('e')+text.count('i')+text.count('o')+text.count('u')
    consonants=len(text)-vowels

# =============================================================================
# TEST SECTION - DO NOT MODIFY
# =============================================================================

def run_all_tests():
    """Test all functions and display results"""
    print("="*50)
    print("PYTHON FUNCTIONS QUIZ - TEST RESULTS")
    print("="*50)
    
    # Test Problem 1
    print("\n--- Problem 1 Tests ---")
    try:
        result1 = welcome_message("Alice", "Python")
        print(f"Test 1: {result1}")
        result2 = welcome_message("Bob", "Data Science")
        print(f"Test 2: {result2}")
        print("✓ Problem 1: PASSED")
    except Exception as e:
        print(f"✗ Problem 1: ERROR - {e}")
    
    # Test Problem 2
    print("\n--- Problem 2 Tests ---")
    try:
        result1 = calculate_circle(5)
        print(f"Test 1: {result1}")
        result2 = calculate_circle(3)
        print(f"Test 2: {result2}")
        print("✓ Problem 2: PASSED")
    except Exception as e:
        print(f"✗ Problem 2: ERROR - {e}")
    
    # Test Problem 3
    print("\n--- Problem 3 Tests ---")
    try:
        result1 = create_user_profile("john_doe")
        print(f"Test 1: {result1}")
        result2 = create_user_profile("alice", 25)
        print(f"Test 2: {result2}")
        result3 = create_user_profile("bob", 30, True)
        print(f"Test 3: {result3}")
        print("✓ Problem 3: PASSED")
    except Exception as e:
        print(f"✗ Problem 3: ERROR - {e}")
    
    # Test Problem 4
    print("\n--- Problem 4 Tests ---")
    try:
        scores1 = [85, 92, 78, 65, 88, 76, 95]
        result1 = analyze_scores(scores1)
        print(f"Test 1: {result1}")
        scores2 = [45, 67, 89, 72, 58]
        result2 = analyze_scores(scores2)
        print(f"Test 2: {result2}")
        print("✓ Problem 4: PASSED")
    except Exception as e:
        print(f"✗ Problem 4: ERROR - {e}")
    
    # Test Problem 5
    print("\n--- Problem 5 Tests ---")
    try:
        result1 = count_vowels_consonants("Hello World")
        print(f"Test 1: {result1}")
        result2 = count_vowels_consonants("Python Programming 2024")
        print(f"Test 2: {result2}")
        print("✓ Problem 5: PASSED")
    except Exception as e:
        print(f"✗ Problem 5: ERROR - {e}")
    
    print("\n" + "="*50)
    print("END OF TESTS")
    print("="*50)

# Run the tests
if __name__ == "__main__":
    run_all_tests()