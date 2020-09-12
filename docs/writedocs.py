import os

for file_ in os.listdir("C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment\\PythonQuickStartModule\\src"):
    if file_.endswith(".py"):
        os.system("python -m pdoc --html --force C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment\\PythonQuickStartModule\\src\\{} -o C:\\Users\\cobyl\\Documents\\Coding\\MicrosoftCode\\ActualDevelopment\\PythonQuickStartModule\\docs".format(file_))