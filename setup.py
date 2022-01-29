import os
import sys
import time
import colorama
import webbrowser

colorama.init()

def print_line(length):
    print(colorama.Fore.RED + '+', end='')
    print(colorama.Fore.RED + '-' * length, end='')
    print(colorama.Fore.RED + '+')


def print_plus(end=True):
    if end:
        print(colorama.Fore.RED + '+', end='')
    else:
        print(colorama.Fore.RED + '+')


def print_ray(end=True):
    if end:
        print(colorama.Fore.RED + '|', end='')
    else:
        print(colorama.Fore.RED + '|')


class Create_table():

    def __init__(self, rows=0, cols=0, data=[], cols_name=[], rows_name=[], name="Django Setup", footer=None, header=True):
        self.name = name
        self.rows = rows
        self.rows_name = rows_name
        self.cols = cols
        self.cols_name = cols_name
        self.data = data
        self.max_length = 0
        self.footer = footer
        self.header = header
        self.header_length = 0

    def initialize(self):
        self.max_length = 0
        for i in self.data:
            if len(i) > self.max_length:
                self.max_length = len(i)

        if self.header:
            if len(self.name) > self.max_length:
                self.max_length = len(self.name)
        
        if self.footer:
            if len(self.footer) > self.max_length:
                self.max_length = len(self.footer)

        self.max_length += 2
        if len(self.rows_name) >= 1:
            self.header_length = int((((self.cols * self.max_length)/2)+(self.cols * self.max_length)) + (self.cols))
        else:
            self.header_length = (self.cols * self.max_length) + (self.cols - 1)

    def print_table(self):
        self.initialize()
        self.print_header()
        if self.cols_name != []:
            self.print_column_name()
        print_line(self.header_length)
        self.print_data()
        self.print_footer()
        print()

    def print_header(self):
        if self.header:
            print_line(self.header_length)
            print_ray()
            print(colorama.Fore.GREEN + '{:^{}}'.format(self.name, self.header_length), end='')
            print_ray(end=False)

        print_line(self.header_length)

    def print_column_name(self):
        if self.rows_name != []:
            print_ray()
            print(colorama.Fore.GREEN + '{:^{}}'.format('', self.max_length), end='')
        for i in range(self.cols):
            if self.cols_name[i] != '':
                print_ray()
                print(colorama.Fore.BLACK + '{:^{}}'.format(self.cols_name[i], self.max_length), end='')
            else:
                print(colorama.Fore.BLACK + '{:^{}}'.format('', self.max_length), end='')
        
        print_ray(end=False)

    def print_data(self):
        data = self.get_data()
        for i in range(len(data)):
            if len(self.rows_name) >= 1:
                print_ray()
                print(colorama.Fore.GREEN + '{:^{}}'.format(self.rows_name[i], self.max_length), end='')
            
            for j in range(self.cols):
                if self.data[data[i][j]] != '':
                    print_ray()
                    print(colorama.Fore.WHITE + '{:^{}}'.format(str(self.data[data[i][j]]), self.max_length), end='')
                else:
                    print_ray()
                    print(colorama.Fore.WHITE + '{:^{}}'.format('', self.max_length), end='')

            
            print_ray(end=False)

    def print_footer(self):
        if self.footer:
            print_line(self.header_length)
            print_ray()
            print(colorama.Fore.GREEN + '{:^{}}'.format(self.footer, self.header_length), end='')
            print_ray(end=False)
        
        print_line(self.header_length)

    def get_data(self):
        __data__ = []
        data_key = []
        dt = []
        if len(self.data) == self.rows*self.cols:
            for i in range(len(self.data)):
                data_key.append(i)
            
            for i in range(self.rows):
                for j in range(self.cols):
                    dt.append(data_key[j])
                __data__.append(dt)
                dt = []
                try:
                    data_key.pop(0)
                    data_key.pop(0)
                except:
                    pass

            return __data__
        else:
            print("Error: Data is not equal to rows*cols")
            time.sleep(3)
            sys.exit()


def server():
    dj_cmd = [
        "1",
        "Startproject",
        "2",
        "Runserver",
        "3",
        "Startapp",
        "4",
        "Makemigrations",
        "5",
        "Migrate",
        "6",
        "Createsuperuser",
        "7",
        "Collectstatic",
    ]

    ct = Create_table()
    ct.rows = int(len(dj_cmd)/2)
    ct.cols = 2
    ct.cols_name = ["Command", "Status"]
    ct.rows_name = [" * ", " ", " * ", " * ", " ", " ** ", " "]
    ct.data = dj_cmd
    ct.footer = "Default input 1 (if no input)"
    ct.initialize()
    ct.print_table()
    exec(f'dj_cmd_{get_input(f"Choose any option from given { int(len(dj_cmd)/2) } options  ::  ")}()')


