from unit.block import Block


class BlockManager:
    def __init__(self, parent):
        self.parent = parent
        self.block_set = set()

    def add_block(self, block):
        block.player = self.parent
        self.block_set.add(block)

    def get_block(self, block_id):
        for block in self.block_set:
            if block.ident == block_id:
                return block
        return None

    def del_block(self, block_id):
        self.block_set.remove(self.get_block(block_id))

    def update(self, block_id, **kwargs):
        block = self.get_block(block_id)
        block.attribute.update(**kwargs)
