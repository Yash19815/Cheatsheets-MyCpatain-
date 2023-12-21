from matplotlib import pyplot as plt

data = {
    'Open Source Softare Tools': 75,
    'Operating Systems': 64,
    'Computational Mathematics': 60,
    'Data Structures Algorithms': 74,
    'Programming in Python': 60,
    'Introduction to Data Science': 48,
}

# Extract keys and values from the dictionary
courses = list(data.keys())
values = list(data.values())

plt.figure(figsize=(10, 5))

# Create bar chart
plt.bar(courses, values, color='blue')

plt.xlabel('Courses')
plt.ylabel('Marks')
plt.title('Bar chart of Marks Scored in Sem 2')
plt.show()