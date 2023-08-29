# slack-bot

## Create your slack App
Docs - https://api.slack.com/apps

## Add os environment variable
```bash
export SLACK_BOT_TOKEN="Your Token"
```

## Invite your bot to the channel


## Demo
```python
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
```

