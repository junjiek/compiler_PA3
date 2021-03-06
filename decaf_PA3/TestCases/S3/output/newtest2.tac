VTABLE(_Math) {
    Math
}

VTABLE(_Main) {
    Main
}

FUNCTION(_Math_New) {
memo ''
_Math_New:
    _T8 = 4
    parm _T8
    _T9 =  call _Alloc
    _T10 = VTBL <_Math>
    *(_T9 + 0) = _T10
    return _T9
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T11 = 4
    parm _T11
    _T12 =  call _Alloc
    _T13 = VTBL <_Main>
    *(_T12 + 0) = _T13
    return _T12
}

FUNCTION(_Math.abs) {
memo '_T0:4'
_Math.abs:
    _T14 = 0
    _T15 = (_T0 >= _T14)
    if (_T15 == 0) branch _L16
    return _T0
    branch _L17
_L16:
    _T16 = - _T0
    return _T16
_L17:
}

FUNCTION(_Math.pow) {
memo '_T1:4 _T2:8'
_Math.pow:
    _T19 = 1
    _T18 = _T19
    _T20 = 0
    _T17 = _T20
    branch _L18
_L19:
    _T21 = 1
    _T22 = (_T17 + _T21)
    _T17 = _T22
_L18:
    _T23 = (_T17 < _T2)
    if (_T23 == 0) branch _L20
    _T24 = (_T18 * _T1)
    _T18 = _T24
    branch _L19
_L20:
    return _T18
}

FUNCTION(_Math.log) {
memo '_T3:4'
_Math.log:
    _T25 = 1
    _T26 = (_T3 < _T25)
    if (_T26 == 0) branch _L21
    _T27 = 1
    _T28 = - _T27
    return _T28
_L21:
    _T30 = 0
    _T29 = _T30
_L22:
    _T31 = 1
    _T32 = (_T3 > _T31)
    if (_T32 == 0) branch _L23
    _T33 = _T29
    _T34 = 1
    _T35 = (_T29 + _T34)
    _T29 = _T35
    _T36 = 2
    _T37 = (_T3 / _T36)
    _T3 = _T37
    branch _L22
_L23:
    return _T29
}

FUNCTION(_Math.max) {
memo '_T4:4 _T5:8'
_Math.max:
    _T39 = (_T4 > _T5)
    if (_T39 == 0) branch _L24
    _T38 = _T4
    branch _L25
_L24:
    _T38 = _T5
_L25:
    return _T38
}

FUNCTION(_Math.min) {
memo '_T6:4 _T7:8'
_Math.min:
    _T41 = (_T6 < _T7)
    if (_T41 == 0) branch _L26
    _T40 = _T6
    branch _L27
_L26:
    _T40 = _T7
_L27:
    return _T40
}

FUNCTION(main) {
memo ''
main:
    _T42 = 1
    _T43 = - _T42
    parm _T43
    _T44 =  call _Math.abs
    parm _T44
    call _PrintInt
    _T45 = "\n"
    parm _T45
    call _PrintString
    _T46 = 2
    _T47 = 3
    parm _T46
    parm _T47
    _T48 =  call _Math.pow
    parm _T48
    call _PrintInt
    _T49 = "\n"
    parm _T49
    call _PrintString
    _T50 = 16
    parm _T50
    _T51 =  call _Math.log
    parm _T51
    call _PrintInt
    _T52 = "\n"
    parm _T52
    call _PrintString
    _T53 = 1
    _T54 = 2
    parm _T53
    parm _T54
    _T55 =  call _Math.max
    parm _T55
    call _PrintInt
    _T56 = "\n"
    parm _T56
    call _PrintString
    _T57 = 1
    _T58 = 2
    parm _T57
    parm _T58
    _T59 =  call _Math.min
    parm _T59
    call _PrintInt
    _T60 = "\n"
    parm _T60
    call _PrintString
}

