from mycroft import MycroftSkill, intent_file_handler


class ComoEsta(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('esta.como.intent')
    def handle_esta_como(self, message):
        self.speak_dialog('esta.como')


def create_skill():
    return ComoEsta()

