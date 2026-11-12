from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContestForm
from .models import Contest


def proposal(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Contest, pk=pk)
    else:
        instance = None
        
    form = ContestForm(request.POST or None, instance=instance)
    
    if form.is_valid():
        form.save()
        return redirect('contest:list')
        
    context = {'form': form}
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contests = Contest.objects.order_by('id')
    context = {'contests': contests}
    return render(request, 'contest/contest_list.html', context)


def delete_contest(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(instance=instance)
    context = {'form': form}
    
    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')
        
    return render(request, 'contest/form.html', context)