import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, AccessRecord, WebPage
from faker import Faker

fakegen = Faker()
topics =  ['Social Media', 'Social Network', 'News', 'Games', 'Messenger']

def populate(N=5):
    """ Function to populate the database with N entries """

    for _ in range(N):
        fake_topic = Topic.objects.get_or_create(topic=random.choice(topics))[0]
        fake_webpage = WebPage.objects.get_or_create(
            topic=fake_topic,
            url=fakegen.url(),
            name=fakegen.company()
        )[0]
        fake_acc_rec = AccessRecord.objects.get_or_create(
            name=fake_webpage,
            date=fakegen.date()
        )[0]

        fake_topic.save()
        fake_webpage.save()
        fake_acc_rec.save()

if '__main__' == __name__:
    n = int(input('No: of entries to populate = '))
    populate(n)
    print('populated..')
