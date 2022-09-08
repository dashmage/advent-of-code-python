[Advent of Code 2021](https://adventofcode.com/2021) solutions using Python.

Solving from CLI using [advent-cli](https://github.com/fergusch/advent-cli)

### Adding session cookie
Add the session cookie as an environment variable in order to authenticate my user.

In order to add the environment variable on Windows:
```powershell
# Open profile settings
> notepad $PROFILE

# Add this line
$env:ADVENT_SESSION_COOKIE = 'xyz123'
```

### Advent-CLI commands
From the documentation on the [GitHub Repo](https://adventofcode.com/2021):

```powershell
# Download a question
$ advent get YYYY/DD

# Test a solution
$ advent test YYYY/DD

# Test a solution providing example input
$ advent test YYYY/DD -e

# Submit answers
$ advent submit YYYY/DD
```

### Solution structure
> When the solution is run, the input will be read from input.txt and automatically passed to parse_input as lines, an array of strings where each string is a line from the input with newline characters removed. You should implement parse_input to return your parsed input or inputs, which will then be passed to part1 and part2. If parse_input returns a tuple, part1 and part2 will be expecting multiple parameters that map to those returned values. The parameter names can be changed to your liking. The only constraint is that part1 and part2 must have the same number of parameters.
>
> If part2 is left unmodified or otherwise returns None, it will be considered unsolved and part1 will be run and submitted. If both functions are implemented, part2 will be submitted.