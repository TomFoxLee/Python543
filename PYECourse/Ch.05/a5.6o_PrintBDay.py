# Ch.05 Exercise 5.6 Official Answer
# Print Birthday using Library datetime as different format

from datetime import datetime

birthday = datetime(1980, 1, 23, 11, 0)

print(birthday)

print("%sY%sM%sD" % (birthday.year, birthday.month, birthday.day))

print("{0:%Y}-{0:%m}={0:%d} {0:%a}".format(birthday))

print("{0:%b}.{0:%d} {0:%Y}".format(birthday))

print(
    "{0:%d}{1:} {0:%b} {0:%Y}".format(
        birthday,
        ["st", "nd", "rd", "th"][
            birthday.day % 10 - 1 if birthday.day % 10 <= 3 else 3
        ],
    )
)
