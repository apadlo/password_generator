# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class PasswordGeneratorTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_password_generation_with_secrets(self):
        """Test that password generation works with secrets module"""
        response = self.client.get(reverse('password'), {
            'length': '12',
            'uppercase': 'on',
            'special': 'on',
            'numbers': 'on'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('password', response.context)
        password = response.context['password']
        self.assertEqual(len(password), 12)
        self.assertIsInstance(password, str)

    def test_password_generation_default_length(self):
        """Test password generation with default length"""
        response = self.client.get(reverse('password'))
        self.assertEqual(response.status_code, 200)
        password = response.context['password']
        self.assertEqual(len(password), 12)  # default length

    def test_password_generation_custom_length(self):
        """Test password generation with custom length"""
        for length in [6, 8, 10, 14]:
            response = self.client.get(reverse('password'), {'length': str(length)})
            self.assertEqual(response.status_code, 200)
            password = response.context['password']
            self.assertEqual(len(password), length)

    def test_password_uniqueness(self):
        """Test that generated passwords are different (with high probability)"""
        passwords = set()
        for _ in range(100):
            response = self.client.get(reverse('password'), {
                'length': '12',
                'uppercase': 'on',
                'special': 'on',
                'numbers': 'on'
            })
            passwords.add(response.context['password'])
        # With secrets module and a large character set, we should get highly unique passwords
        # We expect at least 99 out of 100 to be unique
        self.assertGreaterEqual(len(passwords), 99)
