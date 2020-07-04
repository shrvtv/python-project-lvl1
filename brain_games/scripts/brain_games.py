#!/usr/bin/env python3
import brain_games.cli


def main():
	print('Welcome to the Brain Games!')
	name = brain_games.cli.get_name()
	brain_games.cli.hello(name)


if __name__ == '__main__':
	main()
