from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    # Создаем пустую форму при запросе GET
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form,
            }
        return render(request, 'pages/add_snippet.html', context)
    
    # Получаем данные из формы и на их основе создаем новый Сниппет в БД
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")  # GET /snippets/list
        return render(request,'pages/add_snippet.html', {'form': form})


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
        }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    context = {'pagename': 'Просмотр сниппета'}
    try:
        snippet = Snippet.objects.get(pk=snippet_id)
    except Snippet.DoesNotExist:
        return render(request, "pages/errors.html", context | {"error": f"Snippet with id={snippet_id} not found."})
    else:
        context["snippet"] = snippet
        return render(request, "pages/snippet_detail.html", context)


def snippet_edit(request, snippet_id):
    pass


def snippet_delete(request, snippet_id):
    pass