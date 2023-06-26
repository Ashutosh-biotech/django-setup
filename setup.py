import os
import sys
import time
import webbrowser
import math


def print_line(length: int):
    print("+" + ("-" * length) + "+")


def print_ray(end: bool = True):
    if end:
        print("|", end="")
    else:
        print("|")


class Create_table:
    def __init__(self, data: dict = None, name: str | None = None, desc: str | None = None):
        self.table_data = None
        self.header_length = None
        self.cols = None
        self.cols_name = None
        self.max_length = None
        self.rows = None
        self.rows_name = None
        self.name: str | None = name
        self.desc: str | None = desc
        self.data: dict = data

    def initialize(self):
        rows_name = self.data.get("rows_name")
        if rows_name:  # type: ignore
            self.rows_name = list(rows_name)  # type: ignore
            self.rows = len(self.rows_name)
            self.data.pop("rows_name")  # type: ignore
            data = {"": self.rows_name}
            keys = list(self.data.keys())
            for i in range(len(keys)):
                data[keys[i]] = self.data[keys[i]]
            self.data = data
        else:
            self.rows_name = []
            self.rows = len(max(self.data.values(), key=len))  # type: ignore
        self.max_length = []
        self.cols_name = list(self.data.keys())  # type: ignore
        self.cols = len(self.cols_name)

        for i in range(self.cols):
            self.max_length.append(0)
            for j in range(self.rows):
                if len(str(self.data[self.cols_name[i]][j])) > self.max_length[i]:  # type: ignore
                    self.max_length[i] = len(str(self.data[self.cols_name[i]][j]))  # type: ignore

        for i in range(self.cols):
            if len(self.cols_name[i]) > self.max_length[i]:
                self.max_length[i] = len(self.cols_name[i])

        self.header_length = 0
        for i in range(self.cols):
            self.header_length += self.max_length[i] + 1
        self.header_length -= 1

        self.table_data = []
        for i in range(self.rows):
            self.table_data.append([])
            for j in range(self.cols):
                self.table_data[i].append(self.data[self.cols_name[j]][i])  # type: ignore

    def display_cols(self):
        print_ray()
        for i in range(self.cols):
            print(str(self.cols_name[i]).center(self.max_length[i]), end="|")
        print()

    def print_body(self):
        print_line(self.header_length)
        self.display_cols()
        print_line(self.header_length)
        for i in range(self.rows):
            print_ray()
            for j in range(self.cols):
                print(str(self.table_data[i][j]).center(self.max_length[j]), end="|")
            print()
        print_line(self.header_length)
        self.display_cols()
        print_line(self.header_length)

    def header(self):
        if self.name:
            print_line(self.header_length)
            if len(str(self.name)) > self.header_length:
                bit_length = math.ceil(len(str(self.name)) / self.header_length)
                bit = math.ceil(len(str(self.name)) / bit_length)
                start = 0
                stop = bit
                for i in range(bit_length):
                    if stop > len(str(self.name)):
                        stop = len(str(self.name))
                    if start > len(str(self.name)):
                        break
                    print_ray()
                    print(str(self.name)[start:stop].center(self.header_length), end="")
                    print_ray(False)
                    start += bit
                    stop += bit
            else:
                print_ray()
                print(str(self.name).center(self.header_length), end="|")
                print()

    def footer(self):
        if self.desc:
            if len(str(self.desc)) > self.header_length:
                bit_length = math.ceil(len(str(self.desc)) / self.header_length)
                bit = math.ceil(len(str(self.desc)) / bit_length)
                start = 0
                stop = bit
                for i in range(bit_length):
                    if stop > len(str(self.desc)):
                        stop = len(str(self.desc))
                    if start > len(str(self.desc)):
                        break
                    print_ray()
                    print(str(self.desc)[start:stop].center(self.header_length), end="")
                    print_ray(False)
                    start += bit
                    stop += bit
            else:
                print_ray()
                print(str(self.desc).center(self.header_length), end="|")
                print()
            print_line(self.header_length)

    def draw_table(self):
        self.initialize()
        self.header()
        self.print_body()
        self.footer()
        print()