def get_input(input_name):
    key = input(colorama.Fore.LIGHTBLUE_EX + input_name + colorama.Fore.LIGHTCYAN_EX)
    return key


def dj_cmd_():
    dj_cmd_1()


def dj_cmd_1():
    if os.path.exists("manage.py"):
        project = get_input('Enter your project name :: ')
        os.system(f"django-admin startproject {project}")
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_2():
    if os.path.exists("manage.py"):
        server = get_server_url()
        if sys.platform == "win32":
            webbrowser.open(f'http://{server}')
            print("Please Wait server is starting")
            os.system(f"python manage.py runserver {server}")
        else:
            webbrowser.open(f'http://{server}')
            print("Please Wait server is starting")
            os.system(f"python3 manage.py runserver {server}")
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_3():
    if os.path.exists("manage.py"):
        project = get_input('Enter your app name :: ')
        if sys.platform == "win32":
            os.system(f"python manage.py startapp {project}")
        else:
            os.system(f"python3 manage.py startapp {project}")
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
            else:
                os.system(f"python3 manage.py makemigrations {project}")
        else:
            if sys.platform == "win32":
                os.system("python manage.py makemigrations")
            else:
                os.system("python3 manage.py makemigrations")
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_5():
    if os.path.exists("manage.py"):
        if sys.platform == "win32":
            os.system("python manage.py migrate")
        else:
            os.system("python3 manage.py migrate")
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_6():
    if os.path.exists("manage.py"):
        if sys.platform == "win32":
            os.system("python manage.py createsuperuser")
        else:
            os.system("python3 manage.py createsuperuser")
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def dj_cmd_7():
    if os.path.exists("manage.py"):
        if sys.platform == "win32":
            os.system("python manage.py collectstatic")
        else:
            os.system("python3 manage.py collectstatic")
    else:
        print("Error: manage.py not found")
        time.sleep(3)
        sys.exit()


def virtual_env():
    settings = open('dj.cfg', 'r')
    settings_data = settings.readlines()
    for i in settings_data:
        if 'VIRTUAL_ENV' in i:
            env = i[14:]
            
    VIRTUAL_ENV = eval(env)
    settings.close()
    if VIRTUAL_ENV == None:
        vct = Create_table()
        vct.rows = 1
        vct.cols = 1
        vct.cols_name = []
        vct.rows_name = []
        vct.data = ["You are not in virtual environment"]
        vct.print_table()

        venv = get_input("Due you have virtual environment (y/n) :: ")
        if venv == 'y':
            VIRTUAL_ENV = get_input("Enter the name of virtual environment :: ")
            settings = open('dj.cfg', 'r')
            settings_data = settings.readlines()
            for i in settings_data:
                if 'VIRTUAL_ENV' in i:
                    settings_data[settings_data.index(i)] = f'VIRTUAL_ENV = "{VIRTUAL_ENV}"\n'
                    break
            settings.close()
            settings = open('dj.cfg', 'w')
            settings.writelines(settings_data)
            settings.close()

            if sys.platform == 'win32':
                os.system(f'{VIRTUAL_ENV}\\Scripts\\activate')
            else:
                os.system(f'. {VIRTUAL_ENV}/bin/activate')

        else:
            wgy = get_input("Do you want to create virtual environment (y/n) :: ")
            if wgy == 'y':
                VIRTUAL_ENV = get_input("Enter the name of virtual environment :: ")
                if sys.platform == 'win32':
                    os.system('pip install virtualenv')
                    os.system(f'virtualenv {VIRTUAL_ENV}')
                else:
                    os.system('pip3 install virtualenv')
                    os.system('virtualenv {VIRTUAL_ENV}')
                settings = open('dj.cfg', 'r')
                settings_data = settings.readlines()
                for i in settings_data:
                    if 'VIRTUAL_ENV' in i:
                        settings_data[settings_data.index(i)] = f'VIRTUAL_ENV = {VIRTUAL_ENV}'
                        break
                settings.close()
                settings = open('dj.cfg', 'w')
                settings.writelines(settings_data)
                settings.close()

                if sys.platform == 'win32':
                    os.system(f'{VIRTUAL_ENV}\\Scripts\\activate')
                else:
                    os.system(f'. {VIRTUAL_ENV}/bin/activate')
    else:
        if sys.platform == 'win32':
            os.system(f'{VIRTUAL_ENV}\\Scripts\\activate')
        else:
            os.system(f'. {VIRTUAL_ENV}/bin/activate')


def get_server_url():
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
    if SERVER_URL == None:
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
    virtual_env()
    server()
