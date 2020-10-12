from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create a new user with email is successful"""
        email = 'test@test.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailize(self):
        """Test the email for a new user is normailize"""
        email = 'test@LONDONAPPDEV.COM'
        password = 'TEST123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '121232132')

    def test_create_new_superuser(self):
        """Creates a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'hello123'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

