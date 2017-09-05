from django.shortcuts import render
from .models import IssueModel
from .forms import IssueForm


def example_func(request):
    print('ENTERED IN FUNCTION')
    if request.method == 'GET':
        form = IssueForm()
        try:
            e = IssueModel.objects.get_or_create(title="Exam")
        except Exception as e:
            print(e)
    else:
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            print('FORM OK')
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']
            post = IssueModel.objects.create(title=title, file=file)


    queryset = IssueModel.objects.all()
    return render(request, 'example_template.html', {'object_list': queryset, 'form': form})
