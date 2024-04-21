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
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    banner_title = models.CharField(
            blank=True,
            max_length=255, help_text="Write an Banner title for the site"
        )
    banner_description = RichTextField(blank=True)

    about_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    about_title = models.CharField(
        blank=True,
        max_length=255, help_text="Write an about title for the site"
    )
    about_description = RichTextField(blank=True)
    solution_title = models.CharField(
        blank=True,
        max_length=255, help_text="Write an solution title for the site"
    )
    solution_description = RichTextField(blank=True)

    left_demand_title = models.CharField(
        blank=True,
        max_length=255, help_text="Write an left demand title for the site"
    )
    left_demand_description = RichTextField(blank=True)
    left_demand_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    right_demand_title = models.CharField(
        blank=True,
        max_length=255, help_text="Write an right demand for the site"
    )
    right_demand_description = RichTextField(blank=True)
    right_demand_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    application_title = models.CharField(
        blank=True,
        max_length=255, help_text="Write an application title for the site"
    )
    application_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_image"),
            FieldPanel("banner_title"),
            FieldPanel("banner_description"),
        ], heading="Banner Area", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel("about_image"),
            FieldPanel("about_title"),
            FieldPanel("about_description"),
            FieldPanel("solution_title"),
            FieldPanel("solution_description"),
        ], heading="About Page Area", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel("left_demand_title"),
            FieldPanel("left_demand_description"),
            FieldPanel('left_demand_image'),
        ], heading="service Page Section", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel("right_demand_title"),
            FieldPanel("right_demand_description"),
            FieldPanel('right_demand_image'),
        ], heading="Right Demand Section", classname="collapsible"),

        MultiFieldPanel([
            FieldPanel('application_title'),
            FieldPanel('application_description')
        ], heading="Benefit section", classname="collapsible"),
    ]


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