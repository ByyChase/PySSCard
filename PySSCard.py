from API.portfolios import portfolios
import requests #version 2.26.0 at time of writing
import json

'''
This is an API wrapper for the Security Scorecard API. You can find additional documentation on the API here:

https://securityscorecard.readme.io/reference

This wrapper follows the higherarchy of the endpoints in the documentation above. This API wrapper can return 
the raw response from the API endpoint or it can return the json. The default data being return will be the 
full response. Include the Respone_Type argument to with the value of 'json' for json data to be returned. 
Here is an example of how to do that 

json_data = SSCard.get_all_portfolios(Response_Type = 'json')

The wrapper will be written to not be what causes the program to crash. Try/Catches will be used through 
the wrapper and the error message will be sent back to whatever called the function. All error messages 
will be prefixed with "ERROR: " before sending back the raw error message. Please take this into 
consideration when using this wrapper.
'''




class PySSCard(portfolios):

    def __init__(self, Auth_Token):


        #Declare Variables
        self.Auth_Token = Auth_Token
        header = {'Accept' : 'application/json; charset=utf-8', 'Authorization' : str(Auth_Token)}



###################################### PORTFOLIO FUNCTIONS ######################################

    
    def get_all_portfolios(Request_Type = None):

        '''
        API Documentation: https://securityscorecard.readme.io/reference#get_portfolios

        Parameters
        ----------
        Request_Type : String
            If this is none, the full response gets sent back to the user. If it is equal to 
            'json' then the json is sent back to the user
        ...
        Returns
        -------
        response : API response (full response of json) 
            if Request_Type if set to none then the full response is sent to the user. If it 
            is set to 'json' then the json is sent back
        '''


        try:

            url = "https://api.securityscorecard.io/portfolios"
            response = requests.request("GET", url, headers=headers)

        except Exception as e:

            return "ERROR: " + e


        if Request_Type == 'json':

            return response.json()

        else:

            return response

    
    def create_new_portfolio(Request_Type = None, Name, Description = None, Privacy = None):

        '''
        API Documentation: https://securityscorecard.readme.io/reference#post_portfolios

        Parameters
        ----------
        Request_Type : String
            If this is none, the full response gets sent back to the user. If it is equal to 
            'json' then the json is sent back to the user
        Name : String
            The name of the portfolio that is being created
        Description: String
            The description of the portfolio being created
        Privacy : String ('private', 'shared', 'team')
            The privacy of the portfolio being created

        ...
        Returns
        -------
        response : API response (full response of json) 
            if Request_Type if set to none then the full response is sent to the user. If it 
            is set to 'json' then the json is sent back
        '''
        
        payload = {}
        payload.update("name" = Name)

        if Description != None:
            payload.update("description" = Description)

        if Privacy != None:
            payload.update("privacy" = Privacy)

        try:

            url = "https://api.securityscorecard.io/portfolios"
            response = requests.request("POST", url, json=payload, headers=headers)

        except Exception as e:

            return "ERROR: " + e

        if Request_Type == 'json':

            return response.json()

        else:

            return response

        
    def edit_portfolio(Request_Type = None, Portfolio_ID, Name, Description = None, Privacy = None)

        '''
        API Documentation: https://securityscorecard.readme.io/reference#put_portfolios-portfolio-id

        Parameters
        ----------
        Request_Type : String
            If this is none, the full response gets sent back to the user. If it is equal to 
            'json' then the json is sent back to the user
        Name : String
            The name of the portfolio that is being created
        Description: String
            The description of the portfolio being created
        Privacy : String ('private', 'shared', 'team')
            The privacy of the portfolio being created

        ...
        Returns
        -------
        response : API response (full response of json) 
            if Request_Type if set to none then the full response is sent to the user. If it 
            is set to 'json' then the json is sent back
        '''

        payload = {}
        payload.update("name" = Name)

        if Description != None:
            payload.update("description" = Description)

        if Privacy != None:
            payload.update("privacy" = Privacy)

        try:

            url = "https://api.securityscorecard.io/portfolios/" + str(Portfolio_ID)
            response = requests.request("PUT", url, json=payload, headers=headers)

        except Exception as e:

            return "ERROR: " + e

        if Request_Type == 'json':

            return response.json()

        else:

            return response


    def delete_portfolio(Request_Type = None, Portfolio_ID):

        '''
        API Documentation: https://securityscorecard.readme.io/reference#delete_portfolios-portfolio-id

        Parameters
        ----------
        Request_Type : String
            If this is none, the full response gets sent back to the user. If it is equal to 
            'json' then the json is sent back to the user
        Portfolio_ID : String
            The ID of the portfolio you want to delete

        ...
        Returns
        -------
        response : API response (full response of json) 
            if Request_Type if set to none then the full response is sent to the user. If it 
            is set to 'json' then the json is sent back
        '''

        try:

            url = "https://api.securityscorecard.io/portfolios/" + str(Portfolio_ID)
            response = requests.request("PUT", url, headers=headers)

        except Exception as e:

            return "ERROR: " + e

        if Request_Type == 'json':

            return response.json()

        else:

            return response

    
    def get_all_companies_in_portfolio(Request_Type = None, Portfolio_ID, Grade = None, Industry = None, Vulnerability = None, Issue_type = None, Status = None, Had_breach_within_last_days = None)

        '''
        API Documentation: https://securityscorecard.readme.io/reference#get_portfolios-portfolio-id-companies

        Parameters
        ----------
        Request_Type : String
            If this is none, the full response gets sent back to the user. If it is equal to 
            'json' then the json is sent back to the user
        Portfolio_ID : String
            The ID of the portfolio you want all the companies from
        Grade : String
            Company score grade filter
        Industry : String
            Industry filter
        Vulnerability : String
            CVE vulnerability filter
        Issue_type : String
            Issue type filter 
        Status : String
            company status
        Had_breach_within_last_days : Float
            Companies with breaches in last N days

        ...
        Returns
        -------
        response : API response (full response of json) 
            if Request_Type if set to none then the full response is sent to the user. If it 
            is set to 'json' then the json is sent back
        '''

        if Grade == None, Industry == None and Vulnerability == None and Issue_type == None and Status == None and Had_breach_within_last_days == None:

            try:
                url = "https://api.securityscorecard.io/portfolios/" + str(Portfolio_ID) + "/companies"
                response = requests.request("GET", url, headers=headers)

            except Exception as e:

                return "ERROR: " + e


            if Request_Type == 'json':

                return response.json()

            else:

                return response

        else:

            querystring = {}

            if Grade != None:
                querystring.update("grade" = Grade)

            if Industry != None:
                querystring.update("industry" = Industry)

            if Vulnerability != None:
                querystring.update("vulnerability" = Vulnerability)

            if Issue_type != None:
                querystring.update("issue_type" = Issue_type)

            if Status != None:
                querystring.update("status" = Status)

            if Had_breach_within_last_days != None:
                querystring.update("had_breach_within_last_days" = Had_breach_within_last_days)

            try:

                url = "https://api.securityscorecard.io/portfolios/" + str(Portfolio_ID) + "/companies"
                response = requests.request("GET", url, headers=headers, params=querystring)

            except Exception as e:

                return "ERROR: " + e


            if Request_Type == 'json':

                return response.json()

            else:

                return response

    def add_company_to_portfolio(Request_Type = None, Portfolio_ID, Domain):
            
        '''
        API Documentation: https://securityscorecard.readme.io/reference#put_portfolios-portfolio-id-companies-domain

        Parameters
        ----------
        Request_Type : String
            If this is none, the full response gets sent back to the user. If it is equal to 
            'json' then the json is sent back to the user
        Portfolio_ID : String
            The ID of the portfolio you want all the companies from
        Domain : String
            Company's primary Domain
        ...
        Returns
        -------
        response : API response (full response of json) 
            if Request_Type if set to none then the full response is sent to the user. If it 
            is set to 'json' then the json is sent back
        '''

        try:

            url = "https://api.securityscorecard.io/portfolios/"  + str(Portfolio_ID) + "/companies/" + str(Domain)
            response = requests.request("PUT", url, headers=headers)

        except Exception as e:

                return "ERROR: " + e

        if Request_Type == 'json':

                return response.json()

            else:

                return response

    
    def delete_company_to_portfolio(Request_Type = None, Portfolio_ID, Domain):

        '''
        API Documentation: https://securityscorecard.readme.io/reference#delete_portfolios-portfolio-id-companies-domain

        Parameters
        ----------
        Request_Type : String
            If this is none, the full response gets sent back to the user. If it is equal to 
            'json' then the json is sent back to the user
        Portfolio_ID : String
            The ID of the portfolio you want all the companies from
        Domain : String
            Company's primary Domain
        ...
        Returns
        -------
        response : API response (full response of json) 
            if Request_Type if set to none then the full response is sent to the user. If it 
            is set to 'json' then the json is sent back
        '''

        try:

            url = "https://api.securityscorecard.io/portfolios/"  + str(Portfolio_ID) + "/companies/" + str(Domain)
            response = requests.request("DELETE", url, headers=headers)

        except Exception as e:

                return "ERROR: " + e

        if Request_Type == 'json':

                return response.json()

            else:

                return response








        


        








    
