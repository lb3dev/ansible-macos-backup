class FilterModule(object):

    def filters(self):
        return {
            'restic_status': self.restic_status
        }

    def restic_status(self, value):
        return value['action'] + ': ' + value['item']
