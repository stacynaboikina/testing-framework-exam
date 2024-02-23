# Wikipedia tests quest

This repository contains automated frontend tests for wikipedia. 
Your task is to automate test cases given by your trainer and contribute them here.

### What you have to do:
1. Ask the trainer what test case(s) you need to implement. You are not limited by them, you can add more if you want.
2. Clone this repository.
3. Create a new branch. Please, name it according to what you are going to do. For example: `auto-tests-for-wiki-home`.
4. Open the cloned project in PyCharm. Please, open "testing-framework-exam" folder, not the folder above.
5. Create virtual environment if needed (if PyCharm doesn't create it for you).
6. Install dependencies from requirements.txt.
7. Run the tests (using PyCharm, or in terminal just run: `pytest`).
8. Now you're all set to start making the technical tasks. If you see any issues with the initial setup, please,
contact your trainer, but first try to fix them yourself.
9. YOU DO NOT NEED to update env_configuration.json, it's already configured.
10. Please, create your test file(s) in tests folder. You can create sub-folders if needed as well. 
11. You might need to create a new page object, do not hesitate to do so ;) If you see a need to update an existing 
page object, it's also ok. Don't forget to add your page object to `Pages` class in `frontend/pages.py` - this will
make them available in pages fixture in the tests. 
12. You can put all of your fixtures into `tests/conftest.py`, but please remember that other people also work on
this repo and your fixtures might affect other tests. 
13. When you finish - commit and push your code. 
14. Create a pull request. 
15. Notify your trainer to review the code.

Good luck! :) 
