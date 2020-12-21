class Door:
    def __init__(self):
        self.state = 'closed'

    @property
    def state(self):
        print('getting state...')
        return self._state

    @state.setter
    def state(self, value):
        print('setting state...')
        self._state = value

d = Door()
d.state('open')
