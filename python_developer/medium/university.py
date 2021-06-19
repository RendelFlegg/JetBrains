number_of_students = int(input())
students = []
stages = ["plan_a", "plan_b", "plan_c"]
departments = {"Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"}
departments_dict = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
with open("applicants.txt", "r") as f:
    raw_results = [applicant.rsplit(" ", 4) for applicant in f.read().splitlines()]
results = {}
for result in raw_results:
    results[result[0]] = {"gpa": result[1], "plan_a": result[2], "plan_b": result[3], "plan_c": result[4]}


def department_sorting(department, applicants, stage):
    for applicant in applicants:
        if department in (results[applicant][stage]):
            departments_dict[department].append((applicant, results[applicant]["gpa"]))
            departments_dict[department].sort(key=lambda x: (-float(x[1]), x[0]))
            departments_dict[department] = departments_dict[department][:number_of_students]


def rotate():
    applicants = [key for key in results.keys() if key not in students]
    for dept in departments:
        department_sorting(dept, applicants, stages[0])
    for dept in departments_dict.keys():
        if len(departments_dict[dept]) == number_of_students:
            departments.discard(dept)
    for dept in departments_dict.values():
        for student in dept:
            if student[0] not in students:
                students.append(student[0])
    stages.pop(0)


while len(departments) != 0 and len(students) != len(results):
    rotate()
for item in departments_dict.items():
    print(item[0])
    for result in item[1]:
        print(f"{result[0]} {result[1]}")
    print("")
