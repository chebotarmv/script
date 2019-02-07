#!/usr/bin/python
import click
import sys
import os


@click.group()
def cli():
    pass


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-l', 'lines', is_flag=True, help='Count of lines in file.')
@click.option('-w', 'words', is_flag=True, help='Count of words in file.')
@click.option('-c', 'bytes', is_flag=True, help='Count of bytes in file.' )
def count_file(file, lines, words, bytes):
    """This comand count lines, words and bytes in file."""
    countlines = 0
    countwords = 0
    countbytes = 0
    if lines:
        with open(file, 'r') as myfile:
            for line in myfile:
                line.split('\n')
                countlines += 1
            print (countlines)
    elif words:
        with open(file, 'r') as myfile:
            for line in myfile:
                words = line.split()
                countwords += len(words)
            print (countwords)
    elif bytes:
        countbytes += os.path.getsize(file)
        print (countbytes)
    else:
        with open(file) as myfile:
            for line in myfile:
                line = line.split()
                countwords += len(line)
                countlines += 1
        countbytes += os.path.getsize(file)
        print(countlines, countwords,countbytes)

@click.command()
@click.argument('text', nargs=-1)
@click.option('-l', 'lines', is_flag=True, help='Count of lines in text.')
@click.option('-w', 'words', is_flag=True, help='Count of words in text.')
@click.option('-c', 'bytes', is_flag=True, help='Count of bytes in text.' )
def count_text(text, lines, words, bytes):
    """This comand count lines, words and bytes in text."""
    countlines = 0
    countwords = 0
    countbytes = 0
    if lines:
        for line in text:
            line = line.splitlines()
        countlines += len(line)
        print (countlines)
    elif words:
        for line in text:
            words = line.split()
            countwords += len(words)
        print (countwords)
    elif bytes:
        countbytes += sys.getsizeof(text)
        print (countbytes)
    else:
        for line in text:
            line = line.splitlines()
            countwords += len(line)
        countlines += len(line)
        countbytes += sys.getsizeof(text)
        print(countlines, countwords,countbytes)




cli.add_command(count_file)
cli.add_command(count_text)

if __name__ == "__main__":
    cli()

