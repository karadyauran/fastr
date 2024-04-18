import os
import subprocess
from colorama import Fore, Style

signals = {
    'down_arrow': '\u2193',
    'check_mark': '\u2713',
    'cross_mark': '\u2717',
}

microservices = [
    'authentication',
    'user',
    'product',
    'cart',
    'order',
    'payment',
]


def exit_message(error: bool, msg: str, name: str) -> str:
    color = Fore.RED if not error else Fore.GREEN
    status = f'{signals['cross_mark']} FAILED' if not error else f'{signals['check_mark']} SUCCESS'
    style = Style.BRIGHT
    reset = Style.RESET_ALL
    return f'{color}{style}{status}:{reset} {msg} `{name}` {reset}'


def make_migrations(file) -> str:
    _ = subprocess.run(['python', 'manage.py', 'makemigrations', file])

    if _.returncode == 0:
        return exit_message(error=True, msg='Migration file created', name=file)

    else:
        exception = exit_message(error=False, msg='Not created migration', name=file)
        print(_.stderr)
        raise Exception(exception)


def migrate(microservice) -> str:
    _ = subprocess.run(['python', 'manage.py', 'migrate'], capture_output=True, text=True)

    if 'No migrations to apply.' in _.stdout or _.returncode == 0:
        return exit_message(error=True, msg='Migrated', name=microservice)
    else:
        exception = exit_message(error=False, msg='Not migrated', name=microservice)
        print(_.stderr)
        raise Exception(exception)


def main():
    os.chdir('..')

    for microservice in microservices:
        os.chdir(microservice)

        print(Fore.YELLOW + signals['down_arrow'] + f' {microservice.capitalize()} service' + Style.RESET_ALL)
        files = os.listdir()

        for file in files:
            if 'app' in file:
                print(make_migrations(file))

        print(migrate(microservice))

        os.chdir('..')


if __name__ == '__main__':
    main()
