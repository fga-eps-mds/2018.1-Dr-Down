from test_plus.test import TestCase
from drdown.events.models.model_events import Events
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date


class TestModelEvents(TestCase):

    def test_event_invalid_date(self):
        """
            Test if event day cannot be in future
        """

        with self.assertRaises(ValidationError):
            event = Events.objects.create(
                name="sjdkal",
                date=date.today(),
                organize_by='mano',
                location="sdadsad",
                time='12:45',
                description='sdjkajdlas',
                free=False,
                value=12.5,
            )

            event.clean()
