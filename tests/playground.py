# TLDR: `pip3 install -e .` from the root directory of the package
# Then: `python3 ./tests/playground.py`
#
# development mode: "setuptools allows you to install a package without
# copying any files to your interpreter directory
# (e.g. the site-packages directory)."
# From: https://setuptools.pypa.io/en/latest/userguide/quickstart.html#development-mode


import valuewizard as wiz

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

wiz.res("a", 1.0, r"\mm").print()
# a: 1.0 \mm

wiz.res("b", 1.0, 0.01, r"\mm").print()
# b: (1.0 ± 0.01) \mm

wiz.res("c", 1.0, (0.01, "systematic"), r"\mm").print()
# c: (1.0 ± 0.01 systematic) \mm

wiz.res("d", 1.0, [(0.01, "systematic"), (0.02, "stat")], r"\mm").print()
# d: (1.0 ± 0.01 systematic ± 0.02 stat) \mm

# wiz.standard_sigfigs(4)

wiz.res("e", "1.0", r"\mm").print()
# e: 1.0 \mm

# wiz.standard_sigfigs(3)

wiz.res("f", "1.0e4").print()
# f: 1.0

# wiz.res("g", 1.0, sys=0.01, stat=0.02, unit=r"\mm").print()
# g: (1.0 ± 0.01 sys ± 0.02 stat) \mm

# The following wont' work as we can't have positional arguments (here: unit)
# after keyword arguments (here: uncert)
# wiz.res("d", 1.0, uncert=[(0.01, "systematic"), (0.02, "stat")], r"\mm").print()

# wiz.table(
#     "name",
#     {
#         "Header 1": ["Test", "Test2", ...],
#         "Header 2": [wiz.cell_res(...), wiz.cell_res(...), ...],
#         "Header 3": [wiz.cell_res(values[i], errors[i], r"\mm") for i in range(10)],
#     },
#     "Beschreibung",
#     horizontal = True,
# )


#############################
# Export
#############################

print()
print("### EXPORT")
wiz.export("results.tex")
