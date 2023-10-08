import base64


def encoder_decoder(comm, fi):
    if comm == "encode":
        name = str(input("Enter the name of the application:"))
        password = str(input("Enter the password you would like to execute:"))
        while True:
            if not name or not password:
                print("Name and password cannot be empty.")
                break
            encoded_bytes = base64.b64encode(password.encode())
            with open(fi, 'a') as lg:
                lg.write(f"{name}\n{str(encoded_bytes)[2:-1]}\n")
            name = str(input("Enter the name of the application:"))
            password = str(input("Enter the password you would like to execute:"))
    else:
        with open(fi, "r") as lg:
            counter = 0
            code = lg.read().split('\n')
            for line in code:
                counter += 1
                if counter % 2 == 1 and line:
                    print(f"..:: {line} ::..")
                else:
                    decoded_bytes = base64.b64decode(line)
                    print(f"{decoded_bytes.decode()}")


# Enter the preferred directory you want to save your file in quotation marks
file = 'Q:\\27.5.2023_BackUp_Downloads\\log.txt'
# The command options are encode/decode
command = str(input("Enter the command you would like to execute:"))
encoder_decoder(command, file)

# Read the pep8 instructions https://peps.python.org/pep-0008/
# Read about the base85 and choose the better encode/decode option
# Make error handling for other commands than encode/decode, wrong directory path and more
# Think about a smart way to end the while loop when the user wishes to end the program
# Optimize the loops and make it Big O notation ready. Also count the exec time before and after!
# Level 300 - input sanitization / validation
