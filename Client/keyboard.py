from inputs import get_key


"""Just print out some event infomation when keys are pressed."""
while 1:
    events = get_key()
    if events:
        for event in events:
            print(event.ev_type, event.code, event.state)

