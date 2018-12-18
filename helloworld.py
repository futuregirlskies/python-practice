"""student_names = ["Rashad", "Skies", "Mark", "Katarina", "Elf"]
for name in student_names:
    if name == "Mark":
        print("Found him: "+ name)
        break
    print("Currently testing "+name)
"""

student = {
    "name": "Bizmark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"]="von Skies"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 +last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add these two together!")
    print(error)

print("This code executes")