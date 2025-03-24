from ply import lex
import ply.yacc as yacc

tokens = (
    'COMMA',
    # 'LANG',
    'NOUN1',
    'VERB1',
    'DETERMINER1',
    'ADJECTIVE1',
    'ADJECTIVE2',
    'NOUN2',
    'VERB2',
    'NOUN3',
    'IMPERATIVENEGATIVE1',
    'VERB3',
    'PRONOUN1',
    'NOUN4',
    'PREPOSITION1',
    'PRONOUN2',
    'VERB4',
    'NUMBER',
    'NOUN5',
    'VERB5',
    'DETERMINER2',
    'NOUN6',
    'DETERMINER3',
    'NOUN7',
    'VERB6',
    'ADJECTIVE3',
    'NOUN8',
    'VERB7',
    'NOUN9',
    'ADJECTIVE4', 
    'CONJUNCTION1', 
    'NOUN10', 
    'ADJECTIVE5', 
    'NOUN11', 
    'VERB8', 
    'NOUN12', 
    'VERB9',
    'PREPOSITION2',
    'NOUN13',
    'CONJUNCTION2', 
    'VERB10', 
    'VERB11', 
    'PRONOUN3', 
    'VERB12', 
    'ADVERB1', 
    'VERB13', 
    'NOUN14', 
    'PREPOSITION3', 
    'NOUN15', 
    'PREPOSITION4', 
    'NOUN16', 
    'NOUN17', 
    'NOUN18',
    'NOUN19',
    'PREPOSITION5',
    'NOUN20',
    'NOUN21',
    'VERB14',
    'ADJECTIVE6',
    'NOUN22', 
    'MODALVERB', 
    'VERB15', 
    'NOUN23',

    'fi3l1',
    'fi3l2',
    'fa3il1',
    'fi3l3',
    'fa3il2',
    'ism1',
    '7arf1',
    'ism2',
    '7arf2',
    'ism3',
    'ism4',
    'fi3l4',
    'fa3il3',
    '7arf3',
    'fi3l5',
    'fa3il4',
    '7arf4',
    'fi3l6',
    '7arf5',
    '7arf6',
    'fi3l8',
    'ism5',
    'ism6',
    '7arf7',
    'ism7',
    'maf3oulbih1',
    'fi3l9',
    '7arf8',
    'ism8',
    'fi3l10',
    'fi3l11',
    'ism9',
    'fi3l12',
    'ism10',
    '7arf9',
    'fi3l13',
    'ism11',
    'fi3l14',
    'ism12',
    'fi3l15',
    'ism13',
    'ism14',
    '7arf11',
    'ism15',
    'ism16',
    'ism17',
    'ism18',
    'fi3l16',
    'ism19',

    'determinant1',
    'verbe1',
    'prepos1',
    'nom2',
    'verbe2',
    'adject1',
    'nom3',
    'adverbe1',
    'prepos2',
    'pronom1',
    'conjonction1',
    'nom4',
    'adverbe2',
    'adverbe3',
    'determinant2',
    'nom5',
    'verbe3',
    'nom6',
    'adject3',
    'prepos3',
    'determinant3',
    'nom8',
    'conjonction2',
    'apostrophe',
    'nom9',
    'verbe4',
    'verbe5',
    'pronom2',
    'verbe6',
    'adverbe4',
    'determinant4',
    'nom10',
    'verbe7',
    'prepos4',
    'pronom3',
    'pronom4',
    'verbe8',
    'adverbe5',
    'adverbe6',
    'verbe9',
    'adverbe7',
    'nom11',
    'preposition6',
    'pronom5',
    'adverbe8',
    'verbe10',
    'adject4',
    'adject5',
    'nom12',
    'verbe11',
    'nom13',
    'nom14',
    'determinant5',
    'nom15',
    'prepos5',
    'nom16',
    'nom17',
    'prepos6',
    'nom18',
    'adject6',
    'conjonction3',
    'nom19',
    'nom20',
    'nom21',
    'nom22',
    'nom23',
    'nom24',
    'verbe13',
    'pronom6',
    'verbe14',
    'nom25',
    'nom26',
    'verbe15',
    'verbe16',
    'prepos7',
    'nom27',

    'determiner4',
    'noun24',
    'verb16',
    'preposition7',
    'determiner5',
    'adjective7',

    'verb17',
    'pronoun4',
    'noun25',
    'adverbe9',
    'preposition8',
    'pronoun5',
    'CONJUNCTION3',
    #pronoun4
    'noun26',
    'adverb10',
    'adjective8',

    'article1',
    'noun27',
    #verb16
    #article1
    'preposition9',
    'article2',
    'noun28',
    'adjective9',
    'noun29',

    'adverb11',
    'adverb12',
    #article2
    'noun30',
    'verb18',
    #conjunction3
    'verbe17',
    'verb19',
    'pronoun6',
    'adjective10',
    'verbe18',

    #article2
    'adjective11',
    #noun30
    'verb20',
    #determiner5
    'noun31',

    'verb21',
    #pronoun4
    'noun32',
    'adverb13',
    'conjunction4',
    'pronoun7',
    'verb22',
    'verb23',

    'number1',
    'noun33',
    'verb24',
    #adverb10
    'adjective12',
    #adverb13
    'article3',
    'noun34',

    'pronoun8',
    'noun35',
    'verb25',
    #article3
    'adjective13',
    'noun36',

    'noun37',
    'preposition10',
    'noun38',
    #verb16
    'conjunction5',
    'noun39',
    #preposition10
    'noun40',

    'noun41',
    #verb16
    #article2
    'noun42',
    #article2
    'noun43',

    'noun44',
    'verb26',
    #determiner5
    'noun45',

    #article2
    'noun46',
    'modalverb2',
    'verb27',
    'noun73',

    #italian
    'noun47',
    'verb28',
    'article5',
    'adjective14',

    'verb29',
    'article6',
    'pronoun9',
    'noun48',
    'adjective15',
    'conjunction6',
    #article6
    #pronoun9
    'noun49',
    'adverb14',
    'adverb15',

    'noun50',
    'verb30',
    #article7
    'noun51',
    'adjective17',
    'preposition11',
    'noun52',

    'pronoun10',
    'noun53',
    'conjunction7',
    #article7
    'noun54',
    'verb31',
    #conjunction6
    'pronoun11',
    'verb32',

    'noun55',
    'verb33',
    'noun56',
    'preposition12',
    'noun57',

    'adverb16',
    'verb34',
    #article6
    #pronoun9
    'noun58',
    'conjunction8',
    'conjunction9',
    'adjective18',

    'number2',
    'noun59',
    #adverb16
    'verb35',
    'article9',
    'noun60',

    'noun61',
    #verb33
    #article7
    'pronoun13',
    'noun62',
    'adjective19',

    #article4
    'noun69',
    'preposition14',
    'noun70',
    #verb30
    'conjunction10',
    #article7
    'noun71',
    #preposition14
    'noun72',

    #article8
    'noun63',
    #verb30
    'noun64',
    'preposition13',
    'noun65',

    #article4
    'noun66',
    'verb36',
    'adjective20',

    #article4
    'noun67',
    'verb37',
    'verb38',
    'noun68',
    'verb39',
    'adverb17'
)

