from sources import Helper


class Handler(Helper):
    def __init__(self):
        self.list_urls = ['https://www.ebay.com/sch/i.html_from=R40&_nkw=&_sacat=0&_pgn=1']
        self.list_objects = ['electronics']
    
    def create_new_link(self,
                        device,
                        type_of_object):
    
        str_device = str(device)
        str_type_of_object = str(type_of_object)

        new_link = self.list_urls[0]
        prevous_data_index = new_link.index("nkw=")

