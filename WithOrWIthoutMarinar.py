# ============================
# Welcome Branch
# Simulated OS Boot Screen
# ============================

# Libraries imported for system output control and timing delays
import sys
import time

# ----------------------------
# ANSI color codes for terminal text coloring
# ----------------------------
CYAN = "\033[96m"    # Cyan text (used for titles)
YELLOW = "\033[93m"  # Yellow text (used for boot animation)
GREEN = "\033[92m"   # Green text (used for success message)
RESET = "\033[0m"    # Resets text color back to default

# Display program title and version information
print(f"{CYAN}Welcome Branch - Developer: Matthew Smith{RESET}")
print(f"\n{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# ----------------------------
# Boot animation variables
# ----------------------------
x = 0          # Counter to control how long the boot process runs
ellipsis = 0   # Controls the number of dots shown in the loading message

# ----------------------------
# Simulated OS boot loop
# ----------------------------
while x != 20:
    x += 1  # Increment loop counter each cycle

    # Create the boot message with animated dots
    ellipsisMessage = (
        f"{YELLOW}InfoTechCenter OS is Booting Up{'.' * ellipsis}{RESET}"
    )

    ellipsis += 1  # Increase dot count for animation effect

    # Overwrite the current terminal line with the updated message
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Forces the output to appear immediately

    time.sleep(0.5)  # Pause to simulate boot delay

    # Reset dot animation after 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # Final message once boot process is complete
    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Access Granted{RESET}")