t_ignore = ' \t'
t_COMMA = ','
t_NOUN1 = r'[fF][oO][rR][tT][uU][nN][eE]'
t_VERB1 = r'[fF][aA][vV][oO][rR][sS]'
t_DETERMINER1 = r'[tT][hH][eE]'
t_ADJECTIVE1 = r'[bB][oO][lL][dD]'
t_ADJECTIVE2 = r'[eE][aA][rR][lL][yY]'
t_NOUN2 = r'[bB][iI][rR][dD]'
t_VERB2 = r'[cC][aA][tT][cC][hH][eE][sS]'
t_NOUN3 = r'[wW][oO][rR][mM]'
t_IMPERATIVENEGATIVE1 = r"[dD][oO][nN][']?[tT]"
t_VERB3 = r'[cC][oO][uU][nN][tT]'
t_PRONOUN1 = r'[yY][oO][uU][rR]'
t_NOUN4 = r'[cC][hH][iI][cC][kK][eE][nN][sS]'
t_PREPOSITION1 = r'[bB][eE][fF][oO][rR][eE]'
t_PRONOUN2 = r'[tT][hH][eE][yY]'
t_VERB4 = r'[hH][aA][tT][cC][hH]'
t_NUMBER = r'[tT][wW][oO]'
t_NOUN5 = r'[wW][rR][oO][nN][gG][sS]'
t_VERB5 = r'[mM][aA][kK][eE]'
t_DETERMINER2 = r'[aA]'
t_NOUN6 = r'[rR][iI][gG][hH][tT]'
t_DETERMINER3 = r'[eE][vV][eE][rR][yY]'
t_NOUN7 = r'[cC][lL][oO][uU][dD]'
t_VERB6 = r'[hH][aA][sS]'
t_ADJECTIVE3 = r'[sS][iI][lL][vV][eE][rR]'
t_NOUN8 = r'[lL][iI][nN][iI][nN][gG]'
t_VERB7 = r'[kK][eE][eE][pP]'
t_NOUN9 = r'[fF][rR][iI][eE][nN][dD][sS]'
t_ADJECTIVE4 = r'[cC][lL][oO][sS][eE]'
t_CONJUNCTION1 = r'[aA][nN][dD]'
t_NOUN10 = r'[eE][nN][eE][mM][iI][eE][sS]'
t_ADJECTIVE5 = r'[cC][lL][oO][sS][eE][rR]'
t_NOUN11 = r'[fF][aA][tT][hH][eE][rR]'
t_VERB8 = r'[iI][sS]'
t_NOUN12 = r'[bB][aA][nN][kK][eE][rR]'
t_VERB9 = r'[pP][rR][oO][vV][iI][dD][eE][dD]'
t_PREPOSITION2 = r'[bB][yY]'
t_NOUN13 = r'[nN][aA][tT][uU][rR][eE]'
t_CONJUNCTION2 = r'[wW][hH][eE][nN][eE][vV][eE][rR]'
t_VERB10 = r'[fF][lL][iI][eE][sS]'
t_VERB11 = r'[rR][iI][sS][eE][sS]'
t_PRONOUN3 = r'[iI][tT]'
t_VERB12 = r'[sS][hH][aA][lL][lL]'
t_ADVERB1 = r'[sS][uU][rR][eE][lL][yY]'
t_VERB13 = r'[fF][aA][lL][lL]'
t_NOUN14 = r'[bB][eE][aA][uU][tT][yY]'
t_PREPOSITION3 = r'[wW][iI][tT][hH][oO][uU][tT]'
t_NOUN15 = r'[gG][rR][aA][cC][eE]'
t_PREPOSITION4 = r'[lL][iI][kK][eE]'
t_NOUN16 = r'[hH][oO][oO][kK]'
t_NOUN17 = r'[bB][aA][iI][tT]'
t_NOUN18 = r'[dD][oO][uU][bB][tT]'
t_NOUN19 = r'[bB][eE][gG][iI][nN][nN][iI][nN][gG]'
t_PREPOSITION5 = r'[oO][fF]'
t_NOUN20 = r'[wW][iI][sS][dD][oO][mM]'
t_NOUN21 = r'[pP][rR][aA][cC][tT][iI][cC][eE]'
t_VERB14 = r'[mM][aA][kK][eE][sS]'
t_ADJECTIVE6 = r'[pP][eE][rR][fF][eE][cC][tT]'
t_NOUN22 = r'[fF][aA][iI][tT][hH]'
t_MODALVERB = r'[cC][aA][nN]'
t_VERB15 = r'[mM][oO][vV][eE]'
t_NOUN23 = r'[mM][oO][uU][nN][tT][aA][iI][nN][sS]'


