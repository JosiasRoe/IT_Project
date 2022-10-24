from discord import Webhook
import aiohttp

async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/1032290823385120768/BqpAWBtz4_jd86lYub8Xn236YOqiPf6Pp3U6jkbsiL-mv_Eux4YQGT5o-3-xN-4zIUo7', session=session)
        await webhook.send('Hello World', username='Foo')