from Routes.route_master import bot
import dotenv
import os

dotenv.load_dotenv(verbose=True, override=True)
TOKEN = os.getenv("API_KEY")
bot.run(TOKEN)
