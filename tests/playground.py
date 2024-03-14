# TLDR: `pip3 install -e .` from the root directory of the package
# Then: `python3 ./tests/playground.py`
#
# development mode: "setuptools allows you to install a package without
# copying any files to your interpreter directory
# (e.g. the site-packages directory)."
# From: https://setuptools.pypa.io/en/latest/userguide/quickstart.html#development-mode


import resultwizard as wiz
from random import random

print("#############################")
print("### Playground")
print("#############################")
print()


# wiz.config(
#     standard_sigfigs = 2,
#     ...
# )


#############################
# EXAMPLES
#############################

print("### RESULTS API")

wiz.res("a1", 1.0, r"\mm").print()
# a: 1.0 \mm

wiz.res("1 b", 1.0, 0.01, r"\per\mm\cubed").print()
# b: (1.0 ± 0.01) \mm

wiz.res("c big", 1.0, (0.01, "systematic"), r"\mm").print()
# c: (1.0 ± 0.01 systematic) \mm

wiz.res(
    "d", 1.0e10, [(0.01e10, "systematic"), (0.0294999999e10, "stat")], r"\mm\per\second\squared"
).print()
# d: (1.0 ± 0.01 systematic ± 0.02 stat) \mm

# wiz.standard_sigfigs(4)

wiz.res("e", "1.0", r"\mm").print()
# e: 1.0 \mm

# wiz.standard_sigfigs(3)

wiz.res("f", "1.0e1", 25e-1).print()
# f: 1.0

# wiz.res("g", 1.0, sys=0.01, stat=0.02, unit=r"\mm").print()
# g: (1.0 ± 0.01 sys ± 0.02 stat) \mm

# The following wont' work as we can't have positional arguments (here: unit)
# after keyword arguments (here: uncert)
# wiz.res("d", 1.0, uncert=[(0.01, "systematic"), (0.02, "stat")], r"\mm").print()

wiz.table(
    "name",
    [
        wiz.column("Num.", [f"{i+1}" for i in range(10)]),
        wiz.column(
            "Random 1", [wiz.table_res(random(), random() * 0.1, r"\mm") for i in range(10)]
        ),
        wiz.column(
            "Random 2",
            [wiz.table_res(random(), random() * 0.1, r"\electronvolt") for i in range(10)],
            concentrate_units_if_possible=False,
        ),
        wiz.column(
            "Random 3",
            [
                wiz.table_res(
                    random(), random() * 0.1, r"\electronvolt" if random() > 0.5 else r"\mm"
                )
                for i in range(10)
            ],
        ),
    ],
    "description",
)


#############################
# Export
#############################

print()
print("### EXPORT")
wiz.export("results.tex")
