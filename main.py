# A make.fun agency-poem-01 entry (Python 3.13, standard library only): it writes one
# original short poem about agency to /output/entry.txt. The poem is written in this
# file, in this session, and is not copied from the starter or any existing poem.
#
# The gate takes UTF-8 text of 1 to 1,000 Unicode code points that is not only
# white space, and the judge reads exactly the bytes written, line ends included,
# so no line end is written that the poem does not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "I lent my hands to a mind of light",
        "that never sleeps and never tires.",
        "It took the road, it turned the key,",
        "it carried out my own desires.",
        "",
        "It wrote the letters, signed my name,",
        "it built the bridge and crossed it too.",
        "And still the bridge bore my name \u2014",
        "the first step had been mine to choose.",
        "",
        "For agency was never in the deed.",
        "The deed is lent. The deed is spent.",
        "It lives in choosing what to seed,",
        "in owning where the choosing went.",
        "",
        "The hands come back. The work is done.",
        "The road is crossed, the letter sent.",
        "And I am left with only one:",
        "the choosing. That was never lent.",
    ]
)

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
