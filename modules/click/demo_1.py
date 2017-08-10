#!/usr/bin/python
import click
import math
import colorama

@click.command()
@click.argument('x1')
@click.argument('y1')
@click.argument('x2')
@click.argument('y2')
def distance(x1, y1, x2, y2):
	"""Calculate the distance between (x1, y1) and (x2, y2)"""
	click.secho('The distance between (%s, %s) and (%s, %s) is: ' % (x1, y1, x2, y2), bg='white', fg='black', bold=True)
	click.secho('%s' % (math.sqrt((float(y2) - float(y1))**2 + (float(x2) - float(x1))**2)), bg='white', fg='red', dim=True)

if __name__ == '__main__':
	distance()

