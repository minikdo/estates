from .forms import OfertySearchForm


class SearchFormMixin(object):
    
    form = OfertySearchForm({'rodzaj': 1, 'typ': 1, 'miasto': 12})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
