# lathe-calc
Calculator of gear setups for a lathe

This project was inspired by the lack of complete information about possible gear train vs gearbox settings, particulary on "ОТ-4" lathe. The usual tables give only some gear train settings with gearbox in bypass mode as well as some gearbox settings with gear train in "standard set". This description is far from being complete and does not allow for some specific lead settings I needed.

This small python3 (v3 is mandatory) script offers two useful functions:
lead(...) calculates the lead/feed value in mm per revolution for any given setup
find_setup(...) looks for setups that satisfy the requested lead/feed value to a given tolerance

Although it was designed for "ОТ-4", you can easily customize this calculation for your own lathe.
Feel free to improve and contribute to the project!