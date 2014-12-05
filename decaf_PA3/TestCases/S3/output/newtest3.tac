VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T1 = 4
    parm _T1
    _T2 =  call _Alloc
    _T3 = VTBL <_Main>
    *(_T2 + 0) = _T3
    return _T2
}

FUNCTION(main) {
memo ''
main:
    _T5 = 10
    _T6 = 10
    _T7 = (_T5 * _T6)
    _T4 = _T7
    parm _T4
    _T8 =  call _Main.isSquare
    parm _T8
    call _PrintBool
    _T9 = "\n"
    parm _T9
    call _PrintString
    _T10 = 99
    parm _T10
    _T11 =  call _Main.isSquare
    parm _T11
    call _PrintBool
}

FUNCTION(_Main.isSquare) {
memo '_T0:4'
_Main.isSquare:
    _T14 = 0
    _T12 = _T14
_L11:
    _T15 = 1
    _T16 = (_T12 + _T15)
    _T12 = _T16
    _T17 = (_T0 / _T12)
    _T13 = _T17
    _T18 = (_T12 >= _T13)
    if (_T18 != 0) branch _L12
    branch _L11
_L12:
    _T19 = (_T13 * _T13)
    _T20 = (_T0 == _T19)
    return _T20
}

