import random

from player.block_manager import BlockManager


class Player:
    def __init__(self, ident, name, color):
        self.name = name
        self.color = color
        self.ident = ident

        self.block_manager = BlockManager(self)

    def init_player(self, world_list):
        selected_block = random.choice([b for b in world_list if b.attribute.status == 2])
        self.block_manager.add_block(selected_block)
        selected_block.attribute.update(display=True)

    def __eq__(self, other):
        return other and self.ident == other.ident
