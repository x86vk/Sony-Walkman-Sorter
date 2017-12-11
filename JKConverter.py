#!/usr/bin/python3
# -*- coding:utf-8 -*-

import logging

logger = logging.getLogger("JKConverter")

japanese_dict = {"あ": "a",
                 "ア": "a",
                 "い": "i",
                 "イ": "i",
                 "う": "u",
                 "ウ": "u",
                 "え": "e",
                 "エ": "e",
                 "お": "o",
                 "オ": "o",
                 "か": "ka",
                 "カ": "ka",
                 "き": "ki",
                 "キ": "ki",
                 "く": "ku",
                 "ク": "ku",
                 "け": "ke",
                 "ケ": "ke",
                 "こ": "ko",
                 "コ": "ko",
                 "さ": "sa",
                 "サ": "sa",
                 "し": "shi",
                 "シ": "shi",
                 "す": "su",
                 "ス": "su",
                 "せ": "se",
                 "セ": "se",
                 "そ": "so",
                 "ソ": "so",
                 "た": "ta",
                 "タ": "ta",
                 "ち": "chi",
                 "チ": "chi",
                 "つ": "tsu",
                 "ツ": "tsu",
                 "て": "te",
                 "テ": "te",
                 "と": "to",
                 "ト": "to",
                 "な": "na",
                 "ナ": "na",
                 "に": "ni",
                 "ニ": "ni",
                 "ぬ": "nu",
                 "ヌ": "nu",
                 "ね": "ne",
                 "ネ": "ne",
                 "の": "no",
                 "ノ": "no",
                 "は": "ha",
                 "ハ": "ha",
                 "ひ": "hi",
                 "ヒ": "hi",
                 "ふ": "fu",
                 "フ": "fu",
                 "へ": "he",
                 "ヘ": "he",
                 "ほ": "ho",
                 "ホ": "ho",
                 "ま": "ma",
                 "マ": "ma",
                 "み": "mi",
                 "ミ": "mi",
                 "む": "mu",
                 "ム": "mu",
                 "め": "me",
                 "メ": "me",
                 "も": "mo",
                 "モ": "mo",
                 "や": "ya",
                 "ヤ": "ya",
                 "ゆ": "yu",
                 "ユ": "yu",
                 "よ": "yo",
                 "ヨ": "yo",
                 "ら": "ra",
                 "ラ": "ra",
                 "り": "ri",
                 "リ": "ri",
                 "る": "ru",
                 "ル": "ru",
                 "れ": "re",
                 "レ": "re",
                 "ろ": "ro",
                 "ロ": "ro",
                 "わ": "wa",
                 "ワ": "wa",
                 "を": "o",
                 "ヲ": "o",
                 "ん": "n",
                 "ン": "n",
                 "が": "ga",
                 "ガ": "ga",
                 "ぎ": "gi",
                 "ギ": "gi",
                 "ぐ": "gu",
                 "グ": "gu",
                 "げ": "ge",
                 "ゲ": "ge",
                 "ご": "go",
                 "ゴ": "go",
                 "ざ": "za",
                 "ザ": "za",
                 "じ": "ji",
                 "ジ": "ji",
                 "ず": "zu",
                 "ズ": "zu",
                 "ぜ": "ze",
                 "ゼ": "ze",
                 "ぞ": "zo",
                 "ゾ": "zo",
                 "だ": "da",
                 "ダ": "da",
                 "ぢ": "ji",
                 "ヂ": "ji",
                 "づ": "zu",
                 "ヅ": "zu",
                 "で": "de",
                 "デ": "de",
                 "ど": "do",
                 "ド": "do",
                 "ば": "ba",
                 "バ": "ba",
                 "び": "bi",
                 "ビ": "bi",
                 "ぶ": "bu",
                 "ブ": "bu",
                 "べ": "be",
                 "ベ": "be",
                 "ぼ": "bo",
                 "ボ": "bo",
                 "ぱ": "pa",
                 "パ": "pa",
                 "ぴ": "pi",
                 "ピ": "pi",
                 "ぷ": "pu",
                 "プ": "pu",
                 "ぺ": "pe",
                 "ペ": "pe",
                 "ぽ": "po",
                 "ポ": "po"}

korean_dict = {}


# TODO  Add Korean Dictionary

def convert(jkStr):
    result = ""
    for jkChar in jkStr:
        if jkChar in japanese_dict:
            result += japanese_dict[jkChar]
        elif jkChar in korean_dict:
            result += korean_dict[jkChar]
        else:
            logger.debug('unknown char {0}'.format(jkChar))
            result += jkChar
    return result