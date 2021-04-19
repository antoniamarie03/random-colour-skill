from mycroft import MycroftSkill, intent_file_handler


class RandomColour(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('colour.random.intent')
    def handle_colour_random(self, message):
        self.speak_dialog('colour.random')


def create_skill():
    return RandomColour()

