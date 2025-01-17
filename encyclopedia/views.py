from django.shortcuts import render
from  django.http import HttpResponseRedirect
from . import util

import markdown
import markdownify
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    wiki_markdown = util.get_entry(title)
    if wiki_markdown:
        wiki_html = markdown.markdown(wiki_markdown)
        return render(request, "encyclopedia/wiki.html", {
        "wiki": wiki_html,
        "title": title,
        "edit": True,
    })
    else:
        return render(request, "encyclopedia/error.html",{
            "messenger": "The requested page was not found."
        })

def search(request):
    if request.method == "GET":
        search = request.GET.get("q")
        list_data = util.list_entries()
        if search in list_data:
            return HttpResponseRedirect(f"/wiki/{search}")
        else: 
            result = []
            for data in list_data:
                if search in data:
                    result += [data]
            return render(request, "encyclopedia/search.html", {
                "result": result,    
            })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        data = util.list_entries()
        if title in data:
            return render(request, "encyclopedia/error.html",{
            "messenger": "Encyclopedia entry already exists."
        })
        else:
            content_create = markdownify.markdownify(content)
            util.save_entry(title,content_create)
            return HttpResponseRedirect(f"/wiki/{title}")
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")

def editpage(request):
    if request.method == "GET":
        title_edit = request.GET.get("title_edit")
        #kiểm tra có nhận được dữ liệu title hay không
        if title_edit:
            wiki_markdown = util.get_entry(title_edit)
            #kiểm tra tiêu đề có nằm trong danh sách đã có hay không, nếu có mới được chỉnh sửa
            if wiki_markdown:
                return render(request, "encyclopedia/edit.html",{
                "wiki_markdown": wiki_markdown,
                "title": title_edit,
                })
            #nếu không có thì thông báo lỗi
            else:
                return render(request, "encyclopedia/error.html",{
                "messenger": "No title exists to edit."})
        else:
            return render(request, "encyclopedia/error.html",{
            "messenger": "No title exists to edit."
        })

    if request.method == "POST":
        title_save = request.POST.get("title_save")
        content_save =  request.POST.get("content_save")
        markdown_content = markdownify.markdownify(content_save)
        util.save_entry(title_save,markdown_content)
        return HttpResponseRedirect(f"/wiki/{title_save}")

def random_page(request):
    list_title = util.list_entries()
    title = random.choice(list_title)
    return HttpResponseRedirect(f"/wiki/{title}")
        

