#!/usr/bin/env python3

from brain_games.games.brain_even import provide_task
from brain_games.games.brain_even import operation_type
from brain_games.games.brain_even import operation_result
from brain_games.engine import welcome_user
from brain_games.engine import explain_details
from brain_games.engine import launch_game
from brain_games.engine import name


def main():
    welcome_user()
    explain_details(provide_task())
    launch_game(operation_type(), operation_result())

if __name__ == '__main__':
    main()
