from Core import KEY

TIME_FLOW = 'time_flow'
RESOURCES = 'resources_list'
POWERS = 'power_list'
WAIT_SELECT_ITEMS = 'wait_select_items'
WAIT_ITEMS_TYPE = 'type'
WAIT_ITEMS_OPTIONS = 'options'
RESEARCHER_ITEMS = 'researcher_items'
DETAIL_TEXT = 'detail_text'

WAIT_SELECT_ITEM_TEMPLATE = {
    WAIT_ITEMS_TYPE: None,
    WAIT_ITEMS_OPTIONS: None
}

RESEARCHER_ITEM_TEMPLATE = {
    KEY.MILITARY: (None, None),
    KEY.CIVIL: (None, None),
    KEY.BEYOND: (None, None)
}

MESSAGE_TEMPLATE = {
    TIME_FLOW: 1,
    RESOURCES: None,
    POWERS: None,
    WAIT_SELECT_ITEMS: WAIT_SELECT_ITEM_TEMPLATE,
    RESEARCHER_ITEMS: RESEARCHER_ITEM_TEMPLATE,
    DETAIL_TEXT: None
}