import subprocess
from time import sleep
from main import simulate_robot

def run_test_case(input_instructions):
    simulate_robot(input_instructions)

def main():
    # Define the input instructions as a list of strings
    input_instructions_list = [
        "MOV, 3\n"
    ]

    # Define the expected output as a list of strings
    expected_output_list = [
        """ 
        División------------------------
        ['XX', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        División------------------------
        ['--', '--', '--', 'XX', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
        """
    ]

    # Write the input instructions to a file
    with open("input.txt", "w") as f:
        for i, instructions in enumerate(input_instructions_list):
            f.write(instructions)

            # Run the program with the input instructions and capture the output
            process = subprocess.Popen(["python", "main.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input=instructions)
            # Wait for the subprocess to finish
            process.wait()

            if stdout.strip() == expected_output_list[i].strip():
                print(f"Test {i+1} passed")
            else:
                print(f"Test {i+1} failed")

            # Wait for 1 second before running the next test
            sleep(1)

if __name__ == "__main__":
    main()