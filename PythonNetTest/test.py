import clr
clr.AddReference("Ice.Domain")

from Ice.Domain.Analyses.Functions import AnalysisOutputBuilder

david = AnalysisOutputBuilder()
print(david)