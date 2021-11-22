students={ "student":["geet","sit","ram","laxman","ravan"],
            "scores":[22,44,66,77,88]
}

import pandas

data_student=pandas.DataFrame(students)
print(data_student)
for (index,row) in data_student.iterrows():
    print(row.scores)