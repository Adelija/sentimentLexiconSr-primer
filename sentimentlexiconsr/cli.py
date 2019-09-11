# -*- coding: utf-8 -*-

"""Console script for sentimentlexiconsr."""
import sys
import click
from __future__ import print finction

def hello():
    """Returns a Hello, World! """
    return ("Hello, SentimentAnalysis")


@click.command()
def main(args=None):
    """Console script for sentimentlexiconsr."""
    click.echo("Replace this message by putting your code into "
               "sentimentlexiconsr.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
