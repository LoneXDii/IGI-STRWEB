import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse
from .views import account_views, views, statistics_views, services_views, api_views
from medicalCenter_app.models import Appointment, Client, Doctor, DoctorSpecialization, Schedule, Service


class TestAccountViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_model = get_user_model()

        cls.user_admin = cls.user_model.objects.create_superuser(username='Admin')
        cls.admin = TestClient()
        cls.admin.force_login(cls.user_admin)
        
        cls.user_client1 = cls.user_model.objects.create(username='User1', password='+45125148152*')
        cls.client_profile1 = Client.objects.create(name='Name1', surname='Surname1', second_name='SecondName1', 
                                    birth_date=datetime.date.today() - datetime.timedelta(days=25 * 365),
                                    adress='adress1', phone_number='+375291111111')
        cls.client_profile1.user = cls.user_client1
        cls.client_acc1 = TestClient()
        cls.client_acc1.force_login(cls.user_client1)

        cls.user_client2 = cls.user_model.objects.create(username='User2')
        cls.client_profile2 = Client.objects.create(name='Name2', surname='Surname2', second_name='SecondName2', 
                                    birth_date=datetime.date.today() - datetime.timedelta(days=25 * 365),
                                    adress='adress2', phone_number='+375291111111').user=cls.user_client2
        cls.client_acc2 = TestClient()
        cls.client_acc2.force_login(cls.user_client2)

        cls.specialization = DoctorSpecialization.objects.create(name='Spec1')
        cls.schedule = Schedule.objects.create(work_starts=datetime.time(hour=9, minute=0), work_ends=datetime.time(hour=18, minute=0))
        cls.doctor_client = cls.user_model.objects.create(username='Doctor1')
        cls.doctor_profile = Doctor.objects.create(name='DName1', surname='DSurname1', second_name='DSecondName1', 
                                    birth_date=datetime.date.today() - datetime.timedelta(days=25 * 365),
                                    adress='Dadress1', phone_number='+375292222222',
                                    specialization=cls.specialization, shcedule=cls.schedule).user=cls.doctor_client
        cls.doctor_acc = TestClient()
        cls.doctor_acc.force_login(cls.doctor_client)

        cls.service = Service.objects.create(name='Service1', price=100, specialization_required=cls.specialization)
        
    def test_call_view_login_required_as_anonymous(self):
        response = self.client.get(reverse(account_views.profile), follow=True)
        self.assertRedirects(response, f'/accounts/login/?next={reverse(account_views.profile)}')
        response = self.client.get(reverse(account_views.change_password), follow=True)
        self.assertRedirects(response, f'/accounts/login/?next={reverse(account_views.change_password)}')
        response = self.client.get(reverse(account_views.edit_profile), follow=True)
        self.assertRedirects(response, f'/accounts/login/?next={reverse(account_views.edit_profile)}')
        response = self.client.get(reverse(account_views.logout), follow=True)
        self.assertRedirects(response, f'/accounts/login/?next={reverse(account_views.logout)}')

    def test_index(self):
        response = self.client_acc1.get(reverse(views.index))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        response = self.doctor_acc.get(reverse(views.index))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        response = self.admin.get(reverse(views.index))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_services(self):
        response = self.client_acc1.get(reverse(services_views.services_details, kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/doctor_services.html')
        response = self.doctor_acc.get(reverse(services_views.services_details, kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/doctor_services.html')
        response = self.admin.get(reverse(services_views.services_details, kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/doctor_services.html')

    def test_specializations(self):
        response = self.client_acc1.get(reverse(services_views.services))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/doctors_specializations.html')
        response = self.doctor_acc.get(reverse(services_views.services))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/doctors_specializations.html')
        response = self.admin.get(reverse(services_views.services))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/doctors_specializations.html')

    def test_statistics(self):
        response = self.client_acc1.get(reverse(statistics_views.statistics))
        self.assertEqual(response.status_code, 404)
        response = self.doctor_acc.get(reverse(statistics_views.statistics))
        self.assertEqual(response.status_code, 404)
        response = self.admin.get(reverse(statistics_views.statistics))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statistics/main.html')

    def test_client_info(self):
        response = self.client_acc1.get(reverse(views.client_info, kwargs={'id': self.client_profile1.pk}))
        self.assertEqual(response.status_code, 404)
        response = self.client_acc2.get(reverse(views.client_info, kwargs={'id': self.client_profile1.pk}))
        self.assertEqual(response.status_code, 404)

    def test_login_required_in_services_views(self):
        response = self.client.get(reverse(services_views.service_appointment, kwargs={"service_id": 1}), follow=True)
        self.assertRedirects(response, f'/accounts/login/?next={reverse(services_views.service_appointment, kwargs={"service_id": 1})}')

    def test_service_views(self):
        response = self.client_acc1.get(reverse(services_views.service_appointment, kwargs={"service_id": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/service_appointment.html')
        response = self.doctor_acc.get(reverse(services_views.service_appointment, kwargs={"service_id": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/service_appointment.html')
        response = self.admin.get(reverse(services_views.service_appointment, kwargs={"service_id": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/service_appointment.html')

    def test_coupons(self):
        response = self.client_acc1.get(reverse(views.coupons))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coupons.html')
        response = self.doctor_acc.get(reverse(views.coupons))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coupons.html')
        response = self.admin.get(reverse(views.coupons))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coupons.html')

    def test_contacts(self):
        response = self.client_acc1.get(reverse(views.contacts))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')
        response = self.doctor_acc.get(reverse(views.contacts))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')
        response = self.admin.get(reverse(views.contacts))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')

    def test_vacansies(self):
        response = self.client_acc1.get(reverse(views.vacancies))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancies.html')
        response = self.doctor_acc.get(reverse(views.vacancies))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancies.html')
        response = self.admin.get(reverse(views.vacancies))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancies.html')

    def test_reviews(self):
        response = self.client_acc1.get(reverse(views.reviews))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews.html')
        response = self.doctor_acc.get(reverse(views.reviews))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews.html')
        response = self.admin.get(reverse(views.reviews))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews.html')

    def test_doctor_info(self):
        response = self.client_acc1.get(reverse(views.doctor_info, kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor_info.html')
        response = self.doctor_acc.get(reverse(views.doctor_info, kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor_info.html')
        response = self.admin.get(reverse(views.doctor_info, kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor_info.html')

    def test_terms(self):
        response = self.client_acc1.get(reverse(views.terms_and_defs))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'termsAndDefs.html')
        response = self.doctor_acc.get(reverse(views.terms_and_defs))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'termsAndDefs.html')
        response = self.admin.get(reverse(views.terms_and_defs))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'termsAndDefs.html')

    def test_add_appointment(self):
        #all is ok
        form = {
            'description': 'test_descr',
            'time': '12:20',
            'doctor': '1',
            'date': '2025-01-01',
            'user_pk': f'{self.client_profile1.pk}'
        }
        response = self.client_acc1.post(reverse(services_views.service_appointment, kwargs={'service_id': 1}), data=form)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(services_views.services))
        self.assertTrue(Appointment.objects.filter(description='test_descr').exists())

        #incorrect doctor
        form = {
            'description': 'test_descr',
            'time': '12:20',
            'doctor': '10',
            'date': '2025-01-01',
            'user_pk': f'{self.client_profile1.pk}'
        }
        response = self.client_acc1.post(reverse(services_views.service_appointment, kwargs={'service_id': 1}), data=form)
        self.assertEqual(response.status_code, 200)

        #incorrect date
        form = {
            'description': 'test_descr',
            'time': '12:20',
            'doctor': '10',
            'date': '2023-01-01',
            'user_pk': f'{self.client_profile1.pk}'
        }
        response = self.client_acc1.post(reverse(services_views.service_appointment, kwargs={'service_id': 1}), data=form)
        self.assertEqual(response.status_code, 200)