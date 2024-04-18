import os
import sys
from pathlib import Path
import requests
from dotenv import load_dotenv


def send_login_message(name, email):
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    load_dotenv()

    return requests.post(
        os.getenv('DOMAIN_LINK'),
        auth=("api", os.getenv("MAIL")),
        data={
            "from": "Fastr <postmaster@sandboxe2ef3b9809914ea682e3e9419d4daf58.mailgun.org>",
            "to": f"{name} <{email}>",
            "subject": f"Hello, {name}",
            "text": "New login attempt!"
        }
    )
