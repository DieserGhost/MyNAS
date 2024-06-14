import subprocess

def execute_nas_script():
    script_path = 'nas.py'
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error due to executor: {e}")

# Main program
if __name__ == "__main__":
    execute_nas_script()


# HERE WILL BE MORE ADDED SOON!