import subprocess
import re


"""
If you just use the 'subprocess.run("ipconfig /all")', this will print out the
commands result to the terminal.
Instead of printing it to the terminal, We want to capture that result.
So we use 'stdout=subprocess.PIPE' as an argument. This allows us to capture the result.

'text=True' tells to decode the output of the command to a string using the default text encoding. 
This makes it easier to work with the output as a string.
"""


class GeneralData:

    # ipv4_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    general_data = subprocess.run("ipconfig /all", stdout=subprocess.PIPE, text=True)
    general_data = general_data.stdout
    print(general_data)


GeneralData()
