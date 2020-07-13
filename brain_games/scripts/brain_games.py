#!/usr/bin/env python3
import brain_games.cli


def main():
	print('Welcome to the Brain Games!')
	brain_games.cli.hello(brain_games.cli.get_name())


if __name__ == '__main__':
	main()
