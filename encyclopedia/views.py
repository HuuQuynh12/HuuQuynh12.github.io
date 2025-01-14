from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    wiki = util.get_entry(title)
    if wiki:
        return render(request, "encyclopedia/wiki.html", {
        "wiki": wiki,
        "title": title,
    })
    else:
        return render(request, "encyclopedia/error.html")
