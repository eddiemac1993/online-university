from django.db import models
from django.conf import settings

class Profile(models.Model):
    USER_TYPES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses_taught')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
        ]


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['order']


class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.title}'

    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        indexes = [
            models.Index(fields=['enrollment_date']),
        ]


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'
        indexes = [
            models.Index(fields=['due_date']),
        ]


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.student.username} submission for {self.assignment.title}'

    class Meta:
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'
        indexes = [
            models.Index(fields=['submission_date']),
        ]


class Grade(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.CharField(max_length=10)
    date_awarded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} grade for {self.course.title}'

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        indexes = [
            models.Index(fields=['date_awarded']),
        ]


class Discussion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='discussions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discussions')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Discussion by {self.user.username} in {self.course.title}'

    class Meta:
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}'

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]


class Payment(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Payment by {self.user.username} - {self.amount}'

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        indexes = [
            models.Index(fields=['payment_date']),
        ]
