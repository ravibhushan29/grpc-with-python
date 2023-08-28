class Error(ValueError):
    def __init__(self, field, reason):
        super(Error, self).__init__(f'{field}:{reason}')
        self.field = field
        self.reason = reason

def start_request(request):
    if not request.driver_id:
        raise Error('driver_id', 'empty')
    #todo more field validation