t_fi3l1 = r'[zZ]3[eE][mM]'
t_fi3l2 = r'[tT][aA][kK][lL]'
t_fa3il1 = r'[lL]7[eE][mM]'
t_fi3l3 = r'3[aA][cC][hH][rR]'
t_fa3il2 = r'[lL]3[dD][oO]'
t_ism1 = r'[kK][tT][rR]'
t_7arf1 = r'[mM][nN]'
t_ism2 = r'[sS][dD][iI]9'
t_7arf2 = r'[lL][iI]'
t_ism3 = r'3[nN][dD][oO]'
t_ism4 = r'[bB][aA][hH]'
t_fi3l4 = r'[gG][hH][nN][aA][hH]'
t_fa3il3 = r'[lL][aA][hH]'
t_7arf3 = r'[mM][aA]'
t_fi3l5 = r'[tT][aA][rR][aA]'
t_fa3il4 = r'[tT][aA][yY][rR][oO][nN]'
t_7arf4 = r'[wW][aA]'
t_fi3l6 = r'[iI][rR][tT][aA][fF][aA]3'
t_7arf5 = r'[iI][lL][lL][aA]'
t_7arf6 = r'[kK][aA][mM][aA]'
t_fi3l8 = r'[wW][aA]9[aA]3'
t_ism5 = r'[lL][fF][yY][aA]9'
t_ism6 = r'[bB][kK][rR][iI]'
t_7arf7 = r'[bB]'
t_ism7 = r'[dD][hH][eE][bB]'
t_maf3oulbih1 = r'[mM][cC][hH][rR][iI]'
t_fi3l9 = r'[zZ][rR][eE][bB]'
t_7arf8 = r'3[lL][aA]'
t_ism8 = r'[rR][zZ]9[oO]'
t_fi3l10 = r'[nN][dD][eE][mM]'
t_fi3l11 = r'[mM][aA][tT][rR][eE][dD][sS][hH]'
t_ism9 = r'[lL]3[iI][bB]'
t_fi3l12 = r'[mM][aA][kK][iI][tT][sS][dD]'
t_ism10 = r'[bB][aA][bB]'
t_7arf9 = r'[tT][aA]'
t_fi3l13 = r'[kK][iI][tT]7[lL][oO]'
t_ism11 = r'[bB][iI][bB][aA][nN]'
t_fi3l14 = r'[kK][hH][eE][lL][lL][iI][kK]'
t_ism12 = r'[rR][wW][iI][cC][hH]9[aA]'
t_fi3l15 = r'[tT][bB]9[aA][yY]'
t_ism13 = r'3[wW][iI][cC][hH]9[aA]'
t_ism14 = r'7[kK][mM][aA]'
t_7arf11 = r'[bB][lL][aA]'
t_ism15 = r'[cC][hH][kK]'
t_ism16 = r'[tT][aA][lL][tT][aA]'
t_ism17 = r'[fF][aA][lL][tT][aA]'
t_ism18 = r'[lL]2[iI][mM][aA][nN]'
t_fi3l16 = r'[yY]7[rR][kK]'
t_ism19 = r'[jJ][bB][aA][lL]'

t_determinant1 = r'[lL][aA]'
t_verbe1 = r'[sS][oO][uU][rR][iI][tT]'
t_prepos1 = r'[aA][uU][xX]'
t_nom2 = r'[aA][uU][dD][aA][cC][iI][eE][uU][xX]'
t_verbe2 = r'[gG][aA][rR][dD][eE]'
t_adject1 = r'[tT][eE][sS]'
t_nom3 = r'[aA][mM][iI][sS]'
t_adverbe1 = r'[pP][rR][èÈ][sS]'
t_prepos2 = r'[dD][eE]'
t_pronom1 = r'[tT][oO][iI]'
t_conjonction1 = r'[eE][tT]'
t_nom4 = r'[eE][nN][nN][eE][mM][iI][sS]'
t_adverbe2 = r'[eE][nN][cC][oO][rR][eE]'
t_adverbe3 = r'[pP][lL][uU][sS]'
t_determinant2 = r'[uU][nN]'
t_nom5 = r'[pP][èÈ][rR][eE]'
t_verbe3 = r'[eE][sS][tT]'
t_nom6 = r'[bB][aA][nN][qQ][uU][iI][eE][rR]'
t_adject3 = r'[fF][oO][uU][rR][nN][iI]'
t_prepos3 = r'[pP][aA][rR]'
t_determinant3 = r'[cC][hH][aA][qQ][uU][eE]'
t_nom8 = r'[fF][oO][iI][sS]'
t_conjonction2 = r'[qQ][uU]'
t_apostrophe = r'\''
t_nom9 = r'[oO][iI][sS][eE][aA][uU]'
t_verbe4 = r'[vV][oO][lL][eE]'
t_verbe5 = r'[sS]\'[éÉ][lL][èÈ][vV][eE]'
t_pronom2 = r'[iI][lL]'
t_verbe6 = r'[tT][oO][mM][bB][eE][rR][aA]'
t_adverbe4 = r'[sS][ûÛ][rR][eE][mM][eE][nN][tT]'
t_determinant4 = r'[lL][eE]'
t_nom10 = r'[mM][oO][nN][dD][eE]'
t_verbe7 = r'[aA][pP][pP][aA][rR][tT][iI][eE][nN][tT]'
t_prepos4 = r'[àÀ]'
t_pronom3 = r'[cC][eE][uU][xX]'
t_pronom4 = r'[qQ][uU][iI]'
t_verbe8 = r'[sS][eE][ ][lL][èÈ][vV][eE][nN][tT]'
t_adverbe5 = r'[tT][ôÔ][tT]'
t_adverbe6 = r'[nN][eE]'
t_verbe9 = r'[cC][oO][mM][pP][tT][eE]'
t_adverbe7 = r'[pP][aA][sS]'
t_nom11 = r'[pP][oO][uU][lL][eE][tT][sS]'
t_preposition6 = r'[aA][vV][aA][nN][tT]'
t_pronom5 = r'[iI][lL][sS]'
t_adverbe8 = r'[nN]'
t_verbe10 = r'[aA][iI][eE][nN][tT]'
t_adject4 = r'[éÉ][cC][lL][oO][sS]'
t_adject5 = r'[dD][eE][uU][xX]'
t_nom12 = r'[tT][oO][rR][tT][sS]'
t_verbe11 = r'[fF][oO][nN][tT]'
t_nom13 = r'[dD][rR][oO][iI][tT]'
t_nom14 = r'[nN][uU][aA][gG][eE]'
t_determinant5 = r'[uU][nN][eE]'
t_nom15 = r'[lL][uU][eE][uU][rR]'
t_prepos5 = r'[dD]'
t_nom16 = r'[eE][sS][pP][oO][iI][rR]'
t_nom17 = r'[bB][eE][aA][uU][tT][éÉ]'
t_prepos6 = r'[sS][aA][nN][sS]'
t_nom18 = r'[gG][rR][âÂ][cC][eE]'
t_adject6 = r'[cC]'
t_conjonction3 = r'[cC][oO][mM][mM][eE]'
t_nom19 = r'[cC][rR][oO][cC][hH][eE][tT]'
t_nom20 = r'[aA][pP][pP][âÂ][tT]'
t_nom21 = r'[dD][oO][uU][tT][eE]'
t_nom22 = r'[cC][oO][mM][mM][eE][nN][cC][eE][mM][eE][nN][tT]'
t_nom23 = r'[sS][aA][gG][eE][sS][sS][eE]'
t_nom24 = r'[fF][oO][rR][cC][eE]'
t_verbe13 = r'[fF][oO][rR][gG][eE][rR]'
t_pronom6 = r'[oO][nN]'
t_verbe14 = r'[dD][eE][vV][iI][eE][nN][tT]'
t_nom25= r'[fF][oO][rR][gG][eE][rR][oO][nN]'
t_nom26 = r'[fF][oO][iI]'
t_verbe15 = r'[pP][eE][uU][tT]'
t_verbe16 = r'[dD][éÉ][pP][lL][aA][cC][eE][rR]'
t_prepos7 = r'[dD][eE][sS]'
t_nom27 = r'[mM][oO][nN][tT][aA][gG][nN][eE][sS]'

