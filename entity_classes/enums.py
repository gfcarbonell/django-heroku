#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from enum import Enum, unique

@unique
class EntityScope(Enum):
    ''' 
        This Enumeration: EntityScope is for to identify the category or scope of an entity.
        Esta Enumeración: AmbitoEntidad es para identificar la categoría, ámbito o alcanze de una entidad.
        
        Attributes - Atributos
            >Economic Activity | Actividad Econónica
            >Legal Form | Forma Jurídica
            >Scope of Operation | Ámbito de Operación
            >Size | Tamaño
            >Capital Composition | Composición del Capital
    '''
    ECONOMIC_ACTIVITY = 'Actividad Econónica'
    SCOPE_OF_OPERATION = 'Ámbito de Operación'
    CAPITAL_COMPOSITION = 'Composición del Capital'
    LEGAL_FORM = 'Forma Jurídica'
    SIZE = 'Tamaño'
   
