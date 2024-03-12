import subprocess

IP_Settings = subprocess.run(
    "ipconfig /all", stdout=subprocess.PIPE, text=True
).stdout.lower()
scan = False
IP_Address = ""
Default_Gateway = ""
Subnet_Mask = ""
DNS_Servers = ""
scan = ""


for i in IP_Settings.split("\n"):
    if (i != None) and ("ethernet adapter ethernet:" in i):
        scan = True
    if scan:
        if "ipv4 address" in i and IP_Address == "":
            IP_Address = i.split(":")[1].strip()
            IP_Address = IP_Address.replace("(preferred)", "")
        if "default gateway" in i and Default_Gateway == "":
            Default_Gateway = i.split(":")[1].strip()
        if "subnet mask" in i and Subnet_Mask == "":
            Subnet_Mask = i.split(":")[1].strip()
        if "dns servers" in i and DNS_Servers == "":
            DNS_Servers = i.split(":")[1].strip()

print(IP_Settings)
# print(IP_Address)
# print(Default_Gateway)
# print(Subnet_Mask)
# print(DNS_Servers)
