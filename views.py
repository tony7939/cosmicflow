from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Section

def home(request):
    sections = Section.objects.order_by('-viewer_count')
    return render(request, 'home.html', {'sections': sections})

def add_section(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Untitled')
        content = request.POST.get('content', 'No content provided.')
        category = request.POST.get('category', '')
        Section.objects.create(title=title, content=content, category=category)
        return redirect('home')
    return render(request, 'add_section.html')

def view_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    section.viewer_count += 1
    section.save()
    return render(request, 'section_detail.html', {'section': section})

from django.shortcuts import render
from .models import Section  # 모델을 임포트한 경우

def home(request):
    # 섹션 데이터를 데이터베이스에서 가져옴
    sections = Section.objects.all()  # 예시: 모든 섹션을 가져옴
    return render(request, 'base.html', {'sections': sections})
