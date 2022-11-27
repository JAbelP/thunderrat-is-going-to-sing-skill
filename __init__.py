from mycroft import MycroftSkill, intent_file_handler


class ThunderratIsGoingToSing(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sing.to.going.is.thunderrat.intent')
    def handle_sing_to_going_is_thunderrat(self, message):
        self.speak_dialog('sing.to.going.is.thunderrat')


def create_skill():
    return ThunderratIsGoingToSing()

