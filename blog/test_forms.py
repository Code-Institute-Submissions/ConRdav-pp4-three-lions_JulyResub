from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """ Unit test for comments form """
    def test_post_body_is_required(self):
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('body',)
        )
