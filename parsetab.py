
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftLESSTHANLESSEQUALGREATERTHANGREATEREQUALleftPLUSMINUSleftMULTIPLYDIVIDEleftPOWrightNOTAND ASSIGN BOOL CHAR COMMA DISPLAY DIVIDE DOT DOUBLE ELSE ELSEIF EQUALS GREATEREQUAL GREATERTHAN IDENTIFIER IF INDEX INT LCURLY LESSEQUAL LESSTHAN LROUND LSQBRAC MINUS MINUSMINUS MULTIPLY NEWLINE NOT NOTEQUAL OR PLUS PLUSPLUS POP POW PUSH RCURLY RROUND RSQBRAC SEMICOLON SLICE STRING TYPEelement : stmt SEMICOLONstmt : DISPLAY LROUND params RROUNDoptparams : paramsoptparams : params : exp l_comma paramsparams : stmt : if elseif elseif : IF exp c_stmtelseif : ELSEIF c_exp c_stmt elseifc_exp : expelseif : else : ELSE c_stmtelse : c_stmt : LCURLY c_stmt RCURLYc_stmt : stmtc_stmt : stmt : TYPE IDENTIFIER ASSIGN LSQBRAC listparams RSQBRACl_comma : COMMAl_comma : listparams : INT l_comma listparamslistparams : DOUBLE l_comma listparamslistparams : STRING l_comma listparamslistparams : CHAR l_comma listparamslistparams : BOOL l_comma listparamslistparams : exp : IDENTIFIER LSQBRAC optparams RSQBRACexp : IDENTIFIER DOT list_functions list_functions : PUSH LROUND pparams RROUNDlist_functions : POP LROUND pparams RROUNDlist_functions : SLICE LROUND sliceparams RROUNDlist_functions : INDEX LROUND indexparams RROUNDindexparams : expsliceparams : INTsliceparams : INT COMMA INTsliceparams : pparams : exppparams : stmt : IDENTIFIER ASSIGN expstmt : TYPE IDENTIFIERstmt : TYPE IDENTIFIER ASSIGN expstmt : expexp : LROUND exp RROUNDexp : BOOLexp : IDENTIFIERexp : STRINGexp : INTexp : DOUBLEexp : CHARexp : exp PLUS expexp : LROUND exp PLUS exp RROUNDexp : exp MINUS expexp : exp MULTIPLY expexp : exp DIVIDE expexp : NOT expexp : exp AND expexp : exp OR expexp : IDENTIFIER PLUSPLUSexp : IDENTIFIER MINUSMINUSexp : exp LESSTHAN expexp : exp GREATERTHAN expexp : exp LESSEQUAL expexp : exp GREATEREQUAL expexp : exp NOTEQUAL expexp : exp EQUALS expexp : exp POW expexp : MINUS exp'
    