t_determiner4 = r'[dD][aA][sS]'
t_noun24 = r'[gG][lL][üÜ][cC][kK]'
t_verb16 = r'[iI][sS][tT]'
t_preposition7 = r'[mM][iI][tT]'
t_determiner5 = r'[dD][eE][nN]'
t_adjective7 = r'[Mm][uU][tT][iI][gG][eE][nN]'
t_verb17 = r'[Hh][aA][lL][tT][eE]'
t_pronoun4 = r'[dD][eE][iI][nN][eE]'
t_noun25 = r'[Ff][rR][eE][uU][nN][dD][eE]'
t_adverbe9 = r'[nN][aA][hH]'
t_preposition8 = r'[bB][eE][iI]'
t_pronoun5 = r'[dD][iI][rR]'
t_CONJUNCTION3 = r'[uU][nN][dD]'
t_noun26 = r'[Ff][eE][iI][nN][dD][eE]'
t_adverb10 = r'[nN][oO][cC][hH]'
t_adjective8 = r'[nN][äÄ][hH][eE][rR]'
t_article1 = r'[Ee][iI][nN]'
t_noun27 = r'[Vv][aA][tT][eE][rR]'
t_preposition9 = r'[vV][oO][nN]'
t_article2 = r'[dD][eE][rR]'
t_noun28 = r'[Nn][aA][tT][uU][rR]'
t_adjective9 = r'[bB][eE][rR][eE][iI][tT][gG][eE][sS][tT][eE][lL][lL][tT][eE][rR]'
t_noun29 = r'[Bb][aA][nN][kK][iI][eE][rR]'
t_adverb11 = r'[Ww][aA][nN][nN]'
t_adverb12 = r'[iI][mM][mM][eE][rR]'
t_noun30 = r'[Vv][oO][gG][eE][lL]'
t_verb18 = r'[fF][lL][iI][eE][gG][tT]'
t_verbe17 = r'[aA][uU][fF][sS][tT][eE][iI][gG][tT]'
t_verb19 = r'[wW][iI][rR][dD]'
t_pronoun6 = r'[eE][rR]'
t_adjective10 = r'[sS][iI][cC][hH][eE][rR]'
t_verbe18 = r'[fF][aA][lL][lL][eE][nN]'
t_adjective11 = r'[fF][rR][üÜ][hH][eE]'
t_verb20 = r'[fF][äÄ][nN][gG][tT]'
t_noun31 = r'[Ww][uU][rR][mM]'
t_verb21 = r'[Zz][äÄ][hH][lL][eE]'
t_noun32 = r'[Hh][üÜ][hH][nN][eE][rR]'
t_adverb13 = r'[nN][iI][cC][hH][tT]'
t_conjunction4 = r'[bB][eE][vV][oO][rR]'
t_pronoun7 = r'[sS][iI][eE]'
t_verb22 = r'[gG][eE][sS][cC][hH][lL][üÜ][pP][fF][tT]'
t_verb23 = r'[sS][iI][nN][dD]'
t_number1 = r'[Zz][wW][eE][iI]'
t_noun33 = r'[Ff][eE][hH][lL][eE][rR]'
t_verb24 = r'[eE][rR][gG][eE][bB][eE][nN]'
t_adjective12 = r'[lL][aA][nN][gG][eE]'
t_article3 = r'[eE][iI][nN][eE][nN]'
t_noun34 = r'[Rr][iI][cC][hH][tT][iI][gG][eE][nN]'
t_pronoun8 = r'[Jj][eE][dD][eE]'
t_noun35 = r'[Ww][oO][lL][kK][eE]'
t_verb25 = r'[hH][aA][tT]'
t_adjective13 = r'[sS][iI][lL][bB][eE][rR][nN][eE][nN]'
t_noun36 = r'[Rr][aA][nN][dD]'
t_noun37 = r'[Ss][cC][hH][öÖ][nN][hH][eE][iI][tT]'
t_preposition10 = r'[oO][hH][nN][eE]'
t_noun38 = r'[Aa][nN][mM][uU][tT]'
t_conjunction5 = r'[wW][iI][eE]'
t_noun39 = r'[Hh][aA][kK][eE][nN]'
t_noun40 = r'[Kk][öÖ][dD][eE][rR]'
t_noun41 = r'[Zz][wW][eE][iI][fF][eE][lL]'
t_noun42 = r'[Aa][nN][fF][aA][nN][gG]'
t_noun43 = r'[Ww][eE][iI][sS][hH][eE][iI][tT]'
t_noun44 = r'[Üü][bB][uU][nN][gG]'
t_verb26 = r'[mM][aA][cC][hH][tT]'
t_noun45 = r'[Mm][eE][iI][sS][tT][eE][rR]'
t_noun46 = r'[Gg][lL][aA][uU][bB][eE]'
t_modalverb2 = r'[kK][aA][nN][nN]'
t_noun73 = r'[bB][eE][rR][gG][eE]'
t_verb27 = r'[vV][eE][rR][sS][eE][tT][zZ][eE][nN]'

