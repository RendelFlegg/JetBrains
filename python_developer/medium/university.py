import statistics


def get_results(file):
    with open(file, "r") as f:
        raw_results = [applicant.rsplit(" ", 8) for applicant in f.read().splitlines()]
    list_of_keys = ["phys_exam", "chem_exam", "math_exam", "com_science_exam", "adm_exam", "plan_a", "plan_b", "plan_c"]
    for result in raw_results:
        results[result[0]] = dict(zip(list_of_keys, result[1:]))


def department_sorting(department, applicants, stage):
    places = number_of_students - len(departments_dict[department])
    temp_departments_dict = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
    for applicant in applicants:
        if department in (results[applicant][stage]):
            temp_departments_dict[department].append((applicant, exam_grade(applicant, stage)))
    temp_departments_dict[department].sort(key=lambda x: (-float(x[1]), x[0]))
    temp_departments_dict[department] = temp_departments_dict[department][:places]
    for student in temp_departments_dict[department]:
        departments_dict[department].append(student)
    departments_dict[department].sort(key=lambda x: (-float(x[1]), x[0]))


def exam_grade(applicant, stage):
    applicant_exams = [exam for exam in exams[results[applicant][stage]]]
    grade = statistics.mean([float(results[applicant][exam]) for exam in applicant_exams])
    if grade < float(results[applicant]["adm_exam"]):
        grade = float(results[applicant]["adm_exam"])
    return grade


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


def print_results():
    for item in departments_dict.items():
        print(item[0])
        for result in item[1]:
            print(f"{result[0]} {float(result[1])}")
        print("")


def save_results():
    for item in departments_dict.items():
        with open(f"{item[0].lower()}.txt", "w") as f:
            f.writelines([f"{result[0]} {float(result[1])}\n" for result in item[1]])


number_of_students = int(input())
students = []
stages = ["plan_a", "plan_b", "plan_c"]
departments = {"Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"}
departments_dict = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
exams = {"Biotech": {"chem_exam", "phys_exam"},
         "Chemistry": {"chem_exam"},
         "Engineering": {"com_science_exam", "math_exam"},
         "Mathematics": {"math_exam"},
         "Physics": {"phys_exam", "math_exam"}}
results = {}

get_results("applicant_list_7.txt")
while len(departments) != 0 and len(students) != len(results):
    rotate()
save_results()
