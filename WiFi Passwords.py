import subprocess

print("="*50)
print("       🔐 Wi-Fi Password Viewer by Shubh")
print("="*50)

# Fetch all saved Wi-Fi profiles
output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8', errors='backslashreplace')
lines = output.split('\n')

# Extract profile names
profiles = []
for line in lines:
    if "All User Profile" in line:
        profile = line.split(":")[1].strip()
        profiles.append(profile)

# Print header
print("\n{:<30} | {:<}".format("📶 Wi-Fi Name", "🔑 Password"))
print("-" * 50)

# Get password for each Wi-Fi profile
for profile in profiles:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], encoding='utf-8', errors='backslashreplace')
        result_lines = result.split('\n')
        password_lines = [line.split(":")[1].strip() for line in result_lines if "Key Content" in line]

        password = password_lines[0] if password_lines else "No Password Found"
        print("{:<30} | {:<}".format(profile, password))

    except subprocess.CalledProcessError:
        print("{:<30} | {:<}".format(profile, "ACCESS ERROR"))

input("\n🔚 Press Enter to close...")
