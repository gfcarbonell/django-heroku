#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from enum import Enum, unique


@unique
class PersonType(Enum):
    NATURAL = 'Natural'
    LEGAL = 'Legal'


@unique
class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


@unique
class MaritalStatus(Enum):
    SINGLE = 'Single'
    MARRIED = 'Legal'
    DIVORCED = 'Divorced'
    SEPARATED = 'Separated'
    WIDOWER = 'Widower'

@unique
class BloodGroup(Enum):
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'
