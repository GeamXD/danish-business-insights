import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


def extract_financial_data_from_links(file_path):
    # Create an empty dictionary to store data
    data = {
        'startDate': [],
        'endDate': [],
        'cvr': [],
        'nameofsubmittingenterprise': [],
        'addressofsubmittingenterprisestreetandnumber': [],
        'addressofsubmittingenterprisepostcodeandtown': [],
        'dateofgeneralmeeting': [],
        'nameandsurnameofchairmanofgeneralmeeting': [],
        'informationontypeofsubmittedreport': [],
        'identificationnumbercvrofreportingentity': [],
        'nameofreportingentity': [],
        'addressofreportingentitystreetandnumber': [],
        'addressofreportingentitypostcodeandtown': [],
        'nameoffinancialinstitution': [],
        'reportingperiodstartdate': [],
        'reportingperiodenddate': [],
        'nameofauditfirm': [],
        'addressofauditorstreetandnumber': [],
        'addressofauditorpostcodeandtown': [],
        'grossprofitloss': [],
        'profitlossfromordinaryoperatingactivities': [],
        'otherfinanceincome': [],
        'restofotherfinanceexpenses': [],
        'profitloss': [],
        'shorttermtaxreceivables': [],
        'shorttermreceivables': [],
        'othershortterminvestments': [],
        'shortterminvestments': [],
        'cashandcashequivalents': [],
        'currentassets': [],
        'assets': [],
        'contributedcapital': [],
        'retainedearnings': [],
        'equity': [],
        'shorttermdebttobanks': [],
        'shorttermpayablestoassociates': [],
        'shorttermliabilitiesotherthanprovisions': [],
        'liabilitiesotherthanprovisions': [],
        'liabilitiesandequity': [],
    }

    # Read links from the text file
    with open(file_path, 'r') as file:
        links = file.readlines()

    # Iterate through each link
    for link in links:
        link = link.strip()  # Remove leading/trailing whitespace
        response = requests.get(link)
        if response.status_code == 200:
            soup_2 = BeautifulSoup(response.text, 'lxml')
            # context = soup.find_all()
            # soup_2 = BeautifulSoup(context, 'lxml')
            
            #### CVR NUMBER ###
            identifier_element = soup_2.find('identifier')
            identifier_number = identifier_element.text if identifier_element else None
            data['cvr'].append(identifier_number)
            
            #### start date ####
            start_date_element = soup_2.find('startdate')
            start_date = start_date_element.text if start_date_element else None
            data['startDate'].append(start_date)
            
            #### end date ####
            end_date_element = soup_2.find('enddate')
            end_date = end_date_element.text if end_date_element else None
            data['endDate'].append(end_date)

            ### get all gsd data
            # Find all elements within gsd namespace
            gsd_elements = soup_2.find_all(lambda tag: tag.name.startswith('gsd'))

            # Remove 'gsd:' prefix from element names
            for element in gsd_elements:
                element.name = element.name.split(':')[-1]

            # Extract text content of all gsd elements
            gsd_data = {element.name: element.text for element in gsd_elements}


            ##################### getting all data #################################
            data['nameofsubmittingenterprise'].append(gsd_data.get('nameofsubmittingenterprise', float('nan')))
            data['addressofsubmittingenterprisestreetandnumber'].append(gsd_data.get('addressofsubmittingenterprisestreetandnumber', float('nan')))
            data['addressofsubmittingenterprisepostcodeandtown'].append(gsd_data.get('addressofsubmittingenterprisepostcodeandtown', float('nan')))
            data['dateofgeneralmeeting'].append(gsd_data.get('dateofgeneralmeeting', float('nan')))
            data['nameandsurnameofchairmanofgeneralmeeting'].append(gsd_data.get('nameandsurnameofchairmanofgeneralmeeting', float('nan')))
            data['informationontypeofsubmittedreport'].append(gsd_data.get('informationontypeofsubmittedreport', float('nan')))
            data['identificationnumbercvrofreportingentity'].append(gsd_data.get('identificationnumbercvrofreportingentity', float('nan')))
            data['nameofreportingentity'].append(gsd_data.get('nameofreportingentity', float('nan')))
            data['addressofreportingentitystreetandnumber'].append(gsd_data.get('addressofreportingentitystreetandnumber', float('nan')))
            data['addressofreportingentitypostcodeandtown'].append(gsd_data.get('addressofreportingentitypostcodeandtown', float('nan')))
            data['nameoffinancialinstitution'].append(gsd_data.get('nameoffinancialinstitution', float('nan')))
            data['reportingperiodstartdate'].append(gsd_data.get('reportingperiodstartdate', float('nan')))
            data['reportingperiodenddate'].append(gsd_data.get('reportingperiodenddate', float('nan')))
            data['nameofauditfirm'].append(gsd_data.get('nameofauditfirm', float('nan')))
            data['addressofauditorstreetandnumber'].append(gsd_data.get('addressofauditorstreetandnumber', float('nan')))
            data['addressofauditorpostcodeandtown'].append(gsd_data.get('addressofauditorpostcodeandtown', float('nan')))
            ### get all fas data
            # Find all elements within gsd namespace
            fsa_elements = soup_2.find_all(lambda tag: tag.name.startswith('fsa'))

            # Remove 'gsd:' prefix from element names
            for element in fsa_elements:
                element.name = element.name.split(':')[-1]

            # Extract text content of all gsd elements
            fsa_data = {element.name: element.text for element in fsa_elements}



            ############# get all data #####################
            data['grossprofitloss'].append(fsa_data.get('grossprofitloss', float('nan')))
            data['profitlossfromordinaryoperatingactivities'].append(fsa_data.get('profitlossfromordinaryoperatingactivities', float('nan')))
            data['otherfinanceincome'].append(fsa_data.get('otherfinanceincome', float('nan')))
            data['restofotherfinanceexpenses'].append(fsa_data.get('restofotherfinanceexpenses', float('nan')))
            data['profitloss'].append(fsa_data.get('profitloss', float('nan')))
            data['shorttermtaxreceivables'].append(fsa_data.get('shorttermtaxreceivables', float('nan')))
            data['shorttermreceivables'].append(fsa_data.get('shorttermreceivables', float('nan')))
            data['othershortterminvestments'].append(fsa_data.get('othershortterminvestments', float('nan')))
            data['shortterminvestments'].append(fsa_data.get('shortterminvestments', float('nan')))
            data['cashandcashequivalents'].append(fsa_data.get('cashandcashequivalents', float('nan')))
            data['currentassets'].append(fsa_data.get('currentassets', float('nan')))
            data['assets'].append(fsa_data.get('assets', float('nan')))
            data['contributedcapital'].append(fsa_data.get('contributedcapital', float('nan')))
            data['retainedearnings'].append(fsa_data.get('retainedearnings', float('nan')))
            data['equity'].append(fsa_data.get('equity', float('nan')))
            data['shorttermdebttobanks'].append(fsa_data.get('shorttermdebttobanks', float('nan')))
            data['shorttermpayablestoassociates'].append(fsa_data.get('shorttermpayablestoassociates', float('nan')))
            data['shorttermliabilitiesotherthanprovisions'].append(fsa_data.get('shorttermliabilitiesotherthanprovisions', float('nan')))
            data['liabilitiesotherthanprovisions'].append(fsa_data.get('liabilitiesotherthanprovisions', float('nan')))
            data['liabilitiesandequity'].append(fsa_data.get('liabilitiesandequity', float('nan')))
    return data

# Example usage
file_path = ''  # Path to the text file containing XML links
financial_data_df = extract_financial_data_from_links(file_path)


with open('parsed_xml_1.json', 'w') as file:
    json.dump(financial_data_df, file)
