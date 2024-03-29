from reference import dictionary, templates, functions
from reference.gui import GUI_KEY, NUMBER, SIZE
from unit.block import Block
from unit.zoning import Zoning


class Memory:
    def __init__(self, player, world_number):
        self.world_number = world_number
        self.world_size = SIZE.WORLD_WIDTH // world_number
        self.world_data = [
            Block(i, *functions.ident_to_row_col(i, world_number), self.world_size, world_number)
            for i in range(world_number * world_number)
        ]

        self.player = player
        self.is_observing = False

        self.zoning_number = NUMBER.ZONING_NUMBER
        self.zoning_width = SIZE.ZONING_WIDTH
        self.zoning_data = list()
        self.zoning_display = [Zoning(0, 0, 0, self.zoning_width, -1)]

        self.init_zoning()

        self.msg = ''
        self.filter_type = dictionary.F_DEFAULT

    def init_zoning(self):
        n = 0
        for block in self.world_data:
            size = self.zoning_width // block.z_num
            z_number = block.z_num * block.z_num
            z_list = (Zoning(n + i, *functions.ident_to_row_col(i, block.z_num), size, block.ident)
                      for i in range(z_number))
            block.add_zoning(z_list)
            n += z_number

    def update_block(self, block_id):
        block = self.world_data[block_id]
        if block.attribute.display:
            self.zoning_number = block.z_num
            self.zoning_display = block.z_set

    def command_observing(self):
        print(self.is_observing)
        for block in self.world_data:
            block.attribute.display = True if self.is_observing or block.player == self.player else False

    def dump(self):
        return {
            'GUI': {
                GUI_KEY.WORLD: self.world_data,
                GUI_KEY.ZONING: {
                    'number': self.zoning_number,
                    'data': self.zoning_display
                },
                GUI_KEY.PANEL: [
                    (0, 10),  # dictionary.FOOD:
                    (0, 10),  # dictionary.MINERAL:
                    (0, 10),  # dictionary.ENERGY:
                    (0, 10),  # dictionary.COMMODITY:
                    (0, 10),  # dictionary.ALLOY:
                    10,  # dictionary.POPULATION:
                    10,  # dictionary.CIVIL:
                    10,  # dictionary.MILITARY:
                    10  # dictionary.TECHNOLOGY:
                ],
                GUI_KEY.TECHNOLOGY: [
                    ('矿产探测', 2301, 5689),  # dictionary.CIVIL:
                    ('蓝色激光', 36987, 4321),  # dictionary.MILITARY:
                    ('进化破译', 9568, 10248),  # dictionary.HYPER:

                ],
                GUI_KEY.SELECT: [i for i in range(6)],
                GUI_KEY.TEXT_BROWSER: self.msg,
                GUI_KEY.OTHER: {
                    'more_point': 0
                }
            }
        }


if __name__ == '__main__':
    memory = Memory()
    for block in memory.world_data:
        print(f"{block.ident}: Row: {block.row}, Col: {block.col}")
