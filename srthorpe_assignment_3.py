"""
==========================================
 Program: Personal Data Portfolio
 Author: Steven Thorpe
 Date: September 18, 2025
 Description:
     This program uses hardcoded information based on a
     sample person named Jordan Smith and creates a portfolio with it using
     a collection of types.(Dictionaries, Lists, Sets, Strings, Tuples)
     And it also uses mathematical operations to make calculations.
==========================================
"""

#Personal Information
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
grad_semester = "Spring 2028"
major = "Computer Science"

#Academic Data Organization
current_courses_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_course_list = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours_list = [3, 3, 3, 3 ]
gpa_his_list = [3.2, 3.6, 3.4, 3.7 ]

#Contact information tuples
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street, Charlotte, NC 28202")
instagram = ("Instagram", "@jordan_codes", 312)
twitter = ("Twitter", "@jordandev", 127)
bday = ("Birthday", 5,22,2006)

#Interest Tracking
current_skillset = {"Time management", "Photography", "Problem solving", "HTML", "Python basics"}
learning_goals = {"Data structures", "Web design", "JavaScript", "Git", "Public speaking"}
career_interests = {"Software development", "Game development", "Web development", "Data science"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One piece", "Barry", "Life", "Incantation", "Momento"}

#Organizational Mapping (Dictionaries)
course_credits = {
   "COMP 163": 3, 
   "MATH 150": 3,
   "ENG 101": 3,
   "HIS 105": 3,
}
course_profs = {
    "COMP 163": "Prof. Rhodes",
    "MATH 150": "Dr. Lee",
    "ENG 101": "Dr. Martinez",
    "HIS 105": "Dr. Brown"
}
course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 101": "Crosby 121",
    "HIS 105": "Crosby 210"
}
monthly_budget = {
    "Food": 450,
    "Entertainment": 200,
    "Books": 125,
    "Transportation": 100
}
study_hours = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3,
}
contact_directory = {
    "Mom": "704-555-0199",
    "Roommate": "336-555-7821",
    "Academic Advisor": "336-334-5000"
}

#Required Calculations

total_credits = sum(credit_hours_list)
cumulative_gpa = sum(gpa_his_list) / len(gpa_his_list)
completed_course_count = len(completed_course_list)
total_study_hours = sum(study_hours.values())
academic_load = total_credits + total_study_hours
monthly_budget_total = sum(monthly_budget.values())
daily_food_budget = round(monthly_budget["Food"] / 30) #print to the nearest 1 decimals
annual_budget = monthly_budget_total * 12
Study_cost_per_hour = round(monthly_budget["Books"] / total_study_hours) #also round to one decimals

#Analytics Calculations

total_social_media_followers = instagram[2] + twitter[2]
skills_count_comparison = len(current_skillset) , len(learning_goals) #amount of skillsets + the amount of leraning goals
contact_directory_size_analysis = len(contact_directory)
entertainment_backlog_management_count = len(entertainment_backlog)
academic_workload_assessment = academic_load

#print statements

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student:", full_name, "| Email:", student_email)
print("From:", hometown, "| Graduating:", grad_semester)
print("Major:", major)
print("")
print("=== ACADEMIC PROFILE ===")
print("Current Semester:",total_credits, "credits across", len(credit_hours_list), "courses" )
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print("Weekly Study Time:", total_study_hours, "hours")
print(f"Academic Investment: ${Study_cost_per_hour:.1f} per study hour")
print("")
print("Current Courses:")
print(current_courses_list[0], "-", course_credits["COMP 163"],"credits -", course_profs["COMP 163"], "-", course_rooms["COMP 163"])
print(current_courses_list[1], "-", course_credits["MATH 150"],"credits -", course_profs["MATH 150"], "-", course_rooms["MATH 150"])
print(current_courses_list[2], "-", course_credits["ENG 101"],"credits -", course_profs["ENG 101"], "-", course_rooms["ENG 101"])
print(current_courses_list[3], "-", course_credits["HIS 105"],"credits -", course_profs["HIS 105"], "-", course_rooms["HIS 105"])
print("")
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skillset}")
print(f"Learning Goals: {learning_goals}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {len(current_skillset)}")
print(f"Skills Want to Learn: {len(learning_goals)}")
print()
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget["Food"]} (${daily_food_budget:.1f}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")
print()
print("=== CONNECTIONS & CONTACTS ===")
print("Emergency Contact:", emergency_contact[1], "(",emergency_contact[0],") -", emergency_contact[2])
print("Home Address:", home_address)
print("Social Media Presence:", total_social_media_followers, "followers across 2 platforms")
print("Key Contacts:", contact_directory_size_analysis, "people in directory")
print("")
print("=== LIFE STATISTICS ===")
print("Total Courses Completed:", completed_course_count)
print("Current Academic Load:", academic_load, "weekly commitments")
print("Entertainment Backlog:", entertainment_backlog_management_count, "items")
print("Current Hobbies:", len(hobbies), "activities")
print("================================================================")