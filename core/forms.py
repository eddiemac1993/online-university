from django import forms
from .models import Course, Lesson, Assignment, Submission, Discussion
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor', 'start_date', 'end_date']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content', 'order']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'due_date']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['assignment', 'student', 'grade']

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['course', 'content']