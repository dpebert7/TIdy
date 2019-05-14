# Defalut

HEADING_INDICATOR = "###"
CHUNK_HEADING = """
#####################
### TITLE
#####################
"""
MAX_CONSECUTIVE_BLANK_LINES = 3
DEFAULT_INDIR = 'in'
DEFAULT_OUTDIR = 'out'
DEFAULT_TAB = '\t'
OPERATORS = ['=', '<', '>', '<=', '>=', '<>', '@=', '@<>']

# List of TI keywords
KEYWORDS = ['BREAK', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ENDIF', 'END']

FUNCTION_NAMES = [
    'AddClient', 'AddGroup', 'AllowExternalRequests', 'ASCIIDelete', 'ASCIIOutput', 'AssignClientPassword',
    'AssignClientToGroup', 'AttrDelete', 'AttrInsert', 'AttrPutN', 'AttrPutS', 'AttrToAlias', 'BatchUpdateFinish',
    'BatchUpdateStart', 'CellGetN', 'CellGetS', 'CellIsUpdateable', 'CellPutN', 'CellPutProportionalSpread',
    'CellPutS', 'ChoreQuit', 'CubeCreate', 'CubeDestroy', 'CubeExists', 'CubeGetLogChanges', 'CubeLockOverride',
    'CubeProcessFeeders', 'CubeSetConnParams', 'CubeSetIsVirtual', 'CubeSetLogChanges', 'CubeSetSAPVariablesClause',
    'CubeSetSlicerMembers', 'CubeUnload', 'DeleteClient', 'DeleteGroup', 'DimensionCreate',
    'DimensionDeleteAllElements', 'DimensionDestroy', 'DimensionEditingAliasSet', 'DimensionElementComponentAdd',
    'DimensionElementComponentDelete', 'DimensionElementDelete', 'DimensionElementInsert',
    'DimensionElementInsertByAlias', 'DimensionElementPrincipalName', 'DimensionExists', 'DimensionSortOrder',
    'ElementSecurityGet', 'ElementSecurityPut', 'EncodePassword', 'ExecuteCommand', 'ExecuteProcess', 'Expand',
    'FileExists', 'GetProcessErrorFileDirectory', 'GetProcessErrorFilename', 'IsNull', 'ItemReject', 'ItemSkip',
    'LockOff', 'LockOn', 'NumberToString', 'NumberToStringEx', 'NumericGlobalVariable', 'NumericSessionVariable',
    'ODBCClose', 'ODBCOpen', 'ODBCOutput', 'ProcessBreak', 'ProcessError', 'ProcessExitByBreak',
    'ProcessExitByChoreQuit', 'ProcessExitByQuit', 'ProcessExitMinorError', 'ProcessExitNormal', 'ProcessExitOnInit',
    'ProcessExitSeriousError', 'ProcessExitWithMessage', 'ProcessQuit', 'PublishView', 'RemoveClientFromGroup',
    'ReturnSQLTableHandle', 'ReturnViewHandle', 'RuleLoadFromFile', 'SaveDataAll', 'SecurityRefresh', 'ServerShutDown',
    'SetChoreVerboseMessages', 'StringGlobalVariable', 'StringSessionVariable', 'StringToNumber', 'StringToNumberEx',
    'SubsetAliasSet', 'SubsetCreate', 'SubsetCreateByMDX', 'SubsetDeleteAllElements', 'SubsetDestroy',
    'SubsetElementDelete', 'SubsetElementInsert', 'SubsetExists', 'SubsetFormatStyleSet', 'SubsetGetElementName',
    'SubsetGetSize', 'SubsetIsAllSet', 'SwapAliasWithPrincipalName', 'ViewColumnDimensionSet',
    'ViewColumnSuppressZeroesSet', 'ViewConstruct', 'ViewCreate', 'ViewDestroy', 'ViewExists',
    'ViewExtractSkipRuleValuesSet', 'ViewExtractSkipRuleValuesSet', 'ViewExtractSkipZeroesSet',
    'ViewRowDimensionSet', 'ViewRowSuppressZeroesSet', 'ViewSetSkipCalcs', 'ViewSetSkipRuleValues',
    'ViewSetSkipZeroes', 'ViewSubsetAssign', 'ViewSuppressZeroesSet', 'ViewTitleDimensionSet',
    'ViewTitleElementSet', 'ViewZeroOut', 'WildcardFileSearch'
] + [
    'ABS', 'ACOS', 'ASIN', 'ATAN', 'ATTRN', 'ATTRS', 'AVG', 'BANNR', 'BDATE', 'BDAYN', 'CAPIT', 'CENTR', 'CHAR',
    'CNT', 'CODE', 'COL', 'COS', 'DATE', 'DATES', 'DATFM', 'DAY', 'DAYNO', 'DBG16', 'DBGEN', 'DELET', 'DFRST',
    'DIMIX', 'DIMNM', 'DIMSIZ', 'DISPLY', 'DNEXT', 'DNLEV', 'DTYPE', 'DYS', 'ELCOMP', 'ELCOMPN', 'ELISANC',
    'ELISCOMP', 'ELISPAR', 'ELLEV', 'ELPAR', 'ELPARN', 'ELWEIGHT', 'EXP', 'FILL', 'FV', 'HEX', 'IF', 'INSRT',
    'INT', 'IRR', 'ISLEAF', 'ISUND', 'LIN', 'LN', 'LOG', 'LONG', 'LOOK', 'LOWER', 'MAX', 'MEM', 'MIN', 'MOD',
    'MONTH', 'MOS', 'NCELL', 'NOW', 'NPV', 'PAYMT', 'PV', 'RAND', 'RIGHT', 'ROUND', 'ROUNDP', 'SCAN', 'SCELL',
    'SIGN', 'SIN', 'SLEEP', 'SQRT', 'STDDV', 'STR', 'SUBSIZ', 'SUBST', 'SUM', 'TABDIM', 'TAN', 'TIME', 'TIMST',
    'TIMVL', 'TODAY', 'TRIM', 'UNDEF', 'UPPER', 'VAR', 'WHOAMI', 'WIDTH', 'YEAR', 'YRS'
]


IMPLICIT_VARIABLE_NAMES = [
    'DatasourceASCIIDecimalSeparator', 'DatasourceASCIIDelimiter', 'DatasourceASCIIHeaderRecords',
    'DatasourceASCIIQuoteCharacter', 'DatasourceASCIIThousandSeparator', 'DatasourceCubeview',
    'DatasourceDimensionSubset', 'DatasourceNameForClient', 'DatasourceNameForServer', 'DatasourceODBOCatalog',
    'DatasourceODBOConnectionString', 'DatasourceODBOCubeName', 'DatasourceODBOHierarchyName',
    'DatasourceODBOLocation', 'DatasourceODBOProvider', 'DatasourceODBOSAPClientId', 'DatasourceODBOSAPClientLanguage',
    'DatasourcePassword', 'DatasourceQuery', 'DatasourceType', 'DatasourceUseCallerProcessConnection',
    'DatasourceUsername', 'MinorErrorLogMax', 'NValue', 'OnMinorErrorDoItemSkip', 'SValue', 'Value_Is_String'
]

