class Item :
    def __init__(self):
        self.title = ""
        self.link = ""
        self.description = ""
        self.owner = None
    def set_title(title):
        self.title = title
    def set_link(link):
        self.link = link
    def set_description(description):
        self.description = description
    def set_description(owner):
        if isinstance(owner, User):
            self.owner = owner