t_noun47 = r'[fF][oO][rR][tT][uU][nN][aA]'
t_verb28 = r'[aA][iI][uU][tT][aA]'
t_article5 = r'[gG][lL][iI]'
t_adjective14 = r'[aA][uU][dD][aA][cC][iI]'
t_verb29 = r'[tT][iI][eE][nN][iI]'
t_article6 = r'[iI]'
t_pronoun9 = r'[tT][uU][oO][iI]'
t_noun48 = r'[aA][mM][iI][cC][iI]'
t_adjective15 = r'[vV][iI][cC][iI][nN][iI]'
t_conjunction6 = r'[eE]'
t_noun49 = r'[nN][eE][mM][iI][cC][iI]'
t_adverb14 = r'[aA][nN][cC][oO][rR][aA]'
t_adverb15 = r'[pP][iI][ùÙ]'
t_noun50 = r'[pP][aA][dD][rR][eE]'
t_verb30 = r'[èÈ]'
t_noun51 = r'[bB][aA][nN][cC][hH][iI][eE][rR][eE]'
t_adjective17 = r'[fF][oO][rR][nN][iI][tT][oO]'
t_preposition11 = r'[dD][aA][lL][lL][aA]'
t_noun52 = r'[nN][aA][tT][uU][rR][aA]'
t_pronoun10 = r'[oO][gG][nN][iI]'
t_noun53 = r'[vV][oO][lL][tT][aA]'
t_conjunction7 = r'[cC][hH][eE]'
t_noun54 = r'[uU][cC][cC][eE][lL][lL][oO]'
t_verb31 = r'[vV][oO][lL][aA]'
t_pronoun11 = r'[sS][iI]'
t_verb32 = r'[aA][lL][zZ][aA]'
t_noun55 = r'[mM][aA][tT][tT][iI][nN][oO]'
t_verb33 = r'[hH][aA]'
t_noun56 = r'[lL][\'][oO][rR][oO]'
t_preposition12 = r'[iI][nN]'
t_noun57 = r'[bB][oO][cC][cC][aA]'
t_adverb16 = r'[nN][oO][nN]'
t_verb34 = r'[cC][oO][nN][tT][aA][rR][eE]'
t_noun58 = r'[pP][rR][iI][mM][aA]'
t_conjunction8 = r'[cC][hH][eE]'
t_conjunction9 = r'[sS][iI][aA][nN][oO]'
t_adjective18 = r'[nN][aA][tT][iI]'
t_number2 = r'[Dd][uU][eE]'
t_noun59 = r'[tT][oO][rR][tT][iI]'
t_verb35 = r'[fF][aA][nN][nN][oO]'
t_article9 = r'[uU][nN][aA]'
t_noun60 = r'[rR][aA][gG][iI][oO][nN][eE]'
t_noun61 = r'[nN][uU][vV][oO][lL][aA]'
t_pronoun13 = r'[sS][uU][oO]'
t_noun62 = r'[lL][aA][tT][oO]'
t_adjective19 = r'[pP][oO][sS][iI][tT][iI][vV][oO]'
t_noun69 = r'[bB][eE][lL][lL][eE][zZ][zZ][aA]'
t_preposition14 = r'[sS][eE][nN][zZ][aA]'
t_noun70 = r'[gG][rR][aA][zZ][iI][aA]'
t_conjunction10 = r'[cC][oO][mM][eE]'
t_noun71 = r'[aA][mM][oO]'
t_noun72 = r'[eE][sS][cC][aA]'
t_noun63 = r'[dD][uU][bB][bB][iI][oO]'
t_noun64 = r'[lL][\'][iI][nN][iI][zZ][iI][oO]'
t_preposition13 = r'[dD][eE][lL][lL][aA]'
t_noun65 = r'[sS][aA][gG][gG][eE][zZ][zZ][aA]'
t_noun66 = r'[pP][rR][aA][tT][iI][cC][aA]'
t_verb36 = r'[rR][eE][nN][dD][eE]'
t_adjective20 = r'[pP][eE][rR][fF][eE][tT][tT][iI]'
t_noun67 = r'[fF][eE][dD][eE]'
t_verb37 = r'[pP][uU][òÒ]'
t_verb38 = r'[mM][uU][oO][vV][eE][rR][eE]'
t_noun68 = r'[mM][oO][nN][tT][aA][gG][nN][eE]'
t_adverb17 = r'[cC][eE][rR][tT][aA][mM][eE][nN][tT][eE]'
t_verb39 = r'[cC][aA][dD][rR][àÀ]'


# Track the detected language
detected_language = None

