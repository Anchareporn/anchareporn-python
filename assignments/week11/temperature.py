"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
    
def get_tempertures():
    temperatures = [31,32,28,30,29,31,32]
    return temperatures

def analy_temps(temp_list):
    avg_temp =0
    highest_temp = max(temp_list)
    lowest_temp = min(temp_list)

    sum = 0
    for temp in temp_list:
        sum = sum + temp
    avg_temp = sum / len(temp_list) 
    return(avg_temp,highest_temp,lowest_temp)
   
def display_analysis(avg,high,low):
    print("Temperature Ananlysis for the Week:")
    print("Average: %.2fC"%(avg))
    print(f"Highest:{high} C")
    print("Lowest:",low," C")

my_temp = get_tempertures()   
analyzed_temp = analyze_temps(my_temps)
display_analysis(analyzed_temp[0],analyzed_temp[1],analyzed_temp[2])
