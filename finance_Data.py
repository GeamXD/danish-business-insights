import xml.etree.ElementTree as ET
import pandas as pd

# Load the XML file
tree = ET.parse('your_xml_file.xml')
root = tree.getroot()

# Define namespaces
namespaces = {
    'fsa': 'http://xbrl.dcca.dk/fsa',
    'sob': 'http://xbrl.dcca.dk/sob',
    'gsd': 'http://xbrl.dcca.dk/gsd'
}

# Define a function to extract data from XML elements
def get_text_or_default(element, default='-'):
    return element.text.strip() if element is not None and element.text else default

# Initialize lists to store data
data = {
    'Context ID': [],
    'Start Date': [],
    'End Date': [],
    'Entity Identifier': [],
    'Reporting Period Start Date': [],
    'Reporting Period End Date': [],
    'Name of Submitting Enterprise': [],
    'Address of Submitting Enterprise': [],
    'Date of General Meeting': [],
    'Name and Surname of Chairman': [],
    'Date of Approval of Annual Report': [],
    'Place of Signature of Statement': [],
    'Information on Type of Submitted Report': [],
    'Identification Number CVR of Reporting Entity': [],
    'Name of Reporting Entity': [],
    'Address of Reporting Entity': [],
    'Name of Financial Institution': [],
    'Name of Audit Firm': [],
    'Address of Auditor': [],
    'Identification of Approved Annual Report': [],
    'Confirmation That Annual Report Is Presented': [],
    'Confirmation That Financial Statements Are Exempted': [],
    'Confirmation That Financial Statement Gives True and Fair View': [],
    'Recommendation for Approval of Annual Report': [],
    'Information on Reporting Class of Entity': [],
    'Description of General Matters Related to Recognition Measurement': [],
    'Description of Methods of Recognition and Measurement Basis of Income Statement Items': [],
    'Description of Methods of Recognition and Measurement Basis of External Expenses': [],
    'Description of Methods of Recognition and Measurement Basis of Finance Income and Expenses': [],
    'Description of Methods of Recognition and Measurement Basis of Tax Expenses': [],
    'Description of Methods of Recognition and Measurement Basis of Assets and Liabilities': [],
    'Description of Methods of Recognition and Measurement Basis of Receivables': [],
    'Description of Methods of Dividends': [],
    'Description of Methods of Recognition and Measurement Basis of Tax Payables and Deferred Tax': [],
    'Description of Methods of Recognition and Measurement Basis of Liabilities Other Than Provisions': [],
    'Disclosure of Main Activities and Accounting and Financial Matters': [],
    'Disclosure of Equity': [],
    'Disclosure of Contingent Liabilities': [],
    'Disclosure of Mortgages and Collaterals': [],
    'Gross Profit Loss': [],
    'Profit Loss from Ordinary Operating Activities': [],
    'Other Finance Income': [],
    'Rest of Other Finance Expenses': [],
    'Profit Loss': [],
    'Short-term Tax Receivables': [],
    'Short-term Receivables': [],
    'Other Short-term Investments': [],
    'Short-term Investments': [],
    'Cash and Cash Equivalents': [],
    'Current Assets': [],
    'Assets': [],
    'Contributed Capital': [],
    'Retained Earnings': [],
    'Equity': [],
    'Short-term Debt to Banks': [],
    'Short-term Payables to Associates': [],
    'Short-term Liabilities Other Than Provisions': [],
    'Liabilities Other Than Provisions': [],
    'Liabilities and Equity': []
}

