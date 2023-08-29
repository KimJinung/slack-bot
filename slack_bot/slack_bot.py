import logging

from slack import WebClient
from slack.errors import SlackApiError


class SlackBot:
    def __init__(self, token: str):
        self.token = token
        self.client = WebClient(token=self.token)

    def post(self, channel: str, message: str) -> None:
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=message
            )

            logging.info(response)

        except SlackApiError as e:
            logging.error(e)
