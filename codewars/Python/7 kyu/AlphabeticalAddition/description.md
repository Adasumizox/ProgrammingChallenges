# Alphabetical Addition
Description:

Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.
**Notes:**

* Letters will always be lowercase.
* Letters can overflow (see second to last example of the description)
* If no letters are given, the function should return ```'z'```

**Examples:**

```add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'```

Confused? Roll your mouse/tap over [here](Start by converting the letters to numbers, a => 1, b => 2, etc. Add them up. Think about the overflow yourself. Once that's done, convert it back to a letter.)