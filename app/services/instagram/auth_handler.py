from ..handlers.structures import AbstractHandler

class InstragramHanders(AbstractHandler):

    def __init__(self):
        self.client_id = settings.INSTAGRAM_CLIENT_ID
        self.client_secret = settings.INSTAGRAM_CLIENT_SECRET
        self.base_auth_url = 'https://api.instagram.com/oauth/authorize'
        self.token_url = 'https://api.instagram.com/oauth/access_token'

        # Dynamically get redirect URI
        self.redirect_uri = self._get_redirect_uri()
