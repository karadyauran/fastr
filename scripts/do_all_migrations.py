import os
import subprocess
from colorama import Fore, Style

down_arrow = '\u2193'
check_mark = '\u2713'
cross_mark = '\u2717'

microservices = [
    'authentication',
    'user',
    'product',
    'cart',
    'order',
    'payment',
    'notification'
]


def success_exit(msg, name) -> None:
    print(Style.BRIGHT + Fore.GREEN + check_mark + ' Success ' + Style.RESET_ALL + f'{msg} {name}' + Style.RESET_ALL)


def fail_exit(msg, name) -> None:
    print(Style.BRIGHT + Fore.RED + cross_mark + ' Failed ' + Style.RESET_ALL + f'{msg} `{name}`' + Style.RESET_ALL)


def make_migrations(file) -> bool:
    if file not in ['config', 'manage.py', 'db.sqlite3', '__pycache__']:
        _ = subprocess.run(['python', 'manage.py', 'makemigrations', file])

        if _.returncode == 0:
            success_exit('to make migrations', file)

        else:
            fail_exit('to make migrations', file)
            raise NameError(Style.BRIGHT + Fore.RED + 'Fail to make migrations' + Style.RESET_ALL)

        return True


def migrate(microservice) -> bool:
    _ = subprocess.run(['python', 'manage.py', 'migrate'], capture_output=True, text=True)

    if 'No migrations to apply.' in _.stdout or _.returncode == 0:
        success_exit('to migrate', microservice)
    else:
        fail_exit('to migrate', microservice)
        raise Exception(_.stderr)

    return True


def main():
    os.chdir('..')

    for microservice in microservices:
        os.chdir(microservice)

        print(Fore.YELLOW + down_arrow + f' {microservice.capitalize()} service' + Style.RESET_ALL)
        files = os.listdir()

        for file in files:
            make_migrations(file)

        migrate(microservice)

        os.chdir('..')


if __name__ == '__main__':
    main()
