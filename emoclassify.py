# library imports
import click
from transformers import pipeline


def get_classifier():
    """
    Function to get the emotion classifier

    Args:
        None

    Returns:
        classifier (transformers.pipelines.TextClassificationPipeline): Emotion classifier
    """

    # load the emotion classifier
    classifier = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=None,
    )

    return classifier


def run_classifier(text):
    """
    Function to run the emotion classifier on the given text

    Args:
        text (str): Text to run the emotion classifier on

    Returns:
        result (str): Result of the emotion classifier
    """

    classifier = get_classifier()
    scores = classifier(text)
    result = f"""
    The top 3 emotions in the given text are:
    1. {scores[0][0]["label"]} - {scores[0][0]["score"]*100:.0f}%
    2. {scores[0][1]["label"]} - {scores[0][1]["score"]*100:.0f}%
    3. {scores[0][2]["label"]} - {scores[0][2]["score"]*100:.0f}%
    """
    return result


@click.command
@click.option(
    "--file-path",
    "-f",
    type=click.Path(exists=True),
    help="Path to input text file for emotion classification",
    required=True,
)
def main(file_path):
    """
    Function to run the emotion classifier on the given text file

    Args:
        file_path (str): Path to input text file for emotion classification

    Returns:
        None
    """

    # check if file path is provided
    if file_path is None:
        print("[INFO] Please provide the text input file")
        return

    # read the text file
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # run the emotion classifier
    result = run_classifier(text)

    # print the result
    click.echo(result)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
