import subprocess


def run_ping(hostname):
    try:
        # Execute the ping command
        ping_process = subprocess.Popen(
            ["ping", hostname],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
        )

        # Read and print output line by line
        for line in iter(ping_process.stdout.readline, ""):
            print(line, end="")

        # If there's an error, print it
        for line in iter(ping_process.stderr.readline, ""):
            print("Error:", line)

    except Exception as e:
        print("An error occurred:", e)


# Example usage
hostname = "example.com"
run_ping(hostname)
