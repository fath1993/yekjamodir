import jdatetime

from accounts.models import Profile
from calendar_event.models import EventRemind
from utilities.send_sms import SendSMSWithPatternThread


def event_reminder():
    now = jdatetime.datetime.now()
    now_plus_one_minute = now + jdatetime.timedelta(minutes=1)
    print('event remind from: ' + str(now))
    print('event remind to: ' + str(now_plus_one_minute))
    event_reminds = EventRemind.objects.filter(has_been_reminded=False, date__range=[now, now_plus_one_minute])
    print('events: ' + str(event_reminds))
    for event_remind in event_reminds:
        profile = Profile.objects.get(user=event_remind.created_by)
        message = str(profile.mobile_phone_number) + ';' + str(event_remind.event.event_name) + ';' + str(
            event_remind.event.event_description) + ';' + str(event_remind.date.date())
        SendSMSWithPatternThread(body_id='143432',
                                 target_phone_number=profile.mobile_phone_number,
                                 message_items=message).start()
        event_remind.has_been_reminded = True
        event_remind.save()
