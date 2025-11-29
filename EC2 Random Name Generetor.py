import random
import string

num_instances = int(input("How many EC2 instance names do you need? "))
department = input("Enter your department name: ").lower()

def generate_name(department):
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    numbers = ''.join(random.choice(string.digits) for _ in range(4))
    return f"{department}-{letters}-{numbers}"

ec2_names = []
for _ in range(num_instances):
    ec2_names.append(generate_name(department))

print("\nGenerated EC2 Instance Names:")
for name in ec2_names:
    print(name)