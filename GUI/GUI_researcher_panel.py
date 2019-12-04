from GUI.Panel import OneResearchPanel
from GUI import CONST, KEY


class ResearcherPanel:
    def __init__(self, parent):
        r_military = OneResearchPanel(parent)
        r_military.init_label(CONST.RESEARCH_LABEL_START_X, CONST.RESEARCH_LABEL_START_Y)
        r_military.init_rate_button(CONST.RESEARCH_RATE_BUTTON_START_X, CONST.RESEARCH_RATE_BUTTON_START_Y)
        r_military.rate_button.setText('3')
        r_military.init_transform_button(CONST.RESEARCH_TRANSFORM_START_X, CONST.RESEARCH_TRANSFORM_START_Y)

        r_civil = OneResearchPanel(parent)
        r_civil.init_label(CONST.RESEARCH_LABEL_START_X, CONST.RESEARCH_LABEL_START_Y + 20)
        r_civil.init_rate_button(CONST.RESEARCH_RATE_BUTTON_START_X, CONST.RESEARCH_RATE_BUTTON_START_Y + 20)
        r_civil.rate_button.setText('3')
        r_civil.init_transform_button(CONST.RESEARCH_TRANSFORM_START_X, CONST.RESEARCH_TRANSFORM_START_Y + 20)

        r_beyond = OneResearchPanel(parent)
        r_beyond.init_label(CONST.RESEARCH_LABEL_START_X, CONST.RESEARCH_LABEL_START_Y + 40)
        r_beyond.init_rate_button(CONST.RESEARCH_RATE_BUTTON_START_X, CONST.RESEARCH_RATE_BUTTON_START_Y + 40)
        r_beyond.rate_button.setText('4')
        r_beyond.init_transform_button(CONST.RESEARCH_TRANSFORM_START_X, CONST.RESEARCH_TRANSFORM_START_Y + 40)

        self.military = r_military
        self.civil = r_civil
        self.beyond = r_beyond

        self.researcher_items = {
            KEY.MILITARY: (None, None),
            KEY.CIVIL: (None, None),
            KEY.BEYOND: (None, None)
        }

    def check_items(self, items):
        if items:
            self.researcher_items = items
        else:
            self.researcher_items = {
                KEY.MILITARY: (None, None),
                KEY.CIVIL: (None, None),
                KEY.BEYOND: (None, None)
            }

    def update(self, items):
        self.check_items(items)

        self.military.display(items.get(KEY.MILITARY))
        self.civil.display(items.get(KEY.CIVIL))
        self.beyond.display(items.get(KEY.BEYOND))
