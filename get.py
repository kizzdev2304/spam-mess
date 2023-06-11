# Read the file line by line
with open("acc.txt", "r") as file:
    lines = file.readlines()

# Extract the desired substring from each line and save additional data
additional_data = []
for line in lines:
    items = line.strip().split("|")
    if items:
        user = items[0]
        # password = items[1]
        # verify = items[2]
        # cookie = items[3]
        # print(user,"|", password,"|", verify)
        additional_data.append((user))
# Save the additional data to a separate file
with open("additional_data.txt", "a") as file:
    for data in additional_data:
        file.write("".join(data) + "\n")

print("Additional data saved to additional_data.txt file.")