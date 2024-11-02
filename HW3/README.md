HW3: This project shows how to insert a new row and show an error or Sucess messaage on the front end. It also shows how to present a data table with unique values from two tables.
## Quick Start
### Local Test Setup
Once you have downloaded the repository, cd into the folder.
You will need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```
### What can be done:
### '/api/update_basket_a'
From here, you are introduced to a simple Index page.<br>
You can input '/api/update_basket_a' to insert a new row (5,'Cherry') into table basket_a. If the value exists, it will show an error. If the process is able to be completed, it will display "Success!"<br>
### '/api/unique'
You can input '/api/unique' to display the unique fruits in basket_a and in basket_b in a **HTML table**.
If there are any errors, it will also be displayed.
