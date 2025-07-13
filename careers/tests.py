from django.test import TestCase
from django.urls import reverse
from .models import Career, JobApplication
from django.core.files.uploadedfile import SimpleUploadedFile

class JobApplicationViewTests(TestCase):

    def setUp(self):
        # Sample career object
        self.career = Career.objects.create(
            title='Python Developer',
            location='Remote',
            category='Software Development',
            job_type='Full-time',
            work_mode='Remote',
            description='Develop Python applications.',
            requirements='Write code\nFix bugs',
            qualifications='Bachelor degree\n2 years experience'
        )

    def test_career_detail_view(self):
        response = self.client.get(reverse('careers:career-detail', args=[self.career.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers/career-detail.html')
        self.assertContains(response, 'Resume Parser')


    def test_apply_view_get(self):
        job = Career.objects.create(
            title='Python Developer',
            location='Remote',
            category='Software Development',
            job_type='Full-time',
            work_mode='Remote',
            description='Develop Python applications.',
            requirements='Write code\nFix bugs',
            qualifications='Bachelor degree\n2 years experience'
        )
        response = self.client.get(reverse('careers:career-apply', args=[job.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers/apply.html')
        self.assertContains(response, 'Submit Application')  # Updated to match template


    def test_apply_view_post_valid(self):
        job = Career.objects.create(
            title='Python Developer',
            location='Remote',
            category='Software Development',
            job_type='Full-time',
            work_mode='Remote',
            description='Develop Python applications.',
            requirements='Write code\nFix bugs',
            qualifications='Bachelor degree\n2 years experience'
        )
        response = self.client.post(reverse('careers:career-apply', args=[job.pk]), data={
            'full_name': 'John Doe',
            'email': 'test@example.com',
            'phone': '1234567890',
            'linkedin_url': 'https://linkedin.com/in/johndoe',
            'portfolio_url': 'https://portfolio.com/johndoe',
            'resume': SimpleUploadedFile('resume.pdf', b'file_content'),
            'cover_letter': 'Test cover letter',
        }, follow=True)  # Follow redirects
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers/career-detail.html')
        self.assertContains(response, 'Your application has been submitted successfully.')

    def test_apply_view_post_invalid(self):
        job = Career.objects.create(
            title='Python Developer',
            location='Remote',
            category='Software Development',
            job_type='Full-time',
            work_mode='Remote',
            description='Develop Python applications.',
            requirements='Write code\nFix bugs',
            qualifications='Bachelor degree\n2 years experience'
        )
        response = self.client.post(reverse('careers:career-apply', args=[job.pk]), data={
            'email': 'test@example.com',
            'phone': '1234567890',
            'resume': SimpleUploadedFile('resume.pdf', b'file_content'),
            'cover_letter': 'Test cover letter',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers/apply.html')
        self.assertFormError(response.context['form'], 'full_name', 'This field is required.')
