# Android App - Automation using Python & Appium

This project aims to demonstrate a simple automation solution using
a page object model, which has been a staple to many-a web app testing 
strategies, at it's core as a framework design.

In this project, Pages are replaced by screens as objects.

## Tools of the trade
 * python 3.7.x
 * appium client for python
 * appium desktop client to run a local server
 * android studio for emulator use
 * nose2 (test runner and reporter)
 * unittest (xUnit framework for implementing tests)

## Running Tests

Before running the tests, you may need to install `python 3.7.x` on
your machine. The simplest way for macs is to use homebrew.
`brew install python`
This install `pip` the package installer along with python. Once done
you can check the installation by typing `python --version` in the
terminal.
Additionally, i prefer to alias `python3 as python` which can be done
in your `bash profile` or `.zshrc` files. All python commands mentioned
below take advantage of that alias setting.

It is important to create an emulator device in android studio.
A sample config used in this project is: 
`Pixel 2 XL API 23 Marshmellow`

To run the tests, you can follow the steps in order:  

Move to the repo
`cd web_app`

Activate virtual env
`source venv/bin/activate`

Install package dependencies for the project
`pip install requirements.txt`

To run all tests: 
`nose2 -v --html-report`

To run an individual test: 
`nose2 -v tests.test_app_login --html-report`

To deactivate virtualenv
`deactivate`

## Viewing Reports
You can view reports at: `/reports` within the repo. The reports are
in HTML format and can be viewed in any browser of choice.

## Design Decisions
The overall design of the android app automation code follows the principle
of Page Object Model. 
The tests call on action methods which in turn use element locators
to do specific tasks of replicating app flows.

The project code is split across multiple packages (or folders), each
segregated to better isolate their functioning.

The core folders are listed below with a brief summary:

* `apk`: The apk is stored here and referenced for use.
 * `element_locators`: This package is for storing element locators which
 are separated based on the pages the elements are present in.
 * `report`: This package stores the last run report in HTML format.
 * `screen_objects`: This package is for storing action methods which can be
 performed on the elements in the app view.
 * `setup`: The package has most of the setup and configurations to 
 make the project run.
 * `test_data`: This package can be used to store relevant test data
 or information which can be used across multiple tests.
 * `test`: This package holds all the tests. Each test script can hold
 a set of tests, mostly grouped by screen level actions.
 * `venv`: This is the virtual environment set up package. The isolated
 python packages (3rd party python packages) are set up here. This 
 ensures the entire code repo has only project specific packages which
 do not impact system wide packages thereby creating a good buffer of
 need based packages per project.
 * Additional Files:
    * `nose2.cfg`: This config file allows us to set up nose2 cmd line
    runner. It let's us export reports in HTML format.
    * `requirements.txt`: It keeps a simple copy of external python 
    packages or dependencies required to run the tests. It works well
    with `pip`, the python package manager to setup the dependencies.
    
## Additional Design Decisions:

This project demonstrates the base page as a super class where all the
other classes inherit from it.

Future improvements to this particular code can come in the form of
removing test data and using factory methods to generate data seeding.

Also, as the project can grow in tests and scale, we can incorporate
a steady mix of multi-app version testing by adding configs to ensure 
we cover more flows and real world scenario emulation based on devices
available to the users in the market.

## Reasons for picking the tech stack:
 * Python: 
    * less boilerplate code
    * repl advantage
    * duck typing
    * easy of reading the code
    * robust & active dev community
    * familiarity with the language
 
 * appium:
    * standard api with selenium
    * mature framework
    * flexible across iOS & android automation
    * active community
    * multiple language bindings (python, ruby, javascript, java etc.)
    * flexibility to pick test framework based on language binding
    * open source
    
 * unittest:
    * bundled within python language as a lib
    * similar to other *Unit frameworks
    * flexible and easy to setup and use
 
 * nose2
    * extends unittest capability
    * test discovery
    * better html reporting

 