def t_error(t):
    global isLexFailed
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_proverb(p):
    '''proverb : NOUN1 VERB1 DETERMINER1 ADJECTIVE1
               | VERB7 PRONOUN1 NOUN9 ADJECTIVE4 COMMA CONJUNCTION1 PRONOUN1 NOUN10 ADJECTIVE5 
               | DETERMINER2 NOUN11 VERB8 DETERMINER2 NOUN12 VERB9 PREPOSITION2 NOUN13 
               | CONJUNCTION2 DETERMINER2 NOUN2 VERB10 CONJUNCTION1 VERB11 COMMA PRONOUN3 VERB12 ADVERB1 VERB13 
               | DETERMINER1 ADJECTIVE2 NOUN2 VERB2 DETERMINER1 NOUN3
               | IMPERATIVENEGATIVE1 VERB3 PRONOUN1 NOUN4 PREPOSITION1 PRONOUN2 VERB4
               | NUMBER NOUN5 IMPERATIVENEGATIVE1 VERB5 DETERMINER2 NOUN6 
               | DETERMINER3 NOUN7 VERB6 DETERMINER2 ADJECTIVE3 NOUN8 
               | NOUN14 PREPOSITION3 NOUN15 VERB8 PREPOSITION4 DETERMINER2 NOUN16 PREPOSITION3 NOUN17 
               | NOUN18 VERB8 DETERMINER1 NOUN19 PREPOSITION5 NOUN20
               | NOUN21 VERB14 ADJECTIVE6 
               | NOUN22 MODALVERB VERB15 NOUN23 
               | fi3l1 fi3l2 fa3il1
               | fi3l3 fa3il2 ism1 7arf1 ism2
               | 7arf2 ism3 ism4 fi3l4 fa3il3
               | 7arf3 fi3l5 fa3il4 7arf4 fi3l6 7arf5 7arf6 fi3l5 fi3l8
               | ism5 ism6 7arf7 ism7 maf3oulbih1
               | 7arf2 fi3l9 7arf8 ism8 fi3l10
               | fi3l11 ism9 7arf7 ism9
               | fi3l12 ism10 7arf9 fi3l13 ism11
               | fi3l14 ism12 fi3l15 ism13
               | determinant1 ism14 7arf11 ism15
               | ism16 7arf3 ism17
               | ism18 fi3l16 ism19
               | determinant1 NOUN1 verbe1 prepos1 nom2
               | verbe2 adject1 nom3 adverbe1 prepos2 pronom1 conjonction1 adject1 nom4 adverbe2 adverbe3 adverbe1
               | determinant2 nom5 verbe3 determinant2 nom6 adject3 prepos3 determinant1 NOUN13
               | determinant3 nom8 conjonction2 apostrophe determinant2 nom9 verbe4 conjonction1 verbe5 COMMA pronom2 verbe6 adverbe4
               | determinant4 nom10 verbe7 prepos4 pronom3 pronom4 verbe8 adverbe5
               | adverbe6 verbe9 adverbe7 adject1 nom11 preposition6 conjonction2 apostrophe pronom5 adverbe8 apostrophe verbe10 adject4
               | adject5 nom12 adverbe6 verbe11 adverbe7 determinant2 nom13
               | determinant3 nom14 DETERMINER2 determinant5 nom15 prepos5 apostrophe nom16
               | determinant1 nom17 prepos6 nom18 COMMA adject6 apostrophe verbe3 conjonction3 determinant2 nom19 prepos6 nom20
               | determinant4 nom21 verbe3 determinant4 nom22 prepos2 determinant1 nom23
               | DETERMINER2 nom24 prepos2 verbe13 pronom6 verbe14 nom25
               | determinant1 nom26 verbe15 verbe16 prepos7 nom27
               | determiner4 noun24 verb16 preposition7 determiner5 adjective7
               | verb17 pronoun4 noun25 adverbe9 preposition8 pronoun5 CONJUNCTION3 pronoun4 noun26 adverb10 adjective8
               | article1 noun27 verb16 article1 preposition9 article2 noun28 adjective9 noun29
               | adverb11 adverb12 article1 noun30 verb18 CONJUNCTION3 verbe17 COMMA verb19 pronoun6 adjective10 verbe18
               | article2 adjective11 noun30 verb20 determiner5 noun31
               | verb21 pronoun4 noun32 adverb13 COMMA conjunction4 pronoun7 verb22 verb23
               | number1 noun33 verb24 adverb10 adjective12 adverb13 article3 noun34
               | pronoun8 noun35 verb25 article3 adjective13 noun36
               | noun37 preposition10 noun38 verb16 conjunction5 article1 noun39 preposition10 noun40
               | noun41 verb16 article2 noun42 article2 noun43
               | noun44 verb26 determiner5 noun45
               | article2 noun46 modalverb2 noun73 verb27
               | determinant1 noun47 verb28 article5 adjective14
               | verb29 article6 pronoun9 noun48 adjective15 conjunction6 article6 pronoun9 noun49 adverb14 adverb15 adjective15
               | determinant2 noun50 verb30 determinant2 noun51 adjective17 preposition11 noun52
               | pronoun10 noun53 conjunction7 determinant2 noun54 verb31 conjunction6 pronoun11 verb32 COMMA adverb17 verb39
               | pronom2 noun55 verb33 noun56 preposition12 noun57
               | adverb16 verb34 article6 pronoun9 noun58 conjunction8 conjunction9 adjective18
               | number2 noun59 adverb16 verb35 article9 noun60
               | pronoun10 noun61 verb33 determinant2 pronoun13 noun62 adjective19
               | determinant1 noun69 preposition14 noun70 verb30 conjunction10 determinant2 noun71 preposition14 noun72
               | pronom2 noun63 verb30 noun64 preposition13 noun65
               | determinant1 noun66 verb36 adjective20
               | determinant1 noun67 verb37 verb38 determinant4 noun68

               '''
    p[0] = p[1:]

def p_error(p):
    global detected_language
    print("Syntax error in input!")
    detected_language = None

parser = yacc.yacc()

