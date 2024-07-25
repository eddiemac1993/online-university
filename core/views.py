from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Assignment, Submission, Discussion
from .forms import CourseForm, LessonForm, AssignmentForm, SubmissionForm, DiscussionForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('course_list')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('course_list')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'core/course_detail.html', {'course': course})

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm()
    return render(request, 'core/course_form.html', {'form': form})

@login_required
def create_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = LessonForm()
    return render(request, 'core/lesson_form.html', {'form': form, 'course': course})

@login_required
def create_assignment(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.course = course
            assignment.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = AssignmentForm()
    return render(request, 'core/assignment_form.html', {'form': form, 'course': course})

@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            return redirect('course_detail', course_id=assignment.course.id)
    else:
        form = SubmissionForm()
    return render(request, 'core/submission_form.html', {'form': form, 'assignment': assignment})

@login_required
def create_discussion(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.course = course
            discussion.user = request.user
            discussion.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = DiscussionForm()
    return render(request, 'core/discussion_form.html', {'form': form, 'course': course})

def home(request):
    return render(request, 'core/home.html')