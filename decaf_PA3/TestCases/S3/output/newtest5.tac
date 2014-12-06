VTABLE(_Main) {
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
    _T10 = 3
    _T3 = _T10
    _T11 = _T3
    _T12 = 1
    _T13 = (_T3 + _T12)
    _T3 = _T13
    _T14 = _T3
    _T15 = 1
    _T16 = (_T3 + _T15)
    _T3 = _T16
    _T17 = (_T11 + _T14)
    _T7 = _T17
    _T18 = 1
    _T19 = (_T3 + _T18)
    _T3 = _T19
    _T20 = 1
    _T21 = (_T3 + _T20)
    _T3 = _T21
    _T22 = (_T19 + _T21)
    _T8 = _T22
    _T23 = _T3
    _T24 = 1
    _T25 = (_T3 + _T24)
    _T3 = _T25
    _T26 = 1
    _T27 = (_T3 + _T26)
    _T3 = _T27
    _T28 = (_T23 + _T27)
    _T9 = _T28
    _T29 = _T3
    _T30 = 1
    _T31 = (_T3 + _T30)
    _T3 = _T31
    _T32 = _T3
    _T33 = 1
    _T34 = (_T3 + _T33)
    _T3 = _T34
    _T35 = (_T29 * _T32)
    _T3 = _T35
    parm _T7
    call _PrintInt
    _T36 = "\n"
    parm _T36
    call _PrintString
    parm _T8
    call _PrintInt
    _T37 = "\n"
    parm _T37
    call _PrintString
    parm _T9
    call _PrintInt
    _T38 = "\n"
    parm _T38
    call _PrintString
    parm _T3
    call _PrintInt
    _T39 = "\n"
    parm _T39
    call _PrintString
}

