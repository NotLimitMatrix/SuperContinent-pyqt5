import random, math

from player.block_manager import BlockManager
from player.panel_manager import PanelManager
from reference.functions import check_neighbour_has_player


class Player:
    def __init__(self, ident, name, color):
        self.name = name
        self.color = color
        self.ident = ident

        self.block_manager = BlockManager(self)
        self.panel_manaber = PanelManager(self)

    def select_position(self, world_list):
        while block := random.choice([b for b in world_list if b.attribute.status == 2]):
            if not check_neighbour_has_player(block, world_list):
                block.attribute.update(display=True)
                self.block_manager.add_block(block)
                break

    def __eq__(self, other):
        return other and self.ident == other.ident
