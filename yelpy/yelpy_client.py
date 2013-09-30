from yelpy_signer import YelpySigner


class YelpyClient(object):

    def __init__(self, consumer_key=None, consumer_secret=None, token=None, token_secret=None):
        super(YelpyClient, self).__init__()
        self.signer = YelpySigner(consumer_key, consumer_secret, token, token_secret)
    
    def search(self, term=None, limit=None, offset=None, sort=None, category_filter=None, radius_filter=None, deals_filter=None, cc=None, lang=None, lang_filter=None):
        pass

    def business(self):
        pass
