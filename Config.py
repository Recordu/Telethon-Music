import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "11672400"))
    API_HASH = os.environ.get("API_HASH", "147f3c57888e2950cffaa156e159afac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5857763110:AAGJGcCphKgxeA3o1-PJKb7JrtwDyM63rkM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKsBu0WXN8u_jsFIb-wS0yOT-GeUeNGGSJwAFe5N7WkvO3JdaKGQvzj7aJvbwdsP_PXzUTFW076OQYPVr-OJFxxhqsOyt47V4qli9r4eQ5VA594ZVhOCIoNXiWg_AxrlxEOEpyMs3kPcGMJ6VJPKvS6SGUmhdAYiKjRBmLSRLlZ8PKKa8CjRkEZgq76gXMVHcvlXuOXIpZufWdHNmQUUtYTmx0CDX1olhvK7SOUytCHg4ZWXIPgu5ETNrp7ygxhaGWsPdRcrYBdAfTADy8Jm_M1d28Z6fBqlzyQ_gAVmQLLI_XSI8clxeZA3OZWa2o_0QTqZb99wkDjpSB9vaGDO0mDpIA8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Badnam_Music4_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/b0a47e03104d4d9e56141.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/ed32571b1a18dd7c1bfb6.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "-812234036")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
