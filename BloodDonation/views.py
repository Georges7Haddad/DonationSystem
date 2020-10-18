from django.shortcuts import render


def view_test(request):
    return render(request=request, template_name="test_page.html")
