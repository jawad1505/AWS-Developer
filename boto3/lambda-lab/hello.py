
def handler(event, context):
	message = f'Hello {event["first_name"]} {event["last_name"]}!'
    print("hello version 2")
	return {'message': message, 'event': event}