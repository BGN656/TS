# %%
def custom_range(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


# %%
def custom_enumerate(iterable_value):
    i = 0
    for value in iterable_value:
        yield i, value
        i += 1


# %%
for a in custom_range(1, 5, 0.1):
    print(a)

# %%
b = custom_range(1, 5, 0.1)
# %%
b


# %%
for i, letter in custom_enumerate("Hello"):
    print(i, letter)

# %%
for i, letter in enumerate("Hello"):
    print(i, letter)


# %%
languages = ["Python", "C++", "Java Script", "C#", "C"]
languages.sort(key=lambda language: len(language))
print(languages)