def server():
    ct = Create_table(data = {
        "option": [1, 2, 3, 4, 5, 6, 7, 8,9],
        "command": [
            "Start project",
            "Run server",
            "Start app",
            "Make migrations",
            "Migrate",
            "Create super user",
            "Collect static",
            "Shell",
		"exit"
        ]
    })
    ct.draw_table()
    exec(f'dj_cmd_{get_input(f"Choose any option from given options  ::  ")}()')


def get_input(input_name):
    key = input(input_name)
    return key


def dj_cmd_9():
	sys.exit()


def dj_cmd_8():
    if os.path.exists("manage.py"):
        if sys.platform == "win32":
            os.system("python manage.py shell")
            server()
        else:
            os.system("python3 manage.py shell")
            server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_():
    dj_cmd_1()


def dj_cmd_1():
    if os.path.exists("manage.py"):
        project = get_input('Enter your project name :: ')
        os.system(f"django-admin startproject {project}")
        server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_2():
    if os.path.exists("manage.py"):
        url = get_server_url()
        if sys.platform == "win32":
            webbrowser.open(f'http://{url}')
            print("Please Wait server is starting")
            os.system(f"python manage.py runserver {url}")
            server()
        else:
            webbrowser.open(f'http://{url}')
            print("Please Wait server is starting")
            os.system(f"python3 manage.py runserver {url}")
            server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_3():
    if os.path.exists("manage.py"):
        project = get_input('Enter your app name :: ')
        if sys.platform == "win32":
            os.system(f"python manage.py startapp {project}")
            server()
        else:
            os.system(f"python3 manage.py startapp {project}")
            server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_4():
    if os.path.exists("manage.py"):
        spe = get_input("Any specific App (y/n) :: ")
        if spe == "y":
            project = get_input('Enter your app name :: ')
            if sys.platform == "win32":
                os.system(f"python manage.py makemigrations {project}")
                server()
            else:
                os.system(f"python3 manage.py makemigrations {project}")
                server()
        else:
            if sys.platform == "win32":
                os.system("python manage.py makemigrations")
                server()
            else:
                os.system("python3 manage.py makemigrations")
                server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_5():
    if os.path.exists("manage.py"):
        if sys.platform == "win32":
            os.system("python manage.py migrate")
            server()
        else:
            os.system("python3 manage.py migrate")
            server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_6():
    if os.path.exists("manage.py"):
        if sys.platform == "win32":
            os.system("python manage.py createsuperuser")
            server()
        else:
            os.system("python3 manage.py createsuperuser")
            server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_7():
    if os.path.exists("manage.py"):
        if sys.platform == "win32":
            os.system("python manage.py collectstatic")
            server()
        else:
            os.system("python3 manage.py collectstatic")
            server()
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def get_server_url():
    url = "localhost"
    port = "8000"
    settings = open('dj.cfg', 'r')
    settings_data = settings.readlines()
    for i in settings_data:
        if 'SERVER_URL' in i:
            url = i[13:]

    SERVER_URL = eval(url)

    for i in settings_data:
        if 'SERVER_PORT' in i:
            port = i[13:]

    SERVER_PORT = eval(port)

    settings.close()
    if SERVER_URL is None:
        settings = open('dj.cfg', 'r')
        settings_data = settings.readlines()
        for i in settings_data:
            if 'SERVER_URL' in i:
                settings_data[settings_data.index(i)] = f'SERVER_URL = "127.0.0.1"\n'
                break

        for i in settings_data:
            if 'SERVER_PORT' in i:
                settings_data[settings_data.index(i)] = f'SERVER_PORT = "8000"\n'
                break

        settings.close()
        settings = open('dj.cfg', 'w')
        settings.writelines(settings_data)
        settings.close()
    else:
        pass

    return f"{SERVER_URL}:{SERVER_PORT}"


if __name__ == '__main__':
    server()
