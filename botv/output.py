class Output:

    def __repr__(self):
        return self.__body


    def __init__(self, response=None):
        self.__response= response
        self.__quickReplies = []
        self.__templates= []
        self.__entities = dict()
        self.__output = dict(
                response=self.__response,
                quickReplies=self.__quickReplies,
                templates=self.__templates
                )
        self.__body = dict(
                output = self.__output,
                entities = self.__entities
                )
    @property
    def body(self):
        return self.__body

    @property
    def entities(self):
        return self.__entities

    @property
    def quickReplies(self):
        return self.__quickReplies

    @property
    def templates(self):
        return self.__templates


    def add_entity(self, **kwgs):
        for key,value in kwgs.items():
            self.__entities[key] = value
        return self.__body

    def add_response(self, response):
        self.__output['response'] = response
        return self.__body

    def add_qr(self, quick_replies=None):
        keys = ['targetIntent', 'text', 'title', 'type']
        for key in keys:
            for quick_reply in quick_replies:
                if key not in quick_reply:
                    raise ValueError('Quick Reply should have these keys : targetIntent, text, title, type')
        self.__quickReplies.extend(quick_replies)
        return self.__body

    def add_template(self, templates=None):
        keys = ['action_url', 'image_url', 'subtitle', 'title']
        for key in keys:
            for template in templates:
                if key not in template:
                    raise ValueError('Facebook template should have these keys : action_url, image_url, subtitle, title')
        self.__templates.extend(templates)
        return self.__body



