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
