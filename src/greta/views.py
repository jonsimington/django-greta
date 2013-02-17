from django.views.generic import RedirectView, ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Repository

import logging

logger = logging.getLogger(__name__)



class GretaContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(GretaContextMixin, self).get_context_data(**kwargs)
        context['ref'] = self.kwargs['ref']
        return context


class RepositoryList(ListView):
    model = Repository
    context_object_name = "repos"
    template_name = "greta/repository_list.html"


class RedirectToDefaultBranch(RedirectView):
    def get_redirect_url(self, **kwargs):
        repo = get_object_or_404(Repository, pk=self.kwargs['pk'])
        return repo.get_absolute_url()


class BranchDetail(DetailView):
    model = Repository
    context_object_name = "repo"
    template_name = "greta/branch_detail.html"


class TagDetail(DetailView):
    model = Repository
    context_object_name = "repo"
    template_name = "greta/tag_detail.html"


class RepositoryDetail(GretaContextMixin, DetailView):
    model = Repository
    context_object_name = "repo"
    template_name = "greta/repository_detail.html"

    def get_context_data(self, **kwargs):
        context = super(RepositoryDetail, self).get_context_data(**kwargs)
        context['log'] = self.object.get_log(ref=self.kwargs['ref'])
        return context


class CommitDetail(RepositoryDetail):
    template_name = "greta/commit_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CommitDetail, self).get_context_data(**kwargs)
        context['changes'] = self.object.show(self.kwargs['ref'])
        return context
