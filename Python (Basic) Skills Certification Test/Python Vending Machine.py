#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    def __init__(self, items, coins):
        self.items = items
        self.coins = coins
        
    def buy(self, items, coins):
        try:
            if (self.items >= items):
                if (coins >= int(items * self.coins)):
                    self.items -= items
                    return int(coins-items*self.coins)
                else:
                    raise ValueError("Not enough coins")
            else:
                raise ValueError("Not enough items in the machine")
        except ValueError as err:
            return err
    pass

if __name__ == '__main__':
    fptr = open((__file__).replace((__file__).split("\\")[len((__file__).split("\\"))-1], '') + "output.txt", 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
