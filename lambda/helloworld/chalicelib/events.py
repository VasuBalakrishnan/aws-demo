from chalice import app, Blueprint, Cron, Rate

myevents = app.Blueprint(__name__)

# @myevents.schedule('rate(5 seconds)')
# @myevents.schedule(Rate(1, unit=Rate.MINUTES))
@myevents.schedule('cron(*/1 * * * ? *)')
def cron(event):
    myevents.current_app.log.debug(event.to_dict())
    pass


# @myevents.on_sns_message('MyTopic')
# def handle_sns_message(event):
#     pass