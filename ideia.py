import re
alert_report = re.compile(\
    "(ST300ALT);([0-9]{9});([0-9]{2});([0-9]{3});([0-9]{8});\
     ([0-9]{2}:[0-9]{2}:[0-9]{2});(.{4}[0-9]{2});\
     ([\+|\-][0-9]{2}.[0-9]{6});([\+|\-][0-9]{3}.[0-9]{6});\
     ([0-9]{3}.[0-9]{3});([0-9]{3}.[0-9]{2})", flags=0)

    ST300ALT;205762603;05;469;20170808;
    03:32:16;
    5bbe19;
    -05.025189;
    -042.813043;
    000.069;
    000.00;
    10;
    1;
    3694;
    12.04;
    000000;
    15;
    000140;
    3.8;
    0\r
