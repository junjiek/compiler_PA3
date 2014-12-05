VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T5 = 4
    _T3 = _T5
    _T6 = 3
    _T4 = _T6
    _T7 = _T4
    _T8 = 1
    _T9 = (_T4 + _T8)
    _T4 = _T9
    _T3 = _T7
    _T10 = 4
    _T11 = (_T3 != _T10)
    if (_T11 == 0) branch _L10
    parm _T4
    call _PrintInt
    _T12 = "\n"
    parm _T12
    call _PrintString
_L10:
    _T16 = _T3
    _T17 = 1
    _T18 = (_T3 + _T17)
    _T3 = _T18
    _T19 = _T3
    _T20 = 1
    _T21 = (_T3 + _T20)
    _T3 = _T21
    _T22 = (_T16 + _T19)
    _T13 = _T22
    _T23 = 1
    _T24 = (_T3 + _T23)
    _T3 = _T24
    _T25 = 1
    _T26 = (_T3 + _T25)
    _T3 = _T26
    _T27 = (_T24 + _T26)
    _T14 = _T27
    _T28 = _T3
    _T29 = 1
    _T30 = (_T3 + _T29)
    _T3 = _T30
    _T31 = 1
    _T32 = (_T3 + _T31)
    _T3 = _T32
    _T33 = (_T28 + _T32)
    _T15 = _T33
    _T34 = _T3
    _T35 = 1
    _T36 = (_T3 + _T35)
    _T3 = _T36
    _T37 = _T3
    _T38 = 1
    _T39 = (_T3 + _T38)
    _T3 = _T39
    _T40 = (_T34 * _T37)
    _T3 = _T40
    parm _T13
    call _PrintInt
    _T41 = "\n"
    parm _T41
    call _PrintString
    parm _T14
    call _PrintInt
    _T42 = "\n"
    parm _T42
    call _PrintString
    parm _T15
    call _PrintInt
    _T43 = "\n"
    parm _T43
    call _PrintString
    parm _T3
    call _PrintInt
    _T44 = "\n"
    parm _T44
    call _PrintString
}

