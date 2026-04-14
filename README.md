# Example Import Dojo

This repositories features an example dojo, which imports from [pwncollege/example-dojo](https://github.com/pwncollege/example-dojo).

The dojo is defined by [dojo.yml](./dojo.yml).

## Add some of these challenges to your dojo

### Option 1: Direct Import
1. Fork the pwn.college Example Import Dojo [here](https://github.com/pwncollege/example-import-dojo.git)
2. In `dojo.yml`:
```yaml
id: dojo-id # TODO: UPDATE
name: Your Dojo Name # TODO: UPDATE

modules:
  - id: module-id # TODO: UPDATE
    name: Your Module Name # TODO: UPDATE
    description: Hello World.
    visibility:
      start: "2025-12-31T00:00:00-07:00" # 2025-12-31 is the date, 00:00:00 is the time, and -07:00 is the timezone (UTC-7, Arizona)
    challenges:
      - import:
          dojo: dojo-pvp
          module: basket
          challenge: livectf2022-something # TODO: UPDATE

      - import:
          dojo: dojo-pvp
          module: basket
          challenge: livectf2022-something # TODO: UPDATE
      # include as many challenges as needed.
```
3. Create the dojo on pwn.college, using your fork of the Example Import Dojo repository.

### Option 2: No overlapping solves
1. Fork this repository.
2. Rename the id in the `dojo.yml` file.
3. Remove any unneeded challenges from the `basket/module.yml` file.
4. Create the dojo on pwn.college, using your fork of this repository.

## Shellcoding: Considerations
If shellcoding (and perhaps obtaining a root shell) is required, please include a file called `runme.c` and compile it (either statically or using `.init`):
```c
#include <unistd.h>
#include <stdio.h>
int main() {
    setuid(0);
    setgid(0);
    execl("/run/dojo/bin/python", "python", "/challenge/challenge.py", NULL); // for python-based challenges
    execl("/challenge/challenge", NULL); // for C-based challenges
    return 0; // Hypothetically never reaches this point
}
```

## `.init` for compilation
The `.init` file is a Bash script which gets executed when building a challenge environment. When compiling challenges, ensure that permissions are configured appropriately with `chmod`. When dynamically compiling, ensure that `.c` (or other source/templating) files are removed unless they are supposed to be visible.
