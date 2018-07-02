def getStackTraces(comments):
    bugStackTraces = []
    commentStackTraces = [re.sub('[\s\t]+', ' ', stackTrace.replace('\n', ' ')) for stackTrace in re.findall(
                r'([^\n\s]+Exception[^\n]*\n(?:.*at.*\n)+)', comments)]
    if commentStackTraces is not None and commentStackTraces!=[]:
        bugStackTraces = bugStackTraces + [re.sub(r'\n[.\s]* at', '\nat', stackTrace).strip() for stackTrace
                                           in commentStackTraces]
    return bugStackTraces

def getAllCodeReferences(stackTrace):
    return re.findall("\((\w+\.java:\d+)\)", stackTrace)

def getFirstMatchingCodeReference(stackTrace, packagePrefix):
    packagePrefixMatch = re.search("\s*at\s+"+packagePrefix+"[\w\.<>]+\((\w+\.java:\d+)\)", stackTrace)
    return packagePrefixMatch.group(1) if packagePrefixMatch else "None"

def getModuleReference(stackTrace):
    moduleMatch = re.search("\s*at\s+(com.tpt[\w\.]+\w)\.\w+(?:\.[\w<>]*)\(\w+\.java:\d+\)", stackTrace)
    return moduleMatch.group(1) if moduleMatch else "None"

