from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils.text import slugify
from django.views.generic import FormView, TemplateView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from envelope.views import ContactView as EnvelopeContactView
from djatex import render_latex

from .models import OfertyEst, OfertyFpage, OfertyMiasto, OfertyRodzaj,\
    OfertyTyp, OfertyEstPhoto
from .forms import CategorizedContactForm
from .forms import OfertySearchForm, DetailContactForm
from .mixins import SearchFormMixin


class ContactView(EnvelopeContactView):
    form_class = CategorizedContactForm
    template_name = 'envelope/crispy_contact.html'
    success_url = "/dziekujemy"

    def get_initial(self):
        """
        Automatically fills form fields for authenticated users.
        """

        return FormView.get_initial(self)


def post_data(request):
    """
    Slugify offer search
    """
    if request.POST:
        try:
            rodzaj = int(request.POST.get('rodzaj'))
            typ = int(request.POST.get('typ'))
            miasto = int(request.POST.get("miasto"))
        except (ValueError, TypeError):
            return HttpResponse(status=400)

        # any(not isinstance(x, (int, float)) for x in [a,b,c,d])
        # if any(not isinstance(var, int) for var in [rodzaj,
                                                    # typ,
                                                    # miasto]):
            # return HttpResponse(status=400)

        rodzaj = get_object_or_404(OfertyRodzaj, pk=rodzaj).nazwa
        rodzaj = slugify(rodzaj)
        typ = get_object_or_404(OfertyTyp, pk=typ).nazwa
        typ = slugify(typ)
        miasto = get_object_or_404(OfertyMiasto, pk=miasto).nazwa_flat
    else:
        rodzaj = 'sprzedaz'
        typ = 'dom'
        miasto = 'Ustron'

    return redirect(reverse_lazy('oferty:result',
                                 kwargs={'rodzaj': rodzaj,
                                         'typ': typ,
                                         'miasto': miasto}))


def get_est_id(request):
    """
    Redirect to offer details
    """

    if request.GET:
        try:
            eid = int(request.GET.get("est_id"))
        except (ValueError, TypeError):
            raise Http404()
        est_id = get_object_or_404(OfertyEst, pk=eid).pk

    return redirect(reverse_lazy('oferty:detail', kwargs={'pk': est_id}))


def index(request):
    """
    Shows highlighted offers on home page
    """
    oferty = OfertyEst.objects.filter(status=0).select_related().order_by('id')
    form = OfertySearchForm()
    query = request.GET.get("est_id")

    fpage_ids = []

    if query:
        oferty = oferty.filter(pk=query)
    else:
        for fpage in OfertyFpage.objects.all().order_by('id'):
            fpage_ids.append(fpage.est_id)

        oferty = oferty.filter(pk__in=fpage_ids,
                               status=0)[:9]

    return render(request, 'oferty/fpage.html',
                  {'oferty': oferty, 'form': form})


def get_from_list(objs, msg):
    if len(objs) != 1:
        raise Http404()
    return objs[0]


def sprzedane(request):
    """
    List lately sold offers
    """
    oferty = OfertyEst.objects.filter(status=1)
    oferty = oferty.exclude(data_sprz__isnull=True).select_related()
    oferty = oferty.order_by('-data_sprz')[:50]

    paginator = Paginator(oferty, 10)

    page = request.GET.get('page')
    try:
        oferty = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        oferty = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        oferty = paginator.page(paginator.num_pages)

    # Main offer search form
    # default: (1) sprzedaż / (1) dom / (12) Ustroń
    form = OfertySearchForm({'rodzaj': 1, 'typ': 1, 'miasto': 12})

    return render(request, 'oferty/index.html',
                  {'oferty': oferty, 'form': form, 'sprzedane': 1})


def najnowsze(request):
    """
    List the newest offers
    """

    oferty = OfertyEst.objects.filter(status=0).select_related()
    oferty = oferty.order_by('-data', '-id')[:10]

    paginator = Paginator(oferty, 10)

    page = request.GET.get('page')
    try:
        oferty = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        oferty = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        oferty = paginator.page(paginator.num_pages)

    # Offer search main form
    # default: (1) sprzedaż / (1) dom / (12) Ustroń
    form = OfertySearchForm({'rodzaj': 1, 'typ': 1, 'miasto': 12})

    return render(request, 'oferty/index.html',
                  {'oferty': oferty, 'form': form, 'najnowsze': 1})


def result(request, rodzaj, typ, miasto):
    """
    Offers index
    """

    miasto_id = get_object_or_404(OfertyMiasto, nazwa_flat=miasto).id
    rodzaj_objs = [r for r in OfertyRodzaj.objects.all() if slugify(r.nazwa) == rodzaj]
    typ_objs = [t for t in OfertyTyp.objects.all() if slugify(t.nazwa) == typ]

    rodzaj_id = get_from_list(rodzaj_objs, 'Nie ma takiego rodzaju').id
    typ_id = get_from_list(typ_objs, 'Nie ma takiego typu').id

    oferty = OfertyEst.objects.filter(status=0).select_related()
    oferty = oferty.order_by('-id')

    oferty = oferty.filter(
        Q(rodzaj=rodzaj_id),
        Q(typ=typ_id),
        Q(miasto=miasto_id)
    )

    paginator = Paginator(oferty, 10)

    page = request.GET.get('page')
    try:
        oferty = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        oferty = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        oferty = paginator.page(paginator.num_pages)

    # Offers main search form
    form = OfertySearchForm({'rodzaj': rodzaj_id,
                             'typ': typ_id,
                             'miasto': miasto_id})

    return render(request, 'oferty/index.html',
                  {'oferty': oferty, 'form': form})


class DetailView(DetailView, ContactView):
    """
    Offer details
    """

    form_class = DetailContactForm
    model = OfertyEst
    template_name = 'oferty/detail.html'
    form_invalid_message = _(u"There was an error in the contact form.")
    form_valid_message = _(u"Thank you for your message.")

    def get_queryset(self):
        qs = super(DetailView, self).get_queryset()
        return qs.filter(status="0").select_related()

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = DetailContactForm(initial={
            'sender': self.kwargs['pk']})
        return context

    def post(self, request, *args, **kwargs):
        return ContactView.post(self, request, *args, **kwargs)


class ThankYou(SearchFormMixin, TemplateView):
    """
    email send success message
    """

    template_name = "oferty/thankyou.html"


class PrivacyPolicy(SearchFormMixin, TemplateView):
    """ Privacy Policy """

    template_name = "oferty/policy.html"


def detail_pdf(request, **kwargs):
    """ Render a pdf with offer details """

    pk = kwargs['pk']

    oferta = get_object_or_404(OfertyEst, Q(status=0), pk=pk)

    try:
        photo = oferta.ofertyestphoto_set.get(thumbnail=True).filename
    except OfertyEstPhoto.DoesNotExist:
        photo = ''
    else:
        # escape underscore for xelatex
        photo = photo.replace('_', '\\string_')

    filename = "domino_oferta_{}.pdf".format(pk)

    context = {'oferta': oferta, 'photo': photo,
               'graphicspath': settings.LATEX_GRAPHICSPATH}
    
    return render_latex(request, filename, 'oferty/detail.tex',
                        error_template_name='oferty/error.html',
                        home_dir=settings.TEX_HOME,
                        # build_dir=settings.TEX_HOME,
                        context=context)
