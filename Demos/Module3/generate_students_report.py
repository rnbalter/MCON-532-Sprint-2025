"""
This is an exercise to explore how different prompts affects the responses generated
This code interacts with OpenAI's API directories to generate multiple code that calculates students' gpa
"""

from src.open_api_client import get_openai_client
from pprint import pprint

client = get_openai_client()
pprint(vars(client))
system_prompts = []

def makeRequestAPI(user_input: str):
    """
    Creates a request to OpenAI from the given prompt and prints output in terminal
   Args:
       user_input str: string of input prompt
   """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    # Output the response
    pprint(completion)
    pprint(completion.choices[0].message.content)


def part1():
    input1 = """Create a Python dictionary where each student ID maps to another dictionary containing:
    "name": Student’s name (string)
    "grades": A list of grades (integers).
    "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places."""
    makeRequestAPI(input1)
def part2():
    input2 = """Create a Python dictionary where each student ID maps to another dictionary containing:
"name": Student’s name (string)
"grades": A list of grades (integers).
"gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
Use dictionary comprehension to construct the dictionary."""
    makeRequestAPI(input2)
def part3():
    input3 = """Create a Python dictionary where each student ID maps to another dictionary containing:
    "name": Student’s name (string)
    "grades": A list of grades (integers).
    "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
    Use dictionary comprehension, and then format the output using print() so that the student data is displayed in a well-structured format."""
    makeRequestAPI(input3)
def part4():
    input4 = """Create a Python dictionary where each student ID maps to another dictionary containing:
"name": Student’s name (string)
"grades": A list of grades (integers).
"gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
Use dictionary comprehension to create it.
Then, write unit tests using unittest to verify that:
The dictionary contains the correct number of students.
Each student has a "name", "grades", and "gpa".
The "grades" list contains only integers.
Ensure test coverage using IntelliJ’s built-in coverage tool."""
    makeRequestAPI(input4)

def main():
    part1()
    part2()
    part3()
    part4()

if __name__ == '__main__':
    main()


