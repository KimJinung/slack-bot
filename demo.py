import os
import logging

from slack_bot.slack_bot import SlackBot


def demo():
    bot = SlackBot(token=token)
    bot.post(
        channel="project",
        message="This is a test message"
    )


if __name__ == "__main__":
    token = os.environ["SLACK_BOT_TOKEN"]

    if not token:
        logging.error("Not found API token")
    else:
        demo()
