#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from enum import Enum, unique


@unique
class InstructionLevel(Enum):
    NO_LEVEL = 'Sin nivel'
    PRESCHOOL = 'Pre escolar'
    PRIMARY = 'Primario'
    HIGH_SCHOOL = 'Secundario'
    HIGHER = 'Superior'
