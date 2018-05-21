#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from enum import Enum, unique


@unique
class PersonType(Enum):
    NATURAL = 'Natural'
    LEGAL = 'Jurídica'


@unique
class Gender(Enum):
    MALE = 'Masculino'
    FEMALE = 'Femenino'
    OTHERS = 'Otros'

@unique
class MaritalStatus(Enum):
    SINGLE = 'Soltero'
    MARRIED = 'Casado'
    DIVORCED = 'Divorciado'
    SEPARATED = 'Separado'
    WIDOWER = 'Viudo'

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
