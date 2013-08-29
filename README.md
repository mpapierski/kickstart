kickstart
===

Kickstart your next C++ application.

# What?

You spend too much time writing boilerplate on your next application. Save your time and use this tool. Stop writing boilerplate code. Start writing your next application.


# Usage

Commands are executed in order of existence.

## --init [name]
	
Initialize project with `name`. This will create new directory and there will be stored all boilerplate code for you.

## --flavor [app/lib]

By default it is set to `app`. Library or executable.

## --buildsystem [type]

Valid options are: `cmake`.

### cmake

Generates all boilerplate code needed to build your next application from source. The project is named after the --init option. Target is also named after the project.

### gyp

TODO

#### unix makefiles

TODO

## --tests [library]

Optional. You want to specify this option. Adds `tests/` directory with `CMakeLists.txt` included.

### gtest

Use `gtest` by default for your tests.

### boost.test

Use `boost.test` by default for your tests.

## --add-test [name]

Creates minimal boilerplate code for your test named `name`. This will update file `tests/CMakeLists.txt`. 

## --require [package, package, ...]

Find packages. Adds `find_package` to your `CMakeLists.txt`. This will also add `include_directories` and `target_link_libraries`.

# TODO

- Implement all these options.
- Support for `gyp`.

# License

See `LICENSE`.

# Authors

* Michał Papierski <michal@papierski.net>
