# library imports
import transformers
import pytest
from click.testing import CliRunner
from emoclassify import main, get_classifier


def test_get_classifier():
    """
    Function to test the get_classifier function
    """

    # get the classifier
    classifier = get_classifier()

    # check the classifier is not None and is of the correct type
    assert classifier is not None
    assert isinstance(classifier, transformers.pipelines.TextClassificationPipeline)


@pytest.mark.parametrize(
    "file_path, expected_output",
    [
        (
            "tests/test_1.txt",
            "\n    The top 3 emotions in the given text are:\n    1. joy - 98%\n    2. surprise - 1%\n    3. neutral - 1%\n    \n",
        ),
        (
            "tests/test_2.txt",
            "\n    The top 3 emotions in the given text are:\n    1. surprise - 97%\n    2. disgust - 1%\n    3. neutral - 1%\n    \n",
        ),
    ],
)
def test_main(file_path, expected_output):
    """
    Function to test the emoclassify script's main function using the click.testing.CliRunner
    """

    # create a click testing runner
    runner = CliRunner()

    # run the main function with the provided inputs
    result = runner.invoke(main, ["-f", file_path])

    # check the output is as expected
    assert result.exit_code == 0
    assert expected_output in result.output
