VTABLE(_Main) {
    <empty>
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
}

FUNCTION(main) {
memo ''
main:
    _T23 = 2014
    _T21 = _T23
    _T24 = 11
    _T22 = _T24
    parm _T21
    parm _T22
    _T25 =  call _Main.getNumberOfDays
    parm _T25
    call _PrintInt
}

