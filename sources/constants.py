#!/usr/bin/python
# -*- coding: utf-8 -*-s

class Constants:
    # DISPLAY SIZE
    DISPLAY_W: int = 1280
    DISPLAY_H: int = 720

    # ASSETS DICTIONARY
    ASSETS: dict

    # COLOR
    WHITE: tuple = (255, 255, 255)
    BLACK: tuple = (0, 0, 0)
    RED: tuple = (255, 0, 0)
    BACKGROUND: tuple = (78, 150, 142)

    GOLD: tuple = (255, 174, 49)
    SILVER: tuple = (181, 216, 213)
    BRONZE: tuple = (217, 116, 82)

    # REGEX
    USERNAME_REGEX: str = r"([0-9A-Za-z.\-_*$£&])"

    # SCORE
    SEP = ","

    # SPRITES
    SCORE_VALUE: int = 100
    TIME_INCREASE_DIFFICULTY: int = 25
    NB_SPRITES: int = 5
    VELOCITY: int = 8
    SPRITES: list = []
    SPRITE_AVAILABLE: dict = {"CANNONBALL": True, "HEART": True, "EGG": True, "STAR": True, "COIN": True,
                              "BLUE_GEM": True, "GREEN_GEM": True, "RUBY": True}
