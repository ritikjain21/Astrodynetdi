from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from wagtail.documents import get_document_model
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['products'] = ProductDetailPage.objects.live().public().order_by('-id')[:6]
        context['dropdown_product'] = ProductDetailPage.objects.live().public().order_by('-id')
        context['dropdown_application'] = ApplicationDetailPage.objects.live().public().order_by('-id')
        context['applications'] = ApplicationDetailPage.objects.live().public().order_by('-id')[:4]
        return context


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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['dropdown_product'] = ProductDetailPage.objects.live().public().order_by('-id')
        context['dropdown_application'] = ApplicationDetailPage.objects.live().public().order_by('-id')
        return context


class ProductPage(Page):
    pass

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        product_details = ProductDetailPage.objects.live().public()
        paginator = Paginator(product_details, 1)
        page = request.GET.get('page')
        try:
            product_details = paginator.page(page)
        except PageNotAnInteger:
            product_details = paginator.page(1)
        except EmptyPage:
            product_details = paginator.page(paginator.num_pages)
        context['products'] = product_details
        context['dropdown_product'] = ProductDetailPage.objects.live().public().order_by('-id')
        context['dropdown_application'] = ApplicationDetailPage.objects.live().public().order_by('-id')
        return context


class MultipleProduct(Orderable):
    page = ParentalKey('ProductDetailPage', on_delete=models.CASCADE, related_name='products')
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Products image",
    )
    part_number = models.CharField(max_length=250)
    description = RichTextField()
    output_voltage = models.CharField(max_length=250)
    output_current = models.CharField(max_length=250)
    output_power = models.CharField(max_length=250)
    input_voltage_range = models.CharField(max_length=250)
    isolation = models.CharField(max_length=250)
    form_factor = models.CharField(max_length=250)
    document = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    panels = [
        FieldPanel('image'),
        FieldPanel('part_number'),
        FieldPanel('description'),
        FieldPanel('output_voltage'),
        FieldPanel('output_current'),
        FieldPanel('output_power'),
        FieldPanel('input_voltage_range'),
        FieldPanel('isolation'),
        FieldPanel('form_factor'),
        FieldPanel('document'),
    ]


class ProductDetailPage(Page):
    outer_title = models.CharField(max_length=250, default='')
    outer_description = models.CharField(max_length=250, default='')
    outer_icon = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    outer_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    description = RichTextField(null=True, blank=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('outer_title'),
            FieldPanel('outer_description'),
            FieldPanel('outer_icon'),
            FieldPanel('outer_image'),
        ], heading="Product Listing", classname="collapsible"),
        FieldPanel('description'),
        MultiFieldPanel([
            InlinePanel('products', label="Products", min_num=1)
        ], heading="Products section", classname="collapsible"),
    ]


class ApplicationPage(Page):
    description = RichTextField(null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['dropdown_product'] = ProductDetailPage.objects.live().public().order_by('-id')
        context['dropdown_application'] = ApplicationDetailPage.objects.live().public().order_by('-id')
        return context


class ApplicationDetailPage(Page):
    outer_title = models.CharField(max_length=250, default='')
    outer_description = models.CharField(max_length=250, default='')
    outer_icon = models.ForeignKey(
        get_document_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    outer_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    header_description = RichTextField(null=True, blank=True)
    right_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    right_description = RichTextField(null=True, blank=True)
    middle_description = RichTextField(null=True, blank=True)
    left_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    left_description = RichTextField(null=True, blank=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('outer_title'),
            FieldPanel('outer_description'),
            FieldPanel('outer_icon'),
            FieldPanel('outer_image'),
        ], heading="Application Listing", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('header_description')
        ], heading="Header", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('right_image'),
            FieldPanel('right_description')
        ], heading="Banner bottom", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('middle_description')
        ], heading="Middle Section", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('right_image'),
            FieldPanel('right_description')
        ], heading="End Section", classname="collapsible"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['dropdown_product'] = ProductDetailPage.objects.live().public().order_by('-id')
        context['dropdown_application'] = ApplicationDetailPage.objects.live().public().order_by('-id')
        return context