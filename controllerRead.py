import inputs

def main():
    while True:
        events = inputs.get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)

if __name__ == "__main__":
    main()
