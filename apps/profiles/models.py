from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Role(models.TextChoices):
    LEAD = "Lead", _("Project Lead")
    TECH = "Tech", _("Technical Member")
    OTHER = "Support", _("Support Member")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+14032869011"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="say something about your role"
    )
    license = models.CharField(
        verbose_name=_("User License"), max_length=20, blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )
    role = models.CharField(
        verbose_name=_("Project Role"),
        choices=Role.choices,
        default=Role.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"), default="CA", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Calgary",
        blank=False,
        null=False,
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"), default=False, help_text=_("Buy a licenses?")
    )
    is_seller = models.BooleanField(
        verbose_name=_("Seller"), default=False, help_text=_("Owner of the license?")
    )
    is_agent = models.BooleanField(
        verbose_name=_("Agent"), default=False, help_text=_("Are you an agent?")
    )
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