# Iterate through context elements and extract data
for context in root.findall('.//fsa:ClassOfReportingEntity/..', namespaces):
    data['Context ID'].append(context.get('id'))
    data['Start Date'].append(get_text_or_default(context.find('./period/startDate')))
    data['End Date'].append(get_text_or_default(context.find('./period/endDate')))
    data['Entity Identifier'].append(get_text_or_default(context.find('./entity/identifier')))
    data['Reporting Period Start Date'].append(get_text_or_default(context.find('./fsa:ReportingPeriodStartDate', namespaces)))
    data['Reporting Period End Date'].append(get_text_or_default(context.find('./fsa:ReportingPeriodEndDate', namespaces)))
    data['Name of Submitting Enterprise'].append(get_text_or_default(context.find('./gsd:NameOfSubmittingEnterprise', namespaces)))
    data['Address of Submitting Enterprise'].append(get_text_or_default(context.find('./gsd:AddressOfSubmittingEnterpriseStreetAndNumber', namespaces)) + ", " +
                                                  get_text_or_default(context.find('./gsd:AddressOfSubmittingEnterprisePostcodeAndTown', namespaces)))
    data['Date of General Meeting'].append(get_text_or_default(context.find('./gsd:DateOfGeneralMeeting', namespaces)))
    data['Name and Surname of Chairman'].append(get_text_or_default(context.find('./gsd:NameAndSurnameOfChairman', namespaces)))
    data['Date of Approval of Annual Report'].append(get_text_or_default(context.find('./gsd:DateOfApprovalOfAnnualReport', namespaces)))
    data['Place of Signature of Statement'].append(get_text_or_default(context.find('./gsd:PlaceOfSignatureOfStatement', namespaces)))
    data['Information on Type of Submitted Report'].append(get_text_or_default(context.find('./gsd:InformationOnTypeOfSubmittedReport', namespaces)))
    data['Identification Number CVR of Reporting Entity'].append(get_text_or_default(context.find('./gsd:IdentificationNumberCVRofReportingEntity', namespaces)))
    data['Name of Reporting Entity'].append(get_text_or_default(context.find('./gsd:NameOfReportingEntity', namespaces)))
    data['Address of Reporting Entity'].append(get_text_or_default(context.find('./gsd:AddressOfReportingEntityStreetAndNumber', namespaces)) + ", " +
                                             get_text_or_default(context.find('./gsd:AddressOfReportingEntityPostcodeAndTown', namespaces)))
    data['Name of Financial Institution'].append(get_text_or_default(context.find('./gsd:NameOfFinancialInstitution', namespaces)))
    data['Name of Audit Firm'].append(get_text_or_default(context.find('./gsd:NameOfAuditFirm', namespaces)))
    data['Address of Auditor'].append(get_text_or_default(context.find('./gsd:AddressOfAuditorStreetAndNumber', namespaces)) + ", " +
                                     get_text_or_default(context.find('./gsd:AddressOfAuditorPostcodeAndTown', namespaces)))
    data['Identification of Approved Annual Report'].append(get_text_or_default(context.find('./gsd:IdentificationOfApprovedAnnualReport', namespaces)))
    data['Confirmation That Annual Report Is Presented'].append(get_text_or_default(context.find('./gsd:ConfirmationThatAnnualReportIsPresented', namespaces)))
    data['Confirmation That Financial Statements Are Exempted'].append(get_text_or_default(context.find('./gsd:ConfirmationThatFinancialStatementsAreExempted', namespaces)))
    data['Confirmation That Financial Statement Gives True and Fair View'].append(get_text_or_default(context.find('./gsd:ConfirmationThatFinancialStatementGivesTrueAndFairView', namespaces)))
    data['Recommendation for Approval of Annual Report'].append(get_text_or_default(context.find('./gsd:RecommendationForApprovalOfAnnualReport', namespaces)))
    data['Information on Reporting Class of Entity'].append(get_text_or_default(context.find('./gsd:InformationOnReportingClassOfEntity', namespaces)))
    data['Description of General Matters Related to Recognition Measurement'].append(get_text_or_default(context.find('./fsa:DescriptionOfGeneralMattersRelatedToRecognitionMeasurement', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of Income Statement Items'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfIncomeStatementItems', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of External Expenses'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfExternalExpenses', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of Finance Income and Expenses'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfFinanceIncomeAndExpenses', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of Tax Expenses'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfTaxExpenses', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of Assets and Liabilities'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfAssetsAndLiabilities', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of Receivables'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfReceivables', namespaces)))
    data['Description of Methods of Dividends'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfDividends', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of Tax Payables and Deferred Tax'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfTaxPayablesAndDeferredTax', namespaces)))
    data['Description of Methods of Recognition and Measurement Basis of Liabilities Other Than Provisions'].append(get_text_or_default(context.find('./fsa:DescriptionOfMethodsOfRecognitionAndMeasurementBasisOfLiabilitiesOtherThanProvisions', namespaces)))
    data['Disclosure of Main Activities and Accounting and Financial Matters'].append(get_text_or_default(context.find('./fsa:DisclosureOfMainActivitiesAndAccountingAndFinancialMatters', namespaces)))
    data['Disclosure of Equity'].append(get_text_or_default(context.find('./fsa:DisclosureOfEquity', namespaces)))
    data['Disclosure of Contingent Liabilities'].append(get_text_or_default(context.find('./fsa:DisclosureOfContingentLiabilities', namespaces)))
    data['Disclosure of Mortgages and Collaterals'].append(get_text_or_default(context.find('./fsa:DisclosureOfMortgagesAndCollaterals', namespaces)))
    data['Gross Profit Loss'].append(get_text_or_default(context.find('./fsa:GrossProfitLoss', namespaces)))
    data['Profit Loss from Ordinary Operating Activities'].append(get_text_or_default(context.find('./fsa:ProfitLossFromOrdinaryOperatingActivities', namespaces)))
    data['Other Finance Income'].append(get_text_or_default(context.find('./fsa:OtherFinanceIncome', namespaces)))
    data['Rest of Other Finance Expenses'].append(get_text_or_default(context.find('./fsa:RestOfOtherFinanceExpenses', namespaces)))
    data['Profit Loss'].append(get_text_or_default(context.find('./fsa:ProfitLoss', namespaces)))
    data['Short-term Tax Receivables'].append(get_text_or_default(context.find('./fsa:ShortTermTaxReceivables', namespaces)))
    data['Short-term Receivables'].append(get_text_or_default(context.find('./fsa:ShortTermReceivables', namespaces)))
    data['Other Short-term Investments'].append(get_text_or_default(context.find('./fsa:OtherShortTermInvestments', namespaces)))
    data['Short-term Investments'].append(get_text_or_default(context.find('./fsa:ShortTermInvestments', namespaces)))
    data['Cash and Cash Equivalents'].append(get_text_or_default(context.find('./fsa:CashAndCashEquivalents', namespaces)))
    data['Current Assets'].append(get_text_or_default(context.find('./fsa:CurrentAssets', namespaces)))
    data['Assets'].append(get_text_or_default(context.find('./fsa:Assets', namespaces)))
    data['Contributed Capital'].append(get_text_or_default(context.find('./fsa:ContributedCapital', namespaces)))
    data['Retained Earnings'].append(get_text_or_default(context.find('./fsa:RetainedEarnings', namespaces)))
    data['Equity'].append(get_text_or_default(context.find('./fsa:Equity', namespaces)))
    data['Short-term Debt to Banks'].append(get_text_or_default(context.find('./fsa:ShortTermDebtToBanks', namespaces)))
    data['Short-term Payables to Associates'].append(get_text_or_default(context.find('./fsa:ShortTermPayablesToAssociates', namespaces)))
    data['Short-term Liabilities Other Than Provisions'].append(get_text_or_default(context.find('./fsa:ShortTermLiabilitiesOtherThanProvisions', namespaces)))
    data['Liabilities Other Than Provisions'].append(get_text_or_default(context.find('./fsa:LiabilitiesOtherThanProvisions', namespaces)))
    data['Liabilities and Equity'].append(get_text_or_default(context.find('./fsa:LiabilitiesAndEquity', namespaces)))

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
