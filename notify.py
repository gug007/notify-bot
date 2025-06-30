#!/usr/bin/env python3

import datetime
import os
import sys
from typing import Final

import requests
from dotenv import load_dotenv

load_dotenv()

MESSAGES: Final[dict[str, str]] = {
    "Monday": "Happy Monday! 💡 Start your week strong!",
    "Tuesday": "Terrific Tuesday! 🚀 Keep the momentum going.",
    "Wednesday": "Wonderful Wednesday! 🏃 You are halfway there.",
    "Thursday": "Thriving Thursday! 🌟 The weekend is near.",
    "Friday": "Fantastic Friday! 🎉 Finish the week on a high note.",
    "Saturday": "Superb Saturday! 😎 Enjoy your weekend.",
    "Sunday": "Serene Sunday! 🛌 Rest and recharge.",
}

def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token:
        sys.exit("Error: TELEGRAM_BOT_TOKEN environment variable not set.")
    if not chat_id:
        sys.exit("Error: TELEGRAM_CHAT_ID environment variable not set.")

    today_name = datetime.datetime.now(datetime.UTC).strftime("%A")
    message = MESSAGES.get(today_name, f"Hello! Today is {today_name}.")

    text_url = f"https://api.telegram.org/bot{token}/sendMessage"
    text_payload = {"chat_id": chat_id, "text": message}
    response = requests.post(text_url, data=text_payload)

    if response.ok:
        print(f"Sent message for {today_name}: {message}")
    else:
        print(
            f"Failed to send message — status {response.status_code}: {response.text}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
