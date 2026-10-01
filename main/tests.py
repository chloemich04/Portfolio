from django.test import SimpleTestCase
from django.urls import reverse


class PortfolioPageTests(SimpleTestCase):
    def test_pages_render_with_navigation_and_contact_links(self):
        for name in ("index", "projects", "research", "contact"):
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
            self.assertContains(response, "https://github.com/chloemich04/Atlas")
            self.assertContains(response, "Anime Tracker")
            self.assertNotContains(response, "My contribution")
        collection = self.client.get(reverse("projects"))
        self.assertContains(collection, "Anime Tracker")
        self.assertContains(collection, "tor-anime")
        self.assertContains(collection, "An independently built Python research project")

    def test_contact_uses_real_contact_channels(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, 'mailto:chloemichelle04@gmail.com')
        self.assertContains(response, 'https://www.linkedin.com/in/chloe-robinson-a90b3632a/')
        self.assertContains(response, 'https://github.com/chloemich04')
        self.assertNotContains(response, '<form')

    def test_research_materials_and_study_status(self):
        from django.contrib.staticfiles import finders
        response = self.client.get(reverse("research"))
        self.assertContains(response, "Original study")
        self.assertContains(response, "Ongoing team research")
        self.assertContains(response, "Dr. Bhupendra Acharya")
        for name in ("blackmail-scamming-paper-2025.pdf", "scammer-codebook-presentation-2025.pptx", "blackmail-connections.pdf", "blackmail-connections.png"):
            self.assertContains(response, "research/" + name)
            self.assertIsNotNone(finders.find("research/" + name))
