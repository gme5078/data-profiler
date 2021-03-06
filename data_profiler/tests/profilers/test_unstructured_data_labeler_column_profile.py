import unittest
from unittest import mock
from collections import defaultdict
import pandas as pd

from data_profiler.profilers.unstructured_data_labeler_column_profile import UnstructuredDataLabelerProfile	


class TestUnstructuredDataLabelerProfile(unittest.TestCase):

    def test_char_level_counts(self):
        # setting up objects/profile
        default = UnstructuredDataLabelerProfile()

        sample = pd.Series(["abc123", "Bob", "!@##$%"])

        # running update
        default.update(sample)

        # now getting entity_counts to check for proper structure
        self.assertEqual(
            {'DATETIME': 6, 'BACKGROUND': 3, 'QUANTITY': 6},
            default.profile["entity_counts"]["true_char_level"])

        self.assertEqual(
            {'DATETIME': 6, 'BACKGROUND': 3, 'QUANTITY': 6},
            default.profile["entity_counts"]["postprocess_char_level"],)

        # assert it's not empty for now
        self.assertIsNotNone(default.profile)

        # then assert that correctly counted number of char samples
        self.assertEqual(default.char_sample_size, 15)

    def test_advanced_sample(self):
        # setting up objects/profile
        default = UnstructuredDataLabelerProfile()

        sample = pd.Series(
            ["Help\tJohn Macklemore\tneeds\tfood.\tPlease\tCall\t555-301-1234."
             "\tHis\tssn\tis\tnot\t334-97-1234. I'm a BAN: 000043219499392912."
             "\n", "Hi my name is joe, \t SSN: 123456789 r@nd0m numb3rz!\n"])

        # running update
        default.update(sample)

        # now getting entity_counts to check for proper structure
        self.assertEqual(
            {'BACKGROUND': 106, 'PERSON': 8, 'PHONE_NUMBER': 12, 'SSN': 20,
             'BAN': 18, 'INTEGER': 3, 'ADDRESS': 3},
            default.profile["entity_counts"]["true_char_level"])

        # assert it's not empty for now
        self.assertIsNotNone(default.profile)

    def test_word_level_NER_label_counts(self):
        # setting up objects/profile
        default = UnstructuredDataLabelerProfile()

        sample = pd.Series(
            ["Help\tJohn Macklemore\tneeds\tfood.\tPlease\tCall\t555-301-1234."
             "\tHis\tssn\tis\tnot\t334-97-1234. I'm a BAN: 000049939232194912."
             "\n", "Hi my name is joe, \t SSN: 123456789 r@nd0m numb3rz!\n"])

        # running update
        default.update(sample)

        # now getting entity_counts to check for proper structure
        self.assertEqual(
            {'BACKGROUND': 23,'PHONE_NUMBER': 1, 'SSN': 2, 'BAN': 1},
            default.profile["entity_counts"]["word_level"])

        # assert it's not empty for now
        self.assertIsNotNone(default.profile)

    def test_statistics(self):
        # setting up objects/profile
        default = UnstructuredDataLabelerProfile()

        sample = pd.Series(
            ["Help\tJohn Macklemore\tneeds\tfood.\tPlease\tCall\t555-301-1234."
             "\tHis\tssn\tis\tnot\t334-97-1234. I'm a BAN: 000043219499392912."
             "\n", "Hi my name is joe, \t SSN: 123456789 r@nd0m numb3rz!\n"])
        background_word_level_percent = 0.85185
        background_true_char_level_percent = 0.62352
        background_postprocess_level_percent = 0.705882

        # running update
        default.update(sample)

        self.assertAlmostEqual(
            background_word_level_percent,
            default.entity_percentages['word_level']['BACKGROUND'],
            3)
        self.assertAlmostEqual(
            background_true_char_level_percent,
            default.entity_percentages['true_char_level']['BACKGROUND'],
            3)
        self.assertAlmostEqual(
            background_postprocess_level_percent,
            default.entity_percentages['postprocess_char_level']['BACKGROUND'],
            3)
        self.assertEqual(27, default.word_sample_size)
        self.assertEqual(170, default.char_sample_size)
        self.assertEqual(
            23, default.entity_counts['word_level']['BACKGROUND'])
        self.assertEqual(
            106, default.entity_counts['true_char_level']['BACKGROUND'])
        self.assertEqual(
            120, default.entity_counts['postprocess_char_level']['BACKGROUND'])
        self.assertIsNone(default._get_percentages('WRONG_INPUT'))

        default.update(sample)
        self.assertEqual(54, default.word_sample_size)
        self.assertEqual(340, default.char_sample_size)

    @mock.patch('data_profiler.profilers.'
                'unstructured_data_labeler_column_profile.DataLabeler')
    @mock.patch('data_profiler.profilers.'
                'unstructured_data_labeler_column_profile.'
                'CharPostprocessor')
    def test_profile(self, processor_class_mock, model_class_mock):
        # setup mocks
        model_mock = mock.Mock()
        model_mock.reverse_label_mapping = {1: 'BACKGROUND'}
        model_mock.predict.return_value = dict(pred=[[1]])
        model_class_mock.return_value = model_mock
        processor_mock = mock.Mock()
        processor_mock.process.return_value = dict(pred=[[]])
        processor_class_mock.return_value = processor_mock

        # initialize labeler profile
        default = UnstructuredDataLabelerProfile()

        sample = pd.Series(["a"])
        expected_profile = dict(
            entity_counts={
                'postprocess_char_level': defaultdict(int, {'BACKGROUND': 1}),
                'true_char_level': defaultdict(int, {'BACKGROUND': 1}),
                'word_level': defaultdict(int)
            },
            times=defaultdict(float, {'data_labeler_predict': 1.0})
        )

        time_array = [float(i) for i in range(4, 0, -1)]
        with mock.patch('time.time', side_effect=lambda: time_array.pop()):
            default.update(sample)
        profile = default.profile

        # key and value populated correctly
        self.assertDictEqual(expected_profile, profile)
        

if __name__ == '__main__':
    unittest.main()
