
with open('numbers.txt', 'w') as file:
    # Write numbers from 0 to 5000
    for number in range(5001):
        file.write(str(number) + '\n')