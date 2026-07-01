import enum

class State(enum.Enum):
    Initialize = 0,
    Event1 = 1,
    Event2 = 2,
    Event3 = 3,
    Finalize = 4

class StateMachine:
    def __init__(self):
        self.state = State.Initialize

    def process(self):
        if self.state == State.Initialize:
            self.state = State.Event1
        elif self.state == State.Event1:
            self.state = State.Event2
        elif self.state == State.Event2:
            self.state = State.Event3
        elif self.state == State.Event3:
            self.state = State.Finalize
        elif self.state == State.Finalize:
            self.state = State.Initialize