601,100
602,"0.Intermediate"
562,"NULL"
586,
585,
564,
565,"dieMaX5?Mh]sM[RBmF;k<tbM0@@cA?DMq_hf?_P5q@y4IcPW_J \ ?W1PaA \ DGQTT2B_r:PUYAu5feMrIN6]P8w1e9VyWE]hZ8Rzvzg5?7FRa10rrJQdJLo;MDdD = 6Kb_nYnTYGYhzJjA<?jp>xSm \ Cp7QEmvLCp=4ao20?s1sygk;58=_We@CfnQkroTK9P \ _8Qab`2e6"
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
572,25

#****Begin: Generated Statements***
#****End: Generated Statements****

sErr = '';
sProcess = GetProcessName();

### Run child process a bunch of times

ExecuteProcess('0.Child', 'pOne', 1, 'pTwo', 2, 'pThree', 3);

ExecuteProcess('0.Child', 'pOne', 7, 'pTwo', 2, 'pThree', 4);

ExecuteProcess('0.Child', 'pOne', 1, 'pTwo', 7, 'pThree', 3);

ExecuteProcess('0.Child', 'pOne', 1, 'pTwo', 7, 'pThree', 3);

ExecuteProcess('0.Child', 'pOne', 1, 'pTwo', 2, 'pThree', 3);


### Throw a random error.
IF (1 <> 2);
	sErr = Expand('This process also had an error!!! Wow! One does NOT equal 2.');
ENDIF;

573,3

#****Begin: Generated Statements***
#****End: Generated Statements****
574,3

#****Begin: Generated Statements***
#****End: Generated Statements****
575,9

#****Begin: Generated Statements***
#****End: Generated Statements****

IF (sErr @<> '');
	sGlobalErr = Expand( '%sGlobalErr% ERROR in "%sProcess%": %sErr%   - --   ');
	ItemReject(sErr);
ENDIF;

576,CubeAction = 1511
DataAction = 1503
CubeLogChanges = 0

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
