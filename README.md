# plutus-initialize
A simple python script to initialize a nix-shell inside the plutus directory in the right commit

## Requirements

In order to run the script, you need the following:

* the [plutus repository](https://github.com/input-output-hk/plutus/)
* the [plutus-pioneer-program repository](https://github.com/input-output-hk/plutus-pioneer-program/)
* git, as the script will use it to checkout the lecture's needed version of the repository
* nix, as the program will run `nix-shell` when it finishes everything

## Usage

After cloning this repository (or copying the script content into a .py file), you will need to modify the script to fit your own directories.

In lines 6 and 7, you have two variables: `ppp_dir`, which stores the pioneer program directory and `plutus_dir`, which contains a string corresponding to where plutus is located. You should change both of this variables.

Example
```python3
ppp_dir = "/path/to/plutus-pioneer-program/"
plutus_dir = "/path/to/plutus/"
```

Make sure to insert a slash at the end of the variable.

Finally, you can simply run the script, giving the desired lecture number as an argument. 

Example
```console
foo@bar:~$ python3 initialize.py 1
``` 

This command would change the plutus repo version to the one the first lecture was compatible with, build it and run a nix-shell.
