601,100
602,"0.Master"
562,"NULL"
586,
585,
564,
565,"wu6dfmz<@ \ r:[fkZv1wC^iWa<9c?<EJ<kjjba4`dtiDHlRl \ n8Kh>7^xD_fenOv[;vMSx9CAeq:9]h5gYWb`ma_2u83jxYmyHDkjkE0^OWCgbNpM:Zp2?qUgOx57uLI8t3W03?h8 \ uZ_jQOI;yJN_pVb8FfnSTHHHoRUDkb8iqw@Zfj1ywf5Psd0dokm5NKSLc2:`ZxH"
559,1
928,0
593,
594,
595,
597,
598,
596,
800,
801,
566,0
567,","
588,"."
589,
568,""""
570,
571,
569,0
592,0
599,1000
560,0
561,0
590,0
637,0
577,0
578,0
579,0
580,0
581,0
582,0
603,0
572,18

#****Begin: Generated Statements***
#****End: Generated Statements****

#LASTUPDATED by TIdy 06 October 2019
sErr = '';
StringGlobalVariable('sGlobalErr');


StringGlobalVariable('sErr');


#ExecuteProcess('0.Intermediate');

ExecuteProcess('0.Child', 'pOne', 1, 'pTwo', 2, 'pThree', 7);



573,3

#****Begin: Generated Statements***
#****End: Generated Statements****
574,3

#****Begin: Generated Statements***
#****End: Generated Statements****
575,8

#****Begin: Generated Statements***
#****End: Generated Statements****

sErr = sErr | sGlobalErr;
IF (sErr @<> '');
	ItemReject(sErr);
ENDIF;
576,CubeAction=1511
DataAction=1503
CubeLogChanges=0

930,0
638,1
804,0
1217,0
900,
901,
902,
938,0
937,
936,
935,
934,
932,0
933,0
903,
906,
929,
907,
908,
904,0
905,0
909,0
911,
912,
913,
914,
915,
916,
917,0
918,1
919,0
920,50000
921,""
922,""
923,0
924,""
925,""
926,""
927,""