def parse_proverb(data, is_silent=False) -> (bool, str, str):
    isLexFailed = False
    global detected_language
    meaning = None
    result = None
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if not is_silent: print(tok)

    try:
        result = parser.parse(data)
        if result:
            if not is_silent: print('result:', result)
            if not is_silent: print('first word: ', result[0])

            if result[0] == 'fortune':
                meaning = 'Taking risks and being courageous can bring you success.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'keep':
                meaning = 'You\'ll be safer if you know more about your enemies than you know about your friends.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[1] == 'father':
                meaning = 'The father is seen as the provider of financial security for his family, just like a banker stores and manages money.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'whenever':
                meaning = 'Whenever a bird goes up, it eventually comes down, just like how we experience highs and lows in life.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'the':
                meaning = 'Who starts something first has a better chance of success.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'don\'t':
                meaning = 'Don\'t celebrate too soon, because things might not turn out as planned.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'two':
                meaning = 'Even if someone hurt you, responding with something bad doesn\'t fix the situation.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'every':
                meaning = 'Even when things seem bad, there\'s usually a hidden good side or a reason to hope.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'beauty':
                meaning = 'True allure involves not just external beauty but also inner qualities like grace, kindness, and character, which are essential to attract and engage others.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'doubt':
                meaning = 'Questioning our beliefs and assumptions is the first step towards gaining true understanding.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'practice':
                meaning = 'Repeatedly doing something improves your skill and ability.'
                detected_language = 'English'
                return True, meaning, detected_language
            elif result[0] == 'faith':
                meaning = 'Belief, trust, and confidence in something can overcome seemingly insurmountable obstacles or challenges.'
                detected_language = 'English'
                return True, meaning, detected_language
        
            elif result[0] == 'z3em':
                meaning = 'Ila bghiti tnj7 f7yatk khss tkon chouja3 otghamr.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == '3achr':
                meaning = 'Khssk tkon kat3rf 3la 3dok ktr mn sa7bk bach tb9a fl2aman.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'li' and result[1] == '3ndo':
                meaning = 'L2ab dayr b7al banka, ky9drr ywffr lik ayy 7aja bghiti maddian.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'ma':
                meaning = 'Ch7al ma 3chti aw9at zwina, ayji wa7d nhar oghat3ich aw9at khayba.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'lfya9':
                meaning = 'Ila f9ti bkri kykon 3ndk lw9t tbda achghalk bkri ot3tehom w9thom.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'li' and result[1] == 'zreb':
                meaning = 'Matfr7ch 9bl lw9t, 7ta tchouf dkchi bach ghaysali.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'matredsh':
                meaning = 'Ila adak chiwa7d ordditiha lih, hdchi maghaywslk lta7aja zwina.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'makitsd':
                meaning = 'Flw9itat s3ab darori ma katkon chi haja zwina jaya f tri9 . Katbyn bli ymkn yji lkhir mn dorof s3iba.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'khellik':
                meaning = 'Zin l2af3al w nachat onkhwa aham mn zin lkhariji.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[1] == '7kma':
                meaning = 'Anak tchek flmabadi2 ol9iam dyalk hia awell khotwa ltatawor dati.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'talta':
                meaning = 'Ila b9iti kat3awd l7aja bzf dlmrrat atwelli nadi fiha.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            elif result[0] == 'l2iman':
                meaning = 'L2iman w ti9a f lah y9dro ykhelliwk tghlleb 3la ga3 so3obat.'
                detected_language = 'Darija'
                return True, meaning, detected_language
            
            elif result[1] == 'fortune':
                meaning = 'Prendre des risques et être courageux peut vous apporter le succès.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[0] == 'garde':
                meaning = 'Vous serez plus en sécurité si vous en savez plus sur vos ennemis que sur vos amis.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'père':
                meaning = 'Le père est considéré comme le garant de la sécurité financière de sa famille, tout comme le banquier stocke et gère l\'argent.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'fois':
                meaning = 'Chaque fois qu\'un oiseau monte, il finit par redescendre, tout comme nous vivons des hauts et des bas dans la vie.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'monde':
                meaning = 'Qui commence quelque chose en premier a de meilleures chances de réussir.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'compte':
                meaning = 'Ne célébrez pas trop tôt, car les choses pourraient ne pas se passer comme prévu.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[0] == 'deux':
                meaning = 'Même si quelqu\'un vous a blessé, répondre par quelque chose de mal ne résout pas la situation.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'nuage':
                meaning = 'Même lorsque les choses semblent mauvaises, il y a généralement un bon côté caché ou une raison d\'espérer.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'beauté':
                meaning = 'Le véritable attrait implique non seulement la beauté extérieure, mais aussi des qualités intérieures comme la grâce, la gentillesse et le caractère, qui sont essentielles pour attirer et engager les autres.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'doute':
                meaning = 'Remettre en question nos croyances et nos hypothèses est la première étape vers une véritable compréhension.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'force':
                meaning = 'Faire quelque chose à plusieurs reprises améliore vos compétences et vos capacités.'
                detected_language = 'French'
                return True, meaning, detected_language
            elif result[1] == 'foi':
                meaning = 'La croyance, la confiance et la confiance en quelque chose peuvent surmonter des obstacles ou des défis apparemment insurmontables.'
                detected_language = 'French'
                return True, meaning, detected_language
            
            elif result[0] == 'das':
                meaning = 'Risiken einzugehen und mutig zu sein kann Ihnen Erfolg bringen.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'halte':
                meaning = 'Risiken einzugehen und mutig zu sein kann Ihnen Erfolg bringen.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'ein':
                meaning = 'Der Vater gilt als Garant für die finanzielle Sicherheit seiner Familie, ebenso wie der Bankier das Geld verwahrt und verwaltet.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'wann':
                meaning = 'Jedes Mal, wenn ein Vogel aufsteigt, kommt er schließlich wieder herunter, so wie wir im Leben Höhen und Tiefen erleben.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'der':
                meaning = 'Wer zuerst etwas anfängt, hat bessere Erfolgschancen.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'zähle':
                meaning = 'Feiern Sie nicht zu früh, sonst könnte es sein, dass die Dinge nicht wie geplant verlaufen.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'zwei':
                meaning = 'Selbst wenn dich jemand verletzt hat, löst eine schlechte Reaktion die Situation nicht.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'jede':
                meaning = 'Selbst wenn die Dinge schlecht erscheinen, gibt es normalerweise einen versteckten Lichtblick oder Grund zur Hoffnung.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'schönheit':
                meaning = 'Wahre Attraktivität umfasst nicht nur äußere Schönheit, sondern auch innere Qualitäten wie Anmut, Freundlichkeit und Charakter, die für die Anziehung und Bindung anderer unerlässlich sind.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'zweifel':
                meaning = 'Das Hinterfragen unserer Überzeugungen und Annahmen ist der erste Schritt zum wahren Verständnis.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[0] == 'übung':
                meaning = 'Wenn Sie etwas wiederholt tun, verbessern Sie Ihre Fähigkeiten und Fertigkeiten.'
                detected_language = 'German'
                return True, meaning, detected_language
            elif result[1] == 'glaube':
                meaning = 'Glaube, Vertrauen und Vertrauen in etwas können scheinbar unüberwindbare Hindernisse oder Herausforderungen überwinden.'
                detected_language = 'German'
                return True, meaning, detected_language
            
            elif result[1] == 'fortuna':
                meaning = 'Correre dei rischi ed essere coraggiosi può portarti al successo.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[0] == 'tieni':
                meaning = 'Sarai più sicuro se saprai di più sui tuoi nemici che sui tuoi amici.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'padre':
                meaning = 'Il padre è visto come il garante della sicurezza finanziaria della sua famiglia, proprio come il banchiere immagazzina e gestisce il denaro.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'volta':
                meaning = 'Ogni volta che un uccello sale, prima o poi scende, proprio come accade nella vita con gli alti e bassi.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'mattino':
                meaning = 'Chi inizia qualcosa per primo ha maggiori possibilità di successo.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'contare':
                meaning = 'Non festeggiare troppo presto o le cose potrebbero non andare come previsto.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[0] == 'due':
                meaning = 'Anche se qualcuno ti ferisce, rispondere con qualcosa di brutto non risolve la situazione.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'nuvola':
                meaning = 'Anche quando le cose sembrano brutte, di solito c\'è un lato positivo nascosto o un motivo di speranza.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'bellezza':
                meaning = 'La vera attrattiva coinvolge non solo la bellezza esteriore, ma anche qualità interiori come la grazia, la gentilezza e il carattere, che sono essenziali per attrarre e coinvolgere gli altri.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'dubbio':
                meaning = 'Mettere in discussione le nostre convinzioni e supposizioni è il primo passo verso la vera comprensione.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'pratica':
                meaning = 'Mettere in discussione le nostre convinzioni e supposizioni è il primo passo verso la vera comprensione.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            elif result[1] == 'fede':
                meaning = 'La fede, la fiducia e la fiducia in qualcosa possono superare ostacoli o sfide apparentemente insormontabili.'
                detected_language = 'Italian'
                return True, meaning, detected_language
            else:
                raise Exception("Unknown error")
        else:
            # If the proverb is incorrect, suggest similar ones
            suggestion = suggest_similar_proverb(data)
            if suggestion:
                return False, suggestion, None 
            else:
                return False, None, None

    except lex.LexError as e:
        if not is_silent: print("Lexical error:", e)
        return False, None, None

    except Exception as e:
        if not is_silent: print("An unexpected error occurred:", e)
        return False, None, None

