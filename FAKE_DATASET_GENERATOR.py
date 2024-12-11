import pandas as pd

import random

from faker import Faker




faker = Faker()





num_students = 100000

months = [

    "January", "February", "March", "April", "May", "June",

    "July", "August", "September", "October", "November", "December"

]




def generate_random_major():

    majors = [

        "Computer Science", "Biology", "Mathematics", "Physics",

        "Psychology", "Economics", "Engineering", "Medicine",

        "History", "Literature", "Art", "Philosophy"

    ]

    return random.choice(majors)




student_data = {

    "Student Name": [faker.name() for _ in range(num_students)],

    "Student ID": [f"SID{1000 + i}" for i in range(num_students)],

    "Major": [generate_random_major() for _ in range(num_students)],

}

students_df = pd.DataFrame(student_data)




fee_data = []



for student_id in student_data["Student ID"]:

    for month in months:

        day = random.randint(1, 28)  # Ensure valid day range for all months

        fee_data.append({

            "Student ID": student_id,

            "Fee Status": "Paid",

            "Payment Date": f"{month} {day}"

        })



fees_df = pd.DataFrame(fee_data)





students_file_path = "C:\\Users\\21b-133-cs\\Downloads\\students.csv"

fees_file_path = "C:\\Users\\21b-133-cs\\Downloads\\student_fees.csv"



students_df.to_csv(students_file_path, index=False)

fees_df.to_csv(fees_file_path, index=False)



students_file_path, fees_file_path
