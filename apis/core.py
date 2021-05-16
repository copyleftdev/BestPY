import os
class BestPyAPI(object):

    def __init__(self):
        """Initialize api key via environment variables"""
        try:
            self.api_key = os.getenv('BEST_BUY_API')
            if not self.api_key:
                print("You must have a environmental env setup  with a valid api key BEST_BUY_API=<api-key>")
            else:
                pass
        except:
            print("Something went wrong in the process of setting api key values.")

