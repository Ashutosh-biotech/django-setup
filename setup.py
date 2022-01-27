import os
import sys
import time
import colorama

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
                print(colorama.Fore.YELLOW + '{:^{}}'.format(self.cols_name[i], self.max_length), end='')
            else:
                print(colorama.Fore.YELLOW + '{:^{}}'.format('', self.max_length), end='')
        
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
    ct.rows_name = [" * ", " ", " * ", " * ", " * ", " ** ", " "]
    ct.data = dj_cmd
    ct.footer = "Default input 1 (if no input)"
    ct.initialize()
    ct.print_table()
    request(get_input(f"Choose any option from given { int(len(dj_cmd)/2) } options  ::  "), ct.data)


def get_input(input_name):
    key = input(colorama.Fore.LIGHTBLUE_EX + input_name + colorama.Fore.LIGHTCYAN_EX)
    return key


def request(request, data):
    for i in range(len(data)):
        if i % 2 == 0:
            if int(data[i]) == int(request):
                exec(f'dj_cmd_{request}()')


def dj_cmd_1():
    get_settings()


def get_settings():
    manage = open('manage.py', 'r')
    mgr = manage.readlines()
    var = ""
    record = False
    for i in mgr:
        if "os.environ.setdefault('DJANGO_SETTINGS_MODULE'," in i:
            for j in i:
                if ',' in j:
                    record = True
                if '.' in j:
                    record = False
                if record:
                    var += j

    print(var[3:])


def update_settings():
    setting = open('dj.cfg', 'r')


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
                settings_data[settings_data.index(i)] = f'VIRTUAL_ENV = {VIRTUAL_ENV}'
                break
        settings.close()
        settings = open('dj.cfg', 'w')
        settings.writelines(settings_data)
        settings.close()

        os.system('')


if __name__ == '__main__':
    virtual_env()
    server()
