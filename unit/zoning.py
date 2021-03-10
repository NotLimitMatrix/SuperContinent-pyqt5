class Zoning:
    def __init__(self, ident, belong):
        self.id = ident

        self.build = 0
        self.belong = belong

    def get_xy(self, dx):
        return divmod(self.id, dx)

    def dump(self):
        return {
            'build': self.build,
            'belong': self.belong
        }

    @staticmethod
    def collect(zoning_list):
        return {str(zoning.id): zoning.dump() for zoning in zoning_list}
