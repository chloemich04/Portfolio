from django.test import SimpleTestCase
from django.urls import reverse


class PortfolioPageTests(SimpleTestCase):
    def test_pages_render_with_navigation_and_contact_links(self):
        for name in ("index", "projects", "contact"):
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'aria-current="page"', count=1)
                self.assertContains(response, 'id="main"')
                self.assertNotContains(response, 'href="#"')
                self.assertNotContains(response, 'yourusername')

    def test_home_includes_confirmed_background(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Computer Science graduate")
        self.assertContains(response, "Louisiana Army National Guard")

    def test_project_collection_is_shared(self):
        for name in ("index", "projects"):
            response = self.client.get(reverse(name))
            self.assertContains(response, "Anime Tracker")
            self.assertContains(response, "https://github.com/chloemich04/Portfolio")
            self.assertContains(response, "tor-anime")

    def test_contact_uses_real_contact_channels(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, 'mailto:chloemichelle04@gmail.com')
        self.assertContains(response, 'https://www.linkedin.com/in/chloe-robinson-a90b3632a/')
        self.assertContains(response, 'https://github.com/chloemich04')
        self.assertNotContains(response, '<form')
