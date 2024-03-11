import subprocess


def resolve_domain(domain):
    result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
    return result.stdout


domain_name = "example.com"
resolved_ip = resolve_domain(domain_name)
print(f"The IP address of {domain_name} is: {resolved_ip}")
