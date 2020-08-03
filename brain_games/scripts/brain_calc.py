#!/usr/bin/env python3
import brain_games.modules.brain_calc
import brain_games.cli


def main():
    list = brain_games.modules.brain_calc.main()
    brain_games.cli.engine(list)


if __name__ == '__main__':
    main()