def suggest_similar_proverb(input_proverb):
    known_proverbs = [
        'das glück ist mit den mutigen',
        'la fortuna aiuta gli audaci',
        'fortune favors the bold',
        'la fortune sourit aux audacieux',
        'z3em takl l7em',
        'halte deine freunde nah bei dir und deine feinde noch näher',
        'tieni i tuoi amici vicini e i tuoi nemici ancora più vicini',
        'keep your friends close, and your enemies closer',
        'garde tes amis près de toi et tes ennemis encore plus près',
        '3achr l3do ktr mn sdi9',
        'ein vater ist ein von der natur bereitgestellter bankier',
        'un padre è un banchiere fornito dalla natura',
        'a father is a banker provided by nature',
        'un père est un banquier fourni par la nature',
        'li 3ndo bah ghnah lah',
        'wann immer ein vogel fliegt und aufsteigt, wird er sicher fallen',
        'ogni volta che un uccello vola e si alza, certamente cadrà',
        'whenever a bird flies and rises, it shall surely fall',
        'chaque fois qu\'un oiseau vole et s\'élève, il tombera sûrement',
        'ma tara tayron wa irtafa3 illa kama tara wa9a3',
        'der frühe vogel fängt den wurm',
        'il mattino ha l\'oro in bocca',
        'the early bird catches the worm',
        'le monde appartient à ceux qui se lèvent tôt',
        'lfya9 bkri b dheb mchri',
        'zähle deine hühner nicht, bevor sie geschlüpft sind',
        'non contare i tuoi polli prima che siano nati',
        'don\'t count your chickens before they hatch',
        'ne compte pas tes poulets avant qu\'ils n\'aient éclos',
        'li zreb 3la rz9o ndem',
        'zwei fehler ergeben noch lange nicht einen richtigen',
        'due torti non fanno una ragione',
        'two wrongs don\'t make a right',
        'deux torts ne font pas un droit',
        'matredsh l3ib bl3ib',
        'jede wolke hat einen silbernen rand',
        'ogni nuvola ha un suo lato positivo',
        'every cloud has a silver lining',
        'chaque nuage a une lueur d\'espoir',
        'makitsd bab ta kit7lo biban',
        'schönheit ohne anmut ist wie ein haken ohne köder',
        'la bellezza senza grazia è come un amo senza esca',
        'beauty without grace is like a hook without bait',
        'la beauté sans grâce, c\'est comme un crochet sans appât',
        'khellik rwich9a tb9ay 3wich9a',
        'zweifel ist der anfang der weisheit',
        'il dubbio è l\'inizio della saggezza',
        'doubt is the beginning of wisdom',
        'le doute est le commencement de la sagesse',
        'la 7kma bla chk',
        'übung macht den meister',
        'la pratica rende perfetti',
        'practice makes perfect',
        'a force de forger on devient forgeron',
        'Talta ma falta',
        'der glaube kann berge versetzen',
        'la fede può muovere le montagne',
        'faith can move mountains',
        'la foi peut déplacer des montagnes',
        'l2iman y7rk jbal'
    ]

    input_tokens = input_proverb.split()
    score = []

    for proverb in known_proverbs:
        proverb_tokens = proverb.split()
        count = sum(1 for token in input_tokens if token in proverb_tokens)
        score.append(count)
    
    max_score = max(score)
    if max(score) <= 1:
        return None
    return known_proverbs[score.index(max_score)]