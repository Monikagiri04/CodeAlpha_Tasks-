import re

# file name
input_filename = "input.txt"
output_filename = "emails.txt"

# step 1: open and read the input file
file = open(input_filename, "r", encoding="utf-8")
content = file.read()
file.close()

#step 2: patterns to find emails
pattern = r"[a-zA-Z0-9._/+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"

#step3: extracts emails
found_emails = re.findall(pattern,content)

#step 4: remove duplicate emails
unique_emails = []
for email in found_emails:
    if email not in unique_emails:
        unique_emails.append(email)

#step5 5 : save emails to new file 
out_file = open(output_filename,"w",encoding="utf-8")
for email in unique_emails:
    out_file.write(email+"\n") 

out_file.close()

print("Email extraction completed. check emails.txt file.")