_lr_action_items = {'DISPLAY':([0,10,11,12,13,14,20,27,28,42,43,44,47,50,51,52,57,62,63,64,65,66,67,68,69,70,71,72,73,74,77,87,92,95,117,118,119,121,],[3,-43,-45,-46,-47,-48,-44,-57,-58,3,-66,-54,-42,3,3,-10,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,3,-26,-51,-50,-28,-29,-30,-31,]),'TYPE':([0,10,11,12,13,14,20,27,28,42,43,44,47,50,51,52,57,62,63,64,65,66,67,68,69,70,71,72,73,74,77,87,92,95,117,118,119,121,],[6,-43,-45,-46,-47,-48,-44,-57,-58,6,-66,-54,-42,6,6,-10,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,6,-26,-51,-50,-28,-29,-30,-31,]),'IDENTIFIER':([0,4,6,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,87,88,89,91,92,95,117,118,119,121,],[7,20,23,20,-43,-45,-46,-47,-48,20,20,20,-44,20,20,20,-57,-58,20,20,20,20,20,20,20,20,20,20,20,20,20,7,-66,-54,-19,-42,20,7,7,-10,20,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,20,7,20,-18,-26,20,20,20,-51,-50,-28,-29,-30,-31,]),'IF':([0,10,11,12,13,14,20,27,28,42,43,44,47,50,51,52,57,62,63,64,65,66,67,68,69,70,71,72,73,74,77,87,92,95,117,118,119,121,],[9,-43,-45,-46,-47,-48,-44,-57,-58,9,-66,-54,-42,9,9,-10,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,9,-26,-51,-50,-28,-29,-30,-31,]),'LROUND':([0,3,4,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,87,88,89,91,92,95,117,118,119,121,],[4,18,4,4,-43,-45,-46,-47,-48,4,4,4,-44,4,4,4,-57,-58,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-66,-54,-19,-42,4,4,4,-10,4,-27,88,89,90,91,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,4,4,4,-18,-26,4,4,4,-51,-50,-28,-29,-30,-31,]),'BOOL':([0,4,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,85,87,88,89,91,92,95,98,99,100,101,102,112,113,114,115,116,117,118,119,121,],[10,10,10,-43,-45,-46,-47,-48,10,10,10,-44,10,10,10,-57,-58,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-66,-54,-19,-42,10,10,10,-10,10,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,10,10,10,-18,102,-26,10,10,10,-51,-50,-19,-19,-19,-19,-19,102,102,102,102,102,-28,-29,-30,-31,]),'STRING':([0,4,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,85,87,88,89,91,92,95,98,99,100,101,102,112,113,114,115,116,117,118,119,121,],[11,11,11,-43,-45,-46,-47,-48,11,11,11,-44,11,11,11,-57,-58,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-66,-54,-19,-42,11,11,11,-10,11,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,11,11,11,-18,100,-26,11,11,11,-51,-50,-19,-19,-19,-19,-19,100,100,100,100,100,-28,-29,-30,-31,]),'INT':([0,4,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,85,87,88,89,90,91,92,95,98,99,100,101,102,112,113,114,115,116,117,118,119,120,121,],[12,12,12,-43,-45,-46,-47,-48,12,12,12,-44,12,12,12,-57,-58,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-66,-54,-19,-42,12,12,12,-10,12,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,12,12,12,-18,98,-26,12,12,107,12,-51,-50,-19,-19,-19,-19,-19,98,98,98,98,98,-28,-29,-30,127,-31,]),'DOUBLE':([0,4,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,85,87,88,89,91,92,95,98,99,100,101,102,112,113,114,115,116,117,118,119,121,],[13,13,13,-43,-45,-46,-47,-48,13,13,13,-44,13,13,13,-57,-58,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-66,-54,-19,-42,13,13,13,-10,13,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,13,13,13,-18,99,-26,13,13,13,-51,-50,-19,-19,-19,-19,-19,99,99,99,99,99,-28,-29,-30,-31,]),'CHAR':([0,4,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,85,87,88,89,91,92,95,98,99,100,101,102,112,113,114,115,116,117,118,119,121,],[14,14,14,-43,-45,-46,-47,-48,14,14,14,-44,14,14,14,-57,-58,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-66,-54,-19,-42,14,14,14,-10,14,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,14,14,14,-18,101,-26,14,14,14,-51,-50,-19,-19,-19,-19,-19,101,101,101,101,101,-28,-29,-30,-31,]),'NOT':([0,4,9,10,11,12,13,14,15,16,18,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,87,88,89,91,92,95,117,118,119,121,],[16,16,16,-43,-45,-46,-47,-48,16,16,16,-44,16,16,16,-57,-58,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-66,-54,-19,-42,16,16,16,-10,16,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,16,16,16,-18,-26,16,16,16,-51,-50,-28,-29,-30,-31,]),'MINUS':([0,4,7,8,9,10,11,12,13,14,15,16,18,19,20,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,53,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,80,81,82,86,87,88,89,91,92,95,104,109,117,118,119,121,],[15,15,-44,30,15,-43,-45,-46,-47,-48,15,15,15,30,-44,15,15,15,-57,-58,15,15,15,15,15,15,15,15,15,15,15,15,15,76,-66,-54,30,-42,15,15,15,30,15,30,-27,-49,-51,-52,-53,30,30,30,30,30,30,30,30,-65,15,15,15,-18,-49,30,-26,15,15,15,-51,-50,30,30,-28,-29,-30,-31,]),'$end':([1,17,],[0,-1,]),'SEMICOLON':([2,5,7,8,10,11,12,13,14,20,21,23,27,28,42,43,44,47,49,50,51,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,86,87,92,95,96,110,111,117,118,119,121,],[17,-11,-44,-41,-43,-45,-46,-47,-48,-44,-13,-39,-57,-58,-16,-66,-54,-42,-7,-16,-16,-10,-38,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,-8,-15,-2,-12,-11,-40,-26,-51,-50,-9,-14,-17,-28,-29,-30,-31,]),'ELSEIF':([5,7,8,10,11,12,13,14,20,21,23,27,28,42,43,44,47,49,50,51,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,86,87,92,95,96,110,111,117,118,119,121,],[22,-44,-41,-43,-45,-46,-47,-48,-44,-13,-39,-57,-58,-16,-66,-54,-42,-7,-16,-16,-10,-38,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,-8,-15,-2,-12,22,-40,-26,-51,-50,-9,-14,-17,-28,-29,-30,-31,]),'ELSE':([5,7,8,10,11,12,13,14,20,21,23,27,28,42,43,44,47,49,50,51,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,86,87,92,95,96,110,111,117,118,119,121,],[-11,-44,-41,-43,-45,-46,-47,-48,-44,50,-39,-57,-58,-16,-66,-54,-42,-7,-16,-16,-10,-38,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,-8,-15,-2,-12,-11,-40,-26,-51,-50,-9,-14,-17,-28,-29,-30,-31,]),'RCURLY':([5,7,8,10,11,12,13,14,20,21,23,27,28,42,43,44,47,49,50,51,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,78,79,83,84,86,87,92,93,95,96,110,111,117,118,119,121,],[-11,-44,-41,-43,-45,-46,-47,-48,-44,-13,-39,-57,-58,-16,-66,-54,-42,-7,-16,-16,-10,-38,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,-8,-16,-15,-2,-12,-11,-40,-26,-51,110,-50,-9,-14,-17,-28,-29,-30,-31,]),'ASSIGN':([7,23,],[24,53,]),'LSQBRAC':([7,20,53,],[25,25,85,]),'DOT':([7,20,],[26,26,]),'PLUS':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,29,-43,-45,-46,-47,-48,48,-44,-57,-58,29,-66,-54,29,-42,29,29,-27,-49,-51,-52,-53,29,29,29,29,29,29,29,29,-65,-49,29,-26,-51,-50,29,29,-28,-29,-30,-31,]),'MULTIPLY':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,31,-43,-45,-46,-47,-48,31,-44,-57,-58,31,31,-54,31,-42,31,31,-27,31,31,-52,-53,31,31,31,31,31,31,31,31,-65,31,31,-26,31,-50,31,31,-28,-29,-30,-31,]),'DIVIDE':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,32,-43,-45,-46,-47,-48,32,-44,-57,-58,32,32,-54,32,-42,32,32,-27,32,32,-52,-53,32,32,32,32,32,32,32,32,-65,32,32,-26,32,-50,32,32,-28,-29,-30,-31,]),'AND':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,33,-43,-45,-46,-47,-48,33,-44,-57,-58,33,-66,-54,33,-42,33,33,-27,-49,-51,-52,-53,-55,33,-59,-60,-61,-62,33,33,-65,-49,33,-26,-51,-50,33,33,-28,-29,-30,-31,]),'OR':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,34,-43,-45,-46,-47,-48,34,-44,-57,-58,34,-66,-54,34,-42,34,34,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,34,34,-65,-49,34,-26,-51,-50,34,34,-28,-29,-30,-31,]),'LESSTHAN':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,35,-43,-45,-46,-47,-48,35,-44,-57,-58,35,-66,-54,35,-42,35,35,-27,-49,-51,-52,-53,35,35,-59,-60,-61,-62,35,35,-65,-49,35,-26,-51,-50,35,35,-28,-29,-30,-31,]),'GREATERTHAN':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,36,-43,-45,-46,-47,-48,36,-44,-57,-58,36,-66,-54,36,-42,36,36,-27,-49,-51,-52,-53,36,36,-59,-60,-61,-62,36,36,-65,-49,36,-26,-51,-50,36,36,-28,-29,-30,-31,]),'LESSEQUAL':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,37,-43,-45,-46,-47,-48,37,-44,-57,-58,37,-66,-54,37,-42,37,37,-27,-49,-51,-52,-53,37,37,-59,-60,-61,-62,37,37,-65,-49,37,-26,-51,-50,37,37,-28,-29,-30,-31,]),'GREATEREQUAL':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,38,-43,-45,-46,-47,-48,38,-44,-57,-58,38,-66,-54,38,-42,38,38,-27,-49,-51,-52,-53,38,38,-59,-60,-61,-62,38,38,-65,-49,38,-26,-51,-50,38,38,-28,-29,-30,-31,]),'NOTEQUAL':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,39,-43,-45,-46,-47,-48,39,-44,-57,-58,39,-66,-54,39,-42,39,39,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,39,39,-65,-49,39,-26,-51,-50,39,39,-28,-29,-30,-31,]),'EQUALS':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,40,-43,-45,-46,-47,-48,40,-44,-57,-58,40,-66,-54,40,-42,40,40,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,40,40,-65,-49,40,-26,-51,-50,40,40,-28,-29,-30,-31,]),'POW':([7,8,10,11,12,13,14,19,20,27,28,42,43,44,46,47,52,54,57,62,63,64,65,66,67,68,69,70,71,72,73,74,82,86,87,92,95,104,109,117,118,119,121,],[-44,41,-43,-45,-46,-47,-48,41,-44,-57,-58,41,41,-54,41,-42,41,41,-27,41,41,41,41,41,41,41,41,41,41,41,41,-65,41,41,-26,41,-50,41,41,-28,-29,-30,-31,]),'PLUSPLUS':([7,20,],[27,27,]),'MINUSMINUS':([7,20,],[28,28,]),'RROUND':([10,11,12,13,14,18,19,20,27,28,43,44,45,46,47,57,62,63,64,65,66,67,68,69,70,71,72,73,74,80,81,82,87,88,89,90,94,95,103,104,105,106,107,108,109,117,118,119,121,127,],[-43,-45,-46,-47,-48,-6,47,-44,-57,-58,-66,-54,79,-19,-42,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,-6,-18,-49,-26,-37,-37,-35,-5,-50,117,-36,118,119,-33,121,-32,-28,-29,-30,-31,-34,]),'LCURLY':([10,11,12,13,14,20,27,28,42,43,44,47,50,51,52,57,62,63,64,65,66,67,68,69,70,71,72,73,74,77,87,92,95,117,118,119,121,],[-43,-45,-46,-47,-48,-44,-57,-58,77,-66,-54,-42,77,77,-10,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,77,-26,-51,-50,-28,-29,-30,-31,]),'COMMA':([10,11,12,13,14,20,27,28,43,44,46,47,57,62,63,64,65,66,67,68,69,70,71,72,73,74,87,95,98,99,100,101,102,107,117,118,119,121,],[-43,-45,-46,-47,-48,-44,-57,-58,-66,-54,81,-42,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,-26,-50,81,81,81,81,81,120,-28,-29,-30,-31,]),'RSQBRAC':([10,11,12,13,14,20,25,27,28,43,44,46,47,55,56,57,62,63,64,65,66,67,68,69,70,71,72,73,74,80,81,85,87,94,95,97,98,99,100,101,102,112,113,114,115,116,117,118,119,121,122,123,124,125,126,],[-43,-45,-46,-47,-48,-44,-4,-57,-58,-66,-54,-19,-42,87,-3,-27,-49,-51,-52,-53,-55,-56,-59,-60,-61,-62,-63,-64,-65,-6,-18,-25,-26,-5,-50,111,-19,-19,-19,-19,-19,-25,-25,-25,-25,-25,-28,-29,-30,-31,-20,-21,-22,-23,-24,]),'PUSH':([26,],[58,]),'POP':([26,],[59,]),'SLICE':([26,],[60,]),'INDEX':([26,],[61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'element':([0,],[1,]),'stmt':([0,42,50,51,77,],[2,78,78,78,78,]),'if':([0,42,50,51,77,],[5,5,5,5,5,]),'exp':([0,4,9,15,16,18,22,24,25,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,50,51,53,76,77,80,88,89,91,],[8,19,42,43,44,46,52,54,46,62,63,64,65,66,67,68,69,70,71,72,73,74,8,82,8,8,86,92,8,46,104,104,109,]),'elseif':([5,84,],[21,96,]),'params':([18,25,80,],[45,56,94,]),'else':([21,],[49,]),'c_exp':([22,],[51,]),'optparams':([25,],[55,]),'list_functions':([26,],[57,]),'c_stmt':([42,50,51,77,],[75,83,84,93,]),'l_comma':([46,98,99,100,101,102,],[80,112,113,114,115,116,]),'listparams':([85,112,113,114,115,116,],[97,122,123,124,125,126,]),'pparams':([88,89,],[103,105,]),'sliceparams':([90,],[106,]),'indexparams':([91,],[108,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> element","S'",1,None,None,None),
  ('element -> stmt SEMICOLON','element',2,'p_statement','parser.py',27),
  ('stmt -> DISPLAY LROUND params RROUND','stmt',4,'p_stmt_display','parser.py',32),
  ('optparams -> params','optparams',1,'p_optparams','parser.py',37),
  ('optparams -> <empty>','optparams',0,'p_optparams_empty','parser.py',42),
  ('params -> exp l_comma params','params',3,'p_params','parser.py',47),
  ('params -> <empty>','params',0,'p_params_empty','parser.py',54),
  ('stmt -> if elseif else','stmt',3,'p_if_elseif_else','parser.py',67),
  ('if -> IF exp c_stmt','if',3,'p_if','parser.py',72),
  ('elseif -> ELSEIF c_exp c_stmt elseif','elseif',4,'p_if_elseif','parser.py',77),
  ('c_exp -> exp','c_exp',1,'p_c_exp','parser.py',81),
  ('elseif -> <empty>','elseif',0,'p_if_elseif_empty','parser.py',85),
  ('else -> ELSE c_stmt','else',2,'p_else','parser.py',89),
  ('else -> <empty>','else',0,'p_else_empty','parser.py',94),
  ('c_stmt -> LCURLY c_stmt RCURLY','c_stmt',3,'p_compoundstmt','parser.py',98),
  ('c_stmt -> stmt','c_stmt',1,'p_compoundstmt_stmt','parser.py',103),
  ('c_stmt -> <empty>','c_stmt',0,'p_compoundstmt_empty','parser.py',107),
  ('stmt -> TYPE IDENTIFIER ASSIGN LSQBRAC listparams RSQBRAC','stmt',6,'p_stmt_init_list','parser.py',118),
  ('l_comma -> COMMA','l_comma',1,'p_listcomma','parser.py',124),
  ('l_comma -> <empty>','l_comma',0,'p_listcomma_empty','parser.py',128),
  ('listparams -> INT l_comma listparams','listparams',3,'p_listparams_int','parser.py',132),
  ('listparams -> DOUBLE l_comma listparams','listparams',3,'p_listparams_double','parser.py',136),
  ('listparams -> STRING l_comma listparams','listparams',3,'p_listparams_string','parser.py',140),
  ('listparams -> CHAR l_comma listparams','listparams',3,'p_listparams_char','parser.py',145),
  ('listparams -> BOOL l_comma listparams','listparams',3,'p_listparams_bool','parser.py',149),
  ('listparams -> <empty>','listparams',0,'p_listparams_empty','parser.py',153),
  ('exp -> IDENTIFIER LSQBRAC optparams RSQBRAC','exp',4,'p_list_exp','parser.py',159),
  ('exp -> IDENTIFIER DOT list_functions','exp',3,'p_list_func','parser.py',164),
  ('list_functions -> PUSH LROUND pparams RROUND','list_functions',4,'p_list_func_push','parser.py',168),
  ('list_functions -> POP LROUND pparams RROUND','list_functions',4,'p_list_func_pop','parser.py',173),
  ('list_functions -> SLICE LROUND sliceparams RROUND','list_functions',4,'p_list_func_slice','parser.py',178),
  ('list_functions -> INDEX LROUND indexparams RROUND','list_functions',4,'p_list_func_index','parser.py',182),
  ('indexparams -> exp','indexparams',1,'p_indexparams','parser.py',186),
  ('sliceparams -> INT','sliceparams',1,'p_sliceparams','parser.py',190),
  ('sliceparams -> INT COMMA INT','sliceparams',3,'p_sliceparams_comma','parser.py',194),
  ('sliceparams -> <empty>','sliceparams',0,'p_sliceparams_empty','parser.py',198),
  ('pparams -> exp','pparams',1,'p_pparams','parser.py',204),
  ('pparams -> <empty>','pparams',0,'p_pparams_empty','parser.py',208),
  ('stmt -> IDENTIFIER ASSIGN exp','stmt',3,'p_stmt_assignment','parser.py',216),
  ('stmt -> TYPE IDENTIFIER','stmt',2,'p_stmt_init_empty','parser.py',221),
  ('stmt -> TYPE IDENTIFIER ASSIGN exp','stmt',4,'p_stmt_init_assign','parser.py',226),
  ('stmt -> exp','stmt',1,'p_stmt_exp','parser.py',231),
  ('exp -> LROUND exp RROUND','exp',3,'p_exp_para','parser.py',236),
  ('exp -> BOOL','exp',1,'p_exp_bool','parser.py',240),
  ('exp -> IDENTIFIER','exp',1,'p_exp_identifier','parser.py',245),
  ('exp -> STRING','exp',1,'p_exp_string','parser.py',249),
  ('exp -> INT','exp',1,'p_exp_int','parser.py',252),
  ('exp -> DOUBLE','exp',1,'p_exp_double','parser.py',255),
  ('exp -> CHAR','exp',1,'p_exp_char','parser.py',258),
  ('exp -> exp PLUS exp','exp',3,'p_exp_plus','parser.py',263),
  ('exp -> LROUND exp PLUS exp RROUND','exp',5,'p_exp_plus_brac','parser.py',267),
  ('exp -> exp MINUS exp','exp',3,'p_exp_minus','parser.py',270),
  ('exp -> exp MULTIPLY exp','exp',3,'p_exp_multiply','parser.py',273),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_divide','parser.py',276),
  ('exp -> NOT exp','exp',2,'p_exp_not','parser.py',279),
  ('exp -> exp AND exp','exp',3,'p_exp_and','parser.py',282),
  ('exp -> exp OR exp','exp',3,'p_exp_or','parser.py',285),
  ('exp -> IDENTIFIER PLUSPLUS','exp',2,'p_exp_plusplus','parser.py',288),
  ('exp -> IDENTIFIER MINUSMINUS','exp',2,'p_exp_minusminus','parser.py',291),
  ('exp -> exp LESSTHAN exp','exp',3,'p_exp_lessthan','parser.py',296),
  ('exp -> exp GREATERTHAN exp','exp',3,'p_exp_greaterthan','parser.py',300),
  ('exp -> exp LESSEQUAL exp','exp',3,'p_exp_lessequal','parser.py',303),
  ('exp -> exp GREATEREQUAL exp','exp',3,'p_exp_greaterequal','parser.py',306),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp_notequal','parser.py',309),
  ('exp -> exp EQUALS exp','exp',3,'p_exp_equal','parser.py',312),
  ('exp -> exp POW exp','exp',3,'p_exp_power','parser.py',315),
  ('exp -> MINUS exp','exp',2,'p_neg_num','parser.py',318),
]
