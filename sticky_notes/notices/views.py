from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice
from .forms import NoticeForm


# Create your views here.
def notice_list(request):
    """
    View to display a list of all notices

    :param request: HTTP request object.
    :return: Renders template with a list of notices.
    """
    notices = Notice.objects.all()

    # Creating a context dictionary to pass data
    context = {
        "notices": notices,
        "page_title": "List of Notices"
    }

    return render(request, "notices/notice_list.html", context)


def notice_detail(request, pk):
    """
    View to display details of a specific notice.

    :param request: HTTP reques object.
    :param pk: Primary key of the notice
    return: Rendered template with details of the specific notice.
    """

    notice = get_object_or_404(Notice, pk=pk)
    return render(request, "notices/notice_detail.html", {"notice": notice})


def notice_create(request):
    """
    View to create a new notice.

    :param request: HTTP request object.
    :return: Rendered template for creating a new notice.
    """
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect("notice_list")
    else:
        form = NoticeForm()
    return render(request, "notices/notice_form.html", {"form": form})


def notice_update(request, pk):
    """
    View to update an existing notice.

    :param request: HTTP request object.
    :param pk: Primary key of the notice to be updated.
    :return: Rendered template for updating the specified notice.
    """
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect("notice_list")
    else:
        form = NoticeForm(instance=notice)
    return render(request, "notices/notice_form.html", {"form": form})


def notice_delete(request, pk):
    """
    View to delete an existing notice.

    :param request: HTTP request object.
    :param pk: Primary key of the notice to be deleted.
    :return: Redirect to the notice list after deletion.
    """
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect("notice_list")
