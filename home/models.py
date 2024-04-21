from django.db import models
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
# import FieldRowPanel and InlinePanel:
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.fields import RichTextField

# import AbstractEmailForm and AbstractFormField:
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

# import FormSubmissionsPanel:
from wagtail.contrib.forms.panels import FormSubmissionsPanel


class HomePage(Page):
    # banner_image =
    # banner_title = models.CharField(max_length=250)
    # banner_description =
    # about_image =
    # about_title =
    # about_description =
    # solution_title =
    # solution_description =
    # left_demand_title =
    # left_demand_description =
    # left_demand_image =
    # right_demand_title =
    # right_demand_description =
    # right_demand_image =
    # application_title =
    # application_description =
    pass


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')


class CompanyLocation(Orderable):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='company_location')
    location = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    short_description = RichTextField(null=True, blank=True)
    panels = [
        FieldPanel('location'),
        FieldPanel('state'),
        FieldPanel('phone'),
        FieldPanel('short_description')
    ]


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        InlinePanel('company_location', label="Company location"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


class ProductPage(Page):
    pass


class ProductDetailPage(Page):
    pass


class ApplicantPage(Page):
    pass


class ApplicantDetailPage(Page):
    pass