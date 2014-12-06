VTABLE(_Main) {
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T3 = 4
    parm _T3
    _T4 =  call _Alloc
    _T5 = VTBL <_Main>
    *(_T4 + 0) = _T5
    return _T4
}

FUNCTION(_Main.isLeapYear) {
memo '_T0:4'
_Main.isLeapYear:
    _T6 = 4
    _T7 = (_T0 % _T6)
    _T8 = 0
    _T9 = (_T7 == _T8)
    _T10 = 400
    _T11 = (_T0 % _T10)
    _T12 = 0
    _T13 = (_T11 == _T12)
    _T14 = 100
    _T15 = (_T0 % _T14)
    _T16 = 0
    _T17 = (_T15 != _T16)
    _T18 = (_T13 || _T17)
    _T19 = (_T9 && _T18)
    return _T19
}

FUNCTION(_Main.getNumberOfDays) {
memo '_T1:4 _T2:8'
_Main.getNumberOfDays:
    _T20 = 1
    _T21 = (_T2 - _T20)
    if (_T21 == 0) branch _L14
    _T22 = 2
    _T23 = (_T2 - _T22)
    if (_T23 == 0) branch _L15
    _T24 = 3
    _T25 = (_T2 - _T24)
    if (_T25 == 0) branch _L16
    _T26 = 4
    _T27 = (_T2 - _T26)
    if (_T27 == 0) branch _L17
    _T28 = 5
    _T29 = (_T2 - _T28)
    if (_T29 == 0) branch _L18
    _T30 = 6
    _T31 = (_T2 - _T30)
    if (_T31 == 0) branch _L19
    _T32 = 7
    _T33 = (_T2 - _T32)
    if (_T33 == 0) branch _L20
    _T34 = 8
    _T35 = (_T2 - _T34)
    if (_T35 == 0) branch _L21
    _T36 = 9
    _T37 = (_T2 - _T36)
    if (_T37 == 0) branch _L22
    _T38 = 10
    _T39 = (_T2 - _T38)
    if (_T39 == 0) branch _L23
    _T40 = 11
    _T41 = (_T2 - _T40)
    if (_T41 == 0) branch _L24
    _T42 = 12
    _T43 = (_T2 - _T42)
    if (_T43 == 0) branch _L25
    branch _L13
_L14:
    _T44 = 31
    return _T44
    branch _L12
_L15:
    parm _T1
    _T46 =  call _Main.isLeapYear
    if (_T46 == 0) branch _L26
    _T47 = 29
    _T45 = _T47
    branch _L27
_L26:
    _T48 = 28
    _T45 = _T48
_L27:
    return _T45
    branch _L12
_L16:
    _T49 = 31
    return _T49
    branch _L12
_L17:
    _T50 = 30
    return _T50
    branch _L12
_L18:
    _T51 = 31
    return _T51
    branch _L12
_L19:
    _T52 = 30
    return _T52
    branch _L12
_L20:
    _T53 = 31
    return _T53
    branch _L12
_L21:
    _T54 = 31
    return _T54
    branch _L12
_L22:
    _T55 = 30
    return _T55
    branch _L12
_L23:
    _T56 = 31
    return _T56
    branch _L12
_L24:
    _T57 = 30
    return _T57
    branch _L12
_L25:
    _T58 = 31
    return _T58
    branch _L12
_L13:
    _T59 = 1
    _T60 = - _T59
    return _T60
    branch _L12
_L12:
}

FUNCTION(main) {
memo ''
main:
    _T64 = 2014
    _T62 = _T64
    _T65 = 11
    _T63 = _T65
    parm _T62
    parm _T63
    _T66 =  call _Main.getNumberOfDays
    parm _T66
    call _PrintInt
}

