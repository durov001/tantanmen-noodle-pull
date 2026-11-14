"""food-picture-01 resubmit: Tantanmen (spicy sesame ramen).

ATM from the top leaderboard: the winning formula is kept (tall glossy
noodle pull, dark speckled bowl, jammy egg with dripping yolk, steam,
chili-oil swirls, moody warm light) but the dish changes from tonkotsu
to tantanmen — creamy orange-tan sesame broth, seasoned minced pork
with sesame seeds instead of chashu slices, bok choy. The program
copies the bundled image to /output/entry.png, deterministically.

Resubmit: replaces the earlier spicy miso ramen entry for food-picture-01.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.jpg"),
        "/output/entry.png",
    )


if __name__ == "__main__":
    main()
