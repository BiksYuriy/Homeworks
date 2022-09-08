"""
History:
    You have discovered your folder "Downloads" on your old personal computer.
    And found a lot of files. You are organized human, so you decided to sort your files by some rules.
"""

files = ["april_dashboard.xlsx", "may_dashboard.xlsx", "june_dashboard.xlsx",
         "july_dashboard.xlsx", "october_dashboard.xlsx", "Pro football theory 353-pages.pdf",
         "Clean Code 250-pages.pdf", "War&Peace 150-pages.pdf", "IKEA Instruction 35-pages.pdf",
         "october_dashboard.pptx", "july_dashboard.pptx", "(thriller) The Gray Man (2022).mp4",
         "(thriller) Level 16 (2018).mp4", "(thriller) Synchronic (2019).mp4",
         "(comedy) The Philadelphia Story (1940).mp4", "(comedy) Harold and Maude (1971).mp4",
         "(comedy) Booksmart (2019).mp4"]

for file in files:
           print(file)
number_of_files =  len(files)
print(f"Number of files in folder \"Downloads\" is {number_of_files}.")

file_extensions = []
for i in files:
    print(i.split(".")[-1])
# Не розібрався, як вивести унікальні значення розширення файлів, а також як це робиться у квадратних дужках
# (виводив у себе списком, при чому всі розширення міг зробити у квадртаних дужках, окремо [xlsx], [pdf], тощо.

for i in files:
    # Which method can check file extension at the end?
    if i.endswith("xlsx"):
        excel_files.append(i)
    elif i.endswith("pptx"):
        powerpoint_files.append(i)
    elif i.endswith("pdf"):
        book_files.append(i)
    elif i.endswith("mp4"):
        video_files.append(i)

print("Excel files:", excel_files, end = "\n\n")
print("PowerPoint files:", powerpoint_files, end = "\n\n")
print("Book files:", book_files, end = "\n\n")
print("Video files:", video_files, end = "\n\n")


# How many files in folder?
# Use built-in function len
number_of_files =  # -- * Your code here * --
print(f"Number of files in folder \"Downloads\" is {number_of_files}.")

# RESULT
# Number of files in folder "Downloads" is 17.

# Let's explore unique file-extensions of files
file_extensions = []
for file in files:
    # Use a right method to separate file name and file-extension
    # You can write _ if you it's not important value. In this case I don't need to know file_name
    _, file_extension = file.  # -- * Your code here * --
# Тут взагалі не зрозумів конструкцію _, file_extension = file. Далі твкож не зміг правильно зробити.
    # Easy to understand such condition "not in". Which leads to only unique file-extensions
    if file_extension not in file_extensions:
        file_extensions.append(file_extension)

print(file_extensions)

# RESULT
# ['xlsx', 'pdf', 'pptx', 'mp4']

excel_files = []
powerpoint_files = []
book_files = []
video_files = []

for file in files:
    # Which method can check file extension at the end?
    if file.# -- * Your code here * --
        excel_files.append(file)
    elif # -- * Your code here * --
        powerpoint_files.append(file)
    elif # -- * Your code here * --
        book_files.append(file)
    elif # -- * Your code here * --
        video_files.append(file)

print("Excel files:", excel_files, end = "\n\n")
print("PowerPoint files:", powerpoint_files, end = "\n\n")
print("Book files:", book_files, end = "\n\n")
print("Video files:", video_files, end = "\n\n")

# RESULT
# Excel files: ['april_dashboard.xlsx', 'may_dashboard.xlsx', 'june_dashboard.xlsx', 'july_dashboard.xlsx',
#               'october_dashboard.xlsx']

# PowerPoint files: ['october_dashboard.pptx', 'july_dashboard.pptx']

# Book files: ['Pro football theory 353-pages.pdf', 'Clean Code 250-pages.pdf', 'War&Peace 150-pages.pdf',
#              'IKEA Instruction 35-pages.pdf']

# Video files: ['(thriller) The Gray Man (2022).mp4', '(thriller) Level 16 (2018).mp4',
#               '(thriller) Synchronic (2019).mp4', '(comedy) The Philadelphia Story (1940).mp4',
#               '(comedy) Harold and Maude (1971).mp4', '(comedy) Booksmart (2019).mp4']

# The calendar year can be divided into four quarters, often abbreviated as Q1, Q2, Q3, and Q4.
Q1 = ["January", "February", "March"]
Q2 = ["April", "May", "June"]
Q3 = ["July", "August", "September"]
Q4 = ["October", "November", "December"]

# Your Boss has told you to send dashboard of Q2
excel_files_for_boss = []
for excel_file in excel_files:
    # Separate month and other stuff out of excel file name
    month, _ = excel_file.  # -- * Your code here * --

    # Make condition to check if month belongs to Q2
    if month.  # -- * Your code here * --
        excel_files_for_boss.append(excel_file)

print(excel_files_for_boss)

Q1 = ["January", "February", "March"]
Q2 = ["April", "May", "June"]
Q3 = ["July", "August", "September"]
Q4 = ["October", "November", "December"]

excel_files = ['april_dashboard.xlsx', 'may_dashboard.xlsx', 'june_dashboard.xlsx', 'july_dashboard.xlsx', 'october_dashboard.xlsx']
excel_files_for_boss = []
for excel_file in excel_files:
    # Separate month and other stuff out of excel file name
    str(excel_file.split("_")[-2])
    # Make condition to check if month belongs to Q2
    if str(excel_file.split("_")[-2]) in excel_file != str(Q2).lower:
        excel_files_for_boss.append(excel_file.split("_")[-2])

print(excel_files_for_boss)


# RESULT
# ['april_dashboard.xlsx', 'may_dashboard.xlsx', 'june_dashboard.xlsx']
















