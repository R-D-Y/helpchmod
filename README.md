# hchmod

A command-line tool to decode chmod numbers and provide explanations.

## Overview

`hchmod` is a simple command-line tool written in Python that allows users to decode chmod numbers and get explanations for the permissions. It helps users understand the various permission levels represented by the chmod numbers and provides a breakdown of the permissions for User, Group, and Others.

## Installation

To install `hchmod`, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/R-D-Y/hchmod.git
    ```

2. Navigate to the project directory:

    ```bash
    cd hchmod
    ```

3. Install the package using pip:

    ```bash
    pip install .
    ```

## Usage

After installing `hchmod`, you can use it directly from the command line. Simply type `hchmod` followed by the chmod number you want to decode:

```bash
hchmod xxx
```

For example, to decode the chmod number `755`:

```bash
hchmod 755
```

This will display the decoded permissions for User, Group, and Others, along with the Umask value.

## Explanation

- `r`: Read - Permission to read a file.
- `w`: Write - Permission to modify a file.
- `x`: Execute - Permission to execute a file.

## Example

```bash
hchmod 755
```

Output:
```
Modus for chmod 755: rwxr-xr-x
UGO permissions: User = rwx, Group = r-x, Others = r-x
Umask: 022
```

## License

This project is licensed under the MIT License.

Feel free to modify and use `hchmod` to decode chmod numbers easily and understand permission settings on your Linux system.
