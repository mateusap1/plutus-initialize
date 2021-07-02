import os
import sys
import subprocess


ppp_dir = "/run/media/mateusap1/hard-drive/plutus/plutus-pioneer-program/code/"
plutus_dir = "/run/media/mateusap1/hard-drive/plutus/plutus/"

# Verify if user provided right number of arguments
if len(sys.argv) != 2:
    print("Program requires exactly one argument!")
    sys.exit(1)

# Verify if argument is an integer
try:
    current_week = int(sys.argv[1])
except ValueError:
    print("Argument must be the current week (integer)!")
    sys.exit(1)

# Based on the given argument, makes a string that will be matched to
# our current week directory
curren_week_str = "week{:02d}".format(current_week)

# Get the week directories inside our ppp dir
weeks = os.listdir(ppp_dir)

def get_current_hash(directory):
    """Goes over each line of cabal.project inside the given directory and tries to grab the tag hash"""

    with open(directory + "/cabal.project", "r") as cabal_file:
        for line in cabal_file:
            if line.lstrip().startswith("tag:"):
                return line.strip().lstrip("tag: ")
    
    print("No tag found")
    sys.exit(1)

# Make sure the week given by the user exists
if curren_week_str in weeks:
    commit_hash = get_current_hash(ppp_dir + curren_week_str)
else:
    print(f"{curren_week_str} does not exist, please provide a valid week!")
    sys.exit(1)

os.chdir(plutus_dir)

subprocess.call(["git", "checkout", commit_hash])
subprocess.call(["nix", "build", "-f", "default.nix", "plutus.haskell.packages.plutus-core"])
subprocess.call("nix-shell")

